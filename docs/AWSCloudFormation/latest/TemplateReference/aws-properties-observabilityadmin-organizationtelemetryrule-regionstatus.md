---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-regionstatus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule RegionStatus
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-regionstatus"></a>

 Represents the status of a multi-region operation in a specific AWS Region. This structure is used to report per-region progress for both telemetry evaluation and telemetry rule replication.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-regionstatus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-regionstatus-syntax.json"></a>

```
{
  "[Region](#cfn-observabilityadmin-organizationtelemetryrule-regionstatus-region)" : {{String}},
  "[RuleArn](#cfn-observabilityadmin-organizationtelemetryrule-regionstatus-rulearn)" : {{String}},
  "[Status](#cfn-observabilityadmin-organizationtelemetryrule-regionstatus-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-regionstatus-syntax.yaml"></a>

```
  [Region](#cfn-observabilityadmin-organizationtelemetryrule-regionstatus-region): {{String}}
  [RuleArn](#cfn-observabilityadmin-organizationtelemetryrule-regionstatus-rulearn): {{String}}
  [Status](#cfn-observabilityadmin-organizationtelemetryrule-regionstatus-status): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-regionstatus-properties"></a>

`Region`  <a name="cfn-observabilityadmin-organizationtelemetryrule-regionstatus-region"></a>
 The AWS Region code (for example, `eu-west-1` or `us-west-2`) that this status applies to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleArn`  <a name="cfn-observabilityadmin-organizationtelemetryrule-regionstatus-rulearn"></a>
 The Amazon Resource Name (ARN) of the telemetry rule in this spoke region. This field is only present for telemetry rule region statuses and is populated when the rule has been successfully created in the spoke region (status is `ACTIVE`).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-observabilityadmin-organizationtelemetryrule-regionstatus-status"></a>
 The status of the operation in this region. For telemetry evaluation, valid values include `STARTING`, `RUNNING`, and `FAILED_START`. For telemetry rules, valid values include `PENDING`, `ACTIVE`, and `FAILED`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
