---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EventFeedbackType.html
---

# EventFeedbackType
<a name="API_EventFeedbackType"></a>

The feedback that your application submitted to a threat protection event log, as displayed in an `AdminListUserAuthEvents` response.

## Contents
<a name="API_EventFeedbackType_Contents"></a>

 ** FeedbackValue **   <a name="CognitoUserPools-Type-EventFeedbackType-FeedbackValue"></a>
Your feedback to the authentication event. When you provide a `FeedbackValue` value of `valid`, you tell Amazon Cognito that you trust a user session where Amazon Cognito has evaluated some level of risk. When you provide a `FeedbackValue` value of `invalid`, you tell Amazon Cognito that you don't trust a user session, or you don't believe that Amazon Cognito evaluated a high-enough risk level.
Type: String
Valid Values: `Valid | Invalid`
Required: Yes

 ** Provider **   <a name="CognitoUserPools-Type-EventFeedbackType-Provider"></a>
The submitter of the event feedback. For example, if you submit event feedback in the Amazon Cognito console, this value is `Admin`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: Yes

 ** FeedbackDate **   <a name="CognitoUserPools-Type-EventFeedbackType-FeedbackDate"></a>
The date that you or your user submitted the feedback.
Type: Timestamp
Required: No

## See Also
<a name="API_EventFeedbackType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/EventFeedbackType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/EventFeedbackType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/EventFeedbackType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
