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


class DosThreshold(object):
    # all schemas
    attack_schema = properties.Schema(
        properties.Schema.STRING,
        _("Attack type."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DOS_REQ_IP_URI_RL_DROP_BAD', 'DOS_REQ_CIP_SCAN_BAD_RL_DROP', 'IP_FRAG_OVERRUN', 'POLICY_DROPS', 'IP_FRAG_INCOMPLETE', 'DOS_CONN_IP_RL_DROP', 'FAKE_SESSION', 'DOS_HTTP_ABORT', 'SMURF', 'IP_FRAG_TOOSMALL', 'ICMP_PING_FLOOD', 'DOS_REQ_CIP_SCAN_UNKNOWN_RL_DROP', 'DOS_REQ_IP_URI_RL_DROP', 'LAND', 'UNKOWN_PROTOCOL', 'DOS_SLOW_URL', 'TCP_NON_SYN_FLOOD', 'ZERO_WINDOW_STRESS', 'IP_FRAG_FULL', 'DOS_REQ_RL_DROP', 'SMALL_WINDOW_STRESS', 'BAD_RST_FLOOD', 'DOS_APP_ERROR', 'DOS_SSL_ERROR', 'MALFORMED_FLOOD', 'PORT_SCAN', 'DOS_REQ_IP_RL_DROP', 'DOS_REQ_URI_RL_DROP_BAD', 'TCP_NON_SYN_FLOOD_OLD', 'DOS_REQ_URI_SCAN_BAD_RL_DROP', 'DOS_REQ_IP_RL_DROP_BAD', 'DOS_REQ_URI_RL_DROP', 'SYN_FLOOD', 'DOS_HTTP_ERROR', 'TEARDROP', 'DOS_REQ_URI_SCAN_UNKNOWN_RL_DROP', 'DOS_HTTP_TIMEOUT', 'DOS_CONN_RL_DROP']),
        ],
    )
    min_value_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Minimum number of packets or connections or requests in a given interval of time to be deemed as attack."),
        required=True,
        update_allowed=True,
    )
    max_value_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of packets or connections or requests in a given interval of time to be deemed as attack."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'attack',
        'min_value',
        'max_value',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'attack': attack_schema,
        'min_value': min_value_schema,
        'max_value': max_value_schema,
    }




class DosThresholdProfile(object):
    # all schemas
    thresh_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Timer value in seconds to collect DoS attack metrics based on threshold on the Service Engine for this Virtual Service."),
        required=True,
        update_allowed=True,
    )
    thresh_info_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DosThreshold.properties_schema,
        required=True,
        update_allowed=False,
    )
    thresh_info_schema = properties.Schema(
        properties.Schema.LIST,
        _("Attack type, min and max values for DoS attack detection."),
        schema=thresh_info_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'thresh_period',
        'thresh_info',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'thresh_period': thresh_period_schema,
        'thresh_info': thresh_info_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'thresh_info': getattr(DosThreshold, 'field_references', {}),
    }

