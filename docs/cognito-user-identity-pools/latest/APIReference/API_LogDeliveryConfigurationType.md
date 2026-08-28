---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_LogDeliveryConfigurationType.html
---

# LogDeliveryConfigurationType
<a name="API_LogDeliveryConfigurationType"></a>

The logging parameters of a user pool, as returned in the response to a `GetLogDeliveryConfiguration` request.

## Contents
<a name="API_LogDeliveryConfigurationType_Contents"></a>

 ** LogConfigurations **   <a name="CognitoUserPools-Type-LogDeliveryConfigurationType-LogConfigurations"></a>
A logging destination of a user pool. User pools can have multiple logging destinations for message-delivery and user-activity logs.
Type: Array of [LogConfigurationType](API_LogConfigurationType.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: Yes

 ** UserPoolId **   <a name="CognitoUserPools-Type-LogDeliveryConfigurationType-UserPoolId"></a>
The ID of the user pool where you configured logging.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_LogDeliveryConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/LogDeliveryConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/LogDeliveryConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/LogDeliveryConfigurationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
