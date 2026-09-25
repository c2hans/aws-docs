---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AccessProfile.html
---

# AccessProfile
<a name="API_AccessProfile"></a>

An Access Profile.

## Contents
<a name="API_AccessProfile_Contents"></a>

 ** arn **   <a name="cloudwatchomni-Type-AccessProfile-arn"></a>
The ARN of this access profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** createdAt **   <a name="cloudwatchomni-Type-AccessProfile-createdAt"></a>
The timestamp when the access profile was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-AccessProfile-name"></a>
A name that identifies the access profile.
Type: String
Required: Yes

 ** profileId **   <a name="cloudwatchomni-Type-AccessProfile-profileId"></a>
The unique ID of the access profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** spaceId **   <a name="cloudwatchomni-Type-AccessProfile-spaceId"></a>
The ID of the space the profile belongs to.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-AccessProfile-updatedAt"></a>
The timestamp when the access profile was last updated.
Type: Timestamp
Required: Yes

 ** assumeStatus **   <a name="cloudwatchomni-Type-AccessProfile-assumeStatus"></a>
The calling principal's authorization to assume this access profile.
Type: String
Valid Values: `ALLOWED | DENIED`
Required: No

 ** description **   <a name="cloudwatchomni-Type-AccessProfile-description"></a>
An optional description of the access profile.
Type: String
Required: No

 ** profileType **   <a name="cloudwatchomni-Type-AccessProfile-profileType"></a>
Who manages the access profile.
Type: String
Valid Values: `SERVICE_MANAGED | CUSTOMER_MANAGED`
Required: No

## See Also
<a name="API_AccessProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AccessProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AccessProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AccessProfile)
