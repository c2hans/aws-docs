---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-securityprofile-flowmodule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::SecurityProfile FlowModule
<a name="aws-properties-connect-securityprofile-flowmodule"></a>

 A list of Flow Modules an AI Agent can invoke as a tool

## Syntax
<a name="aws-properties-connect-securityprofile-flowmodule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-securityprofile-flowmodule-syntax.json"></a>

```
{
  "[FlowModuleId](#cfn-connect-securityprofile-flowmodule-flowmoduleid)" : {{String}},
  "[Type](#cfn-connect-securityprofile-flowmodule-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-securityprofile-flowmodule-syntax.yaml"></a>

```
  [FlowModuleId](#cfn-connect-securityprofile-flowmodule-flowmoduleid): {{String}}
  [Type](#cfn-connect-securityprofile-flowmodule-type): {{String}}
```

## Properties
<a name="aws-properties-connect-securityprofile-flowmodule-properties"></a>

`FlowModuleId`  <a name="cfn-connect-securityprofile-flowmodule-flowmoduleid"></a>
 If of Flow Modules invocable as tool
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-securityprofile-flowmodule-type"></a>
 Only Type we support is MCP.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
