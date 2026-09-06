---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_SseConfig.html
---

# SseConfig
<a name="API_SseConfig"></a>

Server-side encryption (SSE) settings for a store.

## Contents
<a name="API_SseConfig_Contents"></a>

 ** type **   <a name="omics-Type-SseConfig-type"></a>
The encryption type.
Type: String
Valid Values: `KMS`
Required: Yes

 ** keyArn **   <a name="omics-Type-SseConfig-keyArn"></a>
An encryption key ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*).*`
Required: No

## See Also
<a name="API_SseConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/SseConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/SseConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/SseConfig)
