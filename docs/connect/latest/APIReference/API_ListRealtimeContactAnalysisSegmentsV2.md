---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListRealtimeContactAnalysisSegmentsV2.html
---

# ListRealtimeContactAnalysisSegmentsV2
<a name="API_ListRealtimeContactAnalysisSegmentsV2"></a>

Provides a list of analysis segments for a real-time chat analysis session. This API supports CHAT channels only.

**Important**
This API does not support VOICE. If you attempt to use it for VOICE, an `InvalidRequestException` occurs.

## Request Syntax
<a name="API_ListRealtimeContactAnalysisSegmentsV2_RequestSyntax"></a>

```
POST /contact/list-real-time-analysis-segments-v2/{{InstanceId}}/{{ContactId}} HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OutputType": "{{string}}",
   "SegmentTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListRealtimeContactAnalysisSegmentsV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_ListRealtimeContactAnalysisSegmentsV2_RequestSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-request-uri-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_ListRealtimeContactAnalysisSegmentsV2_RequestSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_ListRealtimeContactAnalysisSegmentsV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRealtimeContactAnalysisSegmentsV2_RequestSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListRealtimeContactAnalysisSegmentsV2_RequestSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: No

 ** [OutputType](#API_ListRealtimeContactAnalysisSegmentsV2_RequestSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-request-OutputType"></a>
The Contact Lens output type to be returned.
Type: String
Valid Values: `Raw | Redacted`
Required: Yes

 ** [SegmentTypes](#API_ListRealtimeContactAnalysisSegmentsV2_RequestSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-request-SegmentTypes"></a>
Enum with segment types . Each value corresponds to a segment type returned in the segments list of the API. Each segment type has its own structure. Different channels may have different sets of supported segment types.
Type: Array of strings
Array Members: Maximum number of 6 items.
Valid Values: `Transcript | Categories | Issues | Event | Attachments | PostContactSummary`
Required: Yes

## Response Syntax
<a name="API_ListRealtimeContactAnalysisSegmentsV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Channel": "string",
   "NextToken": "string",
   "Segments": [
      { ... }
   ],
   "Status": "string"
}
```

## Response Elements
<a name="API_ListRealtimeContactAnalysisSegmentsV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Channel](#API_ListRealtimeContactAnalysisSegmentsV2_ResponseSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-response-Channel"></a>
The channel of the contact.
Only `CHAT` is supported. This API does not support `VOICE`. If you attempt to use it for the VOICE channel, an `InvalidRequestException` error occurs.
Type: String
Valid Values: `VOICE | CHAT`

 ** [NextToken](#API_ListRealtimeContactAnalysisSegmentsV2_ResponseSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.

 ** [Segments](#API_ListRealtimeContactAnalysisSegmentsV2_ResponseSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-response-Segments"></a>
An analyzed transcript or category.
Type: Array of [RealtimeContactAnalysisSegment](API_RealtimeContactAnalysisSegment.md) objects

 ** [Status](#API_ListRealtimeContactAnalysisSegmentsV2_ResponseSyntax) **   <a name="connect-ListRealtimeContactAnalysisSegmentsV2-response-Status"></a>
Status of real-time contact analysis.
Type: String
Valid Values: `IN_PROGRESS | FAILED | COMPLETED`

## Errors
<a name="API_ListRealtimeContactAnalysisSegmentsV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** OutputTypeNotFoundException **
Thrown for analyzed content when requested OutputType was not enabled for a given contact. For example, if an OutputType.Raw was requested for a contact that had `RedactedOnly` Redaction policy set in the flow.
HTTP Status Code: 404

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListRealtimeContactAnalysisSegmentsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)
