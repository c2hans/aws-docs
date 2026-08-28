---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-scrapercomponent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper ScraperComponent
<a name="aws-properties-aps-scraper-scrapercomponent"></a>

A component of a Amazon Managed Service for Prometheus scraper that can be configured for logging.

## Syntax
<a name="aws-properties-aps-scraper-scrapercomponent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-scrapercomponent-syntax.json"></a>

```
{
  "[Config](#cfn-aps-scraper-scrapercomponent-config)" : {{ComponentConfig}},
  "[Type](#cfn-aps-scraper-scrapercomponent-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-scraper-scrapercomponent-syntax.yaml"></a>

```
  [Config](#cfn-aps-scraper-scrapercomponent-config): {{
    ComponentConfig}}
  [Type](#cfn-aps-scraper-scrapercomponent-type): {{String}}
```

## Properties
<a name="aws-properties-aps-scraper-scrapercomponent-properties"></a>

`Config`  <a name="cfn-aps-scraper-scrapercomponent-config"></a>
The configuration settings for the scraper component.
*Required*: No
*Type*: [ComponentConfig](aws-properties-aps-scraper-componentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-aps-scraper-scrapercomponent-type"></a>
The type of the scraper component.
*Required*: Yes
*Type*: String
*Allowed values*: `SERVICE_DISCOVERY | COLLECTOR | EXPORTER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
