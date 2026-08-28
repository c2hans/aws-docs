---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListDataSourceRuns.html
---

# ListDataSourceRuns
<a name="API_ListDataSourceRuns"></a>

Lists data source runs in Amazon DataZone.

## Request Syntax
<a name="API_ListDataSourceRuns_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/data-sources/{{dataSourceIdentifier}}/runs?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSourceRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceIdentifier](#API_ListDataSourceRuns_RequestSyntax) **   <a name="datazone-ListDataSourceRuns-request-uri-dataSourceIdentifier"></a>
The identifier of the data source.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [domainIdentifier](#API_ListDataSourceRuns_RequestSyntax) **   <a name="datazone-ListDataSourceRuns-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which to invoke the `ListDataSourceRuns` action.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListDataSourceRuns_RequestSyntax) **   <a name="datazone-ListDataSourceRuns-request-uri-maxResults"></a>
The maximum number of runs to return in a single call to `ListDataSourceRuns`. When the number of runs to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListDataSourceRuns` to list the next set of runs.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListDataSourceRuns_RequestSyntax) **   <a name="datazone-ListDataSourceRuns-request-uri-nextToken"></a>
When the number of runs is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of runs, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDataSourceRuns` to list the next set of runs.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [status](#API_ListDataSourceRuns_RequestSyntax) **   <a name="datazone-ListDataSourceRuns-request-uri-status"></a>
The status of the data source.
Valid Values: `REQUESTED | RUNNING | FAILED | PARTIALLY_SUCCEEDED | SUCCESS`

## Request Body
<a name="API_ListDataSourceRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSourceRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": "string",
         "dataSourceId": "string",
         "errorMessage": {
            "errorDetail": "string",
            "errorType": "string"
         },
         "id": "string",
         "lineageSummary": {
            "importStatus": "string"
         },
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataSourceRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListDataSourceRuns_ResponseSyntax) **   <a name="datazone-ListDataSourceRuns-response-items"></a>
The results of the `ListDataSourceRuns` action.
Type: Array of [DataSourceRunSummary](API_DataSourceRunSummary.md) objects

 ** [nextToken](#API_ListDataSourceRuns_ResponseSyntax) **   <a name="datazone-ListDataSourceRuns-response-nextToken"></a>
When the number of runs is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of runs, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDataSourceRuns` to list the next set of runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListDataSourceRuns_Errors"></a>

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
<a name="API_ListDataSourceRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListDataSourceRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListDataSourceRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListDataSourceRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListDataSourceRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListDataSourceRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListDataSourceRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListDataSourceRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListDataSourceRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListDataSourceRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListDataSourceRuns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
