---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule CloudtrailParameters
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters"></a>

 Parameters specific to AWS CloudTrail telemetry configuration.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-syntax.json"></a>

```
{
  "[AdvancedEventSelectors](#cfn-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-advancedeventselectors)" : {{[ AdvancedEventSelector, ... ]}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-syntax.yaml"></a>

```
  [AdvancedEventSelectors](#cfn-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-advancedeventselectors): {{
    - AdvancedEventSelector}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-properties"></a>

`AdvancedEventSelectors`  <a name="cfn-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-advancedeventselectors"></a>
 The advanced event selectors to use for filtering AWS CloudTrail events.
*Required*: Yes
*Type*: Array of [AdvancedEventSelector](aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
