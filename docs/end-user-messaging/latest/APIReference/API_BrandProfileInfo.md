---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_BrandProfileInfo.html
---

# BrandProfileInfo
<a name="API_BrandProfileInfo"></a>

Contains information about a brand profile.

## Contents
<a name="API_BrandProfileInfo_Contents"></a>

 ** brandProfileArn **   <a name="endusermessaging-Type-BrandProfileInfo-brandProfileArn"></a>
The Amazon Resource Name (ARN) of the brand profile.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `arn:[A-Za-z0-9_:/-]+`
Required: Yes

 ** brandProfileId **   <a name="endusermessaging-Type-BrandProfileInfo-brandProfileId"></a>
The unique identifier of the brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** brandProfileName **   <a name="endusermessaging-Type-BrandProfileInfo-brandProfileName"></a>
The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** createdAt **   <a name="endusermessaging-Type-BrandProfileInfo-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** deletionProtectionEnabled **   <a name="endusermessaging-Type-BrandProfileInfo-deletionProtectionEnabled"></a>
Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.
Type: Boolean
Required: Yes

 ** status **   <a name="endusermessaging-Type-BrandProfileInfo-status"></a>
The current lifecycle status of the brand profile.
Type: String
Valid Values: `ACTIVE | BLOCKED | PAUSED | CANCELLED | FAILED`
Required: Yes

 ** updatedAt **   <a name="endusermessaging-Type-BrandProfileInfo-updatedAt"></a>
The time when the resource was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

## See Also
<a name="API_BrandProfileInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/BrandProfileInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/BrandProfileInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/BrandProfileInfo)
