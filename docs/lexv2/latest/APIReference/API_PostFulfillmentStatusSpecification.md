---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostFulfillmentStatusSpecification.html
---

# PostFulfillmentStatusSpecification
<a name="API_PostFulfillmentStatusSpecification"></a>

Provides a setting that determines whether the post-fulfillment response is sent to the user. For more information, see [https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete](https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete)

## Contents
<a name="API_PostFulfillmentStatusSpecification_Contents"></a>

 ** failureConditional **   <a name="lexv2-Type-PostFulfillmentStatusSpecification-failureConditional"></a>
A list of conditional branches to evaluate after the fulfillment code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed`.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** failureNextStep **   <a name="lexv2-Type-PostFulfillmentStatusSpecification-failureNextStep"></a>
Specifies the next step the bot runs after the fulfillment code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed`.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** failureResponse **   <a name="lexv2-Type-PostFulfillmentStatusSpecification-failureResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

 ** successConditional **   <a name="lexv2-Type-PostFulfillmentStatusSpecification-successConditional"></a>
A list of conditional branches to evaluate after the fulfillment code hook finishes successfully.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** successNextStep **   <a name="lexv2-Type-PostFulfillmentStatusSpecification-successNextStep"></a>
Specifies the next step in the conversation that Amazon Lex invokes when the fulfillment code hook completes successfully.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** successResponse **   <a name="lexv2-Type-PostFulfillmentStatusSpecification-successResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

 ** timeoutConditional **   <a name="lexv2-Type-PostFulfillmentStatusSpecification-timeoutConditional"></a>
A list of conditional branches to evaluate if the fulfillment code hook times out.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** timeoutNextStep **   <a name="lexv2-Type-PostFulfillmentStatusSpecification-timeoutNextStep"></a>
Specifies the next step that the bot runs when the fulfillment code hook times out.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** timeoutResponse **   <a name="lexv2-Type-PostFulfillmentStatusSpecification-timeoutResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

## See Also
<a name="API_PostFulfillmentStatusSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/PostFulfillmentStatusSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/PostFulfillmentStatusSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/PostFulfillmentStatusSpecification)
