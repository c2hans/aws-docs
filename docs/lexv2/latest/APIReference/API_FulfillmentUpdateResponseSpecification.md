---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentUpdateResponseSpecification.html
---

# FulfillmentUpdateResponseSpecification
<a name="API_FulfillmentUpdateResponseSpecification"></a>

Provides settings for a message that is sent periodically to the user while a fulfillment Lambda function is running.

## Contents
<a name="API_FulfillmentUpdateResponseSpecification_Contents"></a>

 ** frequencyInSeconds **   <a name="lexv2-Type-FulfillmentUpdateResponseSpecification-frequencyInSeconds"></a>
The frequency that a message is sent to the user. When the period ends, Amazon Lex chooses a message from the message groups and plays it to the user. If the fulfillment Lambda returns before the first period ends, an update message is not played to the user.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 900.
Required: Yes

 ** messageGroups **   <a name="lexv2-Type-FulfillmentUpdateResponseSpecification-messageGroups"></a>
1 - 5 message groups that contain update messages. Amazon Lex chooses one of the messages to play to the user.
Type: Array of [MessageGroup](API_MessageGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** allowInterrupt **   <a name="lexv2-Type-FulfillmentUpdateResponseSpecification-allowInterrupt"></a>
Determines whether the user can interrupt an update message while it is playing.
Type: Boolean
Required: No

## See Also
<a name="API_FulfillmentUpdateResponseSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/FulfillmentUpdateResponseSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/FulfillmentUpdateResponseSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/FulfillmentUpdateResponseSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
