---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_TermsType.html
---

# TermsType
<a name="API_TermsType"></a>

The details of a set of terms documents. For more information, see [Terms documents](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-terms-documents).

This data type is a response parameter of [CreateTerms](API_CreateTerms.md) and [UpdateTerms](API_UpdateTerms.md).

## Contents
<a name="API_TermsType_Contents"></a>

 ** ClientId **   <a name="CognitoUserPools-Type-TermsType-ClientId"></a>
The ID of the app client that the terms documents are assigned to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** CreationDate **   <a name="CognitoUserPools-Type-TermsType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: Yes

 ** Enforcement **   <a name="CognitoUserPools-Type-TermsType-Enforcement"></a>
This parameter is reserved for future use and currently accepts one value.
Type: String
Valid Values: `NONE`
Required: Yes

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-TermsType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: Yes

 ** Links **   <a name="CognitoUserPools-Type-TermsType-Links"></a>
A map of URLs to languages. For each localized language that will view the requested `TermsName`, assign a URL. A selection of `cognito:default` displays for all languages that don't have a language-specific URL.
For example, `"cognito:default": "https://terms.example.com", "cognito:spanish": "https://terms.example.com/es"`.
Type: String to string map
Map Entries: Maximum number of 13 items.
Key Pattern: `^cognito:(default|dutch|english|french|spanish|german|bahasa-indonesia|italian|japanese|korean|portuguese-brazil|chinese-(simplified|traditional))$`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `^[\p{L}\p{M}\p{S}\p{N}\p{P}]+$`
Required: Yes

 ** TermsId **   <a name="CognitoUserPools-Type-TermsType-TermsId"></a>
The ID of the terms documents.
Type: String
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$`
Required: Yes

 ** TermsName **   <a name="CognitoUserPools-Type-TermsType-TermsName"></a>
The type and friendly name of the terms documents.
Type: String
Pattern: `^(terms-of-use|privacy-policy)$`
Required: Yes

 ** TermsSource **   <a name="CognitoUserPools-Type-TermsType-TermsSource"></a>
This parameter is reserved for future use and currently accepts one value.
Type: String
Valid Values: `LINK`
Required: Yes

 ** UserPoolId **   <a name="CognitoUserPools-Type-TermsType-UserPoolId"></a>
The ID of the user pool that contains the terms documents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_TermsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/TermsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/TermsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/TermsType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
