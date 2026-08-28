---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListTimeSeriesDataPoints.html
---

# ListTimeSeriesDataPoints
<a name="API_ListTimeSeriesDataPoints"></a>

Lists time series data points.

## Request Syntax
<a name="API_ListTimeSeriesDataPoints_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/entities/{{entityType}}/{{entityIdentifier}}/time-series-data-points?endedAt={{endedAt}}&formName={{formName}}&maxResults={{maxResults}}&nextToken={{nextToken}}&startedAt={{startedAt}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTimeSeriesDataPoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain that houses the assets for which you want to list time series data points.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [endedAt](#API_ListTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-request-uri-endedAt"></a>
The timestamp at which the data points that you wanted to list ended.

 ** [entityIdentifier](#API_ListTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-request-uri-entityIdentifier"></a>
The ID of the asset for which you want to list data points.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityType](#API_ListTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-request-uri-entityType"></a>
The type of the asset for which you want to list data points.
Valid Values: `ASSET | LISTING`
Required: Yes

 ** [formName](#API_ListTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-request-uri-formName"></a>
The name of the time series data points form.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [maxResults](#API_ListTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-request-uri-maxResults"></a>
The maximum number of data points to return in a single call to ListTimeSeriesDataPoints. When the number of data points to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-request-uri-nextToken"></a>
When the number of data points is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of data points, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [startedAt](#API_ListTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-request-uri-startedAt"></a>
The timestamp at which the data points that you want to list started.

## Request Body
<a name="API_ListTimeSeriesDataPoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTimeSeriesDataPoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "contentSummary": "string",
         "formName": "string",
         "id": "string",
         "timestamp": number,
         "typeIdentifier": "string",
         "typeRevision": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListTimeSeriesDataPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListTimeSeriesDataPoints_ResponseSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-response-items"></a>
The results of the ListTimeSeriesDataPoints action.
Type: Array of [TimeSeriesDataPointSummaryFormOutput](API_TimeSeriesDataPointSummaryFormOutput.md) objects

 ** [nextToken](#API_ListTimeSeriesDataPoints_ResponseSyntax) **   <a name="datazone-ListTimeSeriesDataPoints-response-nextToken"></a>
When the number of data points is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of data points, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListTimeSeriesDataPoints_Errors"></a>

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
<a name="API_ListTimeSeriesDataPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListTimeSeriesDataPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListTimeSeriesDataPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListTimeSeriesDataPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListTimeSeriesDataPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListTimeSeriesDataPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListTimeSeriesDataPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListTimeSeriesDataPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListTimeSeriesDataPoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListTimeSeriesDataPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListTimeSeriesDataPoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
