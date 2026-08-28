---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-accesspoint-vpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::AccessPoint VpcConfiguration
<a name="aws-properties-s3express-accesspoint-vpcconfiguration"></a>

<a name="aws-properties-s3express-accesspoint-vpcconfiguration-description"></a>The `VpcConfiguration` property type specifies Property description not available. for an [AWS::S3Express::AccessPoint](aws-resource-s3express-accesspoint.md).

## Syntax
<a name="aws-properties-s3express-accesspoint-vpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-accesspoint-vpcconfiguration-syntax.json"></a>

```
{
  "[VpcId](#cfn-s3express-accesspoint-vpcconfiguration-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3express-accesspoint-vpcconfiguration-syntax.yaml"></a>

```
  [VpcId](#cfn-s3express-accesspoint-vpcconfiguration-vpcid): {{String}}
```

## Properties
<a name="aws-properties-s3express-accesspoint-vpcconfiguration-properties"></a>

`VpcId`  <a name="cfn-s3express-accesspoint-vpcconfiguration-vpcid"></a>
If this field is specified, this access point will only allow connections from the specified VPC ID.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
