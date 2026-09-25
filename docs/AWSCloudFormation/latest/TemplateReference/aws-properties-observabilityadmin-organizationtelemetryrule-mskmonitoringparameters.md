---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-mskmonitoringparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule MskMonitoringParameters
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-mskmonitoringparameters"></a>

 Configuration parameters for Amazon MSK cluster monitoring, including enhanced monitoring level settings.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-mskmonitoringparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-mskmonitoringparameters-syntax.json"></a>

```
{
  "[EnhancedMonitoring](#cfn-observabilityadmin-organizationtelemetryrule-mskmonitoringparameters-enhancedmonitoring)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-mskmonitoringparameters-syntax.yaml"></a>

```
  [EnhancedMonitoring](#cfn-observabilityadmin-organizationtelemetryrule-mskmonitoringparameters-enhancedmonitoring): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-mskmonitoringparameters-properties"></a>

`EnhancedMonitoring`  <a name="cfn-observabilityadmin-organizationtelemetryrule-mskmonitoringparameters-enhancedmonitoring"></a>
 The level of enhanced monitoring for the MSK cluster.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | PER_BROKER | PER_TOPIC_PER_BROKER | PER_TOPIC_PER_PARTITION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
