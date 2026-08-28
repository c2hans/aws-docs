---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentCodeHookSettings.html
---

# FulfillmentCodeHookSettings
<a name="API_FulfillmentCodeHookSettings"></a>

Determines if a Lambda function should be invoked for a specific intent.

## Contents
<a name="API_FulfillmentCodeHookSettings_Contents"></a>

 ** enabled **   <a name="lexv2-Type-FulfillmentCodeHookSettings-enabled"></a>
Indicates whether a Lambda function should be invoked to fulfill a specific intent.
Type: Boolean
Required: Yes

 ** active **   <a name="lexv2-Type-FulfillmentCodeHookSettings-active"></a>
Determines whether the fulfillment code hook is used. When `active` is false, the code hook doesn't run.
Type: Boolean
Required: No

 ** fulfillmentUpdatesSpecification **   <a name="lexv2-Type-FulfillmentCodeHookSettings-fulfillmentUpdatesSpecification"></a>
Provides settings for update messages sent to the user for long-running Lambda fulfillment functions. Fulfillment updates can be used only with streaming conversations.
Type: [FulfillmentUpdatesSpecification](API_FulfillmentUpdatesSpecification.md) object
Required: No

 ** postFulfillmentStatusSpecification **   <a name="lexv2-Type-FulfillmentCodeHookSettings-postFulfillmentStatusSpecification"></a>
Provides settings for messages sent to the user for after the Lambda fulfillment function completes. Post-fulfillment messages can be sent for both streaming and non-streaming conversations.
Type: [PostFulfillmentStatusSpecification](API_PostFulfillmentStatusSpecification.md) object
Required: No

## See Also
<a name="API_FulfillmentCodeHookSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/FulfillmentCodeHookSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/FulfillmentCodeHookSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/FulfillmentCodeHookSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
