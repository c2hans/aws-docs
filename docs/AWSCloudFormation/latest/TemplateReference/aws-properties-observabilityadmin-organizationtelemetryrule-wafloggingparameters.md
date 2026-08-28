---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule WAFLoggingParameters
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters"></a>

 Configuration parameters for WAF logging, including redacted fields and logging filters.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters-syntax.json"></a>

```
{
  "[LoggingFilter](#cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-loggingfilter)" : {{LoggingFilter}},
  "[LogType](#cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-logtype)" : {{String}},
  "[RedactedFields](#cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-redactedfields)" : {{[ FieldToMatch, ... ]}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters-syntax.yaml"></a>

```
  [LoggingFilter](#cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-loggingfilter): {{
    LoggingFilter}}
  [LogType](#cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-logtype): {{String}}
  [RedactedFields](#cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-redactedfields): {{
    - FieldToMatch}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters-properties"></a>

`LoggingFilter`  <a name="cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-loggingfilter"></a>
 A filter configuration that determines which WAF log records to include or exclude.
*Required*: No
*Type*: [LoggingFilter](aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogType`  <a name="cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-logtype"></a>
 The type of WAF logs to collect (currently supports WAF\_LOGS).
*Required*: No
*Type*: String
*Allowed values*: `WAF_LOGS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedactedFields`  <a name="cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-redactedfields"></a>
 The fields to redact from WAF logs to protect sensitive information.
*Required*: No
*Type*: Array of [FieldToMatch](aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
