---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ProactiveRefreshTokenRenewal.html
---

# ProactiveRefreshTokenRenewal
<a name="API_ProactiveRefreshTokenRenewal"></a>

Configuration settings for proactively refreshing OAuth tokens before they expire.

## Contents
<a name="API_ProactiveRefreshTokenRenewal_Contents"></a>

 ** DaysBeforeRenewal **   <a name="managedintegrations-Type-ProactiveRefreshTokenRenewal-DaysBeforeRenewal"></a>
The days before token expiration when the system should attempt to renew the token, specified in days.
Type: Integer
Valid Range: Minimum value of 30.
Required: No

 ** enabled **   <a name="managedintegrations-Type-ProactiveRefreshTokenRenewal-enabled"></a>
Indicates whether proactive refresh token renewal is enabled.
Type: Boolean
Required: No

## See Also
<a name="API_ProactiveRefreshTokenRenewal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ProactiveRefreshTokenRenewal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ProactiveRefreshTokenRenewal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ProactiveRefreshTokenRenewal)
