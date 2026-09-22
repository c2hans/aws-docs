---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityagent-securityrequirementpack.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::SecurityRequirementPack
<a name="aws-resource-securityagent-securityrequirementpack"></a>

The `AWS::SecurityAgent::SecurityRequirementPack` resource specifies a security requirement pack. A security requirement pack is a collection of security requirements that define evaluation criteria and remediation guidance for security testing.

## Syntax
<a name="aws-resource-securityagent-securityrequirementpack-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityagent-securityrequirementpack-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityAgent::SecurityRequirementPack",
  "Properties" : {
      "[Description](#cfn-securityagent-securityrequirementpack-description)" : {{String}},
      "[KmsKeyId](#cfn-securityagent-securityrequirementpack-kmskeyid)" : {{String}},
      "[Name](#cfn-securityagent-securityrequirementpack-name)" : {{String}},
      "[SecurityRequirements](#cfn-securityagent-securityrequirementpack-securityrequirements)" : {{[ SecurityRequirement, ... ]}},
      "[Status](#cfn-securityagent-securityrequirementpack-status)" : {{String}},
      "[Tags](#cfn-securityagent-securityrequirementpack-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-securityagent-securityrequirementpack-syntax.yaml"></a>

```
Type: AWS::SecurityAgent::SecurityRequirementPack
Properties:
  [Description](#cfn-securityagent-securityrequirementpack-description): {{String}}
  [KmsKeyId](#cfn-securityagent-securityrequirementpack-kmskeyid): {{String}}
  [Name](#cfn-securityagent-securityrequirementpack-name): {{String}}
  [SecurityRequirements](#cfn-securityagent-securityrequirementpack-securityrequirements): {{
    - SecurityRequirement}}
  [Status](#cfn-securityagent-securityrequirementpack-status): {{String}}
  [Tags](#cfn-securityagent-securityrequirementpack-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-securityagent-securityrequirementpack-properties"></a>

`Description`  <a name="cfn-securityagent-securityrequirementpack-description"></a>
A description of the security requirement pack.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-securityagent-securityrequirementpack-kmskeyid"></a>
The identifier of the Amazon Web Services KMS key to use for encrypting data in the security requirement pack. This property can only be specified during creation.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-securityagent-securityrequirementpack-name"></a>
The name of the security requirement pack.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityRequirements`  <a name="cfn-securityagent-securityrequirementpack-securityrequirements"></a>
Property description not available.
*Required*: No
*Type*: Array of [SecurityRequirement](aws-properties-securityagent-securityrequirementpack-securityrequirement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-securityagent-securityrequirementpack-status"></a>
The status of the pack. Defaults to ENABLED if not provided.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityagent-securityrequirementpack-tags"></a>
The tags to associate with the security requirement pack.
*Required*: No
*Type*: Array of [Tag](aws-properties-securityagent-securityrequirementpack-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityagent-securityrequirementpack-return-values"></a>

### Ref
<a name="aws-resource-securityagent-securityrequirementpack-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the pack ID. For example:

 `{ "Ref": "MySecurityRequirementPack" }`

For the security requirement pack `MySecurityRequirementPack`, `Ref` returns the unique identifier of the pack.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityagent-securityrequirementpack-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityagent-securityrequirementpack-return-values-fn--getatt-fn--getatt"></a>

`PackId`  <a name="PackId-fn::getatt"></a>
The unique identifier of the security requirement pack. For example: `srp-cm-0123456789abcdef0`.
