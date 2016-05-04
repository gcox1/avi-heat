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


class AvgUptimeChangeDetails(object):
    # all schemas
    metric_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    metric_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    current_value_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    resource_str_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'metric_name',
        'metric_id',
        'current_value',
        'threshold',
        'resource_str',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'metric_name': metric_name_schema,
        'metric_id': metric_id_schema,
        'current_value': current_value_schema,
        'threshold': threshold_schema,
        'resource_str': resource_str_schema,
    }




class MetricThresoldUpDetails(object):
    # all schemas
    metric_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    metric_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    current_value_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_schema = properties.Schema(
        properties.Schema.STRING,
        _("Server IP:Port on which event was generated"),
        required=False,
        update_allowed=True,
    )
    pool_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Identity of the Pool"),
        required=False,
        update_allowed=True,
    )
    entity_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("ID of the object whose metric has hit the threshold"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'metric_name',
        'metric_id',
        'current_value',
        'threshold',
        'server',
        'pool_uuid',
        'entity_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'metric_name': metric_name_schema,
        'metric_id': metric_id_schema,
        'current_value': current_value_schema,
        'threshold': threshold_schema,
        'server': server_schema,
        'pool_uuid': pool_uuid_schema,
        'entity_uuid': entity_uuid_schema,
    }




class MetricsDbDiskEventDetails(object):
    # all schemas
    metrics_quota_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    metrics_free_sz_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    metrics_deleted_tables_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    metrics_deleted_tables_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=metrics_deleted_tables_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'metrics_quota',
        'metrics_free_sz',
        'metrics_deleted_tables',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'metrics_quota': metrics_quota_schema,
        'metrics_free_sz': metrics_free_sz_schema,
        'metrics_deleted_tables': metrics_deleted_tables_schema,
    }




class LicenseExpiryDetails(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    expiry_at_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
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
        _(""),
        required=False,
        update_allowed=True,
    )
    max_ses_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    backend_servers_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    max_apps_schema = properties.Schema(
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
    license_id_schema = properties.Schema(
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
    sockets_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'expiry_at',
        'throughput',
        'cores',
        'max_ses',
        'backend_servers',
        'max_apps',
        'license_tier',
        'license_id',
        'license_type',
        'sockets',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'expiry_at': expiry_at_schema,
        'throughput': throughput_schema,
        'cores': cores_schema,
        'max_ses': max_ses_schema,
        'backend_servers': backend_servers_schema,
        'max_apps': max_apps_schema,
        'license_tier': license_tier_schema,
        'license_id': license_id_schema,
        'license_type': license_type_schema,
        'sockets': sockets_schema,
    }




class LicenseDetails(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    expiry_at_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    backend_servers_schema = properties.Schema(
        properties.Schema.NUMBER,
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
    license_type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'expiry_at',
        'backend_servers',
        'license_id',
        'license_type',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'expiry_at': expiry_at_schema,
        'backend_servers': backend_servers_schema,
        'license_id': license_id_schema,
        'license_type': license_type_schema,
    }


