---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReadBasicAuthConnectionMetadata.html
---

# ReadBasicAuthConnectionMetadata
<a name="API_ReadBasicAuthConnectionMetadata"></a>

Read-only metadata for basic authentication connections, containing non-sensitive configuration details.

## Contents
<a name="API_ReadBasicAuthConnectionMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BaseEndpoint **   <a name="QS-Type-ReadBasicAuthConnectionMetadata-BaseEndpoint"></a>
The base endpoint URL for basic authentication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** Username **   <a name="QS-Type-ReadBasicAuthConnectionMetadata-Username"></a>
The username used for basic authentication.
Type: String
Required: Yes

## See Also
<a name="API_ReadBasicAuthConnectionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReadBasicAuthConnectionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReadBasicAuthConnectionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReadBasicAuthConnectionMetadata)
