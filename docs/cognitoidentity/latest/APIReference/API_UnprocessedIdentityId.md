---
source_url: https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UnprocessedIdentityId.html
---

# UnprocessedIdentityId
<a name="API_UnprocessedIdentityId"></a>

An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.

## Contents
<a name="API_UnprocessedIdentityId_Contents"></a>

 ** ErrorCode **   <a name="CognitoIdentity-Type-UnprocessedIdentityId-ErrorCode"></a>
The error code indicating the type of error that occurred.
Type: String
Valid Values: `AccessDenied | InternalServerError`
Required: No

 ** IdentityId **   <a name="CognitoIdentity-Type-UnprocessedIdentityId-IdentityId"></a>
A unique identifier in the format REGION:GUID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: No

## See Also
<a name="API_UnprocessedIdentityId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/UnprocessedIdentityId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/UnprocessedIdentityId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/UnprocessedIdentityId)
