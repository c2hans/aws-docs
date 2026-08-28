---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-processingresources.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob ProcessingResources
<a name="aws-properties-sagemaker-processingjob-processingresources"></a>

Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.

## Syntax
<a name="aws-properties-sagemaker-processingjob-processingresources-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-processingresources-syntax.json"></a>

```
{
  "[ClusterConfig](#cfn-sagemaker-processingjob-processingresources-clusterconfig)" : {{ClusterConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-processingresources-syntax.yaml"></a>

```
  [ClusterConfig](#cfn-sagemaker-processingjob-processingresources-clusterconfig): {{
    ClusterConfig}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-processingresources-properties"></a>

`ClusterConfig`  <a name="cfn-sagemaker-processingjob-processingresources-clusterconfig"></a>
The configuration for the resources in a cluster used to run the processing job.
*Required*: Yes
*Type*: [ClusterConfig](aws-properties-sagemaker-processingjob-clusterconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
