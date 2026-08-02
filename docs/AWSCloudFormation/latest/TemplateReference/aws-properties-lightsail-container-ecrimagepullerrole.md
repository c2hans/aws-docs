---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-container-ecrimagepullerrole.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Container EcrImagePullerRole
<a name="aws-properties-lightsail-container-ecrimagepullerrole"></a>

Describes the IAM role that you can use to grant a Lightsail container service access to Amazon ECR private repositories.

## Syntax
<a name="aws-properties-lightsail-container-ecrimagepullerrole-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-container-ecrimagepullerrole-syntax.json"></a>

```
{
  "[IsActive](#cfn-lightsail-container-ecrimagepullerrole-isactive)" : {{Boolean}},
  "[PrincipalArn](#cfn-lightsail-container-ecrimagepullerrole-principalarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-container-ecrimagepullerrole-syntax.yaml"></a>

```
  [IsActive](#cfn-lightsail-container-ecrimagepullerrole-isactive): {{Boolean}}
  [PrincipalArn](#cfn-lightsail-container-ecrimagepullerrole-principalarn): {{String}}
```

## Properties
<a name="aws-properties-lightsail-container-ecrimagepullerrole-properties"></a>

`IsActive`  <a name="cfn-lightsail-container-ecrimagepullerrole-isactive"></a>
A boolean value that indicates whether the `ECRImagePullerRole` is active.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrincipalArn`  <a name="cfn-lightsail-container-ecrimagepullerrole-principalarn"></a>
The principle Amazon Resource Name (ARN) of the role. This property is read-only.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
