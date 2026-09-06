---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecr-signingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::SigningConfiguration
<a name="aws-resource-ecr-signingconfiguration"></a>

The signing configuration for a registry, which specifies rules for automatically signing images when pushed.

## Syntax
<a name="aws-resource-ecr-signingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecr-signingconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::ECR::SigningConfiguration",
  "Properties" : {
      "[Rules](#cfn-ecr-signingconfiguration-rules)" : {{[ Rule, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ecr-signingconfiguration-syntax.yaml"></a>

```
Type: AWS::ECR::SigningConfiguration
Properties:
  [Rules](#cfn-ecr-signingconfiguration-rules): {{
    - Rule}}
```

## Properties
<a name="aws-resource-ecr-signingconfiguration-properties"></a>

`Rules`  <a name="cfn-ecr-signingconfiguration-rules"></a>
A list of signing rules. Each rule defines a signing profile and optional repository filters that determine which images are automatically signed.
*Required*: Yes
*Type*: Array of [Rule](aws-properties-ecr-signingconfiguration-rule.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ecr-signingconfiguration-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-ecr-signingconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ecr-signingconfiguration-return-values-fn--getatt-fn--getatt"></a>

`RegistryId`  <a name="RegistryId-fn::getatt"></a>
The account ID of the destination registry.
