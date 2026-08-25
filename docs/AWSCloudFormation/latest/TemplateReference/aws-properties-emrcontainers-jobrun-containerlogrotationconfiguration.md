---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobrun-containerlogrotationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun ContainerLogRotationConfiguration
<a name="aws-properties-emrcontainers-jobrun-containerlogrotationconfiguration"></a>

The settings for container log rotation.

## Syntax
<a name="aws-properties-emrcontainers-jobrun-containerlogrotationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobrun-containerlogrotationconfiguration-syntax.json"></a>

```
{
  "[MaxFilesToKeep](#cfn-emrcontainers-jobrun-containerlogrotationconfiguration-maxfilestokeep)" : {{Integer}},
  "[RotationSize](#cfn-emrcontainers-jobrun-containerlogrotationconfiguration-rotationsize)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobrun-containerlogrotationconfiguration-syntax.yaml"></a>

```
  [MaxFilesToKeep](#cfn-emrcontainers-jobrun-containerlogrotationconfiguration-maxfilestokeep): {{Integer}}
  [RotationSize](#cfn-emrcontainers-jobrun-containerlogrotationconfiguration-rotationsize): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-jobrun-containerlogrotationconfiguration-properties"></a>

`MaxFilesToKeep`  <a name="cfn-emrcontainers-jobrun-containerlogrotationconfiguration-maxfilestokeep"></a>
The number of files to keep in container after rotation.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RotationSize`  <a name="cfn-emrcontainers-jobrun-containerlogrotationconfiguration-rotationsize"></a>
The file size at which to rotate logs. Minimum of 2KB, Maximum of 2GB.
*Required*: Yes
*Type*: String
*Pattern*: `^\d+(\.\d+)?[KMG][Bb]?$`
*Minimum*: `3`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
