---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListDataSourceRunActivities.html
---

# ListDataSourceRunActivities
<a name="API_ListDataSourceRunActivities"></a>

Lists data source run activities.

## Request Syntax
<a name="API_ListDataSourceRunActivities_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/data-source-runs/{{identifier}}/activities?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSourceRunActivities_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListDataSourceRunActivities_RequestSyntax) **   <a name="datazone-ListDataSourceRunActivities-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which to list data source run activities.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_ListDataSourceRunActivities_RequestSyntax) **   <a name="datazone-ListDataSourceRunActivities-request-uri-identifier"></a>
The identifier of the data source run.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListDataSourceRunActivities_RequestSyntax) **   <a name="datazone-ListDataSourceRunActivities-request-uri-maxResults"></a>
The maximum number of activities to return in a single call to `ListDataSourceRunActivities`. When the number of activities to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListDataSourceRunActivities` to list the next set of activities.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListDataSourceRunActivities_RequestSyntax) **   <a name="datazone-ListDataSourceRunActivities-request-uri-nextToken"></a>
When the number of activities is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of activities, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDataSourceRunActivities` to list the next set of activities.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [status](#API_ListDataSourceRunActivities_RequestSyntax) **   <a name="datazone-ListDataSourceRunActivities-request-uri-status"></a>
The status of the data source run.
Valid Values: `FAILED | PUBLISHING_FAILED | SUCCEEDED_CREATED | SUCCEEDED_UPDATED | SKIPPED_ALREADY_IMPORTED | SKIPPED_ARCHIVED | SKIPPED_NO_ACCESS | UNCHANGED`

## Request Body
<a name="API_ListDataSourceRunActivities_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSourceRunActivities_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": "string",
         "dataAssetId": "string",
         "dataAssetStatus": "string",
         "database": "string",
         "dataSourceRunId": "string",
         "errorMessage": {
            "errorDetail": "string",
            "errorType": "string"
         },
         "lineageSummary": {
            "errorMessage": "string",
            "eventId": "string",
            "eventStatus": "string"
         },
         "projectId": "string",
         "technicalDescription": "string",
         "technicalName": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataSourceRunActivities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListDataSourceRunActivities_ResponseSyntax) **   <a name="datazone-ListDataSourceRunActivities-response-items"></a>
The results of the `ListDataSourceRunActivities` action.
Type: Array of [DataSourceRunActivity](API_DataSourceRunActivity.md) objects

 ** [nextToken](#API_ListDataSourceRunActivities_ResponseSyntax) **   <a name="datazone-ListDataSourceRunActivities-response-nextToken"></a>
When the number of activities is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of activities, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDataSourceRunActivities` to list the next set of activities.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListDataSourceRunActivities_Errors"></a>

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
<a name="API_ListDataSourceRunActivities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListDataSourceRunActivities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListDataSourceRunActivities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListDataSourceRunActivities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListDataSourceRunActivities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListDataSourceRunActivities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListDataSourceRunActivities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListDataSourceRunActivities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListDataSourceRunActivities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListDataSourceRunActivities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListDataSourceRunActivities)
