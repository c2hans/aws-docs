---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/node-ns.html
---

# AWS.NS
<a name="node-ns"></a>

Defines an AWS network service (NS) node.

## Syntax
<a name="node-ns-syntax"></a>

```
tosca.nodes.AWS.NS:
  properties:
    descriptor\_id: String
    descriptor\_version: String
    descriptor\_name: String
```

## Properties
<a name="node-ns-properties"></a>

 `descriptor_id`
The UUID of the descriptor.
Required: Yes
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 `descriptor_version`
The version of the NSD.
Required: Yes
Type: String
Pattern: `^[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}.*`

 `descriptor_name`
The name of the descriptor.
Required: Yes
Type: String

## Example
<a name="node-ns-example"></a>

```
SampleNS:
  type: tosca.nodes.AWS.NS
  properties:
    descriptor_id: "{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}"
    descriptor_version: "1.0.0"
    descriptor_name: "Test NS Template"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
