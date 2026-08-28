---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-s3action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet S3Action
<a name="aws-properties-ses-mailmanagerruleset-s3action"></a>

Writes the MIME content of the email to an S3 bucket.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-s3action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-s3action-syntax.json"></a>

```
{
  "[ActionFailurePolicy](#cfn-ses-mailmanagerruleset-s3action-actionfailurepolicy)" : {{String}},
  "[RoleArn](#cfn-ses-mailmanagerruleset-s3action-rolearn)" : {{String}},
  "[S3Bucket](#cfn-ses-mailmanagerruleset-s3action-s3bucket)" : {{String}},
  "[S3Prefix](#cfn-ses-mailmanagerruleset-s3action-s3prefix)" : {{String}},
  "[S3SseKmsKeyId](#cfn-ses-mailmanagerruleset-s3action-s3ssekmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-s3action-syntax.yaml"></a>

```
  [ActionFailurePolicy](#cfn-ses-mailmanagerruleset-s3action-actionfailurepolicy): {{String}}
  [RoleArn](#cfn-ses-mailmanagerruleset-s3action-rolearn): {{String}}
  [S3Bucket](#cfn-ses-mailmanagerruleset-s3action-s3bucket): {{String}}
  [S3Prefix](#cfn-ses-mailmanagerruleset-s3action-s3prefix): {{String}}
  [S3SseKmsKeyId](#cfn-ses-mailmanagerruleset-s3action-s3ssekmskeyid): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-s3action-properties"></a>

`ActionFailurePolicy`  <a name="cfn-ses-mailmanagerruleset-s3action-actionfailurepolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified the bucket has been deleted.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ses-mailmanagerruleset-s3action-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM Role to use while writing to S3. This role must have access to the s3:PutObject, kms:Encrypt, and kms:GenerateDataKey APIs for the given bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Bucket`  <a name="cfn-ses-mailmanagerruleset-s3action-s3bucket"></a>
The bucket name of the S3 bucket to write to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9.-]+$`
*Minimum*: `1`
*Maximum*: `62`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Prefix`  <a name="cfn-ses-mailmanagerruleset-s3action-s3prefix"></a>
The S3 prefix to use for the write to the s3 bucket.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9!_.*'()/-]+$`
*Minimum*: `1`
*Maximum*: `62`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3SseKmsKeyId`  <a name="cfn-ses-mailmanagerruleset-s3action-s3ssekmskeyid"></a>
The KMS Key ID to use to encrypt the message in S3.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-:/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
