---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-statemachine-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::StateMachine S3Location
<a name="aws-properties-stepfunctions-statemachine-s3location"></a>

Defines the S3 bucket location where a state machine definition is stored. The state machine definition must be a JSON or YAML file.

## Syntax
<a name="aws-properties-stepfunctions-statemachine-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-statemachine-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-stepfunctions-statemachine-s3location-bucket)" : {{String}},
  "[Key](#cfn-stepfunctions-statemachine-s3location-key)" : {{String}},
  "[Version](#cfn-stepfunctions-statemachine-s3location-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-stepfunctions-statemachine-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-stepfunctions-statemachine-s3location-bucket): {{String}}
  [Key](#cfn-stepfunctions-statemachine-s3location-key): {{String}}
  [Version](#cfn-stepfunctions-statemachine-s3location-version): {{String}}
```

## Properties
<a name="aws-properties-stepfunctions-statemachine-s3location-properties"></a>

`Bucket`  <a name="cfn-stepfunctions-statemachine-s3location-bucket"></a>
The name of the S3 bucket where the state machine definition JSON or YAML file is stored.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-stepfunctions-statemachine-s3location-key"></a>
The name of the state machine definition file (Amazon S3 object name).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-stepfunctions-statemachine-s3location-version"></a>
For versioning-enabled buckets, a specific version of the state machine definition.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
