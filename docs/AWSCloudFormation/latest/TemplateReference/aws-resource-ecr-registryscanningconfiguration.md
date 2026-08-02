---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecr-registryscanningconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::RegistryScanningConfiguration
<a name="aws-resource-ecr-registryscanningconfiguration"></a>

The scanning configuration for a private registry.

## Syntax
<a name="aws-resource-ecr-registryscanningconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecr-registryscanningconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::ECR::RegistryScanningConfiguration",
  "Properties" : {
      "[Rules](#cfn-ecr-registryscanningconfiguration-rules)" : {{[ ScanningRule, ... ]}},
      "[ScanType](#cfn-ecr-registryscanningconfiguration-scantype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ecr-registryscanningconfiguration-syntax.yaml"></a>

```
Type: AWS::ECR::RegistryScanningConfiguration
Properties:
  [Rules](#cfn-ecr-registryscanningconfiguration-rules): {{
    - ScanningRule}}
  [ScanType](#cfn-ecr-registryscanningconfiguration-scantype): {{String}}
```

## Properties
<a name="aws-resource-ecr-registryscanningconfiguration-properties"></a>

`Rules`  <a name="cfn-ecr-registryscanningconfiguration-rules"></a>
The scanning rules associated with the registry.
*Required*: Yes
*Type*: Array of [ScanningRule](aws-properties-ecr-registryscanningconfiguration-scanningrule.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScanType`  <a name="cfn-ecr-registryscanningconfiguration-scantype"></a>
The type of scanning configured for the registry.
*Required*: Yes
*Type*: String
*Allowed values*: `BASIC | ENHANCED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ecr-registryscanningconfiguration-return-values"></a>

### Ref
<a name="aws-resource-ecr-registryscanningconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ecr-registryscanningconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-ecr-registryscanningconfiguration-return-values-fn--getatt-fn--getatt"></a>

`RegistryId`  <a name="RegistryId-fn::getatt"></a>
The account ID of the destination registry.
