---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-datalake-replicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::DataLake ReplicationConfiguration
<a name="aws-properties-securitylake-datalake-replicationconfiguration"></a>

Provides replication configuration details for objects stored in the Amazon Security Lake data lake.

## Syntax
<a name="aws-properties-securitylake-datalake-replicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-datalake-replicationconfiguration-syntax.json"></a>

```
{
  "[Regions](#cfn-securitylake-datalake-replicationconfiguration-regions)" : {{[ String, ... ]}},
  "[RoleArn](#cfn-securitylake-datalake-replicationconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-securitylake-datalake-replicationconfiguration-syntax.yaml"></a>

```
  [Regions](#cfn-securitylake-datalake-replicationconfiguration-regions): {{
    - String}}
  [RoleArn](#cfn-securitylake-datalake-replicationconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-securitylake-datalake-replicationconfiguration-properties"></a>

`Regions`  <a name="cfn-securitylake-datalake-replicationconfiguration-regions"></a>
Specifies one or more centralized rollup Regions. The AWS Region specified in the region parameter of the `CreateDataLake` or `UpdateDataLake` operations contributes data to the rollup Region or Regions specified in this parameter.
 Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. S3 buckets that are configured for object replication can be owned by the same AWS account or by different accounts. You can replicate objects to a single destination bucket or to multiple destination buckets. The destination buckets can be in different Regions or within the same Region as the source bucket.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-securitylake-datalake-replicationconfiguration-rolearn"></a>
Replication settings for the Amazon S3 buckets. This parameter uses the AWS Identity and Access Management (IAM) role you created that is managed by Security Lake, to ensure the replication setting is correct.
*Required*: No
*Type*: String
*Pattern*: `^arn:.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
