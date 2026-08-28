---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RecoveryOptionType.html
---

# RecoveryOptionType
<a name="API_RecoveryOptionType"></a>

A recovery option for a user. The `AccountRecoverySettingType` data type is an array of this object. Each `RecoveryOptionType` has a priority property that determines whether it is a primary or secondary option.

For example, if `verified_email` has a priority of `1` and `verified_phone_number` has a priority of `2`, your user pool sends account-recovery messages to a verified email address but falls back to an SMS message if the user has a verified phone number. The `admin_only` option prevents self-service account recovery.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_RecoveryOptionType_Contents"></a>

 ** Name **   <a name="CognitoUserPools-Type-RecoveryOptionType-Name"></a>
The recovery method that this object sets a recovery option for.
Type: String
Valid Values: `verified_email | verified_phone_number | admin_only`
Required: Yes

 ** Priority **   <a name="CognitoUserPools-Type-RecoveryOptionType-Priority"></a>
Your priority preference for using the specified attribute in account recovery. The highest priority is `1`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: Yes

## See Also
<a name="API_RecoveryOptionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/RecoveryOptionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/RecoveryOptionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/RecoveryOptionType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
