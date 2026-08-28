---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEventsResultEntry.html
---

# PutEventsResultEntry
<a name="API_PutEventsResultEntry"></a>

Represents the results of an event submitted to an event bus.

If the submission was successful, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.

For information about the errors that are common to all actions, see [Common Errors](https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html).

## Contents
<a name="API_PutEventsResultEntry_Contents"></a>

 ** ErrorCode **   <a name="eventbridge-Type-PutEventsResultEntry-ErrorCode"></a>
The error code that indicates why the event submission failed.
Retryable errors include:
+  ` [InternalFailure](https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html) `

  The request processing has failed because of an unknown error, exception or failure.
+  ` [ThrottlingException](https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html) `

  The request was denied due to request throttling.
Non-retryable errors include:
+  ` [AccessDeniedException](https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html) `

  You do not have sufficient access to perform this action.
+  `InvalidAccountIdException`

  The account ID provided is not valid.
+  `InvalidArgument`

  A specified parameter is not valid.
+  `MalformedDetail`

  The JSON provided is not valid.
+  `RedactionFailure`

  Redacting the CloudTrail event failed.
+  `NotAuthorizedForSourceException`

  You do not have permissions to publish events with this source onto this event bus.
+  `NotAuthorizedForDetailTypeException`

  You do not have permissions to publish events with this detail type onto this event bus.
Type: String
Required: No

 ** ErrorMessage **   <a name="eventbridge-Type-PutEventsResultEntry-ErrorMessage"></a>
The error message that explains why the event submission failed.
Type: String
Required: No

 ** EventId **   <a name="eventbridge-Type-PutEventsResultEntry-EventId"></a>
The ID of the event.
Type: String
Length Constraints: Maximum length of 64.
Required: No

## See Also
<a name="API_PutEventsResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/PutEventsResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutEventsResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/PutEventsResultEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
