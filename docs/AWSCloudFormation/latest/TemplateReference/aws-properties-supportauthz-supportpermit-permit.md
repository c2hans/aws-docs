---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-supportauthz-supportpermit-permit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SupportAuthZ::SupportPermit Permit
<a name="aws-properties-supportauthz-supportpermit-permit"></a>

The grant definition for a support permit: the actions AWS Support is authorized to perform, the resources they apply to, and optional time-window conditions. `Permit` is a property of the [AWS::SupportAuthZ::SupportPermit](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-supportauthz-supportpermit.html) resource.

## Syntax
<a name="aws-properties-supportauthz-supportpermit-permit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-supportauthz-supportpermit-permit-syntax.json"></a>

```
{
  "[Actions](#cfn-supportauthz-supportpermit-permit-actions)" : {{ActionSet}},
  "[Conditions](#cfn-supportauthz-supportpermit-permit-conditions)" : {{[ Condition, ... ]}},
  "[Resources](#cfn-supportauthz-supportpermit-permit-resources)" : {{ResourceSet}}
}
```

### YAML
<a name="aws-properties-supportauthz-supportpermit-permit-syntax.yaml"></a>

```
  [Actions](#cfn-supportauthz-supportpermit-permit-actions): {{
    ActionSet}}
  [Conditions](#cfn-supportauthz-supportpermit-permit-conditions): {{
    - Condition}}
  [Resources](#cfn-supportauthz-supportpermit-permit-resources): {{
    ResourceSet}}
```

## Properties
<a name="aws-properties-supportauthz-supportpermit-permit-properties"></a>

`Actions`  <a name="cfn-supportauthz-supportpermit-permit-actions"></a>
The set of actions the permit grants.
*Required*: Yes
*Type*: [ActionSet](aws-properties-supportauthz-supportpermit-actionset.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Conditions`  <a name="cfn-supportauthz-supportpermit-permit-conditions"></a>
Optional time-window conditions that control when the permit is active. You can specify up to two conditions.
*Required*: No
*Type*: Array of [Condition](aws-properties-supportauthz-supportpermit-condition.md)
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Resources`  <a name="cfn-supportauthz-supportpermit-permit-resources"></a>
The set of resources the granted actions apply to.
*Required*: Yes
*Type*: [ResourceSet](aws-properties-supportauthz-supportpermit-resourceset.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
