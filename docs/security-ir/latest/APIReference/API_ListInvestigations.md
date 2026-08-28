---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListInvestigations.html
---

# ListInvestigations
<a name="API_ListInvestigations"></a>

Lists all investigations associated with cases that the requester has access to. Investigations are performed by agents to analyze and respond to security incidents.

## Request Syntax
<a name="API_ListInvestigations_RequestSyntax"></a>

```
GET /v1/cases/{{caseId}}/list-investigations?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInvestigations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_ListInvestigations_RequestSyntax) **   <a name="securityir-ListInvestigations-request-uri-caseId"></a>
Required element that specifies the unique identifier of the case for which to list investigations.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

 ** [maxResults](#API_ListInvestigations_RequestSyntax) **   <a name="securityir-ListInvestigations-request-uri-maxResults"></a>
Optional element for ListInvestigations to limit the number of responses.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListInvestigations_RequestSyntax) **   <a name="securityir-ListInvestigations-request-uri-nextToken"></a>
An optional string that, if supplied, must be copied from the output of a previous call to ListInvestigations. When provided in this manner, the API fetches the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 2000.

## Request Body
<a name="API_ListInvestigations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInvestigations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "investigationActions": [
      {
         "actionType": "string",
         "content": "string",
         "feedback": {
            "comment": "string",
            "submittedAt": number,
            "usefulness": "string"
         },
         "investigationId": "string",
         "lastUpdated": number,
         "status": "string",
         "title": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListInvestigations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [investigationActions](#API_ListInvestigations_ResponseSyntax) **   <a name="securityir-ListInvestigations-response-investigationActions"></a>
A list of investigation actions associated with the returned investigations. Each action represents a specific step or activity performed during the investigation process.
Type: Array of [InvestigationAction](API_InvestigationAction.md) objects

 ** [nextToken](#API_ListInvestigations_ResponseSyntax) **   <a name="securityir-ListInvestigations-response-nextToken"></a>
An optional string that, if supplied on subsequent calls to ListInvestigations, allows the API to fetch the next page of results.
Type: String

## Errors
<a name="API_ListInvestigations_Errors"></a>

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
<a name="API_ListInvestigations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/ListInvestigations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/ListInvestigations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/ListInvestigations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/ListInvestigations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/ListInvestigations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/ListInvestigations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/ListInvestigations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/ListInvestigations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/ListInvestigations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/ListInvestigations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
