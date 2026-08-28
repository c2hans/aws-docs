---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/node-resource-import.html
---

# AWS.Resource.Import
<a name="node-resource-import"></a>

You can import the following AWS resources into AWS TNB:
+ VPC
+ Subnet
+ Route Table
+ Internet Gateway
+ Security Group

## Syntax
<a name="node-resource-import-syntax"></a>

```
tosca.nodes.AWS.Resource.Import
  properties:
    resource\_type: String
    resource\_id: String
```

## Properties
<a name="node-resource-import-properties"></a>

 `resource_type`
The resource type that is imported to AWS TNB.
Required: No
Type: List

 `resource_id`
The resource ID that is imported to AWS TNB.
Required: No
Type: List

## Example
<a name="node-resource-import-example"></a>

```
SampleImportedVPC:
  type: tosca.nodes.AWS.Resource.Import
  properties:
    resource_type: "tosca.nodes.AWS.Networking.VPC"
    resource_id: "{{vpc-123456}}"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
