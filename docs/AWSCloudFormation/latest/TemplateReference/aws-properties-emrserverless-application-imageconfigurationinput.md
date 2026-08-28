---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-imageconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application ImageConfigurationInput
<a name="aws-properties-emrserverless-application-imageconfigurationinput"></a>

The image configuration.

## Syntax
<a name="aws-properties-emrserverless-application-imageconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-imageconfigurationinput-syntax.json"></a>

```
{
  "[ImageUri](#cfn-emrserverless-application-imageconfigurationinput-imageuri)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-imageconfigurationinput-syntax.yaml"></a>

```
  [ImageUri](#cfn-emrserverless-application-imageconfigurationinput-imageuri): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-application-imageconfigurationinput-properties"></a>

`ImageUri`  <a name="cfn-emrserverless-application-imageconfigurationinput-imageuri"></a>
The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.
*Required*: No
*Type*: String
*Pattern*: `^([a-z0-9]+[a-z0-9-.]*)\/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*\/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(?:\:([a-zA-Z0-9_][a-zA-Z0-9-._]{0,299})|@(sha256:[0-9a-f]{64}))$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
