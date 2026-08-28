---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-executecommandlogconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Cluster ExecuteCommandLogConfiguration
<a name="aws-properties-ecs-cluster-executecommandlogconfiguration"></a>

The log configuration for the results of the execute command actions. The logs can be sent to CloudWatch Logs or an Amazon S3 bucket.

## Syntax
<a name="aws-properties-ecs-cluster-executecommandlogconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-cluster-executecommandlogconfiguration-syntax.json"></a>

```
{
  "[CloudWatchEncryptionEnabled](#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchencryptionenabled)" : {{Boolean}},
  "[CloudWatchLogGroupName](#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchloggroupname)" : {{String}},
  "[S3BucketName](#cfn-ecs-cluster-executecommandlogconfiguration-s3bucketname)" : {{String}},
  "[S3EncryptionEnabled](#cfn-ecs-cluster-executecommandlogconfiguration-s3encryptionenabled)" : {{Boolean}},
  "[S3KeyPrefix](#cfn-ecs-cluster-executecommandlogconfiguration-s3keyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-cluster-executecommandlogconfiguration-syntax.yaml"></a>

```
  [CloudWatchEncryptionEnabled](#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchencryptionenabled): {{Boolean}}
  [CloudWatchLogGroupName](#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchloggroupname): {{String}}
  [S3BucketName](#cfn-ecs-cluster-executecommandlogconfiguration-s3bucketname): {{String}}
  [S3EncryptionEnabled](#cfn-ecs-cluster-executecommandlogconfiguration-s3encryptionenabled): {{Boolean}}
  [S3KeyPrefix](#cfn-ecs-cluster-executecommandlogconfiguration-s3keyprefix): {{String}}
```

## Properties
<a name="aws-properties-ecs-cluster-executecommandlogconfiguration-properties"></a>

`CloudWatchEncryptionEnabled`  <a name="cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchencryptionenabled"></a>
Determines whether to use encryption on the CloudWatch logs. If not specified, encryption will be off.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CloudWatchLogGroupName`  <a name="cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchloggroupname"></a>
The name of the CloudWatch log group to send logs to.
The CloudWatch log group must already be created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketName`  <a name="cfn-ecs-cluster-executecommandlogconfiguration-s3bucketname"></a>
The name of the S3 bucket to send logs to.
The S3 bucket must already be created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3EncryptionEnabled`  <a name="cfn-ecs-cluster-executecommandlogconfiguration-s3encryptionenabled"></a>
Determines whether to use encryption on the S3 logs. If not specified, encryption is not used.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3KeyPrefix`  <a name="cfn-ecs-cluster-executecommandlogconfiguration-s3keyprefix"></a>
An optional folder in the S3 bucket to place logs in.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-cluster-executecommandlogconfiguration--seealso"></a>
+  [ Define a cluster with the AWS Fargate capacity providers and a default capacity provider strategy defined](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#aws-resource-ecs-cluster--examples--Define_a_cluster_with_the__capacity_providers_and_a_default_capacity_provider_strategy_defined)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
