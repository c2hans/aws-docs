---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ClientMetadataURLType.html
---

# ClientMetadataURLType

A client metadata document URL that Amazon Cognito has received for a Client ID Metadata Document (CIMD) policy, with its cache state.

## Contents
<a name="API_ClientMetadataURLType_Contents"></a>

 ** URL **   <a name="CognitoUserPools-Type-ClientMetadataURLType-URL"></a>
The client metadata document URL.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.
Pattern: `^https://[^\s]+$`
Required: Yes

 ** CachedDate **   <a name="CognitoUserPools-Type-ClientMetadataURLType-CachedDate"></a>
The date and time when Amazon Cognito cached the client metadata document from this URL. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** ExpirationDate **   <a name="CognitoUserPools-Type-ClientMetadataURLType-ExpirationDate"></a>
The date and time when the cached client metadata document expires. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

## See Also
<a name="API_ClientMetadataURLType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ClientMetadataURLType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ClientMetadataURLType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ClientMetadataURLType)
