---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-container-healthcheckconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Container HealthCheckConfig
<a name="aws-properties-lightsail-container-healthcheckconfig"></a>

`HealthCheckConfig` is a property of the [PublicEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html) property. It describes the healthcheck configuration of a container deployment on a container service.

## Syntax
<a name="aws-properties-lightsail-container-healthcheckconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-container-healthcheckconfig-syntax.json"></a>

```
{
  "[HealthyThreshold](#cfn-lightsail-container-healthcheckconfig-healthythreshold)" : {{Integer}},
  "[IntervalSeconds](#cfn-lightsail-container-healthcheckconfig-intervalseconds)" : {{Integer}},
  "[Path](#cfn-lightsail-container-healthcheckconfig-path)" : {{String}},
  "[SuccessCodes](#cfn-lightsail-container-healthcheckconfig-successcodes)" : {{String}},
  "[TimeoutSeconds](#cfn-lightsail-container-healthcheckconfig-timeoutseconds)" : {{Integer}},
  "[UnhealthyThreshold](#cfn-lightsail-container-healthcheckconfig-unhealthythreshold)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lightsail-container-healthcheckconfig-syntax.yaml"></a>

```
  [HealthyThreshold](#cfn-lightsail-container-healthcheckconfig-healthythreshold): {{Integer}}
  [IntervalSeconds](#cfn-lightsail-container-healthcheckconfig-intervalseconds): {{Integer}}
  [Path](#cfn-lightsail-container-healthcheckconfig-path): {{String}}
  [SuccessCodes](#cfn-lightsail-container-healthcheckconfig-successcodes): {{String}}
  [TimeoutSeconds](#cfn-lightsail-container-healthcheckconfig-timeoutseconds): {{Integer}}
  [UnhealthyThreshold](#cfn-lightsail-container-healthcheckconfig-unhealthythreshold): {{Integer}}
```

## Properties
<a name="aws-properties-lightsail-container-healthcheckconfig-properties"></a>

`HealthyThreshold`  <a name="cfn-lightsail-container-healthcheckconfig-healthythreshold"></a>
The number of consecutive health check successes required before moving the container to the `Healthy` state. The default value is `2`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntervalSeconds`  <a name="cfn-lightsail-container-healthcheckconfig-intervalseconds"></a>
The approximate interval, in seconds, between health checks of an individual container. You can specify between `5` and `300` seconds. The default value is `5`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-lightsail-container-healthcheckconfig-path"></a>
The path on the container on which to perform the health check. The default value is `/`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessCodes`  <a name="cfn-lightsail-container-healthcheckconfig-successcodes"></a>
The HTTP codes to use when checking for a successful response from a container. You can specify values between `200` and `499`. You can specify multiple values (for example, `200,202`) or a range of values (for example, `200-299`).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutSeconds`  <a name="cfn-lightsail-container-healthcheckconfig-timeoutseconds"></a>
The amount of time, in seconds, during which no response means a failed health check. You can specify between `2` and `60` seconds. The default value is `2`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnhealthyThreshold`  <a name="cfn-lightsail-container-healthcheckconfig-unhealthythreshold"></a>
The number of consecutive health check failures required before moving the container to the `Unhealthy` state. The default value is `2`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
