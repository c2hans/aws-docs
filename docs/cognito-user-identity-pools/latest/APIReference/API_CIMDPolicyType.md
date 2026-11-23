---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CIMDPolicyType.html
---

# CIMDPolicyType

The configuration of a Client ID Metadata Document (CIMD) policy, including its app client, name, cache duration, and URL patterns.

## Contents
<a name="API_CIMDPolicyType_Contents"></a>

 ** CIMDPolicyId **   <a name="CognitoUserPools-Type-CIMDPolicyType-CIMDPolicyId"></a>
The ID of the CIMD policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9]+$`
Required: Yes

 ** PolicyName **   <a name="CognitoUserPools-Type-CIMDPolicyType-PolicyName"></a>
The friendly name of the CIMD policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
Required: Yes

 ** UserPoolId **   <a name="CognitoUserPools-Type-CIMDPolicyType-UserPoolId"></a>
The ID of the user pool that contains the CIMD policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

 ** CacheDuration **   <a name="CognitoUserPools-Type-CIMDPolicyType-CacheDuration"></a>
The length of time, in seconds, that Amazon Cognito caches a client metadata document when the document's `Cache-Control` header doesn't set a `max-age` between one day and one year. When the header sets a `max-age` in that range, Amazon Cognito uses the header value instead.
Type: Integer
Valid Range: Minimum value of 86400. Maximum value of 31556952.
Required: No

 ** ClientId **   <a name="CognitoUserPools-Type-CIMDPolicyType-ClientId"></a>
The ID of the app client that the CIMD policy is associated with. Amazon Cognito omits this value when the app client no longer exists.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: No

 ** CreationDate **   <a name="CognitoUserPools-Type-CIMDPolicyType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-CIMDPolicyType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** URLPatterns **   <a name="CognitoUserPools-Type-CIMDPolicyType-URLPatterns"></a>
The HTTPS URL patterns that a client ID metadata document URL must match. Each pattern contains at most one `*` wildcard.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 12. Maximum length of 256.
Pattern: `^https://[!$-;=@-\[\]_a-z~]+$`
Required: No

## See Also
<a name="API_CIMDPolicyType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CIMDPolicyType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CIMDPolicyType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CIMDPolicyType)
