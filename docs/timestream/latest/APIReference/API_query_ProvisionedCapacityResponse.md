---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ProvisionedCapacityResponse.html
---

# ProvisionedCapacityResponse
<a name="API_query_ProvisionedCapacityResponse"></a>

The response to a request to update the provisioned capacity settings for querying data.

## Contents
<a name="API_query_ProvisionedCapacityResponse_Contents"></a>

 ** ActiveQueryTCU **   <a name="timestream-Type-query_ProvisionedCapacityResponse-ActiveQueryTCU"></a>
The number of Timestream Compute Units (TCUs) provisioned in the account. This field is only visible when the compute mode is `PROVISIONED`.
Type: Integer
Required: No

 ** LastUpdate **   <a name="timestream-Type-query_ProvisionedCapacityResponse-LastUpdate"></a>
Information about the last update to the provisioned capacity settings.
Type: [LastUpdate](API_query_LastUpdate.md) object
Required: No

 ** NotificationConfiguration **   <a name="timestream-Type-query_ProvisionedCapacityResponse-NotificationConfiguration"></a>
An object that contains settings for notifications that are sent whenever the provisioned capacity settings are modified. This field is only visible when the compute mode is `PROVISIONED`.
Type: [AccountSettingsNotificationConfiguration](API_query_AccountSettingsNotificationConfiguration.md) object
Required: No

## See Also
<a name="API_query_ProvisionedCapacityResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ProvisionedCapacityResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ProvisionedCapacityResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ProvisionedCapacityResponse)
