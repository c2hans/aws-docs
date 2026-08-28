---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule VPCFlowLogParameters
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters"></a>

 Configuration parameters specific to VPC Flow Logs.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-syntax.json"></a>

```
{
  "[LogFormat](#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-logformat)" : {{String}},
  "[MaxAggregationInterval](#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-maxaggregationinterval)" : {{Integer}},
  "[TrafficType](#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-traffictype)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-syntax.yaml"></a>

```
  [LogFormat](#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-logformat): {{String}}
  [MaxAggregationInterval](#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-maxaggregationinterval): {{Integer}}
  [TrafficType](#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-traffictype): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-properties"></a>

`LogFormat`  <a name="cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-logformat"></a>
 The format in which VPC Flow Log entries should be logged.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxAggregationInterval`  <a name="cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-maxaggregationinterval"></a>
 The maximum interval in seconds between the capture of flow log records.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrafficType`  <a name="cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-traffictype"></a>
 The type of traffic to log (ACCEPT, REJECT, or ALL).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
