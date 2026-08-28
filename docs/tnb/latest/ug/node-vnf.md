---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/node-vnf.html
---

# AWS.VNF
<a name="node-vnf"></a>

Defines an AWS virtual network function (VNF) node.

## Syntax
<a name="vnf-syntax"></a>

```
tosca.nodes.AWS.VNF:
  properties:
    descriptor\_id: String
    descriptor\_version: String
    descriptor\_name: String
    provider: String
  requirements:
    helm: String
```

## Properties
<a name="vnf-properties"></a>

 `descriptor_id`
The UUID of the descriptor.
Required: Yes
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 `descriptor_version`
The version of the VNFD.
Required: Yes
Type: String
Pattern: `^[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}.*`

 `descriptor_name`
The name of the descriptor.
Required: Yes
Type: String

 `provider`
The author of the VNFD.
Required: Yes
Type: String

## Requirements
<a name="vnf-requirements"></a>

 `helm`
The Helm directory defining container artifacts. This is a reference to [AWS.Artifacts.Helm](node-helm.md).
Required: Yes
Type: String

## Example
<a name="vnf-example"></a>

```
SampleVNF:
  type: tosca.nodes.AWS.VNF
  properties:
    descriptor_id: "{{6a792e0c-be2a-45fa-989e-5f89d94ca898}}"
    descriptor_version: "{{1.0.0}}"
    descriptor_name: "{{Test VNF Template}}"
    provider: "{{Operator}}"
  requirements:
    helm: SampleHelm
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
