---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-canary-browserconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary BrowserConfig
<a name="aws-properties-synthetics-canary-browserconfig"></a>

A structure that specifies the browser type to use for a canary run.

## Syntax
<a name="aws-properties-synthetics-canary-browserconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-canary-browserconfig-syntax.json"></a>

```
{
  "[BrowserType](#cfn-synthetics-canary-browserconfig-browsertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-synthetics-canary-browserconfig-syntax.yaml"></a>

```
  [BrowserType](#cfn-synthetics-canary-browserconfig-browsertype): {{String}}
```

## Properties
<a name="aws-properties-synthetics-canary-browserconfig-properties"></a>

`BrowserType`  <a name="cfn-synthetics-canary-browserconfig-browsertype"></a>
The browser type associated with this browser configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `CHROME | FIREFOX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
