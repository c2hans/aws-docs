---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssmquicksetup-lifecycleautomation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMQuickSetup::LifecycleAutomation
<a name="aws-resource-ssmquicksetup-lifecycleautomation"></a>

Creates a lifecycle automation resource that executes SSM Automation documents during CloudFormation stack operations. This resource replaces inline AWS Lambda custom resources and provides a managed way to handle lifecycle events in Quick Setup configurations.

## Syntax
<a name="aws-resource-ssmquicksetup-lifecycleautomation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssmquicksetup-lifecycleautomation-syntax.json"></a>

```
{
  "Type" : "AWS::SSMQuickSetup::LifecycleAutomation",
  "Properties" : {
      "[AutomationDocument](#cfn-ssmquicksetup-lifecycleautomation-automationdocument)" : {{String}},
      "[AutomationParameters](#cfn-ssmquicksetup-lifecycleautomation-automationparameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ResourceKey](#cfn-ssmquicksetup-lifecycleautomation-resourcekey)" : {{String}},
      "[Tags](#cfn-ssmquicksetup-lifecycleautomation-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-ssmquicksetup-lifecycleautomation-syntax.yaml"></a>

```
Type: AWS::SSMQuickSetup::LifecycleAutomation
Properties:
  [AutomationDocument](#cfn-ssmquicksetup-lifecycleautomation-automationdocument): {{String}}
  [AutomationParameters](#cfn-ssmquicksetup-lifecycleautomation-automationparameters): {{
    {{Key}}: {{Value}}}}
  [ResourceKey](#cfn-ssmquicksetup-lifecycleautomation-resourcekey): {{String}}
  [Tags](#cfn-ssmquicksetup-lifecycleautomation-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-ssmquicksetup-lifecycleautomation-properties"></a>

`AutomationDocument`  <a name="cfn-ssmquicksetup-lifecycleautomation-automationdocument"></a>
The name of the SSM Automation document to execute in response to CloudFormation lifecycle events (CREATE, UPDATE, DELETE).
*Required*: Yes
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutomationParameters`  <a name="cfn-ssmquicksetup-lifecycleautomation-automationparameters"></a>
A map of key-value parameters passed to the Automation document during execution. Each parameter name maps to a list of values, even for single values. Parameters can include configuration-specific values for your automation workflow.
*Required*: Yes
*Type*: Object of Array
*Pattern*: `^[a-zA-Z0-9_]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceKey`  <a name="cfn-ssmquicksetup-lifecycleautomation-resourcekey"></a>
A unique identifier used for generating the SSM Association name. This ensures uniqueness when multiple lifecycle automation resources exist in the same stack.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ssmquicksetup-lifecycleautomation-tags"></a>
Tags applied to the underlying SSM Association created by this resource. Tags help identify and organize automation executions.
*Required*: No
*Type*: Object of String
*Pattern*: `^[A-Za-z0-9 +=@_\/:.-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssmquicksetup-lifecycleautomation-return-values"></a>

### Ref
<a name="aws-resource-ssmquicksetup-lifecycleautomation-return-values-ref"></a>

Returns the AssociationId of the lifecycle automation resource, which is the same as the association ID of the underlying Systems Manager association.

### Fn::GetAtt
<a name="aws-resource-ssmquicksetup-lifecycleautomation-return-values-fn--getatt"></a>

Returns the value of an attribute from the `AWS::SSMQuickSetup::LifecycleAutomation` resource. This resource executes SSM Automation documents in response to CloudFormation lifecycle events (CREATE, UPDATE, DELETE) and replaces inline Lambda custom resources in Quick Setup templates.

####
<a name="aws-resource-ssmquicksetup-lifecycleautomation-return-values-fn--getatt-fn--getatt"></a>

`AssociationId`  <a name="AssociationId-fn::getatt"></a>
Returns the ID of the SSM Association created to manage the automation document execution lifecycle.
