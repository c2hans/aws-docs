---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-automatedreasoningpolicyversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AutomatedReasoningPolicyVersion
<a name="aws-resource-bedrock-automatedreasoningpolicyversion"></a>

Creates a new version of an existing Automated Reasoning policy. This allows you to iterate on your policy rules while maintaining previous versions for rollback or comparison purposes.

## Syntax
<a name="aws-resource-bedrock-automatedreasoningpolicyversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-automatedreasoningpolicyversion-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::AutomatedReasoningPolicyVersion",
  "Properties" : {
      "[LastUpdatedDefinitionHash](#cfn-bedrock-automatedreasoningpolicyversion-lastupdateddefinitionhash)" : {{String}},
      "[PolicyArn](#cfn-bedrock-automatedreasoningpolicyversion-policyarn)" : {{String}},
      "[Tags](#cfn-bedrock-automatedreasoningpolicyversion-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-automatedreasoningpolicyversion-syntax.yaml"></a>

```
Type: AWS::Bedrock::AutomatedReasoningPolicyVersion
Properties:
  [LastUpdatedDefinitionHash](#cfn-bedrock-automatedreasoningpolicyversion-lastupdateddefinitionhash): {{String}}
  [PolicyArn](#cfn-bedrock-automatedreasoningpolicyversion-policyarn): {{String}}
  [Tags](#cfn-bedrock-automatedreasoningpolicyversion-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrock-automatedreasoningpolicyversion-properties"></a>

`LastUpdatedDefinitionHash`  <a name="cfn-bedrock-automatedreasoningpolicyversion-lastupdateddefinitionhash"></a>
The hash of the policy definition that was last updated.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-z]{128}$`
*Minimum*: `128`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyArn`  <a name="cfn-bedrock-automatedreasoningpolicyversion-policyarn"></a>
The Amazon Resource Name (ARN) of the policy.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy\/[a-z0-9]{12}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrock-automatedreasoningpolicyversion-tags"></a>
The tags associated with the Automated Reasoning policy version.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-automatedreasoningpolicyversion-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrock-automatedreasoningpolicyversion-return-values"></a>

### Ref
<a name="aws-resource-bedrock-automatedreasoningpolicyversion-return-values-ref"></a>

Returns the policy version ID.

### Fn::GetAtt
<a name="aws-resource-bedrock-automatedreasoningpolicyversion-return-values-fn--getatt"></a>

Returns the value of an attribute from a resource in the template.

####
<a name="aws-resource-bedrock-automatedreasoningpolicyversion-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the policy version was created.

`DefinitionHash`  <a name="DefinitionHash-fn::getatt"></a>
A hash of the policy definition used to identify the version.

`Description`  <a name="Description-fn::getatt"></a>
The description of the policy version.

`Name`  <a name="Name-fn::getatt"></a>
The name of the policy version.

`PolicyId`  <a name="PolicyId-fn::getatt"></a>
The unique identifier of the policy.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the policy version was last updated.

`Version`  <a name="Version-fn::getatt"></a>
The version number of the policy version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
