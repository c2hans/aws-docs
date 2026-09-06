---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails.html
---

# AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails
<a name="API_AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails"></a>

 The scheduled time period (UTC) during which Amazon MQ begins to apply pending updates or patches to the broker.

## Contents
<a name="API_AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails_Contents"></a>

 ** DayOfWeek **   <a name="securityhub-Type-AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails-DayOfWeek"></a>
 The day of the week on which the maintenance window falls.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TimeOfDay **   <a name="securityhub-Type-AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails-TimeOfDay"></a>
 The time, in 24-hour format, on which the maintenance window falls.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TimeZone **   <a name="securityhub-Type-AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails-TimeZone"></a>
 The time zone in either the Country/City format or the UTC offset format. UTC is the default format.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails)
