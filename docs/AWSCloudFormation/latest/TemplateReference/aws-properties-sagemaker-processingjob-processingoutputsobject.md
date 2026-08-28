---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-processingoutputsobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob ProcessingOutputsObject
<a name="aws-properties-sagemaker-processingjob-processingoutputsobject"></a>

Describes the results of a processing job. The processing output must specify exactly one of either `S3Output` or `FeatureStoreOutput` types.

## Syntax
<a name="aws-properties-sagemaker-processingjob-processingoutputsobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-processingoutputsobject-syntax.json"></a>

```
{
  "[AppManaged](#cfn-sagemaker-processingjob-processingoutputsobject-appmanaged)" : {{Boolean}},
  "[FeatureStoreOutput](#cfn-sagemaker-processingjob-processingoutputsobject-featurestoreoutput)" : {{FeatureStoreOutput}},
  "[OutputName](#cfn-sagemaker-processingjob-processingoutputsobject-outputname)" : {{String}},
  "[S3Output](#cfn-sagemaker-processingjob-processingoutputsobject-s3output)" : {{S3Output}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-processingoutputsobject-syntax.yaml"></a>

```
  [AppManaged](#cfn-sagemaker-processingjob-processingoutputsobject-appmanaged): {{Boolean}}
  [FeatureStoreOutput](#cfn-sagemaker-processingjob-processingoutputsobject-featurestoreoutput): {{
    FeatureStoreOutput}}
  [OutputName](#cfn-sagemaker-processingjob-processingoutputsobject-outputname): {{String}}
  [S3Output](#cfn-sagemaker-processingjob-processingoutputsobject-s3output): {{
    S3Output}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-processingoutputsobject-properties"></a>

`AppManaged`  <a name="cfn-sagemaker-processingjob-processingoutputsobject-appmanaged"></a>
When `True`, output operations such as data upload are managed natively by the processing job application. When `False` (default), output operations are managed by Amazon SageMaker.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FeatureStoreOutput`  <a name="cfn-sagemaker-processingjob-processingoutputsobject-featurestoreoutput"></a>
Configuration for processing job outputs in Amazon SageMaker Feature Store.
*Required*: No
*Type*: [FeatureStoreOutput](aws-properties-sagemaker-processingjob-featurestoreoutput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputName`  <a name="cfn-sagemaker-processingjob-processingoutputsobject-outputname"></a>
The name for the processing job output.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Output`  <a name="cfn-sagemaker-processingjob-processingoutputsobject-s3output"></a>
Configuration for uploading output data to Amazon S3 from the processing container.
*Required*: No
*Type*: [S3Output](aws-properties-sagemaker-processingjob-s3output.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
