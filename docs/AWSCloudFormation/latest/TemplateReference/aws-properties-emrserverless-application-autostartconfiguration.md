---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-autostartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application AutoStartConfiguration
<a name="aws-properties-emrserverless-application-autostartconfiguration"></a>

The configuration for an application to automatically start on job submission.

## Syntax
<a name="aws-properties-emrserverless-application-autostartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-autostartconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-emrserverless-application-autostartconfiguration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-autostartconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-emrserverless-application-autostartconfiguration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-emrserverless-application-autostartconfiguration-properties"></a>

`Enabled`  <a name="cfn-emrserverless-application-autostartconfiguration-enabled"></a>
Enables the application to automatically start on job submission.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
