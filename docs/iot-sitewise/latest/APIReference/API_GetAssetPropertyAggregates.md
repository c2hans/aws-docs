---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyAggregates.html
---

# GetAssetPropertyAggregates
<a name="API_GetAssetPropertyAggregates"></a>

Gets aggregated values for an asset property. For more information, see [Querying aggregates](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates) in the * AWS IoT SiteWise User Guide*.

To identify an asset property, you must specify one of the following:
+ The `assetId` and `propertyId` of an asset property.
+ A `propertyAlias`, which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature`). To define an asset property's alias, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html).

## Request Syntax
<a name="API_GetAssetPropertyAggregates_RequestSyntax"></a>

```
GET /properties/aggregates?aggregateTypes={{aggregateTypes}}&assetId={{assetId}}&endDate={{endDate}}&maxResults={{maxResults}}&nextToken={{nextToken}}&propertyAlias={{propertyAlias}}&propertyId={{propertyId}}&qualities={{qualities}}&resolution={{resolution}}&startDate={{startDate}}&timeOrdering={{timeOrdering}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAssetPropertyAggregates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aggregateTypes](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-aggregateTypes"></a>
The data aggregating function.
Array Members: Minimum number of 1 item.
Valid Values: `AVERAGE | COUNT | MAXIMUM | MINIMUM | SUM | STANDARD_DEVIATION`
Required: Yes

 ** [assetId](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-assetId"></a>
The ID of the asset, in UUID format.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [endDate](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-endDate"></a>
The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
Required: Yes

 ** [maxResults](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.
+ The size of the result set is equal to 1 MB.
+ The number of data points in the result set is equal to the value of `maxResults`. The maximum value of `maxResults` is 2500.
Valid Range: Minimum value of 1.

 ** [nextToken](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [propertyAlias](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-propertyAlias"></a>
The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature`). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [propertyId](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-propertyId"></a>
The ID of the asset property, in UUID format.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [qualities](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-qualities"></a>
The quality by which to filter asset data.
Array Members: Fixed number of 1 item.
Valid Values: `GOOD | BAD | UNCERTAIN`

 ** [resolution](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-resolution"></a>
The time interval over which to aggregate data.
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `1m|15m|1h|1d`
Required: Yes

 ** [startDate](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-startDate"></a>
The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
Required: Yes

 ** [timeOrdering](#API_GetAssetPropertyAggregates_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-request-uri-timeOrdering"></a>
The chronological sorting order of the requested information.
Default: `ASCENDING`
Valid Values: `ASCENDING | DESCENDING`

## Request Body
<a name="API_GetAssetPropertyAggregates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAssetPropertyAggregates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregatedValues": [
      {
         "quality": "string",
         "timestamp": number,
         "value": {
            "average": number,
            "count": number,
            "maximum": number,
            "minimum": number,
            "standardDeviation": number,
            "sum": number
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetAssetPropertyAggregates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregatedValues](#API_GetAssetPropertyAggregates_ResponseSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-response-aggregatedValues"></a>
The requested aggregated values.
Type: Array of [AggregatedValue](API_AggregatedValue.md) objects

 ** [nextToken](#API_GetAssetPropertyAggregates_ResponseSyntax) **   <a name="iotsitewise-GetAssetPropertyAggregates-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_GetAssetPropertyAggregates_Errors"></a>

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

 ** ServiceUnavailableException **
The requested service is unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_GetAssetPropertyAggregates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/GetAssetPropertyAggregates)
