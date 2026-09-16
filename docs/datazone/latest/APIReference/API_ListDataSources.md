---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListDataSources.html
---

# ListDataSources
<a name="API_ListDataSources"></a>

Lists data sources in Amazon DataZone.

## Request Syntax
<a name="API_ListDataSources_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/data-sources?connectionIdentifier={{connectionIdentifier}}&environmentIdentifier={{environmentIdentifier}}&maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&projectIdentifier={{projectIdentifier}}&status={{status}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectionIdentifier](#API_ListDataSources_RequestSyntax) **   <a name="datazone-ListDataSources-request-uri-connectionIdentifier"></a>
The ID of the connection.

 ** [domainIdentifier](#API_ListDataSources_RequestSyntax) **   <a name="datazone-ListDataSources-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which to list the data sources.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentIdentifier](#API_ListDataSources_RequestSyntax) **   <a name="datazone-ListDataSources-request-uri-environmentIdentifier"></a>
The identifier of the environment in which to list the data sources.

 ** [maxResults](#API_ListDataSources_RequestSyntax) **   <a name="datazone-ListDataSources-request-uri-maxResults"></a>
The maximum number of data sources to return in a single call to `ListDataSources`. When the number of data sources to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListDataSources` to list the next set of data sources.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [name](#API_ListDataSources_RequestSyntax) **   <a name="datazone-ListDataSources-request-uri-name"></a>
The name of the data source.
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [nextToken](#API_ListDataSources_RequestSyntax) **   <a name="datazone-ListDataSources-request-uri-nextToken"></a>
When the number of data sources is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of data sources, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDataSources` to list the next set of data sources.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [projectIdentifier](#API_ListDataSources_RequestSyntax) **   <a name="datazone-ListDataSources-request-uri-projectIdentifier"></a>
The identifier of the project in which to list data sources.
Required: Yes

 ** [status](#API_ListDataSources_RequestSyntax) **   <a name="datazone-ListDataSources-request-uri-status"></a>
The status of the data source.
Valid Values: `CREATING | FAILED_CREATION | READY | UPDATING | FAILED_UPDATE | RUNNING | DELETING | FAILED_DELETION`

 ** [type](#API_ListDataSources_RequestSyntax) **   <a name="datazone-ListDataSources-request-uri-type"></a>
The type of the data source.
Length Constraints: Minimum length of 1. Maximum length of 256.

## Request Body
<a name="API_ListDataSources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "connectionId": "string",
         "createdAt": "string",
         "dataSourceId": "string",
         "description": "string",
         "domainId": "string",
         "enableSetting": "string",
         "environmentId": "string",
         "lastRunAssetCount": number,
         "lastRunAt": "string",
         "lastRunErrorMessage": {
            "errorDetail": "string",
            "errorType": "string"
         },
         "lastRunStatus": "string",
         "name": "string",
         "schedule": {
            "schedule": "string",
            "timezone": "string"
         },
         "status": "string",
         "type": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListDataSources_ResponseSyntax) **   <a name="datazone-ListDataSources-response-items"></a>
The results of the `ListDataSources` action.
Type: Array of [DataSourceSummary](API_DataSourceSummary.md) objects

 ** [nextToken](#API_ListDataSources_ResponseSyntax) **   <a name="datazone-ListDataSources-response-nextToken"></a>
When the number of data sources is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of data sources, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDataSources` to list the next set of data sources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListDataSources_Errors"></a>

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
<a name="API_ListDataSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListDataSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListDataSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListDataSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListDataSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListDataSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListDataSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListDataSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListDataSources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListDataSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListDataSources)
