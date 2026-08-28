---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetJobRun.html
---

# GetJobRun
<a name="API_GetJobRun"></a>

The details of the job run.

## Request Syntax
<a name="API_GetJobRun_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/jobRuns/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetJobRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetJobRun_RequestSyntax) **   <a name="datazone-GetJobRun-request-uri-domainIdentifier"></a>
The ID of the domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetJobRun_RequestSyntax) **   <a name="datazone-GetJobRun-request-uri-identifier"></a>
The ID of the job run.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetJobRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetJobRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "details": { ... },
   "domainId": "string",
   "endTime": number,
   "error": {
      "message": "string"
   },
   "id": "string",
   "jobId": "string",
   "jobType": "string",
   "runMode": "string",
   "startTime": number,
   "status": "string"
}
```

## Response Elements
<a name="API_GetJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-createdAt"></a>
The timestamp of when the job run was created.
Type: Timestamp

 ** [createdBy](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-createdBy"></a>
The user who created the job run.
Type: String

 ** [details](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-details"></a>
The details of the job run.
Type: [JobRunDetails](API_JobRunDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [domainId](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-domainId"></a>
The ID of the domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [endTime](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-endTime"></a>
The timestamp of when the job run ended.
Type: Timestamp

 ** [error](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-error"></a>
The error generated if the action is not completed successfully.
Type: [JobRunError](API_JobRunError.md) object

 ** [id](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-id"></a>
The ID of the job run.
Type: String

 ** [jobId](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-jobId"></a>
The ID of the job run.
Type: String

 ** [jobType](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-jobType"></a>
The type of the job run.
Type: String
Valid Values: `LINEAGE`

 ** [runMode](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-runMode"></a>
The mode of the job run.
Type: String
Valid Values: `SCHEDULED | ON_DEMAND`

 ** [startTime](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-startTime"></a>
The timestamp of when the job run started.
Type: Timestamp

 ** [status](#API_GetJobRun_ResponseSyntax) **   <a name="datazone-GetJobRun-response-status"></a>
The status of the job run.
Type: String
Valid Values: `SCHEDULED | IN_PROGRESS | SUCCESS | PARTIALLY_SUCCEEDED | FAILED | ABORTED | TIMED_OUT | CANCELED`

## Errors
<a name="API_GetJobRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetJobRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetJobRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
