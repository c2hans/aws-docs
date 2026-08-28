---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-replicationtimevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket ReplicationTimeValue
<a name="aws-properties-s3-bucket-replicationtimevalue"></a>

 A container specifying the time value for S3 Replication Time Control (S3 RTC) and replication metrics `EventThreshold`.

## Syntax
<a name="aws-properties-s3-bucket-replicationtimevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-replicationtimevalue-syntax.json"></a>

```
{
  "[Minutes](#cfn-s3-bucket-replicationtimevalue-minutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3-bucket-replicationtimevalue-syntax.yaml"></a>

```
  [Minutes](#cfn-s3-bucket-replicationtimevalue-minutes): {{Integer}}
```

## Properties
<a name="aws-properties-s3-bucket-replicationtimevalue-properties"></a>

`Minutes`  <a name="cfn-s3-bucket-replicationtimevalue-minutes"></a>
 Contains an integer specifying time in minutes.
 Valid value: 15
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
