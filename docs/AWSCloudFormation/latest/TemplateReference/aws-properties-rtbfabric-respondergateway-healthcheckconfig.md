---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-respondergateway-healthcheckconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::ResponderGateway HealthCheckConfig
<a name="aws-properties-rtbfabric-respondergateway-healthcheckconfig"></a>

<a name="aws-properties-rtbfabric-respondergateway-healthcheckconfig-description"></a>The `HealthCheckConfig` property type specifies Property description not available. for an [AWS::RTBFabric::ResponderGateway](aws-resource-rtbfabric-respondergateway.md).

## Syntax
<a name="aws-properties-rtbfabric-respondergateway-healthcheckconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-respondergateway-healthcheckconfig-syntax.json"></a>

```
{
  "[HealthyThresholdCount](#cfn-rtbfabric-respondergateway-healthcheckconfig-healthythresholdcount)" : {{Integer}},
  "[IntervalSeconds](#cfn-rtbfabric-respondergateway-healthcheckconfig-intervalseconds)" : {{Integer}},
  "[Path](#cfn-rtbfabric-respondergateway-healthcheckconfig-path)" : {{String}},
  "[Port](#cfn-rtbfabric-respondergateway-healthcheckconfig-port)" : {{Integer}},
  "[Protocol](#cfn-rtbfabric-respondergateway-healthcheckconfig-protocol)" : {{String}},
  "[StatusCodeMatcher](#cfn-rtbfabric-respondergateway-healthcheckconfig-statuscodematcher)" : {{String}},
  "[TimeoutMs](#cfn-rtbfabric-respondergateway-healthcheckconfig-timeoutms)" : {{Integer}},
  "[UnhealthyThresholdCount](#cfn-rtbfabric-respondergateway-healthcheckconfig-unhealthythresholdcount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-rtbfabric-respondergateway-healthcheckconfig-syntax.yaml"></a>

```
  [HealthyThresholdCount](#cfn-rtbfabric-respondergateway-healthcheckconfig-healthythresholdcount): {{Integer}}
  [IntervalSeconds](#cfn-rtbfabric-respondergateway-healthcheckconfig-intervalseconds): {{Integer}}
  [Path](#cfn-rtbfabric-respondergateway-healthcheckconfig-path): {{String}}
  [Port](#cfn-rtbfabric-respondergateway-healthcheckconfig-port): {{Integer}}
  [Protocol](#cfn-rtbfabric-respondergateway-healthcheckconfig-protocol): {{String}}
  [StatusCodeMatcher](#cfn-rtbfabric-respondergateway-healthcheckconfig-statuscodematcher): {{String}}
  [TimeoutMs](#cfn-rtbfabric-respondergateway-healthcheckconfig-timeoutms): {{Integer}}
  [UnhealthyThresholdCount](#cfn-rtbfabric-respondergateway-healthcheckconfig-unhealthythresholdcount): {{Integer}}
```

## Properties
<a name="aws-properties-rtbfabric-respondergateway-healthcheckconfig-properties"></a>

`HealthyThresholdCount`  <a name="cfn-rtbfabric-respondergateway-healthcheckconfig-healthythresholdcount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `10`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`IntervalSeconds`  <a name="cfn-rtbfabric-respondergateway-healthcheckconfig-intervalseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `5`
*Maximum*: `60`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Path`  <a name="cfn-rtbfabric-respondergateway-healthcheckconfig-path"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^/.*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Port`  <a name="cfn-rtbfabric-respondergateway-healthcheckconfig-port"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `80`
*Maximum*: `65535`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Protocol`  <a name="cfn-rtbfabric-respondergateway-healthcheckconfig-protocol"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `HTTP | HTTPS`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`StatusCodeMatcher`  <a name="cfn-rtbfabric-respondergateway-healthcheckconfig-statuscodematcher"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9,\-]+$`
*Minimum*: `3`
*Maximum*: `2000`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`TimeoutMs`  <a name="cfn-rtbfabric-respondergateway-healthcheckconfig-timeoutms"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `5000`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`UnhealthyThresholdCount`  <a name="cfn-rtbfabric-respondergateway-healthcheckconfig-unhealthythresholdcount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `10`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
