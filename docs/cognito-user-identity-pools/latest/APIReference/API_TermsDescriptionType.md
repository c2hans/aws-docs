---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_TermsDescriptionType.html
---

# TermsDescriptionType
<a name="API_TermsDescriptionType"></a>

The details of a set of terms documents. For more information, see [Terms documents](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-terms-documents).

This data type is a response parameter of [ListTerms](API_ListTerms.md).

## Contents
<a name="API_TermsDescriptionType_Contents"></a>

 ** CreationDate **   <a name="CognitoUserPools-Type-TermsDescriptionType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: Yes

 ** Enforcement **   <a name="CognitoUserPools-Type-TermsDescriptionType-Enforcement"></a>
This parameter is reserved for future use and currently accepts one value.
Type: String
Valid Values: `NONE`
Required: Yes

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-TermsDescriptionType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: Yes

 ** TermsId **   <a name="CognitoUserPools-Type-TermsDescriptionType-TermsId"></a>
The ID of the requested terms documents.
Type: String
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$`
Required: Yes

 ** TermsName **   <a name="CognitoUserPools-Type-TermsDescriptionType-TermsName"></a>
The type and friendly name of the requested terms documents.
Type: String
Pattern: `^(terms-of-use|privacy-policy)$`
Required: Yes

## See Also
<a name="API_TermsDescriptionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/TermsDescriptionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/TermsDescriptionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/TermsDescriptionType)
