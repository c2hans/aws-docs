---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wellarchitected-agentcontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::AgentContext
<a name="aws-resource-wellarchitected-agentcontext"></a>

**Note**
AWS Well-Architected Agent is in preview release and is subject to change.

Creates a context associated with an optimization profile. Contexts provide application and environment information used during recommendation generation.

## Syntax
<a name="aws-resource-wellarchitected-agentcontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wellarchitected-agentcontext-syntax.json"></a>

```
{
  "Type" : "AWS::WellArchitected::AgentContext",
  "Properties" : {
      "[Content](#cfn-wellarchitected-agentcontext-content)" : {{Json}},
      "[ContextType](#cfn-wellarchitected-agentcontext-contexttype)" : {{String}},
      "[ProfileArn](#cfn-wellarchitected-agentcontext-profilearn)" : {{String}},
      "[Title](#cfn-wellarchitected-agentcontext-title)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wellarchitected-agentcontext-syntax.yaml"></a>

```
Type: AWS::WellArchitected::AgentContext
Properties:
  [Content](#cfn-wellarchitected-agentcontext-content): {{Json}}
  [ContextType](#cfn-wellarchitected-agentcontext-contexttype): {{String}}
  [ProfileArn](#cfn-wellarchitected-agentcontext-profilearn): {{String}}
  [Title](#cfn-wellarchitected-agentcontext-title): {{String}}
```

## Properties
<a name="aws-resource-wellarchitected-agentcontext-properties"></a>

`Content`  <a name="cfn-wellarchitected-agentcontext-content"></a>
The free-form content of the agent context, supplied as a JSON object. This content provides supplemental application information used to improve recommendation quality.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContextType`  <a name="cfn-wellarchitected-agentcontext-contexttype"></a>
The type of the agent context. Valid value: `APPLICATION`.
*Required*: Yes
*Type*: String
*Allowed values*: `APPLICATION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileArn`  <a name="cfn-wellarchitected-agentcontext-profilearn"></a>
The Amazon Resource Name (ARN) of the parent agent profile that owns this context.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:[0-9]{12}:agent-profile/[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Title`  <a name="cfn-wellarchitected-agentcontext-title"></a>
The title of the agent context.
*Required*: Yes
*Type*: String
*Pattern*: `^[\P{C}]+$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wellarchitected-agentcontext-return-values"></a>

### Ref
<a name="aws-resource-wellarchitected-agentcontext-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the agent context ARN.

### Fn::GetAtt
<a name="aws-resource-wellarchitected-agentcontext-return-values-fn--getatt"></a>

####
<a name="aws-resource-wellarchitected-agentcontext-return-values-fn--getatt-fn--getatt"></a>

`ApplicationType`  <a name="ApplicationType-fn::getatt"></a>
The type of the application described by this context. Valid values: `SAS` \| `DESKTOP_APPLICATION` \| `OTHER`.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the agent context.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the context was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The identifier of the system or user that created this context.

`Criticality`  <a name="Criticality-fn::getatt"></a>
The business criticality of the application described by this context. Valid values: `MISSION_CRITICAL` \| `BUSINESS_CRITICAL` \| `NON_CRITICAL` \| `TEST_DEVELOPMENT`.

`Id`  <a name="Id-fn::getatt"></a>
The service-generated unique identifier of the agent context.

`LastModifiedAt`  <a name="LastModifiedAt-fn::getatt"></a>
The timestamp when the context was last modified.

`LastModifiedBy`  <a name="LastModifiedBy-fn::getatt"></a>
The identifier of the system or user that last modified this context.
