---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_StartDataSourceRun.html
---

# StartDataSourceRun
<a name="API_StartDataSourceRun"></a>

Start the run of the specified data source in Amazon DataZone.

## Request Syntax
<a name="API_StartDataSourceRun_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/data-sources/{{dataSourceIdentifier}}/runs HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartDataSourceRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceIdentifier](#API_StartDataSourceRun_RequestSyntax) **   <a name="datazone-StartDataSourceRun-request-uri-dataSourceIdentifier"></a>
The identifier of the data source.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [domainIdentifier](#API_StartDataSourceRun_RequestSyntax) **   <a name="datazone-StartDataSourceRun-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which to start a data source run.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_StartDataSourceRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartDataSourceRun_RequestSyntax) **   <a name="datazone-StartDataSourceRun-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Required: No

## Response Syntax
<a name="API_StartDataSourceRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "dataSourceConfigurationSnapshot": "string",
   "dataSourceId": "string",
   "domainId": "string",
   "errorMessage": {
      "errorDetail": "string",
      "errorType": "string"
   },
   "id": "string",
   "projectId": "string",
   "runStatisticsForAssets": {
      "added": number,
      "failed": number,
      "skipped": number,
      "unchanged": number,
      "updated": number
   },
   "startedAt": "string",
   "status": "string",
   "stoppedAt": "string",
   "type": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_StartDataSourceRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-createdAt"></a>
The timestamp of when data source run was created.
Type: Timestamp

 ** [dataSourceConfigurationSnapshot](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-dataSourceConfigurationSnapshot"></a>
The configuration snapshot of the data source that is being run.
Type: String

 ** [dataSourceId](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-dataSourceId"></a>
The identifier of the data source.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [domainId](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-domainId"></a>
The identifier of the Amazon DataZone domain in which to start a data source run.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [errorMessage](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-errorMessage"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object

 ** [id](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-id"></a>
The identifier of the data source run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [projectId](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-projectId"></a>
The identifier of the project.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [runStatisticsForAssets](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-runStatisticsForAssets"></a>
Specifies run statistics for assets.
Type: [RunStatisticsForAssets](API_RunStatisticsForAssets.md) object

 ** [startedAt](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-startedAt"></a>
The timestamp of when the data source run was started.
Type: Timestamp

 ** [status](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-status"></a>
The status of the data source run.
Type: String
Valid Values: `REQUESTED | RUNNING | FAILED | PARTIALLY_SUCCEEDED | SUCCESS`

 ** [stoppedAt](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-stoppedAt"></a>
The timestamp of when the data source run was stopped.
Type: Timestamp

 ** [type](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-type"></a>
The type of the data source run.
Type: String
Valid Values: `PRIORITIZED | SCHEDULED`

 ** [updatedAt](#API_StartDataSourceRun_ResponseSyntax) **   <a name="datazone-StartDataSourceRun-response-updatedAt"></a>
The timestamp of when the data source run was updated.
Type: Timestamp

## Errors
<a name="API_StartDataSourceRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_StartDataSourceRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/StartDataSourceRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/StartDataSourceRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/StartDataSourceRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/StartDataSourceRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/StartDataSourceRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/StartDataSourceRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/StartDataSourceRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/StartDataSourceRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/StartDataSourceRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/StartDataSourceRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
