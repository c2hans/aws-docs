---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ServerlessFunctionMetadata.html
---

# ServerlessFunctionMetadata
<a name="API_ServerlessFunctionMetadata"></a>

Contains metadata about a serverless function associated with a covered resource.

## Contents
<a name="API_ServerlessFunctionMetadata_Contents"></a>

 ** functionTags **   <a name="inspector2-Type-ServerlessFunctionMetadata-functionTags"></a>
The tags associated with the serverless function.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** runtime **   <a name="inspector2-Type-ServerlessFunctionMetadata-runtime"></a>
The runtime of the serverless function.
Type: String
Required: No

 ** serverlessFunctionName **   <a name="inspector2-Type-ServerlessFunctionMetadata-serverlessFunctionName"></a>
The name of the serverless function.
Type: String
Required: No

## See Also
<a name="API_ServerlessFunctionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ServerlessFunctionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ServerlessFunctionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ServerlessFunctionMetadata)
