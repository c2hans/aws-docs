---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ResourceDefinition S3MachineLearningModelResourceData
<a name="aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata"></a>

<a name="aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-description"></a>Settings for an Amazon S3 machine learning resource. For more information, see [Perform Machine Learning Inference](https://docs.aws.amazon.com/greengrass/v1/developerguide/ml-inference.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.

<a name="aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-inheritance"></a> In an CloudFormation template, `S3MachineLearningModelResourceData` can be used in the [`ResourceDataContainer`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html) property type.

## Syntax
<a name="aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-syntax.json"></a>

```
{
  "[DestinationPath](#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-destinationpath)" : {{String}},
  "[OwnerSetting](#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-ownersetting)" : {{ResourceDownloadOwnerSetting}},
  "[S3Uri](#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-syntax.yaml"></a>

```
  [DestinationPath](#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-destinationpath): {{String}}
  [OwnerSetting](#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-ownersetting): {{
    ResourceDownloadOwnerSetting}}
  [S3Uri](#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-s3uri): {{String}}
```

## Properties
<a name="aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-properties"></a>

`DestinationPath`  <a name="cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-destinationpath"></a>
The absolute local path of the resource inside the Lambda environment.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OwnerSetting`  <a name="cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-ownersetting"></a>
The owner setting for the downloaded machine learning resource. For more information, see [Access Machine Learning Resources from Lambda Functions](https://docs.aws.amazon.com/greengrass/v1/developerguide/access-ml-resources.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.
*Required*: No
*Type*: [ResourceDownloadOwnerSetting](aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-s3uri"></a>
The URI of the source model in an Amazon S3 bucket. The model package must be in `tar.gz` or `.zip` format.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata--seealso"></a>
+ [S3MachineLearningModelResourceData](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-s3machinelearningmodelresourcedata.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
