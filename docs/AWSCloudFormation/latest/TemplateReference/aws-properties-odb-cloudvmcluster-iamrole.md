---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-cloudvmcluster-iamrole.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::CloudVmCluster IamRole
<a name="aws-properties-odb-cloudvmcluster-iamrole"></a>

Information about an AWS Identity and Access Management (IAM) service role associated with a resource.

## Syntax
<a name="aws-properties-odb-cloudvmcluster-iamrole-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-cloudvmcluster-iamrole-syntax.json"></a>

```
{
  "[AwsIntegration](#cfn-odb-cloudvmcluster-iamrole-awsintegration)" : {{String}},
  "[IamRoleArn](#cfn-odb-cloudvmcluster-iamrole-iamrolearn)" : {{String}},
  "[Status](#cfn-odb-cloudvmcluster-iamrole-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-cloudvmcluster-iamrole-syntax.yaml"></a>

```
  [AwsIntegration](#cfn-odb-cloudvmcluster-iamrole-awsintegration): {{String}}
  [IamRoleArn](#cfn-odb-cloudvmcluster-iamrole-iamrolearn): {{String}}
  [Status](#cfn-odb-cloudvmcluster-iamrole-status): {{String}}
```

## Properties
<a name="aws-properties-odb-cloudvmcluster-iamrole-properties"></a>

`AwsIntegration`  <a name="cfn-odb-cloudvmcluster-iamrole-awsintegration"></a>
The AWS integration configuration settings for the AWS Identity and Access Management (IAM) service role.
*Required*: No
*Type*: String
*Allowed values*: `KmsTde`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamRoleArn`  <a name="cfn-odb-cloudvmcluster-iamrole-iamrolearn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role.
*Required*: No
*Type*: String
*Pattern*: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{12}:role/.+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-odb-cloudvmcluster-iamrole-status"></a>
The current status of the AWS Identity and Access Management (IAM) service role.
*Required*: No
*Type*: String
*Allowed values*: `ASSOCIATING | DISASSOCIATING | FAILED | CONNECTED | DISCONNECTED | PARTIALLY_CONNECTED | UNKNOWN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
