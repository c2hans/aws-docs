---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule VPCFlowLogParameters
<a name="aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters"></a>

 Configuration parameters specific to VPC Flow Logs.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters-syntax.json"></a>

```
{
  "[LogFormat](#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-logformat)" : {{String}},
  "[MaxAggregationInterval](#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-maxaggregationinterval)" : {{Integer}},
  "[TrafficType](#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-traffictype)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters-syntax.yaml"></a>

```
  [LogFormat](#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-logformat): {{String}}
  [MaxAggregationInterval](#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-maxaggregationinterval): {{Integer}}
  [TrafficType](#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-traffictype): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters-properties"></a>

`LogFormat`  <a name="cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-logformat"></a>
 The format in which VPC Flow Log entries should be logged.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxAggregationInterval`  <a name="cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-maxaggregationinterval"></a>
 The maximum interval in seconds between the capture of flow log records.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrafficType`  <a name="cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-traffictype"></a>
 The type of traffic to log (ACCEPT, REJECT, or ALL).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
