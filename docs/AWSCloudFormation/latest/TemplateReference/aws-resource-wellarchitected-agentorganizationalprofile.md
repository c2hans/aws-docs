---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wellarchitected-agentorganizationalprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::AgentOrganizationalProfile
<a name="aws-resource-wellarchitected-agentorganizationalprofile"></a>

Creates an Organizational Profile for use with AWS Organizations integration. Organizational Profiles are scoped to an organization in AWS Organizations and do not require an execution role or aggregation configuration. The organization is inferred from the caller's identity.

## Syntax
<a name="aws-resource-wellarchitected-agentorganizationalprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wellarchitected-agentorganizationalprofile-syntax.json"></a>

```
{
  "Type" : "AWS::WellArchitected::AgentOrganizationalProfile",
  "Properties" : {
      "[BusinessOverview](#cfn-wellarchitected-agentorganizationalprofile-businessoverview)" : {{String}},
      "[DeletionProtection](#cfn-wellarchitected-agentorganizationalprofile-deletionprotection)" : {{Boolean}},
      "[Description](#cfn-wellarchitected-agentorganizationalprofile-description)" : {{String}},
      "[DisplayName](#cfn-wellarchitected-agentorganizationalprofile-displayname)" : {{String}},
      "[Name](#cfn-wellarchitected-agentorganizationalprofile-name)" : {{String}},
      "[Pillars](#cfn-wellarchitected-agentorganizationalprofile-pillars)" : {{[ String, ... ]}},
      "[Tags](#cfn-wellarchitected-agentorganizationalprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wellarchitected-agentorganizationalprofile-syntax.yaml"></a>

```
Type: AWS::WellArchitected::AgentOrganizationalProfile
Properties:
  [BusinessOverview](#cfn-wellarchitected-agentorganizationalprofile-businessoverview): {{String}}
  [DeletionProtection](#cfn-wellarchitected-agentorganizationalprofile-deletionprotection): {{Boolean}}
  [Description](#cfn-wellarchitected-agentorganizationalprofile-description): {{String}}
  [DisplayName](#cfn-wellarchitected-agentorganizationalprofile-displayname): {{String}}
  [Name](#cfn-wellarchitected-agentorganizationalprofile-name): {{String}}
  [Pillars](#cfn-wellarchitected-agentorganizationalprofile-pillars): {{
    - String}}
  [Tags](#cfn-wellarchitected-agentorganizationalprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-wellarchitected-agentorganizationalprofile-properties"></a>

`BusinessOverview`  <a name="cfn-wellarchitected-agentorganizationalprofile-businessoverview"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtection`  <a name="cfn-wellarchitected-agentorganizationalprofile-deletionprotection"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-wellarchitected-agentorganizationalprofile-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-wellarchitected-agentorganizationalprofile-displayname"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wellarchitected-agentorganizationalprofile-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `3`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Pillars`  <a name="cfn-wellarchitected-agentorganizationalprofile-pillars"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-wellarchitected-agentorganizationalprofile-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-wellarchitected-agentorganizationalprofile-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wellarchitected-agentorganizationalprofile-return-values"></a>

### Ref
<a name="aws-resource-wellarchitected-agentorganizationalprofile-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wellarchitected-agentorganizationalprofile-return-values-fn--getatt"></a>

####
<a name="aws-resource-wellarchitected-agentorganizationalprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
Property description not available.

`LastModifiedAt`  <a name="LastModifiedAt-fn::getatt"></a>
Property description not available.

`LastModifiedBy`  <a name="LastModifiedBy-fn::getatt"></a>
Property description not available.
