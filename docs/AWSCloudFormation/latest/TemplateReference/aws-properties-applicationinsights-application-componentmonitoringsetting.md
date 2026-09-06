---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-componentmonitoringsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application ComponentMonitoringSetting
<a name="aws-properties-applicationinsights-application-componentmonitoringsetting"></a>

The `AWS::ApplicationInsights::Application ComponentMonitoringSetting` property type defines the monitoring setting of the component.

## Syntax
<a name="aws-properties-applicationinsights-application-componentmonitoringsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-componentmonitoringsetting-syntax.json"></a>

```
{
  "[ComponentARN](#cfn-applicationinsights-application-componentmonitoringsetting-componentarn)" : {{String}},
  "[ComponentConfigurationMode](#cfn-applicationinsights-application-componentmonitoringsetting-componentconfigurationmode)" : {{String}},
  "[ComponentName](#cfn-applicationinsights-application-componentmonitoringsetting-componentname)" : {{String}},
  "[CustomComponentConfiguration](#cfn-applicationinsights-application-componentmonitoringsetting-customcomponentconfiguration)" : {{ComponentConfiguration}},
  "[DefaultOverwriteComponentConfiguration](#cfn-applicationinsights-application-componentmonitoringsetting-defaultoverwritecomponentconfiguration)" : {{ComponentConfiguration}},
  "[Tier](#cfn-applicationinsights-application-componentmonitoringsetting-tier)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-componentmonitoringsetting-syntax.yaml"></a>

```
  [ComponentARN](#cfn-applicationinsights-application-componentmonitoringsetting-componentarn): {{String}}
  [ComponentConfigurationMode](#cfn-applicationinsights-application-componentmonitoringsetting-componentconfigurationmode): {{String}}
  [ComponentName](#cfn-applicationinsights-application-componentmonitoringsetting-componentname): {{String}}
  [CustomComponentConfiguration](#cfn-applicationinsights-application-componentmonitoringsetting-customcomponentconfiguration): {{
    ComponentConfiguration}}
  [DefaultOverwriteComponentConfiguration](#cfn-applicationinsights-application-componentmonitoringsetting-defaultoverwritecomponentconfiguration): {{
    ComponentConfiguration}}
  [Tier](#cfn-applicationinsights-application-componentmonitoringsetting-tier): {{String}}
```

## Properties
<a name="aws-properties-applicationinsights-application-componentmonitoringsetting-properties"></a>

`ComponentARN`  <a name="cfn-applicationinsights-application-componentmonitoringsetting-componentarn"></a>
The ARN of the component. Either the component ARN or the component name is required.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[\w]+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
*Minimum*: `20`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComponentConfigurationMode`  <a name="cfn-applicationinsights-application-componentmonitoringsetting-componentconfigurationmode"></a>
Component monitoring can be configured in one of the following three modes:
+ `DEFAULT`: The component will be configured with the recommended default monitoring settings of the selected `Tier`.
+ `CUSTOM`: The component will be configured with the customized monitoring settings that are specified in `CustomComponentConfiguration`. If used, `CustomComponentConfiguration` must be provided.
+ `DEFAULT_WITH_OVERWRITE`: The component will be configured with the recommended default monitoring settings of the selected `Tier`, and merged with customized overwrite settings that are specified in `DefaultOverwriteComponentConfiguration`. If used, `DefaultOverwriteComponentConfiguration` must be provided.
*Required*: Yes
*Type*: String
*Allowed values*: `DEFAULT | DEFAULT_WITH_OVERWRITE | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComponentName`  <a name="cfn-applicationinsights-application-componentmonitoringsetting-componentname"></a>
The name of the component. Either the component ARN or the component name is required.
*Required*: No
*Type*: String
*Pattern*: `^[\d\w\-_.+]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomComponentConfiguration`  <a name="cfn-applicationinsights-application-componentmonitoringsetting-customcomponentconfiguration"></a>
Customized monitoring settings. Required if CUSTOM mode is configured in `ComponentConfigurationMode`.
*Required*: No
*Type*: [ComponentConfiguration](aws-properties-applicationinsights-application-componentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOverwriteComponentConfiguration`  <a name="cfn-applicationinsights-application-componentmonitoringsetting-defaultoverwritecomponentconfiguration"></a>
Customized overwrite monitoring settings. Required if CUSTOM mode is configured in `ComponentConfigurationMode`.
*Required*: No
*Type*: [ComponentConfiguration](aws-properties-applicationinsights-application-componentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tier`  <a name="cfn-applicationinsights-application-componentmonitoringsetting-tier"></a>
The tier of the application component. Supported tiers include `DOT_NET_CORE`, `DOT_NET_WORKER`, `DOT_NET_WEB`, `SQL_SERVER`, `SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP`, `SQL_SERVER_FAILOVER_CLUSTER_INSTANCE`, `MYSQL`, `POSTGRESQL`, `JAVA_JMX`, `ORACLE`, `SAP_HANA_MULTI_NODE`, `SAP_HANA_SINGLE_NODE`, `SAP_HANA_HIGH_AVAILABILITY`, `SHAREPOINT`. `ACTIVE_DIRECTORY`, and `DEFAULT`.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Z][A-Z_]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
