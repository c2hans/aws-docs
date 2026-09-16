---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetInterpolatedAssetPropertyValues.html
---

# GetInterpolatedAssetPropertyValues
<a name="API_GetInterpolatedAssetPropertyValues"></a>

Get interpolated values for an asset property for a specified time interval, during a period of time. If your time series is missing data points during the specified time interval, you can use interpolation to estimate the missing data.

For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days.

To identify an asset property, you must specify one of the following:
+ The `assetId` and `propertyId` of an asset property.
+ A `propertyAlias`, which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature`). To define an asset property's alias, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html).

## Request Syntax
<a name="API_GetInterpolatedAssetPropertyValues_RequestSyntax"></a>

```
GET /properties/interpolated?assetId={{assetId}}&endTimeInSeconds={{endTimeInSeconds}}&endTimeOffsetInNanos={{endTimeOffsetInNanos}}&intervalInSeconds={{intervalInSeconds}}&intervalWindowInSeconds={{intervalWindowInSeconds}}&maxResults={{maxResults}}&nextToken={{nextToken}}&propertyAlias={{propertyAlias}}&propertyId={{propertyId}}&quality={{quality}}&startTimeInSeconds={{startTimeInSeconds}}&startTimeOffsetInNanos={{startTimeOffsetInNanos}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInterpolatedAssetPropertyValues_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetId](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-assetId"></a>
The ID of the asset, in UUID format.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [endTimeInSeconds](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-endTimeInSeconds"></a>
The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time.
Valid Range: Minimum value of 1. Maximum value of 9223372036854774.
Required: Yes

 ** [endTimeOffsetInNanos](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-endTimeOffsetInNanos"></a>
The nanosecond offset converted from `endTimeInSeconds`.
Valid Range: Minimum value of 0. Maximum value of 999999999.

 ** [intervalInSeconds](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-intervalInSeconds"></a>
The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends.
Valid Range: Minimum value of 1. Maximum value of 320000000.
Required: Yes

 ** [intervalWindowInSeconds](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-intervalWindowInSeconds"></a>
The query interval for the window, in seconds. AWS IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.
+ If you specify a value for the `intervalWindowInSeconds` parameter, the value for the `type` parameter must be `LINEAR_INTERPOLATION`.
+ If a data point isn't found during the specified query window, AWS IoT SiteWise won't return an interpolated value for the interval. This indicates that there's a gap in the ingested data points.
For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, AWS IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, AWS IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on.
Valid Range: Minimum value of 1. Maximum value of 320000000.

 ** [maxResults](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request. If not specified, the default value is 10.
Valid Range: Minimum value of 1.

 ** [nextToken](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [propertyAlias](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-propertyAlias"></a>
The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature`). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [propertyId](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-propertyId"></a>
The ID of the asset property, in UUID format.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [quality](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-quality"></a>
The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality.
Valid Values: `GOOD | BAD | UNCERTAIN`
Required: Yes

 ** [startTimeInSeconds](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-startTimeInSeconds"></a>
The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time.
Valid Range: Minimum value of 1. Maximum value of 9223372036854774.
Required: Yes

 ** [startTimeOffsetInNanos](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-startTimeOffsetInNanos"></a>
The nanosecond offset converted from `startTimeInSeconds`.
Valid Range: Minimum value of 0. Maximum value of 999999999.

 ** [type](#API_GetInterpolatedAssetPropertyValues_RequestSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-request-uri-type"></a>
The interpolation type.
Valid values: `LINEAR_INTERPOLATION | LOCF_INTERPOLATION`
+  `LINEAR_INTERPOLATION` – Estimates missing data using [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation).

  For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, AWS IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.
+  `LOCF_INTERPOLATION` – Estimates missing data using last observation carried forward interpolation

  If no data point is found for an interval, AWS IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found.

  For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, AWS IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isn't found after 9 AM on July 2, 2021, AWS IoT SiteWise uses the same interpolated value for the rest of the days.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetInterpolatedAssetPropertyValues_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInterpolatedAssetPropertyValues_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "interpolatedAssetPropertyValues": [
      {
         "timestamp": {
            "offsetInNanos": number,
            "timeInSeconds": number
         },
         "value": {
            "booleanValue": boolean,
            "doubleValue": number,
            "integerValue": number,
            "nullValue": {
               "valueType": "string"
            },
            "stringValue": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetInterpolatedAssetPropertyValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [interpolatedAssetPropertyValues](#API_GetInterpolatedAssetPropertyValues_ResponseSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-response-interpolatedAssetPropertyValues"></a>
The requested interpolated values.
Type: Array of [InterpolatedAssetPropertyValue](API_InterpolatedAssetPropertyValue.md) objects

 ** [nextToken](#API_GetInterpolatedAssetPropertyValues_ResponseSyntax) **   <a name="iotsitewise-GetInterpolatedAssetPropertyValues-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_GetInterpolatedAssetPropertyValues_Errors"></a>

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

## Examples
<a name="API_GetInterpolatedAssetPropertyValues_Examples"></a>

### Example
<a name="API_GetInterpolatedAssetPropertyValues_Example_1"></a>

The following example uses the AWS Command Line Interface (AWS CLI) to retrieve the interpolated temperature values for a wind turbine every 24 hours between April 26, 2021 at midnight and May 3, 2021 at midnight in Pacific Time (PT).

**Note**
Replace `<asset-ID>` and `<property-ID>` with your asset ID and property ID.
The `--start-time-offset-in-nanos` and `--end-time-offset-in-nanos` parameters are optional. You can use these parameters to specify the nanosecond offsets for `startTimeInSeconds` and `startTimeInSeconds`.

#### Sample Request
<a name="API_GetInterpolatedAssetPropertyValues_Example_1_Request"></a>

```
aws iotsitewise get-interpolated-asset-property-values --asset-id <asset-ID> --property-id <property-ID> --start-time-in-seconds 1619420400 --start-time-offset-in-nanos 0 --end-time-in-seconds 1620025200
          --end-time-offset-in-nanos 0 --end-time-offset-in-nanos 1 --quality GOOD  --interval-in-seconds 3600 --type LINEAR_INTERPOLATION
```

#### Sample Response
<a name="API_GetInterpolatedAssetPropertyValues_Example_1_Response"></a>

```
{
    "interpolatedAssetPropertyValues": [
        {
            "timestamp": {
                "timeInSeconds": 1619420400,
                "offsetInNanos": 0
            },
            "value": {
                "doubleValue": 30.0
            }
        },
        {
            "timestamp": {
                "timeInSeconds": 1619424000,
                "offsetInNanos": 0
            },
            "value": {
                "doubleValue": 41.25
            }
        },
        {
            "timestamp": {
                "timeInSeconds": 1619427600,
                "offsetInNanos": 0
            },
            "value": {
                "doubleValue": 35.85
            }
        },
        ...
    ],
    ...
}
```

## See Also
<a name="API_GetInterpolatedAssetPropertyValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/GetInterpolatedAssetPropertyValues)
