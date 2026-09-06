---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule FieldToMatch
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch"></a>

 Specifies a field in the request to redact from WAF logs, such as headers, query parameters, or body content.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch-syntax.json"></a>

```
{
  "[Method](#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-method)" : {{String}},
  "[QueryString](#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-querystring)" : {{String}},
  "[SingleHeader](#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-singleheader)" : {{SingleHeader}},
  "[UriPath](#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-uripath)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch-syntax.yaml"></a>

```
  [Method](#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-method): {{String}}
  [QueryString](#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-querystring): {{
    String}}
  [SingleHeader](#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-singleheader): {{
    SingleHeader}}
  [UriPath](#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-uripath): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch-properties"></a>

`Method`  <a name="cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-method"></a>
 Redacts the HTTP method from WAF logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryString`  <a name="cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-querystring"></a>
 Redacts the entire query string from WAF logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleHeader`  <a name="cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-singleheader"></a>
 Redacts a specific header field by name from WAF logs.
*Required*: No
*Type*: [SingleHeader](aws-properties-observabilityadmin-organizationtelemetryrule-singleheader.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UriPath`  <a name="cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-uripath"></a>
 Redacts the URI path from WAF logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
