---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-logdeliveryparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule LogDeliveryParameters
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-logdeliveryparameters"></a>

The configuration parameters for log delivery, including `logType` settings. Applies to resource types that support configurable log delivery, such as Amazon Bedrock Knowledge Bases and Elastic Load Balancing Application Load Balancers.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-logdeliveryparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-logdeliveryparameters-syntax.json"></a>

```
{
  "[LogTypes](#cfn-observabilityadmin-organizationtelemetryrule-logdeliveryparameters-logtypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-logdeliveryparameters-syntax.yaml"></a>

```
  [LogTypes](#cfn-observabilityadmin-organizationtelemetryrule-logdeliveryparameters-logtypes): {{
    - String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-logdeliveryparameters-properties"></a>

`LogTypes`  <a name="cfn-observabilityadmin-organizationtelemetryrule-logdeliveryparameters-logtypes"></a>
The types of logs to collect from the resource.
*Required*: No
*Type*: Array of String
*Allowed values*: `SECURITY_FINDING_LOGS`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
