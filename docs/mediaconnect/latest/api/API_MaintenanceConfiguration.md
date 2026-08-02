---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MaintenanceConfiguration.html
---

# MaintenanceConfiguration
<a name="API_MaintenanceConfiguration"></a>

The configuration settings for maintenance operations, including preferred maintenance windows and schedules.

## Contents
<a name="API_MaintenanceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** default **   <a name="mediaconnect-Type-MaintenanceConfiguration-default"></a>
Default maintenance configuration settings.
Type: [DefaultMaintenanceConfiguration](API_DefaultMaintenanceConfiguration.md) object
Required: No

 ** preferredDayTime **   <a name="mediaconnect-Type-MaintenanceConfiguration-preferredDayTime"></a>
Preferred day and time maintenance configuration settings.
Type: [PreferredDayTimeMaintenanceConfiguration](API_PreferredDayTimeMaintenanceConfiguration.md) object
Required: No

## See Also
<a name="API_MaintenanceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MaintenanceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MaintenanceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MaintenanceConfiguration)
