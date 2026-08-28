---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelExplainabilityJobDefinition MonitoringResources
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources"></a>

Identifies the resources to deploy for a monitoring job.

## Syntax
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources-syntax.json"></a>

```
{
  "[ClusterConfig](#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringresources-clusterconfig)" : {{ClusterConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources-syntax.yaml"></a>

```
  [ClusterConfig](#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringresources-clusterconfig): {{
    ClusterConfig}}
```

## Properties
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources-properties"></a>

`ClusterConfig`  <a name="cfn-sagemaker-modelexplainabilityjobdefinition-monitoringresources-clusterconfig"></a>
The configuration for the cluster resources used to run the processing job.
*Required*: Yes
*Type*: [ClusterConfig](aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
