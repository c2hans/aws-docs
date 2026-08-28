---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-application-iamidentitycenteroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Application IamIdentityCenterOptions
<a name="aws-properties-opensearchservice-application-iamidentitycenteroptions"></a>

Configuration settings for IAM Identity Center in an OpenSearch application.

## Syntax
<a name="aws-properties-opensearchservice-application-iamidentitycenteroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-application-iamidentitycenteroptions-syntax.json"></a>

```
{
  "[Enabled](#cfn-opensearchservice-application-iamidentitycenteroptions-enabled)" : {{Boolean}},
  "[IamIdentityCenterInstanceArn](#cfn-opensearchservice-application-iamidentitycenteroptions-iamidentitycenterinstancearn)" : {{String}},
  "[IamRoleForIdentityCenterApplicationArn](#cfn-opensearchservice-application-iamidentitycenteroptions-iamroleforidentitycenterapplicationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-application-iamidentitycenteroptions-syntax.yaml"></a>

```
  [Enabled](#cfn-opensearchservice-application-iamidentitycenteroptions-enabled): {{Boolean}}
  [IamIdentityCenterInstanceArn](#cfn-opensearchservice-application-iamidentitycenteroptions-iamidentitycenterinstancearn): {{String}}
  [IamRoleForIdentityCenterApplicationArn](#cfn-opensearchservice-application-iamidentitycenteroptions-iamroleforidentitycenterapplicationarn): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-application-iamidentitycenteroptions-properties"></a>

`Enabled`  <a name="cfn-opensearchservice-application-iamidentitycenteroptions-enabled"></a>
Indicates whether IAM Identity Center is enabled for the OpenSearch application.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamIdentityCenterInstanceArn`  <a name="cfn-opensearchservice-application-iamidentitycenteroptions-iamidentitycenterinstancearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamRoleForIdentityCenterApplicationArn`  <a name="cfn-opensearchservice-application-iamidentitycenteroptions-iamroleforidentitycenterapplicationarn"></a>
The Amazon Resource Name (ARN) of the IAM role assigned to the IAM Identity Center application for the OpenSearch application.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):iam::[0-9]+:role\/.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
