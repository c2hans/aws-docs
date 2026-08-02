---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceUserSummary.html
---

# AppInstanceUserSummary
<a name="API_AppInstanceUserSummary"></a>

Summary of the details of an `AppInstanceUser`.

## Contents
<a name="API_AppInstanceUserSummary_Contents"></a>

 ** AppInstanceUserArn **   <a name="chimesdk-Type-AppInstanceUserSummary-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** Metadata **   <a name="chimesdk-Type-AppInstanceUserSummary-Metadata"></a>
The metadata of the `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Name **   <a name="chimesdk-Type-AppInstanceUserSummary-Name"></a>
The name of an `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AppInstanceUserSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/AppInstanceUserSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/AppInstanceUserSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/AppInstanceUserSummary)
