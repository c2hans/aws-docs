---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3outposts-endpoint-networkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Outposts::Endpoint NetworkInterface
<a name="aws-properties-s3outposts-endpoint-networkinterface"></a>

The container for the network interface.

## Syntax
<a name="aws-properties-s3outposts-endpoint-networkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3outposts-endpoint-networkinterface-syntax.json"></a>

```
{
  "[NetworkInterfaceId](#cfn-s3outposts-endpoint-networkinterface-networkinterfaceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3outposts-endpoint-networkinterface-syntax.yaml"></a>

```
  [NetworkInterfaceId](#cfn-s3outposts-endpoint-networkinterface-networkinterfaceid): {{String}}
```

## Properties
<a name="aws-properties-s3outposts-endpoint-networkinterface-properties"></a>

`NetworkInterfaceId`  <a name="cfn-s3outposts-endpoint-networkinterface-networkinterfaceid"></a>
The ID for the network interface.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
