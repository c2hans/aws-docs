---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-workertypespecificationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application WorkerTypeSpecificationInput
<a name="aws-properties-emrserverless-application-workertypespecificationinput"></a>

The specifications for a worker type.

## Syntax
<a name="aws-properties-emrserverless-application-workertypespecificationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-workertypespecificationinput-syntax.json"></a>

```
{
  "[ImageConfiguration](#cfn-emrserverless-application-workertypespecificationinput-imageconfiguration)" : {{ImageConfigurationInput}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-workertypespecificationinput-syntax.yaml"></a>

```
  [ImageConfiguration](#cfn-emrserverless-application-workertypespecificationinput-imageconfiguration): {{
    ImageConfigurationInput}}
```

## Properties
<a name="aws-properties-emrserverless-application-workertypespecificationinput-properties"></a>

`ImageConfiguration`  <a name="cfn-emrserverless-application-workertypespecificationinput-imageconfiguration"></a>
The image configuration for a worker type.
*Required*: No
*Type*: [ImageConfigurationInput](aws-properties-emrserverless-application-imageconfigurationinput.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
