---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityagent-securityrequirementpack.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::SecurityRequirementPack
<a name="aws-resource-securityagent-securityrequirementpack"></a>

Creates a customer managed security requirement pack.

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
Identifier of a KMS key. Can be a key ID, key ARN, alias name, or alias ARN.
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
The status of the security requirement pack.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityagent-securityrequirementpack-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-securityagent-securityrequirementpack-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityagent-securityrequirementpack-return-values"></a>

### Ref
<a name="aws-resource-securityagent-securityrequirementpack-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-securityagent-securityrequirementpack-return-values-fn--getatt"></a>

####
<a name="aws-resource-securityagent-securityrequirementpack-return-values-fn--getatt-fn--getatt"></a>

`PackId`  <a name="PackId-fn::getatt"></a>
The unique identifier of the security requirement pack.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
