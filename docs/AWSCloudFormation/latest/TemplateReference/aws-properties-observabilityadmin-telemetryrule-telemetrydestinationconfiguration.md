---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule TelemetryDestinationConfiguration
<a name="aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration"></a>

 Configuration specifying where and how telemetry data should be delivered for AWS resources.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-syntax.json"></a>

```
{
  "[CloudtrailParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-cloudtrailparameters)" : {{CloudtrailParameters}},
  "[DestinationPattern](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationpattern)" : {{String}},
  "[DestinationType](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationtype)" : {{String}},
  "[ELBLoadBalancerLoggingParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-elbloadbalancerloggingparameters)" : {{ELBLoadBalancerLoggingParameters}},
  "[LogDeliveryParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-logdeliveryparameters)" : {{LogDeliveryParameters}},
  "[RetentionInDays](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-retentionindays)" : {{Integer}},
  "[VPCFlowLogParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-vpcflowlogparameters)" : {{VPCFlowLogParameters}},
  "[WAFLoggingParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-wafloggingparameters)" : {{WAFLoggingParameters}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-syntax.yaml"></a>

```
  [CloudtrailParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-cloudtrailparameters): {{
    CloudtrailParameters}}
  [DestinationPattern](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationpattern): {{String}}
  [DestinationType](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationtype): {{String}}
  [ELBLoadBalancerLoggingParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-elbloadbalancerloggingparameters): {{
    ELBLoadBalancerLoggingParameters}}
  [LogDeliveryParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-logdeliveryparameters): {{
    LogDeliveryParameters}}
  [RetentionInDays](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-retentionindays): {{Integer}}
  [VPCFlowLogParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-vpcflowlogparameters): {{
    VPCFlowLogParameters}}
  [WAFLoggingParameters](#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-wafloggingparameters): {{
    WAFLoggingParameters}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-properties"></a>

`CloudtrailParameters`  <a name="cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-cloudtrailparameters"></a>
 Configuration parameters specific to AWS CloudTrail when CloudTrail is the source type.
*Required*: No
*Type*: [CloudtrailParameters](aws-properties-observabilityadmin-telemetryrule-cloudtrailparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPattern`  <a name="cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationpattern"></a>
 The pattern used to generate the destination path or name, supporting macros like <resourceId> and <accountId>.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationType`  <a name="cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationtype"></a>
 The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").
*Required*: No
*Type*: String
*Allowed values*: `cloud-watch-logs`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ELBLoadBalancerLoggingParameters`  <a name="cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-elbloadbalancerloggingparameters"></a>
 Configuration parameters specific to ELB load balancer logging when ELB is the resource type.
*Required*: No
*Type*: [ELBLoadBalancerLoggingParameters](aws-properties-observabilityadmin-telemetryrule-elbloadbalancerloggingparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogDeliveryParameters`  <a name="cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-logdeliveryparameters"></a>
The configuration parameters for log delivery when the resource type supports configurable log types, such as Amazon Bedrock Knowledge Bases or Elastic Load Balancing Application Load Balancers.
*Required*: No
*Type*: [LogDeliveryParameters](aws-properties-observabilityadmin-telemetryrule-logdeliveryparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetentionInDays`  <a name="cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-retentionindays"></a>
 The number of days to retain the telemetry data in the destination.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VPCFlowLogParameters`  <a name="cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-vpcflowlogparameters"></a>
 Configuration parameters specific to VPC Flow Logs when VPC is the resource type.
*Required*: No
*Type*: [VPCFlowLogParameters](aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WAFLoggingParameters`  <a name="cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-wafloggingparameters"></a>
 Configuration parameters specific to WAF logging when WAF is the resource type.
*Required*: No
*Type*: [WAFLoggingParameters](aws-properties-observabilityadmin-telemetryrule-wafloggingparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
