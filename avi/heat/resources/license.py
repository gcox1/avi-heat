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


class SingleLicense(object):
    # all schemas
    license_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    start_on_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    valid_until_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    customer_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    throughput_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    cores_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of service engine cores in non-container clouds"),
        required=False,
        update_allowed=True,
    )
    backend_servers_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    max_ses_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of service engines hosts in container clouds"),
        required=False,
        update_allowed=True,
    )
    license_tier_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    license_tier_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=license_tier_item_schema,
        required=False,
        update_allowed=True,
    )
    max_apps_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    license_string_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    license_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    version_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    created_on_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    last_update_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    license_type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    enforced_params_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    enforced_params_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=enforced_params_item_schema,
        required=False,
        update_allowed=True,
    )
    sockets_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of physical cpu sockets across service engines in no access and linux server clouds"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'license_name',
        'start_on',
        'valid_until',
        'customer_name',
        'throughput',
        'cores',
        'backend_servers',
        'max_ses',
        'license_tier',
        'max_apps',
        'license_string',
        'license_id',
        'version',
        'created_on',
        'last_update',
        'license_type',
        'enforced_params',
        'sockets',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'license_name': license_name_schema,
        'start_on': start_on_schema,
        'valid_until': valid_until_schema,
        'customer_name': customer_name_schema,
        'throughput': throughput_schema,
        'cores': cores_schema,
        'backend_servers': backend_servers_schema,
        'max_ses': max_ses_schema,
        'license_tier': license_tier_schema,
        'max_apps': max_apps_schema,
        'license_string': license_string_schema,
        'license_id': license_id_schema,
        'version': version_schema,
        'created_on': created_on_schema,
        'last_update': last_update_schema,
        'license_type': license_type_schema,
        'enforced_params': enforced_params_schema,
        'sockets': sockets_schema,
    }




class ControllerLicense(AviResource):
    resource_name = "controllerlicense"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    start_on_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    valid_until_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    customer_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    throughput_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    cores_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of service engine cores in non-container clouds"),
        required=False,
        update_allowed=True,
    )
    backend_servers_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    license_tier_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    license_tier_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=license_tier_item_schema,
        required=False,
        update_allowed=True,
    )
    max_ses_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of service engines hosts in container clouds"),
        required=False,
        update_allowed=True,
    )
    max_apps_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    max_vses_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Deprecated"),
        required=False,
        update_allowed=True,
    )
    sockets_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of physical cpu sockets across service engines in no access and linux server clouds"),
        required=False,
        update_allowed=True,
    )
    licenses_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SingleLicense.properties_schema,
        required=True,
        update_allowed=False,
    )
    licenses_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=licenses_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'start_on',
        'valid_until',
        'customer_name',
        'throughput',
        'cores',
        'backend_servers',
        'license_tier',
        'max_ses',
        'max_apps',
        'max_vses',
        'sockets',
        'licenses',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'start_on': start_on_schema,
        'valid_until': valid_until_schema,
        'customer_name': customer_name_schema,
        'throughput': throughput_schema,
        'cores': cores_schema,
        'backend_servers': backend_servers_schema,
        'license_tier': license_tier_schema,
        'max_ses': max_ses_schema,
        'max_apps': max_apps_schema,
        'max_vses': max_vses_schema,
        'sockets': sockets_schema,
        'licenses': licenses_schema,
    }




class ControllerLicenseLicenseTier(AviNestedResource):
    resource_name = "controllerlicense"
    nested_property_name = "license_tier"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of controllerlicense"),
        required=True,
        update_allowed=False,
    )
    license_tier_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = ('controllerlicense_uuid',
                  'license_tier',
                 )

    # mapping of properties to their schemas
    properties_schema = {
        'controllerlicense_uuid': parent_uuid_schema,
        'license_tier': license_tier_item_schema,
    }


class ControllerLicenseLicenses(AviNestedResource, SingleLicense):
    resource_name = "controllerlicense"
    nested_property_name = "licenses"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of controllerlicense"),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = SingleLicense.PROPERTIES + ('controllerlicense_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'controllerlicense_uuid': parent_uuid_schema,
    }
    properties_schema.update(SingleLicense.properties_schema)


def resource_mapping():
    return {
        'Avi::ControllerLicense': ControllerLicense,
        'Avi::ControllerLicense::LicenseTier': ControllerLicenseLicenseTier,
        'Avi::ControllerLicense::License': ControllerLicenseLicenses,
    }

