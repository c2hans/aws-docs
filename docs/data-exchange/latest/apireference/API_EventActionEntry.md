---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_EventActionEntry.html
---

# EventActionEntry
<a name="API_EventActionEntry"></a>

An event action is an object that defines the relationship between a specific event and an automated action that will be taken on behalf of the customer.

## Contents
<a name="API_EventActionEntry_Contents"></a>

 ** Action **   <a name="dataexchange-Type-EventActionEntry-Action"></a>
What occurs after a certain event.
Type: [Action](API_Action.md) object
Required: Yes

 ** Arn **   <a name="dataexchange-Type-EventActionEntry-Arn"></a>
The Amazon Resource Name (ARN) for the event action.
Type: String
Required: Yes

 ** CreatedAt **   <a name="dataexchange-Type-EventActionEntry-CreatedAt"></a>
The date and time that the event action was created, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** Event **   <a name="dataexchange-Type-EventActionEntry-Event"></a>
What occurs to start an action.
Type: [Event](API_Event.md) object
Required: Yes

 ** Id **   <a name="dataexchange-Type-EventActionEntry-Id"></a>
The unique identifier for the event action.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** UpdatedAt **   <a name="dataexchange-Type-EventActionEntry-UpdatedAt"></a>
The date and time that the event action was last updated, in ISO 8601 format.
Type: Timestamp
Required: Yes

## See Also
<a name="API_EventActionEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/EventActionEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/EventActionEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/EventActionEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
