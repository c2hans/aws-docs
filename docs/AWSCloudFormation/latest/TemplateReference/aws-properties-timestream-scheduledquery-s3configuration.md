---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-s3configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery S3Configuration
<a name="aws-properties-timestream-scheduledquery-s3configuration"></a>

Details on S3 location for error reports that result from running a query.

## Syntax
<a name="aws-properties-timestream-scheduledquery-s3configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-s3configuration-syntax.json"></a>

```
{
  "[BucketName](#cfn-timestream-scheduledquery-s3configuration-bucketname)" : {{String}},
  "[EncryptionOption](#cfn-timestream-scheduledquery-s3configuration-encryptionoption)" : {{String}},
  "[ObjectKeyPrefix](#cfn-timestream-scheduledquery-s3configuration-objectkeyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-s3configuration-syntax.yaml"></a>

```
  [BucketName](#cfn-timestream-scheduledquery-s3configuration-bucketname): {{String}}
  [EncryptionOption](#cfn-timestream-scheduledquery-s3configuration-encryptionoption): {{String}}
  [ObjectKeyPrefix](#cfn-timestream-scheduledquery-s3configuration-objectkeyprefix): {{String}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-s3configuration-properties"></a>

`BucketName`  <a name="cfn-timestream-scheduledquery-s3configuration-bucketname"></a>
 Name of the S3 bucket under which error reports will be created.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionOption`  <a name="cfn-timestream-scheduledquery-s3configuration-encryptionoption"></a>
 Encryption at rest options for the error reports. If no encryption option is specified, Timestream will choose SSE\_S3 as default.
*Required*: No
*Type*: String
*Allowed values*: `SSE_S3 | SSE_KMS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ObjectKeyPrefix`  <a name="cfn-timestream-scheduledquery-s3configuration-objectkeyprefix"></a>
 Prefix for the error report key. Timestream by default adds the following prefix to the error report path.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`
*Minimum*: `1`
*Maximum*: `896`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
