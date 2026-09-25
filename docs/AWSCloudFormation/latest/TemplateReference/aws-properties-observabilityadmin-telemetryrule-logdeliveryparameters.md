---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-logdeliveryparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule LogDeliveryParameters
<a name="aws-properties-observabilityadmin-telemetryrule-logdeliveryparameters"></a>

The configuration parameters for log delivery, including `logType` settings. Applies to resource types that support configurable log delivery, such as Amazon Bedrock Knowledge Bases and Elastic Load Balancing Application Load Balancers.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-logdeliveryparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-logdeliveryparameters-syntax.json"></a>

```
{
  "[LogTypes](#cfn-observabilityadmin-telemetryrule-logdeliveryparameters-logtypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-logdeliveryparameters-syntax.yaml"></a>

```
  [LogTypes](#cfn-observabilityadmin-telemetryrule-logdeliveryparameters-logtypes): {{
    - String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-logdeliveryparameters-properties"></a>

`LogTypes`  <a name="cfn-observabilityadmin-telemetryrule-logdeliveryparameters-logtypes"></a>
The types of logs to collect from the resource.
*Required*: No
*Type*: Array of String
*Allowed values*: `APPLICATION_LOGS | USAGE_LOGS | SECURITY_FINDING_LOGS | S3_SERVER_ACCESS_LOGS | ACCESS_LOGS | CONNECTION_LOGS | ALB_ACCESS_LOGS | ALB_CONNECTION_LOGS | ALB_HEALTH_CHECK_LOGS`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
