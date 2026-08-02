---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-emrsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile EmrSettings
<a name="aws-properties-sagemaker-userprofile-emrsettings"></a>

The configuration parameters that specify the IAM roles assumed by the execution role of SageMaker (assumable roles) and the cluster instances or job execution environments (execution roles or runtime roles) to manage and access resources required for running Amazon EMR clusters or Amazon EMR Serverless applications.

## Syntax
<a name="aws-properties-sagemaker-userprofile-emrsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-emrsettings-syntax.json"></a>

```
{
  "[AssumableRoleArns](#cfn-sagemaker-userprofile-emrsettings-assumablerolearns)" : {{[ String, ... ]}},
  "[ExecutionRoleArns](#cfn-sagemaker-userprofile-emrsettings-executionrolearns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-emrsettings-syntax.yaml"></a>

```
  [AssumableRoleArns](#cfn-sagemaker-userprofile-emrsettings-assumablerolearns): {{
    - String}}
  [ExecutionRoleArns](#cfn-sagemaker-userprofile-emrsettings-executionrolearns): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-emrsettings-properties"></a>

`AssumableRoleArns`  <a name="cfn-sagemaker-userprofile-emrsettings-assumablerolearns"></a>
An array of Amazon Resource Names (ARNs) of the IAM roles that the execution role of SageMaker can assume for performing operations or tasks related to Amazon EMR clusters or Amazon EMR Serverless applications. These roles define the permissions and access policies required when performing Amazon EMR-related operations, such as listing, connecting to, or terminating Amazon EMR clusters or Amazon EMR Serverless applications. They are typically used in cross-account access scenarios, where the Amazon EMR resources (clusters or serverless applications) are located in a different AWS account than the SageMaker domain.
*Required*: No
*Type*: Array of String
*Minimum*: `20 | 0`
*Maximum*: `2048 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArns`  <a name="cfn-sagemaker-userprofile-emrsettings-executionrolearns"></a>
An array of Amazon Resource Names (ARNs) of the IAM roles used by the Amazon EMR cluster instances or job execution environments to access other AWS services and resources needed during the runtime of your Amazon EMR or Amazon EMR Serverless workloads, such as Amazon S3 for data access, Amazon CloudWatch for logging, or other AWS services based on the particular workload requirements.
*Required*: No
*Type*: Array of String
*Minimum*: `20 | 0`
*Maximum*: `2048 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
