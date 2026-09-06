---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ExpirationSettings.html
---

# ExpirationSettings
<a name="API_ExpirationSettings"></a>

Determines the interval after which an `AppInstanceUser` is automatically deleted.

## Contents
<a name="API_ExpirationSettings_Contents"></a>

 ** ExpirationCriterion **   <a name="chimesdk-Type-ExpirationSettings-ExpirationCriterion"></a>
Specifies the conditions under which an `AppInstanceUser` will expire.
Type: String
Valid Values: `CREATED_TIMESTAMP`
Required: Yes

 ** ExpirationDays **   <a name="chimesdk-Type-ExpirationSettings-ExpirationDays"></a>
The period in days after which an `AppInstanceUser` will be automatically deleted.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5475.
Required: Yes

## See Also
<a name="API_ExpirationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/ExpirationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/ExpirationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/ExpirationSettings)
