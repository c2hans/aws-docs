---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_CognitoUserPoolConfig.html
---

# CognitoUserPoolConfig
<a name="API_CognitoUserPoolConfig"></a>

Describes an Amazon Cognito user pool configuration.

## Contents
<a name="API_CognitoUserPoolConfig_Contents"></a>

 ** awsRegion **   <a name="appsync-Type-CognitoUserPoolConfig-awsRegion"></a>
The AWS Region in which the user pool was created.
Type: String
Required: Yes

 ** userPoolId **   <a name="appsync-Type-CognitoUserPoolConfig-userPoolId"></a>
The user pool ID.
Type: String
Required: Yes

 ** appIdClientRegex **   <a name="appsync-Type-CognitoUserPoolConfig-appIdClientRegex"></a>
A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isn't set, no filtering is applied.
Type: String
Required: No

## See Also
<a name="API_CognitoUserPoolConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/CognitoUserPoolConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/CognitoUserPoolConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/CognitoUserPoolConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
