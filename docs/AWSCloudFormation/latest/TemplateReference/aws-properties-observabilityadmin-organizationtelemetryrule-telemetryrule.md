---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule TelemetryRule
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule"></a>

 Defines how telemetry should be configured for specific AWS resources.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule-syntax.json"></a>

```
{
  "[AllowFieldUpdates](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-allowfieldupdates)" : {{Boolean}},
  "[AllRegions](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-allregions)" : {{Boolean}},
  "[DestinationConfiguration](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-destinationconfiguration)" : {{TelemetryDestinationConfiguration}},
  "[Regions](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-regions)" : {{[ String, ... ]}},
  "[ResourceType](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-resourcetype)" : {{String}},
  "[Scope](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-scope)" : {{String}},
  "[SelectionCriteria](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-selectioncriteria)" : {{String}},
  "[TelemetrySourceTypes](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrysourcetypes)" : {{[ String, ... ]}},
  "[TelemetryType](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule-syntax.yaml"></a>

```
  [AllowFieldUpdates](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-allowfieldupdates): {{Boolean}}
  [AllRegions](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-allregions): {{Boolean}}
  [DestinationConfiguration](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-destinationconfiguration): {{
    TelemetryDestinationConfiguration}}
  [Regions](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-regions): {{
    - String}}
  [ResourceType](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-resourcetype): {{String}}
  [Scope](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-scope): {{String}}
  [SelectionCriteria](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-selectioncriteria): {{String}}
  [TelemetrySourceTypes](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrysourcetypes): {{
    - String}}
  [TelemetryType](#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrytype): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule-properties"></a>

`AllowFieldUpdates`  <a name="cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-allowfieldupdates"></a>
 If set to `true`, Amazon CloudWatch Observability Admin detects and remediates configuration drift in telemetry resources that it manages. For example, if a VPC flow log's format, traffic type, or aggregation interval no longer matches the rule's destination configuration, the flow log is replaced with one that matches. Only Observability Admin-managed resources are updated; customer-created resources are never modified. Currently supported for `AWS::EC2::VPC` resources (VPC flow logs).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllRegions`  <a name="cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-allregions"></a>
 If set to `true`, the telemetry rule is replicated to all AWS Regions where Amazon CloudWatch Observability Admin is available in the current partition. When new regions become available, the rule automatically replicates to them. Mutually exclusive with `Regions`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationConfiguration`  <a name="cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-destinationconfiguration"></a>
 Configuration specifying where and how the telemetry data should be delivered.
*Required*: No
*Type*: [TelemetryDestinationConfiguration](aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-regions"></a>
 An optional list of AWS Regions where this telemetry rule should be replicated. When specified, the rule is created in the home region and automatically replicated to all listed regions. Mutually exclusive with `AllRegions`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-resourcetype"></a>
 The type of AWS resource to configure telemetry for (for example, `AWS::EC2::VPC`, `AWS::EKS::Cluster`, `AWS::ElasticLoadBalancingV2::LoadBalancer`, or `AWS::Bedrock::KnowledgeBase`).
*Required*: Yes
*Type*: String
*Allowed values*: `AWS::EC2::VPC | AWS::WAFv2::WebACL | AWS::CloudTrail | AWS::EKS::Cluster | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::EC2::Instance | AWS::SecurityHub::Hub`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-scope"></a>
 The organizational scope to which the rule applies, specified using accounts or organizational units.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectionCriteria`  <a name="cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-selectioncriteria"></a>
 Criteria for selecting which resources the rule applies to, such as resource tags.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TelemetrySourceTypes`  <a name="cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrysourcetypes"></a>
 The specific telemetry source types to configure for the resource, such as VPC\_FLOW\_LOGS or EKS\_AUDIT\_LOGS. TelemetrySourceTypes must be correlated with the specific resource type.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TelemetryType`  <a name="cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrytype"></a>
 The type of telemetry to collect (Logs, Metrics, or Traces).
*Required*: Yes
*Type*: String
*Allowed values*: `Logs | Metrics`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
