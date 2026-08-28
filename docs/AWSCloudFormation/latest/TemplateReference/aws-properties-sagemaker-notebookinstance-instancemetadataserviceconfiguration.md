---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::NotebookInstance InstanceMetadataServiceConfiguration
<a name="aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration"></a>

Information on the IMDS configuration of the notebook instance

## Syntax
<a name="aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration-syntax.json"></a>

```
{
  "[MinimumInstanceMetadataServiceVersion](#cfn-sagemaker-notebookinstance-instancemetadataserviceconfiguration-minimuminstancemetadataserviceversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration-syntax.yaml"></a>

```
  [MinimumInstanceMetadataServiceVersion](#cfn-sagemaker-notebookinstance-instancemetadataserviceconfiguration-minimuminstancemetadataserviceversion): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration-properties"></a>

`MinimumInstanceMetadataServiceVersion`  <a name="cfn-sagemaker-notebookinstance-instancemetadataserviceconfiguration-minimuminstancemetadataserviceversion"></a>
Indicates the minimum IMDS version that the notebook instance supports. When passed as part of `CreateNotebookInstance`, if no value is selected, then it defaults to IMDSv1. This means that both IMDSv1 and IMDSv2 are supported. If passed as part of `UpdateNotebookInstance`, there is no default.
*Required*: Yes
*Type*: String
*Pattern*: `1|2`
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
