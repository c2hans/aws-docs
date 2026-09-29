---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-eksaccessentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment EksAccessEntry
<a name="aws-properties-batch-computeenvironment-eksaccessentry"></a>

<a name="aws-properties-batch-computeenvironment-eksaccessentry-description"></a>The `EksAccessEntry` property type specifies Property description not available. for an [AWS::Batch::ComputeEnvironment](aws-resource-batch-computeenvironment.md).

## Syntax
<a name="aws-properties-batch-computeenvironment-eksaccessentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-eksaccessentry-syntax.json"></a>

```
{
  "[DesiredState](#cfn-batch-computeenvironment-eksaccessentry-desiredstate)" : {{String}},
  "[Status](#cfn-batch-computeenvironment-eksaccessentry-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-eksaccessentry-syntax.yaml"></a>

```
  [DesiredState](#cfn-batch-computeenvironment-eksaccessentry-desiredstate): {{String}}
  [Status](#cfn-batch-computeenvironment-eksaccessentry-status): {{String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-eksaccessentry-properties"></a>

`DesiredState`  <a name="cfn-batch-computeenvironment-eksaccessentry-desiredstate"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED | INHERIT_FROM_CLUSTER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-batch-computeenvironment-eksaccessentry-status"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | INACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
