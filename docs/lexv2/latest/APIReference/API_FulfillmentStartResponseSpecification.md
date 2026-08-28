---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentStartResponseSpecification.html
---

# FulfillmentStartResponseSpecification
<a name="API_FulfillmentStartResponseSpecification"></a>

Provides settings for a message that is sent to the user when a fulfillment Lambda function starts running.

## Contents
<a name="API_FulfillmentStartResponseSpecification_Contents"></a>

 ** delayInSeconds **   <a name="lexv2-Type-FulfillmentStartResponseSpecification-delayInSeconds"></a>
The delay between when the Lambda fulfillment function starts running and the start message is played. If the Lambda function returns before the delay is over, the start message isn't played.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 900.
Required: Yes

 ** messageGroups **   <a name="lexv2-Type-FulfillmentStartResponseSpecification-messageGroups"></a>
1 - 5 message groups that contain start messages. Amazon Lex chooses one of the messages to play to the user.
Type: Array of [MessageGroup](API_MessageGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** allowInterrupt **   <a name="lexv2-Type-FulfillmentStartResponseSpecification-allowInterrupt"></a>
Determines whether the user can interrupt the start message while it is playing.
Type: Boolean
Required: No

## See Also
<a name="API_FulfillmentStartResponseSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/FulfillmentStartResponseSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/FulfillmentStartResponseSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/FulfillmentStartResponseSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
