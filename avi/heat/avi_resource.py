import uuid
import logging
from heat.engine import resource
from avi.sdk.avi_api import ApiSession
from avi.sdk.avi_api import ObjectNotFound

LOG = logging.getLogger(__name__)


def os2avi_uuid(obj_type, eid):
    uid = str(uuid.UUID(eid))
    return obj_type + "-" + uid


class AviResource(resource.Resource):
    def get_avi_tenant_uuid(self):
        if self.context.auth_token_info['token']['project']['name'] == 'admin':
            return "admin"
        return os2avi_uuid("tenant",
                           self.context.tenant_id)

    def get_avi_client(self):

        try:
            endpoint = self.client("keystone").url_for(
                service_type="avi-lbaas",
                endpoint_type="publicURL")
            address = endpoint.split("//")[1].split("/")[0]
        except Exception as e:
            LOG.exception("Error during finding avi address: %s", e)
            return None
        # from IPython.core.debugger import Pdb
        # pdb = Pdb()
        # pdb.set_trace()
        username = self.context.auth_token_info['token']['user']['name']
        api_session = ApiSession.get_session(
            controller_ip=address,
            username=username,
            token=self.context.auth_token,
        )
        return api_session

    def handle_create(self):
        res_def = dict()
        for k, v in self.properties.items():
            if v is None:
                continue
            res_def[k] = v
        client = self.get_avi_client()
        obj = client.post(self.resource_name,
                          data=res_def,
                          tenant_uuid=self.get_avi_tenant_uuid()
                          ).json()
        self.resource_id_set(obj['uuid'])

    def _show_resource(self):
        client = self.get_avi_client()
        hm = client.get("%s/%s" % (self.resource_name,
                                   self.resource_id),
                        tenant_uuid=self.get_avi_tenant_uuid()
                        ).json()
        return hm

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        pass

    def handle_delete(self):
        client = self.get_avi_client()
        try:
            client.delete("%s/%s" % (self.resource_name,
                                     self.resource_id),
                          tenant_uuid=self.get_avi_tenant_uuid()
                          ).json()
        except ObjectNotFound as e:
            LOG.exception("Object %s not found: %s", (self.resource_name,
                                                      self.resource_id), e)
        return True