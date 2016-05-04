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
from clustering import *


class ClusterServiceFailedEvent(object):
    # all schemas
    service_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the controller service."),
        required=False,
        update_allowed=True,
    )
    node_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of controller node."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'service_name',
        'node_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'service_name': service_name_schema,
        'node_name': node_name_schema,
    }




class ClusterLeaderFailoverEvent(object):
    # all schemas
    leader_node_schema = properties.Schema(
        properties.Schema.MAP,
        _("Details of the new controller cluster leader node."),
        schema=ClusterNode.properties_schema,
        required=False,
        update_allowed=True,
    )
    previous_leader_node_schema = properties.Schema(
        properties.Schema.MAP,
        _("Details of the previous controller cluster leader."),
        schema=ClusterNode.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'leader_node',
        'previous_leader_node',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'leader_node': leader_node_schema,
        'previous_leader_node': previous_leader_node_schema,
    }




class ClusterNodeRemoveEvent(object):
    # all schemas
    node_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of controller node."),
        required=False,
        update_allowed=True,
    )
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address of the controller VM."),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    role_schema = properties.Schema(
        properties.Schema.STRING,
        _("Role of the node when it left the controller cluster."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'node_name',
        'ip',
        'role',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'node_name': node_name_schema,
        'ip': ip_schema,
        'role': role_schema,
    }




class ClusterNodeAddEvent(object):
    # all schemas
    node_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of controller node."),
        required=False,
        update_allowed=True,
    )
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address of the controller VM."),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    role_schema = properties.Schema(
        properties.Schema.STRING,
        _("Role of the controller within the cluster."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'node_name',
        'ip',
        'role',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'node_name': node_name_schema,
        'ip': ip_schema,
        'role': role_schema,
    }




class ClusterWarmRebootEvent(object):
    # all schemas

    # properties list
    PROPERTIES = (
    )

    # mapping of properties to their schemas
    properties_schema = {
    }


