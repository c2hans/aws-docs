---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-fieldtomatch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule FieldToMatch
<a name="aws-properties-observabilityadmin-telemetryrule-fieldtomatch"></a>

 Specifies a field in the request to redact from WAF logs, such as headers, query parameters, or body content.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-fieldtomatch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-fieldtomatch-syntax.json"></a>

```
{
  "[Method](#cfn-observabilityadmin-telemetryrule-fieldtomatch-method)" : {{String}},
  "[QueryString](#cfn-observabilityadmin-telemetryrule-fieldtomatch-querystring)" : {{String}},
  "[SingleHeader](#cfn-observabilityadmin-telemetryrule-fieldtomatch-singleheader)" : {{SingleHeader}},
  "[UriPath](#cfn-observabilityadmin-telemetryrule-fieldtomatch-uripath)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-fieldtomatch-syntax.yaml"></a>

```
  [Method](#cfn-observabilityadmin-telemetryrule-fieldtomatch-method): {{String}}
  [QueryString](#cfn-observabilityadmin-telemetryrule-fieldtomatch-querystring): {{
    String}}
  [SingleHeader](#cfn-observabilityadmin-telemetryrule-fieldtomatch-singleheader): {{
    SingleHeader}}
  [UriPath](#cfn-observabilityadmin-telemetryrule-fieldtomatch-uripath): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-fieldtomatch-properties"></a>

`Method`  <a name="cfn-observabilityadmin-telemetryrule-fieldtomatch-method"></a>
 Redacts the HTTP method from WAF logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryString`  <a name="cfn-observabilityadmin-telemetryrule-fieldtomatch-querystring"></a>
 Redacts the entire query string from WAF logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleHeader`  <a name="cfn-observabilityadmin-telemetryrule-fieldtomatch-singleheader"></a>
 Redacts a specific header field by name from WAF logs.
*Required*: No
*Type*: [SingleHeader](aws-properties-observabilityadmin-telemetryrule-singleheader.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UriPath`  <a name="cfn-observabilityadmin-telemetryrule-fieldtomatch-uripath"></a>
 Redacts the URI path from WAF logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
