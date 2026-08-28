---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/node-internet-gateway.html
---

# AWS.Networking.InternetGateway
<a name="node-internet-gateway"></a>

Defines an AWS Internet Gateway Node.

## Syntax
<a name="node-internet-gateway-syntax"></a>

```
tosca.nodes.AWS.Networking.InternetGateway:
  capabilities:
    routing:
      properties:
        dest\_cidr: String
        ipv6\_dest\_cidr: String
  properties:
    tags: List
    egress\_only: Boolean
  requirements:
    vpc: String
    route\_table: String
```

## Capabilities
<a name="node-internet-gateway-capabilities"></a><a name="node_internet_gateway_routing"></a>`routing`

Properties that define the routing connection within the VPC. You must include either the `dest_cidr` or `ipv6_dest_cidr` property.

 `dest_cidr`
The IPv4 CIDR block used for the destination match. This property is used to create a route in `RouteTable` and its value is used as the `DestinationCidrBlock`.
Required: No if you included the `ipv6_dest_cidr` property.
Type: String

 `ipv6_dest_cidr`
The IPv6 CIDR block used for the destination match.
Required: No if you included the `dest_cidr` property.
Type: String

## Properties
<a name="node-internet-gateway-properties"></a>

 `tags`
The tags to be attached to the resource.
Required: No
Type: List

 `egress_only`
An IPv6-specific property. Indicates if the internet gateway is only for egress communication or not. When `egress_only` is true, you must define the `ipv6_dest_cidr` property.
Required: No
Type: Boolean

## Requirements
<a name="node-internet-gateway-requirements"></a>

 `vpc`
An [AWS.Networking.VPC](node-vpc.md) node.
Required: Yes
Type: String

 `route_table`
An [AWS.Networking.RouteTable](node-route-table.md) node.
Required: Yes
Type: String

## Example
<a name="node-internet-gateway-example"></a>

```
Free5GCIGW:
  type: tosca.nodes.AWS.Networking.InternetGateway
  properties:
    egress_only: false
  capabilities:
    routing:
      properties:
        dest_cidr: "0.0.0.0/0"
        ipv6_dest_cidr: "::/0"
  requirements:
    route_table: Free5GCRouteTable
    vpc: Free5GCVPC
Free5GCEGW:
  type: tosca.nodes.AWS.Networking.InternetGateway
  properties:
    egress_only: true
  capabilities:
    routing:
      properties:
        ipv6_dest_cidr: "::/0"
  requirements:
    route_table: Free5GCPrivateRouteTable
    vpc: Free5GCVPC
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
