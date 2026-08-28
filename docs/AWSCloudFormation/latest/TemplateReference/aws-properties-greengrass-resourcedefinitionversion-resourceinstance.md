---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ResourceDefinitionVersion ResourceInstance
<a name="aws-properties-greengrass-resourcedefinitionversion-resourceinstance"></a>

<a name="aws-properties-greengrass-resourcedefinitionversion-resourceinstance-description"></a>A local resource, machine learning resource, or secret resource. For more information, see [Access Local Resources with Lambda Functions](https://docs.aws.amazon.com/greengrass/v1/developerguide/access-local-resources.html), [Perform Machine Learning Inference](https://docs.aws.amazon.com/greengrass/v1/developerguide/ml-inference.html), and [Deploy Secrets to the AWS IoT Greengrass Core](https://docs.aws.amazon.com/greengrass/v1/developerguide/secrets.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.

<a name="aws-properties-greengrass-resourcedefinitionversion-resourceinstance-inheritance"></a> In an CloudFormation template, the `Resources` property of the [`AWS::Greengrass::ResourceDefinitionVersion`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html) resource contains a list of `ResourceInstance` property types.

## Syntax
<a name="aws-properties-greengrass-resourcedefinitionversion-resourceinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-resourcedefinitionversion-resourceinstance-syntax.json"></a>

```
{
  "[Id](#cfn-greengrass-resourcedefinitionversion-resourceinstance-id)" : {{String}},
  "[Name](#cfn-greengrass-resourcedefinitionversion-resourceinstance-name)" : {{String}},
  "[ResourceDataContainer](#cfn-greengrass-resourcedefinitionversion-resourceinstance-resourcedatacontainer)" : {{ResourceDataContainer}}
}
```

### YAML
<a name="aws-properties-greengrass-resourcedefinitionversion-resourceinstance-syntax.yaml"></a>

```
  [Id](#cfn-greengrass-resourcedefinitionversion-resourceinstance-id): {{String}}
  [Name](#cfn-greengrass-resourcedefinitionversion-resourceinstance-name): {{String}}
  [ResourceDataContainer](#cfn-greengrass-resourcedefinitionversion-resourceinstance-resourcedatacontainer): {{
    ResourceDataContainer}}
```

## Properties
<a name="aws-properties-greengrass-resourcedefinitionversion-resourceinstance-properties"></a>

`Id`  <a name="cfn-greengrass-resourcedefinitionversion-resourceinstance-id"></a>
A descriptive or arbitrary ID for the resource. This value must be unique within the resource definition version. Maximum length is 128 characters with pattern `[a-zA-Z0-9:_-]+`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-greengrass-resourcedefinitionversion-resourceinstance-name"></a>
The descriptive resource name, which is displayed on the AWS IoT Greengrass console. Maximum length 128 characters with pattern [a-zA-Z0-9:\_-]\+. This must be unique within a Greengrass group.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceDataContainer`  <a name="cfn-greengrass-resourcedefinitionversion-resourceinstance-resourcedatacontainer"></a>
A container for resource data. The container takes only one of the following supported resource data types: `LocalDeviceResourceData`, `LocalVolumeResourceData`, `SageMakerMachineLearningModelResourceData`, `S3MachineLearningModelResourceData`, or `SecretsManagerSecretResourceData`.
Only one resource type can be defined for a `ResourceDataContainer` instance.
*Required*: Yes
*Type*: [ResourceDataContainer](aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-resourcedefinitionversion-resourceinstance--seealso"></a>
+ [Resource](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resource.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
