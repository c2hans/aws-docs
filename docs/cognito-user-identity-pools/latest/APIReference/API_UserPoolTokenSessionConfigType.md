---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolTokenSessionConfigType.html
---

# UserPoolTokenSessionConfigType
<a name="API_UserPoolTokenSessionConfigType"></a>

The pool-wide token session settings for a user pool.

## Contents
<a name="API_UserPoolTokenSessionConfigType_Contents"></a>

 ** MaxPerUser **   <a name="CognitoUserPools-Type-UserPoolTokenSessionConfigType-MaxPerUser"></a>
The maximum number of active token sessions that a user can have across the user pool. The minimum value is `1` and the maximum value is `100`. The default is `20`. When a user reaches this limit, the next successful authentication automatically evicts that user's least recently used token session before it creates the new session. Lowering this value doesn't evict existing sessions on its own; the user is brought back within the limit on their next sign-in.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

## See Also
<a name="API_UserPoolTokenSessionConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserPoolTokenSessionConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserPoolTokenSessionConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserPoolTokenSessionConfigType)
