---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html
---

# PutPartnerEvents
<a name="API_PutPartnerEvents"></a>

This is used by SaaS partners to write events to a customer's partner event bus. AWS customers do not use this operation.

For information on calculating event batch size, see [Calculating EventBridge PutEvents event entry size](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-putevent-size.html) in the *EventBridge User Guide*.

## Request Syntax
<a name="API_PutPartnerEvents_RequestSyntax"></a>

```
{
   "Entries": [
      {
         "Detail": "{{string}}",
         "DetailType": "{{string}}",
         "Resources": [ "{{string}}" ],
         "Source": "{{string}}",
         "Time": {{number}}
      }
   ]
}
```

## Request Parameters
<a name="API_PutPartnerEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Entries](#API_PutPartnerEvents_RequestSyntax) **   <a name="eventbridge-PutPartnerEvents-request-Entries"></a>
The list of events to write to the event bus.
Type: Array of [PutPartnerEventsRequestEntry](API_PutPartnerEventsRequestEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_PutPartnerEvents_ResponseSyntax"></a>

```
{
   "Entries": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "EventId": "string"
      }
   ],
   "FailedEntryCount": number
}
```

## Response Elements
<a name="API_PutPartnerEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_PutPartnerEvents_ResponseSyntax) **   <a name="eventbridge-PutPartnerEvents-response-Entries"></a>
The results for each event entry the partner submitted in this request. If the event was successfully submitted, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.
For each record, the index of the response element is the same as the index in the request array.
Type: Array of [PutPartnerEventsResultEntry](API_PutPartnerEventsResultEntry.md) objects

 ** [FailedEntryCount](#API_PutPartnerEvents_ResponseSyntax) **   <a name="eventbridge-PutPartnerEvents-response-FailedEntryCount"></a>
The number of events from this operation that could not be written to the partner event bus.
Type: Integer

## Errors
<a name="API_PutPartnerEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** OperationDisabledException **
The operation you are attempting is not available in this region.
HTTP Status Code: 400

## See Also
<a name="API_PutPartnerEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/PutPartnerEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/PutPartnerEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/PutPartnerEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/PutPartnerEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutPartnerEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/PutPartnerEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/PutPartnerEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/PutPartnerEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/PutPartnerEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/PutPartnerEvents)
