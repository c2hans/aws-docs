---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appintegrations-application-externalurlconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppIntegrations::Application ExternalUrlConfig
<a name="aws-properties-appintegrations-application-externalurlconfig"></a>

The external URL source for the application.

## Syntax
<a name="aws-properties-appintegrations-application-externalurlconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appintegrations-application-externalurlconfig-syntax.json"></a>

```
{
  "[AccessUrl](#cfn-appintegrations-application-externalurlconfig-accessurl)" : {{String}},
  "[ApprovedOrigins](#cfn-appintegrations-application-externalurlconfig-approvedorigins)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-appintegrations-application-externalurlconfig-syntax.yaml"></a>

```
  [AccessUrl](#cfn-appintegrations-application-externalurlconfig-accessurl): {{String}}
  [ApprovedOrigins](#cfn-appintegrations-application-externalurlconfig-approvedorigins): {{
    - String}}
```

## Properties
<a name="aws-properties-appintegrations-application-externalurlconfig-properties"></a>

`AccessUrl`  <a name="cfn-appintegrations-application-externalurlconfig-accessurl"></a>
The URL to access the application.
*Required*: Yes
*Type*: String
*Pattern*: `^\w+\:\/\/.*$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApprovedOrigins`  <a name="cfn-appintegrations-application-externalurlconfig-approvedorigins"></a>
Additional URLs to allow list if different than the access URL.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
