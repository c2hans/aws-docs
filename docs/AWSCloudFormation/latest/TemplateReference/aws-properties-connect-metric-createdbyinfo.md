---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-metric-createdbyinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric CreatedByInfo
<a name="aws-properties-connect-metric-createdbyinfo"></a>

Information on the identity that created the file.

## Syntax
<a name="aws-properties-connect-metric-createdbyinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-metric-createdbyinfo-syntax.json"></a>

```
{
  "[AWSIdentityArn](#cfn-connect-metric-createdbyinfo-awsidentityarn)" : {{String}},
  "[ConnectUserArn](#cfn-connect-metric-createdbyinfo-connectuserarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-metric-createdbyinfo-syntax.yaml"></a>

```
  [AWSIdentityArn](#cfn-connect-metric-createdbyinfo-awsidentityarn): {{String}}
  [ConnectUserArn](#cfn-connect-metric-createdbyinfo-connectuserarn): {{String}}
```

## Properties
<a name="aws-properties-connect-metric-createdbyinfo-properties"></a>

`AWSIdentityArn`  <a name="cfn-connect-metric-createdbyinfo-awsidentityarn"></a>
STS or IAM ARN representing the identity of API Caller. SDK users cannot populate this and this value is calculated automatically if `ConnectUserArn` is not provided.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectUserArn`  <a name="cfn-connect-metric-createdbyinfo-connectuserarn"></a>
An agent ARN representing a [connect user](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-resources-for-iam-policies).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
