---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-internetmonitor-monitor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InternetMonitor::Monitor
<a name="aws-resource-internetmonitor-monitor"></a>

The `AWS::InternetMonitor::Monitor` resource is an Internet Monitor resource type that contains information about how you create a monitor in Amazon CloudWatch Internet Monitor. A monitor in Internet Monitor provides visibility into performance and availability between your applications hosted on AWS and your end users, using a traffic profile that it creates based on the application resources that you add: Virtual Private Clouds (VPCs), Amazon CloudFront distributions, or WorkSpaces directories.

Internet Monitor also alerts you to internet issues that impact your application in the city-networks (geographies and networks) where your end users use it. With Internet Monitor, you can quickly pinpoint the locations and providers that are affected, so that you can address the issue.

For more information, see [ Using Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) in the *Amazon CloudWatch User Guide*.

## Syntax
<a name="aws-resource-internetmonitor-monitor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-internetmonitor-monitor-syntax.json"></a>

```
{
  "Type" : "AWS::InternetMonitor::Monitor",
  "Properties" : {
      "[HealthEventsConfig](#cfn-internetmonitor-monitor-healtheventsconfig)" : {{HealthEventsConfig}},
      "[IncludeLinkedAccounts](#cfn-internetmonitor-monitor-includelinkedaccounts)" : {{Boolean}},
      "[InternetMeasurementsLogDelivery](#cfn-internetmonitor-monitor-internetmeasurementslogdelivery)" : {{InternetMeasurementsLogDelivery}},
      "[LinkedAccountId](#cfn-internetmonitor-monitor-linkedaccountid)" : {{String}},
      "[MaxCityNetworksToMonitor](#cfn-internetmonitor-monitor-maxcitynetworkstomonitor)" : {{Integer}},
      "[MonitorName](#cfn-internetmonitor-monitor-monitorname)" : {{String}},
      "[Resources](#cfn-internetmonitor-monitor-resources)" : {{[ String, ... ]}},
      "[ResourcesToAdd](#cfn-internetmonitor-monitor-resourcestoadd)" : {{[ String, ... ]}},
      "[ResourcesToRemove](#cfn-internetmonitor-monitor-resourcestoremove)" : {{[ String, ... ]}},
      "[Status](#cfn-internetmonitor-monitor-status)" : {{String}},
      "[Tags](#cfn-internetmonitor-monitor-tags)" : {{[ Tag, ... ]}},
      "[TrafficPercentageToMonitor](#cfn-internetmonitor-monitor-trafficpercentagetomonitor)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-internetmonitor-monitor-syntax.yaml"></a>

```
Type: AWS::InternetMonitor::Monitor
Properties:
  [HealthEventsConfig](#cfn-internetmonitor-monitor-healtheventsconfig): {{
    HealthEventsConfig}}
  [IncludeLinkedAccounts](#cfn-internetmonitor-monitor-includelinkedaccounts): {{Boolean}}
  [InternetMeasurementsLogDelivery](#cfn-internetmonitor-monitor-internetmeasurementslogdelivery): {{
    InternetMeasurementsLogDelivery}}
  [LinkedAccountId](#cfn-internetmonitor-monitor-linkedaccountid): {{String}}
  [MaxCityNetworksToMonitor](#cfn-internetmonitor-monitor-maxcitynetworkstomonitor): {{Integer}}
  [MonitorName](#cfn-internetmonitor-monitor-monitorname): {{String}}
  [Resources](#cfn-internetmonitor-monitor-resources): {{
    - String}}
  [ResourcesToAdd](#cfn-internetmonitor-monitor-resourcestoadd): {{
    - String}}
  [ResourcesToRemove](#cfn-internetmonitor-monitor-resourcestoremove): {{
    - String}}
  [Status](#cfn-internetmonitor-monitor-status): {{String}}
  [Tags](#cfn-internetmonitor-monitor-tags): {{
    - Tag}}
  [TrafficPercentageToMonitor](#cfn-internetmonitor-monitor-trafficpercentagetomonitor): {{Integer}}
```

## Properties
<a name="aws-resource-internetmonitor-monitor-properties"></a>

`HealthEventsConfig`  <a name="cfn-internetmonitor-monitor-healtheventsconfig"></a>
A complex type with the configuration information that determines the threshold and other conditions for when Internet Monitor creates a health event for an overall performance or availability issue, across an application's geographies.
Defines the percentages, for overall performance scores and availability scores for an application, that are the thresholds for when Internet Monitor creates a health event. You can override the defaults to set a custom threshold for overall performance or availability scores, or both.
You can also set thresholds for local health scores,, where Internet Monitor creates a health event when scores cross a threshold for one or more city-networks, in addition to creating an event when an overall score crosses a threshold.
If you don't set a health event threshold, the default value is 95%.
For local thresholds, you also set a minimum percentage of overall traffic that is impacted by an issue before Internet Monitor creates an event. In addition, you can disable local thresholds, for performance scores, availability scores, or both.
For more information, see [ Change health event thresholds](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview) in the Internet Monitor section of the *CloudWatch User Guide*.
*Required*: No
*Type*: [HealthEventsConfig](aws-properties-internetmonitor-monitor-healtheventsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeLinkedAccounts`  <a name="cfn-internetmonitor-monitor-includelinkedaccounts"></a>
A boolean option that you can set to `TRUE` to include monitors for linked accounts in a list of monitors, when you've set up cross-account sharing in Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see [Internet Monitor cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html) in the Amazon CloudWatch User Guide.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InternetMeasurementsLogDelivery`  <a name="cfn-internetmonitor-monitor-internetmeasurementslogdelivery"></a>
Publish internet measurements for a monitor for all city-networks (up to the 500,000 service limit) to another location, such as an Amazon S3 bucket. Measurements are also published to Amazon CloudWatch Logs for the first 500 (by traffic volume) city-networks (client locations and ASNs, typically internet service providers or ISPs).
*Required*: No
*Type*: [InternetMeasurementsLogDelivery](aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkedAccountId`  <a name="cfn-internetmonitor-monitor-linkedaccountid"></a>
The account ID for an account that you've set up cross-account sharing for in Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see [Internet Monitor cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html) in the Amazon CloudWatch User Guide.
*Required*: No
*Type*: String
*Pattern*: `^(\d{12})$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxCityNetworksToMonitor`  <a name="cfn-internetmonitor-monitor-maxcitynetworkstomonitor"></a>
The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the network, such as an internet service provider, that clients access the resources through.
For more information, see [ Choosing a city-network maximum value](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html) in *Using Amazon CloudWatch Internet Monitor*.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `500000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MonitorName`  <a name="cfn-internetmonitor-monitor-monitorname"></a>
The name of the monitor. A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (\_).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Resources`  <a name="cfn-internetmonitor-monitor-resources"></a>
The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs). Use this option to add or remove resources when making an update.
Be aware that if you include content in the `Resources` field when you update a monitor, the `ResourcesToAdd` and `ResourcesToRemove` fields must be empty.
*Required*: No
*Type*: Array of String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesToAdd`  <a name="cfn-internetmonitor-monitor-resourcestoadd"></a>
The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be Amazon Virtual Private Cloud VPCs, Network Load Balancers (NLBs), Amazon CloudFront distributions, or Amazon WorkSpaces directories.
You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.
If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.
You can specify this field for a monitor update only if the `Resources` field is empty.
*Required*: No
*Type*: Array of String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesToRemove`  <a name="cfn-internetmonitor-monitor-resourcestoremove"></a>
The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs)
You can specify this field for a monitor update only if the `Resources` field is empty.
*Required*: No
*Type*: Array of String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-internetmonitor-monitor-status"></a>
The status of a monitor. The accepted values that you can specify for `Status` are `ACTIVE` and `INACTIVE`.
*Required*: No
*Type*: String
*Allowed values*: `PENDING | ACTIVE | INACTIVE | ERROR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-internetmonitor-monitor-tags"></a>
The tags for a monitor, listed as a set of *key:value* pairs.
*Required*: No
*Type*: Array of [Tag](aws-properties-internetmonitor-monitor-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrafficPercentageToMonitor`  <a name="cfn-internetmonitor-monitor-trafficpercentagetomonitor"></a>
The percentage of the internet-facing traffic for your application that you want to monitor. You can also, optionally, set a limit for the number of city-networks (client locations and ASNs, typically internet service providers) that Internet Monitor will monitor traffic for. The city-networks maximum limit caps the number of city-networks that Internet Monitor monitors for your application, regardless of the percentage of traffic that you choose to monitor.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-internetmonitor-monitor-return-values"></a>

### Ref
<a name="aws-resource-internetmonitor-monitor-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the monitor, such as `arn:aws:internetmonitor:us-east-1:111122223333:monitor/TestMonitor`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-internetmonitor-monitor-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-internetmonitor-monitor-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time when the monitor was created.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The last time that the monitor was modified.

`MonitorArn`  <a name="MonitorArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the monitor.

`ProcessingStatus`  <a name="ProcessingStatus-fn::getatt"></a>
The health of data processing for the monitor. For more information, see `ProcessingStatus` under [ MonitorListMember](https://docs.aws.amazon.com/internet-monitor/latest/api/API_MonitorListMember.html) in the *Amazon CloudWatch Internet Monitor API Reference*.

`ProcessingStatusInfo`  <a name="ProcessingStatusInfo-fn::getatt"></a>
Additional information about the health of the data processing for the monitor.
