---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule ELBLoadBalancerLoggingParameters
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters"></a>

 Configuration parameters for ELB load balancer logging, including output format and field delimiter settings.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-syntax.json"></a>

```
{
  "[FieldDelimiter](#cfn-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-fielddelimiter)" : {{String}},
  "[OutputFormat](#cfn-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-outputformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-syntax.yaml"></a>

```
  [FieldDelimiter](#cfn-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-fielddelimiter): {{String}}
  [OutputFormat](#cfn-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-outputformat): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-properties"></a>

`FieldDelimiter`  <a name="cfn-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-fielddelimiter"></a>
 The delimiter character used to separate fields in ELB access log entries when using plain text format.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputFormat`  <a name="cfn-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-outputformat"></a>
 The format for ELB access log entries (plain text or JSON format).
*Required*: No
*Type*: String
*Allowed values*: `plain | json`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
