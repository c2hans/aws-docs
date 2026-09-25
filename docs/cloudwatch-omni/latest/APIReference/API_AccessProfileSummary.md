---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AccessProfileSummary.html
---

# AccessProfileSummary
<a name="API_AccessProfileSummary"></a>

Summary of an access profile. Call GetAccessProfile for the full profile.

## Contents
<a name="API_AccessProfileSummary_Contents"></a>

 ** arn **   <a name="cloudwatchomni-Type-AccessProfileSummary-arn"></a>
The ARN of this access profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-AccessProfileSummary-name"></a>
A name that identifies the access profile.
Type: String
Required: Yes

 ** profileId **   <a name="cloudwatchomni-Type-AccessProfileSummary-profileId"></a>
The unique ID of the access profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** description **   <a name="cloudwatchomni-Type-AccessProfileSummary-description"></a>
An optional description of the access profile.
Type: String
Required: No

 ** profileType **   <a name="cloudwatchomni-Type-AccessProfileSummary-profileType"></a>
Who manages the access profile.
Type: String
Valid Values: `SERVICE_MANAGED | CUSTOMER_MANAGED`
Required: No

## See Also
<a name="API_AccessProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AccessProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AccessProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AccessProfileSummary)
