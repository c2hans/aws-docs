---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_RetryInfo.html
---

# RetryInfo
<a name="API_RetryInfo"></a>

Contains information about whether running a failed protected query or protected job again might succeed.

## Contents
<a name="API_RetryInfo_Contents"></a>

 ** retryable **   <a name="API-Type-RetryInfo-retryable"></a>
Specifies whether running the same request again might succeed. `true` means that the failure was transient. `false` means that running the same request again is not expected to succeed.
Type: Boolean
Required: No

## See Also
<a name="API_RetryInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/RetryInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/RetryInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/RetryInfo)
