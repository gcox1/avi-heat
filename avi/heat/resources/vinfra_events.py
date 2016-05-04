# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *


class VinfraVcenterObjDeleteDetails(object):
    # all schemas
    vcenter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    obj_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vcenter',
        'obj_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vcenter': vcenter_schema,
        'obj_name': obj_name_schema,
    }




class VinfraDiscSummaryDetails(object):
    # all schemas
    vcenter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    num_dcs_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_hosts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_clusters_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_vms_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_nws_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vcenter',
        'num_dcs',
        'num_hosts',
        'num_clusters',
        'num_vms',
        'num_nws',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vcenter': vcenter_schema,
        'num_dcs': num_dcs_schema,
        'num_hosts': num_hosts_schema,
        'num_clusters': num_clusters_schema,
        'num_vms': num_vms_schema,
        'num_nws': num_nws_schema,
    }




class VinfraVmDetails(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    datacenter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    host_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'datacenter',
        'host',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'datacenter': datacenter_schema,
        'host': host_schema,
    }




class VinfraVcenterDiscoveryFailure(object):
    # all schemas
    vcenter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    state_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vcenter',
        'state',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vcenter': vcenter_schema,
        'state': state_schema,
    }




class VinfraMgmtNwChangeDetails(object):
    # all schemas
    vcenter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    existing_nw_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    new_nw_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vcenter',
        'existing_nw',
        'new_nw',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vcenter': vcenter_schema,
        'existing_nw': existing_nw_schema,
        'new_nw': new_nw_schema,
    }




class VinfraVcenterBadCredentials(object):
    # all schemas
    vcenter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    vcenter_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vcenter',
        'name',
        'vcenter_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vcenter': vcenter_schema,
        'name': name_schema,
        'vcenter_name': vcenter_name_schema,
    }




class VinfraPoolServerDeleteDetails(object):
    # all schemas
    pool_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_ip_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    server_ip_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=server_ip_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'pool_name',
        'server_ip',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'pool_name': pool_name_schema,
        'server_ip': server_ip_schema,
    }




class VinfraCntlrHostUnreachableList(object):
    # all schemas
    vcenter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    host_name_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    host_name_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=host_name_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vcenter',
        'host_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vcenter': vcenter_schema,
        'host_name': host_name_schema,
    }


