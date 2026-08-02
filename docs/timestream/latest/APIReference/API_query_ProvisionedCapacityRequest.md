---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ProvisionedCapacityRequest.html
---

# ProvisionedCapacityRequest
<a name="API_query_ProvisionedCapacityRequest"></a>

A request to update the provisioned capacity settings for querying data.

## Contents
<a name="API_query_ProvisionedCapacityRequest_Contents"></a>

 ** TargetQueryTCU **   <a name="timestream-Type-query_ProvisionedCapacityRequest-TargetQueryTCU"></a>
The target compute capacity for querying data, specified in Timestream Compute Units (TCUs).
Type: Integer
Required: Yes

 ** NotificationConfiguration **   <a name="timestream-Type-query_ProvisionedCapacityRequest-NotificationConfiguration"></a>
Configuration settings for notifications related to the provisioned capacity update.
Type: [AccountSettingsNotificationConfiguration](API_query_AccountSettingsNotificationConfiguration.md) object
Required: No

## See Also
<a name="API_query_ProvisionedCapacityRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ProvisionedCapacityRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ProvisionedCapacityRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ProvisionedCapacityRequest)
