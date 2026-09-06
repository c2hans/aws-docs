---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-containerprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration ContainerProvider
<a name="aws-properties-emrcontainers-securityconfiguration-containerprovider"></a>

The information about the container provider.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-containerprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-containerprovider-syntax.json"></a>

```
{
  "[Id](#cfn-emrcontainers-securityconfiguration-containerprovider-id)" : {{String}},
  "[Info](#cfn-emrcontainers-securityconfiguration-containerprovider-info)" : {{ContainerInfo}},
  "[Type](#cfn-emrcontainers-securityconfiguration-containerprovider-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-containerprovider-syntax.yaml"></a>

```
  [Id](#cfn-emrcontainers-securityconfiguration-containerprovider-id): {{String}}
  [Info](#cfn-emrcontainers-securityconfiguration-containerprovider-info): {{
    ContainerInfo}}
  [Type](#cfn-emrcontainers-securityconfiguration-containerprovider-type): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-containerprovider-properties"></a>

`Id`  <a name="cfn-emrcontainers-securityconfiguration-containerprovider-id"></a>
The ID of the container cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z][A-Za-z0-9\-_]*`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Info`  <a name="cfn-emrcontainers-securityconfiguration-containerprovider-info"></a>
The information about the container cluster.
*Required*: No
*Type*: [ContainerInfo](aws-properties-emrcontainers-securityconfiguration-containerinfo.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-emrcontainers-securityconfiguration-containerprovider-type"></a>
The type of the container provider. Amazon EKS is the only supported type as of now.
*Required*: Yes
*Type*: String
*Allowed values*: `EKS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
