---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BasicAuthConnectionMetadata.html
---

# BasicAuthConnectionMetadata
<a name="API_BasicAuthConnectionMetadata"></a>

Metadata for basic authentication using username and password.

## Contents
<a name="API_BasicAuthConnectionMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BaseEndpoint **   <a name="QS-Type-BasicAuthConnectionMetadata-BaseEndpoint"></a>
The base URL endpoint for the external service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** Password **   <a name="QS-Type-BasicAuthConnectionMetadata-Password"></a>
The password for basic authentication.
Type: String
Required: Yes

 ** Username **   <a name="QS-Type-BasicAuthConnectionMetadata-Username"></a>
The username for basic authentication.
Type: String
Required: Yes

## See Also
<a name="API_BasicAuthConnectionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BasicAuthConnectionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BasicAuthConnectionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BasicAuthConnectionMetadata)
