---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_MessageReviewHandler.html
---

# MessageReviewHandler
<a name="API_MessageReviewHandler"></a>

Configuration information for optional message review.

## Contents
<a name="API_MessageReviewHandler_Contents"></a>

 ** fallbackResult **   <a name="ivs-Type-MessageReviewHandler-fallbackResult"></a>
Specifies the fallback behavior (whether the message is allowed or denied) if the handler does not return a valid response, encounters an error, or times out. (For the timeout period, see [ Service Quotas](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/service-quotas.html).) If allowed, the message is delivered with returned content to all users connected to the room. If denied, the message is not delivered to any user. Default: `ALLOW`.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** uri **   <a name="ivs-Type-MessageReviewHandler-uri"></a>
Identifier of the message review handler. Currently this must be an ARN of a lambda function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 170.
Pattern: `$|^arn:aws:lambda:[a-z0-9-]+:[0-9]{12}:function:.+.*`
Required: No

## See Also
<a name="API_MessageReviewHandler_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/MessageReviewHandler)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/MessageReviewHandler)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/MessageReviewHandler)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
