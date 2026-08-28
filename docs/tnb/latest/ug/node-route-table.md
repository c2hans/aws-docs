---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/node-route-table.html
---

# AWS.Networking.RouteTable
<a name="node-route-table"></a>

A route table contains a set of rules, called routes, that determine where network traffic from subnets within your VPC or gateway is directed. You must associate a route table with a VPC.

## Syntax
<a name="node-route-table-syntax"></a>

```
tosca.nodes.AWS.Networking.RouteTable:
  properties:
    tags: List
  requirements:
    vpc: String
```

## Properties
<a name="node-route-table-properties"></a>

 `tags`
Tags to be attached to the resource.
Required: No
Type: List

## Requirements
<a name="node-route-table-requirements"></a>

 `vpc`
An [AWS.Networking.VPC](node-vpc.md) node.
Required: Yes
Type: String

## Example
<a name="node-route-table-example"></a>

```
SampleRouteTable:
  type: tosca.nodes.AWS.Networking.RouteTable
  properties:
    tags:
      - "Name=SampleVPC"
      - "Environment=Testing"
  requirements:
    vpc: SampleVPC
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
