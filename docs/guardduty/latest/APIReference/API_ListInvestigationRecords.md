---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListInvestigationRecords.html
---

# ListInvestigationRecords
<a name="API_ListInvestigationRecords"></a>

This API is currently available as a preview. This feature is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and Asia Pacific (Tokyo).

Returns the records for a specific GuardDuty investigation. Each record is one step in the reasoning that GuardDuty followed to reach the results of the investigation.

An administrator account can list the records of any investigation within the organization. Member accounts can only list the records of investigations that belong to them.

## Request Syntax
<a name="API_ListInvestigationRecords_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/investigation/records HTTP/1.1
Content-type: application/json

{
   "investigationId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "recordTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListInvestigationRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_ListInvestigationRecords_RequestSyntax) **   <a name="guardduty-ListInvestigationRecords-request-uri-DetectorId"></a>
The unique ID of the GuardDuty detector associated with the investigation.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_ListInvestigationRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [investigationId](#API_ListInvestigationRecords_RequestSyntax) **   <a name="guardduty-ListInvestigationRecords-request-investigationId"></a>
The unique identifier of the investigation whose records you want to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-fA-F0-9\-]+`
Required: Yes

 ** [maxResults](#API_ListInvestigationRecords_RequestSyntax) **   <a name="guardduty-ListInvestigationRecords-request-maxResults"></a>
The maximum number of records to return in a single response. Valid values are 1 to 50. The default value is 20. A response can contain fewer records than this value, or no records, and still include a `NextToken`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListInvestigationRecords_RequestSyntax) **   <a name="guardduty-ListInvestigationRecords-request-nextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data. Use the same `InvestigationId` and `RecordTypes` values that you used in the previous request.
If you specify this parameter for an investigation whose status isn't `COMPLETED`, the operation returns a `BadRequestException`. A `NextToken` expires 24 hours after it's returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9+/=_\-]+`
Required: No

 ** [recordTypes](#API_ListInvestigationRecords_RequestSyntax) **   <a name="guardduty-ListInvestigationRecords-request-recordTypes"></a>
The types of records to return. Possible values are `UPDATE`, `FETCH`, `OBSERVATION`, `ANALYSIS`, and `METADATA`. If you don't specify this parameter, GuardDuty returns records of all types.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `OBSERVATION | ANALYSIS | UPDATE | FETCH | METADATA`
Required: No

## Response Syntax
<a name="API_ListInvestigationRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "investigationId": "string",
   "nextToken": "string",
   "records": [
      {
         "createdAt": number,
         "narrative": "string",
         "recordId": "string",
         "supportingData": { ... },
         "title": "string",
         "type": "string"
      }
   ],
   "status": "string"
}
```

## Response Elements
<a name="API_ListInvestigationRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [investigationId](#API_ListInvestigationRecords_ResponseSyntax) **   <a name="guardduty-ListInvestigationRecords-response-investigationId"></a>
The unique identifier of the investigation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-fA-F0-9\-]+`

 ** [nextToken](#API_ListInvestigationRecords_ResponseSyntax) **   <a name="guardduty-ListInvestigationRecords-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items. If this value is absent, there are no more records to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9+/=_\-]+`

 ** [records](#API_ListInvestigationRecords_ResponseSyntax) **   <a name="guardduty-ListInvestigationRecords-response-records"></a>
The records for the investigation, in the order that GuardDuty created them, oldest first. This list can contain fewer records than `MaxResults`, or no records, even when more records are available. To check for more records, use `NextToken`.
Type: Array of [InvestigationRecord](API_InvestigationRecord.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [status](#API_ListInvestigationRecords_ResponseSyntax) **   <a name="guardduty-ListInvestigationRecords-response-status"></a>
The current status of the investigation. Possible values are `RUNNING`, `COMPLETED`, and `FAILED`. Records are returned only when the status is `COMPLETED`. If the status is `RUNNING` or `FAILED`, the response contains an empty list of records and no `NextToken`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `RUNNING | COMPLETED | FAILED`

## Errors
<a name="API_ListInvestigationRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An access denied exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 403

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 404

## See Also
<a name="API_ListInvestigationRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListInvestigationRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListInvestigationRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListInvestigationRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListInvestigationRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListInvestigationRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListInvestigationRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListInvestigationRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListInvestigationRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListInvestigationRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListInvestigationRecords)
