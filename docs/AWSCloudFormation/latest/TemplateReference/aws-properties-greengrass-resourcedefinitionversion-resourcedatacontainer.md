---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ResourceDefinitionVersion ResourceDataContainer
<a name="aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer"></a>

<a name="aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer-description"></a>A container for resource data, which defines the resource type. The container takes only one of the following supported resource data types: `LocalDeviceResourceData`, `LocalVolumeResourceData`, `SageMakerMachineLearningModelResourceData`, `S3MachineLearningModelResourceData`, or `SecretsManagerSecretResourceData`.

**Note**
Only one resource type can be defined for a `ResourceDataContainer` instance.

<a name="aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer-inheritance"></a> In an CloudFormation template, `ResourceDataContainer` is a property of the [`ResourceInstance`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html) property type.

## Syntax
<a name="aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer-syntax.json"></a>

```
{
  "[LocalDeviceResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localdeviceresourcedata)" : {{LocalDeviceResourceData}},
  "[LocalVolumeResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localvolumeresourcedata)" : {{LocalVolumeResourceData}},
  "[S3MachineLearningModelResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-s3machinelearningmodelresourcedata)" : {{S3MachineLearningModelResourceData}},
  "[SageMakerMachineLearningModelResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-sagemakermachinelearningmodelresourcedata)" : {{SageMakerMachineLearningModelResourceData}},
  "[SecretsManagerSecretResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-secretsmanagersecretresourcedata)" : {{SecretsManagerSecretResourceData}}
}
```

### YAML
<a name="aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer-syntax.yaml"></a>

```
  [LocalDeviceResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localdeviceresourcedata): {{
    LocalDeviceResourceData}}
  [LocalVolumeResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localvolumeresourcedata): {{
    LocalVolumeResourceData}}
  [S3MachineLearningModelResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-s3machinelearningmodelresourcedata): {{
    S3MachineLearningModelResourceData}}
  [SageMakerMachineLearningModelResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-sagemakermachinelearningmodelresourcedata): {{
    SageMakerMachineLearningModelResourceData}}
  [SecretsManagerSecretResourceData](#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-secretsmanagersecretresourcedata): {{
    SecretsManagerSecretResourceData}}
```

## Properties
<a name="aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer-properties"></a>

`LocalDeviceResourceData`  <a name="cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localdeviceresourcedata"></a>
Settings for a local device resource.
*Required*: No
*Type*: [LocalDeviceResourceData](aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalVolumeResourceData`  <a name="cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localvolumeresourcedata"></a>
Settings for a local volume resource.
*Required*: No
*Type*: [LocalVolumeResourceData](aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3MachineLearningModelResourceData`  <a name="cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-s3machinelearningmodelresourcedata"></a>
Settings for a machine learning resource stored in Amazon S3.
*Required*: No
*Type*: [S3MachineLearningModelResourceData](aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SageMakerMachineLearningModelResourceData`  <a name="cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-sagemakermachinelearningmodelresourcedata"></a>
Settings for a machine learning resource saved as an SageMaker AI training job.
*Required*: No
*Type*: [SageMakerMachineLearningModelResourceData](aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecretsManagerSecretResourceData`  <a name="cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-secretsmanagersecretresourcedata"></a>
Settings for a secret resource.
*Required*: No
*Type*: [SecretsManagerSecretResourceData](aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer--seealso"></a>
+ [ResourceDataContainer](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resourcedatacontainer.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)
