---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::FunctionDefinition ResourceAccessPolicy
<a name="aws-properties-greengrass-functiondefinition-resourceaccesspolicy"></a>

<a name="aws-properties-greengrass-functiondefinition-resourceaccesspolicy-description"></a>A list of the [resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html) in the group that the function can access, with the corresponding read-only or read-write permissions. The maximum is 10 resources.

**Note**
This property applies only to Lambda functions that run in a Greengrass container.

<a name="aws-properties-greengrass-functiondefinition-resourceaccesspolicy-inheritance"></a> In an CloudFormation template, `ResourceAccessPolicy` is a property of the [`Environment`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html) property type.

## Syntax
<a name="aws-properties-greengrass-functiondefinition-resourceaccesspolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-functiondefinition-resourceaccesspolicy-syntax.json"></a>

```
{
  "[Permission](#cfn-greengrass-functiondefinition-resourceaccesspolicy-permission)" : {{String}},
  "[ResourceId](#cfn-greengrass-functiondefinition-resourceaccesspolicy-resourceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrass-functiondefinition-resourceaccesspolicy-syntax.yaml"></a>

```
  [Permission](#cfn-greengrass-functiondefinition-resourceaccesspolicy-permission): {{String}}
  [ResourceId](#cfn-greengrass-functiondefinition-resourceaccesspolicy-resourceid): {{String}}
```

## Properties
<a name="aws-properties-greengrass-functiondefinition-resourceaccesspolicy-properties"></a>

`Permission`  <a name="cfn-greengrass-functiondefinition-resourceaccesspolicy-permission"></a>
The read-only or read-write access that the Lambda function has to the resource. Valid values are `ro` or `rw`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceId`  <a name="cfn-greengrass-functiondefinition-resourceaccesspolicy-resourceid"></a>
The ID of the resource. This ID is assigned to the resource when you create the resource definition.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-functiondefinition-resourceaccesspolicy--seealso"></a>
+ [ResourceAccessPolicy](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resourceaccesspolicy.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
