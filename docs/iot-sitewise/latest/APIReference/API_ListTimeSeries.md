---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListTimeSeries.html
---

# ListTimeSeries
<a name="API_ListTimeSeries"></a>

Retrieves a paginated list of time series (data streams).

## Request Syntax
<a name="API_ListTimeSeries_RequestSyntax"></a>

```
GET /timeseries/?aliasPrefix={{aliasPrefix}}&assetId={{assetId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&timeSeriesType={{timeSeriesType}}&workspaceName={{workspaceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTimeSeries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aliasPrefix](#API_ListTimeSeries_RequestSyntax) **   <a name="iotsitewise-ListTimeSeries-request-uri-aliasPrefix"></a>
The alias prefix of the time series.
Length Constraints: Minimum length of 1.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetId](#API_ListTimeSeries_RequestSyntax) **   <a name="iotsitewise-ListTimeSeries-request-uri-assetId"></a>
The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`

 ** [maxResults](#API_ListTimeSeries_RequestSyntax) **   <a name="iotsitewise-ListTimeSeries-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListTimeSeries_RequestSyntax) **   <a name="iotsitewise-ListTimeSeries-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [timeSeriesType](#API_ListTimeSeries_RequestSyntax) **   <a name="iotsitewise-ListTimeSeries-request-uri-timeSeriesType"></a>
The type of the time series. The time series type can be one of the following values:
+  `ASSOCIATED` – The time series is associated with an asset property.
+  `DISASSOCIATED` – The time series isn't associated with any asset property.
Valid Values: `ASSOCIATED | DISASSOCIATED`

 ** [workspaceName](#API_ListTimeSeries_RequestSyntax) **   <a name="iotsitewise-ListTimeSeries-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Request Body
<a name="API_ListTimeSeries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTimeSeries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "TimeSeriesSummaries": [
      {
         "alias": "string",
         "assetId": "string",
         "dataType": "string",
         "dataTypeSpec": "string",
         "propertyId": "string",
         "timeSeriesArn": "string",
         "timeSeriesCreationDate": number,
         "timeSeriesId": "string",
         "timeSeriesLastUpdateDate": number
      }
   ],
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_ListTimeSeries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTimeSeries_ResponseSyntax) **   <a name="iotsitewise-ListTimeSeries-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [TimeSeriesSummaries](#API_ListTimeSeries_ResponseSyntax) **   <a name="iotsitewise-ListTimeSeries-response-TimeSeriesSummaries"></a>
One or more time series summaries to list.
Type: Array of [TimeSeriesSummary](API_TimeSeriesSummary.md) objects

 ** [workspaceName](#API_ListTimeSeries_ResponseSyntax) **   <a name="iotsitewise-ListTimeSeries-response-workspaceName"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_ListTimeSeries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_ListTimeSeries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListTimeSeries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListTimeSeries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListTimeSeries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListTimeSeries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListTimeSeries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListTimeSeries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListTimeSeries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListTimeSeries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListTimeSeries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListTimeSeries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
