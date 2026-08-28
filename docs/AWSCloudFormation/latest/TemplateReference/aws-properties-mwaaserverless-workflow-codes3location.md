---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mwaaserverless-workflow-codes3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAAServerless::Workflow CodeS3Location
<a name="aws-properties-mwaaserverless-workflow-codes3location"></a>

<a name="aws-properties-mwaaserverless-workflow-codes3location-description"></a>The `CodeS3Location` property type specifies Property description not available. for an [AWS::MWAAServerless::Workflow](aws-resource-mwaaserverless-workflow.md).

## Syntax
<a name="aws-properties-mwaaserverless-workflow-codes3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mwaaserverless-workflow-codes3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-mwaaserverless-workflow-codes3location-bucket)" : {{String}},
  "[ObjectKey](#cfn-mwaaserverless-workflow-codes3location-objectkey)" : {{String}},
  "[VersionId](#cfn-mwaaserverless-workflow-codes3location-versionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mwaaserverless-workflow-codes3location-syntax.yaml"></a>

```
  [Bucket](#cfn-mwaaserverless-workflow-codes3location-bucket): {{String}}
  [ObjectKey](#cfn-mwaaserverless-workflow-codes3location-objectkey): {{String}}
  [VersionId](#cfn-mwaaserverless-workflow-codes3location-versionid): {{String}}
```

## Properties
<a name="aws-properties-mwaaserverless-workflow-codes3location-properties"></a>

`Bucket`  <a name="cfn-mwaaserverless-workflow-codes3location-bucket"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectKey`  <a name="cfn-mwaaserverless-workflow-codes3location-objectkey"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionId`  <a name="cfn-mwaaserverless-workflow-codes3location-versionid"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
