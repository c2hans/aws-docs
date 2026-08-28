---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-walworkspace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::WALWorkspace
<a name="aws-resource-emr-walworkspace"></a>

<a name="aws-resource-emr-walworkspace-description"></a>The `AWS::EMR::WALWorkspace` resource Property description not available. for EMR.

## Syntax
<a name="aws-resource-emr-walworkspace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emr-walworkspace-syntax.json"></a>

```
{
  "Type" : "AWS::EMR::WALWorkspace",
  "Properties" : {
      "[Tags](#cfn-emr-walworkspace-tags)" : {{[ Tag, ... ]}},
      "[WALWorkspaceName](#cfn-emr-walworkspace-walworkspacename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-emr-walworkspace-syntax.yaml"></a>

```
Type: AWS::EMR::WALWorkspace
Properties:
  [Tags](#cfn-emr-walworkspace-tags): {{
    - Tag}}
  [WALWorkspaceName](#cfn-emr-walworkspace-walworkspacename): {{String}}
```

## Properties
<a name="aws-resource-emr-walworkspace-properties"></a>

`Tags`  <a name="cfn-emr-walworkspace-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-emr-walworkspace-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WALWorkspaceName`  <a name="cfn-emr-walworkspace-walworkspacename"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-emr-walworkspace-return-values"></a>

### Ref
<a name="aws-resource-emr-walworkspace-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
