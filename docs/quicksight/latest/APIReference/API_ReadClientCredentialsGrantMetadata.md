---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReadClientCredentialsGrantMetadata.html
---

# ReadClientCredentialsGrantMetadata
<a name="API_ReadClientCredentialsGrantMetadata"></a>

Read-only metadata for OAuth2 client credentials grant authentication configuration.

## Contents
<a name="API_ReadClientCredentialsGrantMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BaseEndpoint **   <a name="QS-Type-ReadClientCredentialsGrantMetadata-BaseEndpoint"></a>
The base endpoint URL for the OAuth2 client credentials grant flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** ClientCredentialsSource **   <a name="QS-Type-ReadClientCredentialsGrantMetadata-ClientCredentialsSource"></a>
The source of client credentials for the OAuth2 client credentials grant flow.
Type: String
Valid Values: `PLAIN_CREDENTIALS`
Required: No

 ** ReadClientCredentialsDetails **   <a name="QS-Type-ReadClientCredentialsGrantMetadata-ReadClientCredentialsDetails"></a>
The read-only client credentials configuration details.
Type: [ReadClientCredentialsDetails](API_ReadClientCredentialsDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ReadClientCredentialsGrantMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReadClientCredentialsGrantMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReadClientCredentialsGrantMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReadClientCredentialsGrantMetadata)
