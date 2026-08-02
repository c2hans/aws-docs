---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-iamconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration IAMConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration"></a>

<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration-description"></a>The `IAMConfiguration` property type specifies Property description not available. for an [AWS::EMRContainers::SecurityConfiguration](aws-resource-emrcontainers-securityconfiguration.md).

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration-syntax.json"></a>

```
{
  "[SystemRole](#cfn-emrcontainers-securityconfiguration-iamconfiguration-systemrole)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration-syntax.yaml"></a>

```
  [SystemRole](#cfn-emrcontainers-securityconfiguration-iamconfiguration-systemrole): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration-properties"></a>

`SystemRole`  <a name="cfn-emrcontainers-securityconfiguration-iamconfiguration-systemrole"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):iam::\d{12}:role/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
