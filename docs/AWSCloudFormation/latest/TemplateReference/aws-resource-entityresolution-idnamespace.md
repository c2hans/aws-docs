---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-entityresolution-idnamespace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdNamespace
<a name="aws-resource-entityresolution-idnamespace"></a>

Creates an ID namespace object which will help customers provide metadata explaining their dataset and how to use it. Each ID namespace must have a unique name. To modify an existing ID namespace, use the UpdateIdNamespace API.

## Syntax
<a name="aws-resource-entityresolution-idnamespace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-entityresolution-idnamespace-syntax.json"></a>

```
{
  "Type" : "AWS::EntityResolution::IdNamespace",
  "Properties" : {
      "[Description](#cfn-entityresolution-idnamespace-description)" : {{String}},
      "[IdMappingWorkflowProperties](#cfn-entityresolution-idnamespace-idmappingworkflowproperties)" : {{[ IdNamespaceIdMappingWorkflowProperties, ... ]}},
      "[IdNamespaceName](#cfn-entityresolution-idnamespace-idnamespacename)" : {{String}},
      "[InputSourceConfig](#cfn-entityresolution-idnamespace-inputsourceconfig)" : {{[ IdNamespaceInputSource, ... ]}},
      "[RoleArn](#cfn-entityresolution-idnamespace-rolearn)" : {{String}},
      "[Tags](#cfn-entityresolution-idnamespace-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-entityresolution-idnamespace-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-entityresolution-idnamespace-syntax.yaml"></a>

```
Type: AWS::EntityResolution::IdNamespace
Properties:
  [Description](#cfn-entityresolution-idnamespace-description): {{String}}
  [IdMappingWorkflowProperties](#cfn-entityresolution-idnamespace-idmappingworkflowproperties): {{
    - IdNamespaceIdMappingWorkflowProperties}}
  [IdNamespaceName](#cfn-entityresolution-idnamespace-idnamespacename): {{String}}
  [InputSourceConfig](#cfn-entityresolution-idnamespace-inputsourceconfig): {{
    - IdNamespaceInputSource}}
  [RoleArn](#cfn-entityresolution-idnamespace-rolearn): {{String}}
  [Tags](#cfn-entityresolution-idnamespace-tags): {{
    - Tag}}
  [Type](#cfn-entityresolution-idnamespace-type): {{String}}
```

## Properties
<a name="aws-resource-entityresolution-idnamespace-properties"></a>

`Description`  <a name="cfn-entityresolution-idnamespace-description"></a>
The description of the ID namespace.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdMappingWorkflowProperties`  <a name="cfn-entityresolution-idnamespace-idmappingworkflowproperties"></a>
Determines the properties of `IdMappingWorflow` where this `IdNamespace` can be used as a `Source` or a `Target`.
*Required*: No
*Type*: Array of [IdNamespaceIdMappingWorkflowProperties](aws-properties-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdNamespaceName`  <a name="cfn-entityresolution-idnamespace-idnamespacename"></a>
The name of the ID namespace.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_0-9-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputSourceConfig`  <a name="cfn-entityresolution-idnamespace-inputsourceconfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
*Required*: No
*Type*: Array of [IdNamespaceInputSource](aws-properties-entityresolution-idnamespace-idnamespaceinputsource.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-entityresolution-idnamespace-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to access the resources defined in this `IdNamespace` on your behalf as part of the workflow run.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `32`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-entityresolution-idnamespace-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-entityresolution-idnamespace-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-entityresolution-idnamespace-type"></a>
The type of ID namespace. There are two types: `SOURCE` and `TARGET`.
The `SOURCE` contains configurations for `sourceId` data that will be processed in an ID mapping workflow.
The `TARGET` contains a configuration of `targetId` which all `sourceIds` will resolve to.
*Required*: Yes
*Type*: String
*Allowed values*: `SOURCE | TARGET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
