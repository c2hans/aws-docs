---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appintegrations-application-applicationsourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppIntegrations::Application ApplicationSourceConfig
<a name="aws-properties-appintegrations-application-applicationsourceconfig"></a>

The configuration for where the application should be loaded from.

## Syntax
<a name="aws-properties-appintegrations-application-applicationsourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appintegrations-application-applicationsourceconfig-syntax.json"></a>

```
{
  "[ExternalUrlConfig](#cfn-appintegrations-application-applicationsourceconfig-externalurlconfig)" : {{ExternalUrlConfig}}
}
```

### YAML
<a name="aws-properties-appintegrations-application-applicationsourceconfig-syntax.yaml"></a>

```
  [ExternalUrlConfig](#cfn-appintegrations-application-applicationsourceconfig-externalurlconfig): {{
    ExternalUrlConfig}}
```

## Properties
<a name="aws-properties-appintegrations-application-applicationsourceconfig-properties"></a>

`ExternalUrlConfig`  <a name="cfn-appintegrations-application-applicationsourceconfig-externalurlconfig"></a>
The external URL source for the application.
*Required*: Yes
*Type*: [ExternalUrlConfig](aws-properties-appintegrations-application-externalurlconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
