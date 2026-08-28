---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentUpdatesSpecification.html
---

# FulfillmentUpdatesSpecification
<a name="API_FulfillmentUpdatesSpecification"></a>

Provides information for updating the user on the progress of fulfilling an intent.

## Contents
<a name="API_FulfillmentUpdatesSpecification_Contents"></a>

 ** active **   <a name="lexv2-Type-FulfillmentUpdatesSpecification-active"></a>
Determines whether fulfillment updates are sent to the user. When this field is true, updates are sent.
If the `active` field is set to true, the `startResponse`, `updateResponse`, and `timeoutInSeconds` fields are required.
Type: Boolean
Required: Yes

 ** startResponse **   <a name="lexv2-Type-FulfillmentUpdatesSpecification-startResponse"></a>
Provides configuration information for the message sent to users when the fulfillment Lambda functions starts running.
Type: [FulfillmentStartResponseSpecification](API_FulfillmentStartResponseSpecification.md) object
Required: No

 ** timeoutInSeconds **   <a name="lexv2-Type-FulfillmentUpdatesSpecification-timeoutInSeconds"></a>
The length of time that the fulfillment Lambda function should run before it times out.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 900.
Required: No

 ** updateResponse **   <a name="lexv2-Type-FulfillmentUpdatesSpecification-updateResponse"></a>
Provides configuration information for messages sent periodically to the user while the fulfillment Lambda function is running.
Type: [FulfillmentUpdateResponseSpecification](API_FulfillmentUpdateResponseSpecification.md) object
Required: No

## See Also
<a name="API_FulfillmentUpdatesSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/FulfillmentUpdatesSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/FulfillmentUpdatesSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/FulfillmentUpdatesSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
