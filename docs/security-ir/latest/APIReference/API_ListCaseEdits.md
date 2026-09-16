---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListCaseEdits.html
---

# ListCaseEdits
<a name="API_ListCaseEdits"></a>

Views the case history for edits made to a designated case.

## Request Syntax
<a name="API_ListCaseEdits_RequestSyntax"></a>

```
POST /v1/cases/{{caseId}}/list-case-edits HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCaseEdits_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_ListCaseEdits_RequestSyntax) **   <a name="securityir-ListCaseEdits-request-uri-caseId"></a>
Required element used with ListCaseEdits to identify the case to query.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

## Request Body
<a name="API_ListCaseEdits_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListCaseEdits_RequestSyntax) **   <a name="securityir-ListCaseEdits-request-maxResults"></a>
Optional element to identify how many results to obtain. There is a maximum value of 25.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListCaseEdits_RequestSyntax) **   <a name="securityir-ListCaseEdits-request-nextToken"></a>
An optional string that, if supplied, must be copied from the output of a previous call to ListCaseEdits. When provided in this manner, the API fetches the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_ListCaseEdits_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "action": "string",
         "eventTimestamp": number,
         "message": "string",
         "principal": "string"
      }
   ],
   "nextToken": "string",
   "total": number
}
```

## Response Elements
<a name="API_ListCaseEdits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListCaseEdits_ResponseSyntax) **   <a name="securityir-ListCaseEdits-response-items"></a>
Response element for ListCaseEdits that includes the action, event timestamp, message, and principal for the response.
Type: Array of [CaseEditItem](API_CaseEditItem.md) objects

 ** [nextToken](#API_ListCaseEdits_ResponseSyntax) **   <a name="securityir-ListCaseEdits-response-nextToken"></a>
An optional string that, if supplied on subsequent calls to ListCaseEdits, allows the API to fetch the next page of results.
Type: String

 ** [total](#API_ListCaseEdits_ResponseSyntax) **   <a name="securityir-ListCaseEdits-response-total"></a>
Response element for ListCaseEdits that identifies the total number of edits.
Type: Integer

## Errors
<a name="API_ListCaseEdits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** message **
The ID of the resource which lead to the access denial.
HTTP Status Code: 403

 ** ConflictException **
Returned when there is a conflict with the current state of the resource.
For UpdateResolverType, this error may occur when attempting to change an AWS-supported case to Self-managed, which is not supported.
 ** message **
The exception message.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **

 ** message **
The exception message.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
HTTP Status Code: 500

 ** InvalidTokenException **

 ** message **
The exception message.
HTTP Status Code: 423

 ** ResourceNotFoundException **

 ** message **
The exception message.
HTTP Status Code: 404

 ** SecurityIncidentResponseNotActiveException **

 ** message **
The exception message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

 ** message **
The exception message.
 ** quotaCode **
The code of the quota.
 ** resourceId **
The ID of the requested resource which lead to the service quota exception.
 ** resourceType **
The type of the requested resource which lead to the service quota exception.
 ** serviceCode **
The service code of the quota.
HTTP Status Code: 402

 ** ThrottlingException **

 ** message **
The exception message.
 ** quotaCode **
The quota code of the exception.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
 ** serviceCode **
The service code of the exception.
HTTP Status Code: 429

 ** ValidationException **
Returned when the request contains invalid parameters.
For UpdateResolverType, this error may occur when attempting an unsupported resolver type transition.
 ** fieldList **
The fields which lead to the exception.
 ** message **
The exception message.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListCaseEdits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/ListCaseEdits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/ListCaseEdits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/ListCaseEdits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/ListCaseEdits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/ListCaseEdits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/ListCaseEdits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/ListCaseEdits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/ListCaseEdits)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/ListCaseEdits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/ListCaseEdits)
