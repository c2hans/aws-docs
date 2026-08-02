---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_PushSync.html
---

# PushSync
<a name="API_PushSync"></a>

Configuration options to be applied to the identity pool.

## Contents
<a name="API_PushSync_Contents"></a>

 ** ApplicationArns **   <a name="Cognito-Type-PushSync-ApplicationArns"></a>
List of SNS platform application ARNs that could be used by clients.
Type: Array of strings
Pattern: `arn:aws:sns:[-0-9a-z]+:\d+:app/[A-Z_]+/[a-zA-Z0-9_.-]+`
Required: No

 ** RoleArn **   <a name="Cognito-Type-PushSync-RoleArn"></a>
A role configured to allow Cognito to call SNS on behalf of the developer.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:iam::\d+:role/.*`
Required: No

## See Also
<a name="API_PushSync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/PushSync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/PushSync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/PushSync)
