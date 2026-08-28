---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-memorydb-subnetgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::SubnetGroup
<a name="aws-resource-memorydb-subnetgroup"></a>

Specifies a subnet group. A subnet group is a collection of subnets (typically private) that you can designate for your clusters running in an Amazon Virtual Private Cloud (VPC) environment. When you create a cluster in an Amazon VPC, you must specify a subnet group. MemoryDB uses that subnet group to choose a subnet and IP addresses within that subnet to associate with your nodes. For more information, see [Subnets and subnet groups](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.html).

## Syntax
<a name="aws-resource-memorydb-subnetgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-memorydb-subnetgroup-syntax.json"></a>

```
{
  "Type" : "AWS::MemoryDB::SubnetGroup",
  "Properties" : {
      "[Description](#cfn-memorydb-subnetgroup-description)" : {{String}},
      "[SubnetGroupName](#cfn-memorydb-subnetgroup-subnetgroupname)" : {{String}},
      "[SubnetIds](#cfn-memorydb-subnetgroup-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-memorydb-subnetgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-memorydb-subnetgroup-syntax.yaml"></a>

```
Type: AWS::MemoryDB::SubnetGroup
Properties:
  [Description](#cfn-memorydb-subnetgroup-description): {{String}}
  [SubnetGroupName](#cfn-memorydb-subnetgroup-subnetgroupname): {{String}}
  [SubnetIds](#cfn-memorydb-subnetgroup-subnetids): {{
    - String}}
  [Tags](#cfn-memorydb-subnetgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-memorydb-subnetgroup-properties"></a>

`Description`  <a name="cfn-memorydb-subnetgroup-description"></a>
A description of the subnet group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetGroupName`  <a name="cfn-memorydb-subnetgroup-subnetgroupname"></a>
The name of the subnet group to be used for the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z][a-z0-9\-]*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-memorydb-subnetgroup-subnetids"></a>
A list of Amazon VPC subnet IDs for the subnet group.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-memorydb-subnetgroup-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-memorydb-subnetgroup-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-memorydb-subnetgroup-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-memorydb-subnetgroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-memorydb-subnetgroup-return-values-fn--getatt-fn--getatt"></a>

`ARN`  <a name="ARN-fn::getatt"></a>
When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the ARN of the subnet group, such as `arn:aws:memorydb:us-east-1:123456789012:subnetgroup/my-subnet-group`

`SupportedNetworkTypes`  <a name="SupportedNetworkTypes-fn::getatt"></a>
The network types supported by this subnet. Returns an array of strings that can include 'ipv4', 'ipv6', or both, indicating whether the subnet supports IPv4 only, IPv6 only, or dual-stack deployments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
