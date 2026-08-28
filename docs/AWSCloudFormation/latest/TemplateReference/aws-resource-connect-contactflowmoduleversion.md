---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-contactflowmoduleversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::ContactFlowModuleVersion
<a name="aws-resource-connect-contactflowmoduleversion"></a>

Creates an immutable snapshot of a contact flow module, preserving its content and settings at a specific point in time for version control and rollback capabilities.

## Syntax
<a name="aws-resource-connect-contactflowmoduleversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-contactflowmoduleversion-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::ContactFlowModuleVersion",
  "Properties" : {
      "[ContactFlowModuleId](#cfn-connect-contactflowmoduleversion-contactflowmoduleid)" : {{String}},
      "[Description](#cfn-connect-contactflowmoduleversion-description)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-contactflowmoduleversion-syntax.yaml"></a>

```
Type: AWS::Connect::ContactFlowModuleVersion
Properties:
  [ContactFlowModuleId](#cfn-connect-contactflowmoduleversion-contactflowmoduleid): {{String}}
  [Description](#cfn-connect-contactflowmoduleversion-description): {{String}}
```

## Properties
<a name="aws-resource-connect-contactflowmoduleversion-properties"></a>

`ContactFlowModuleId`  <a name="cfn-connect-contactflowmoduleversion-contactflowmoduleid"></a>
The identifier of the flow module.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]+:[0-9]{12}:instance/[-a-zA-Z0-9]+/flow-module/[-a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-connect-contactflowmoduleversion-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-connect-contactflowmoduleversion-return-values"></a>

### Ref
<a name="aws-resource-connect-contactflowmoduleversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-contactflowmoduleversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-connect-contactflowmoduleversion-return-values-fn--getatt-fn--getatt"></a>

`ContactFlowModuleVersionARN`  <a name="ContactFlowModuleVersionARN-fn::getatt"></a>
Property description not available.

`FlowModuleContentSha256`  <a name="FlowModuleContentSha256-fn::getatt"></a>
Property description not available.

`Version`  <a name="Version-fn::getatt"></a>
The version of the flow module.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
