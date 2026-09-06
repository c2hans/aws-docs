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
