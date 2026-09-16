---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeTimeSeries.html
---

# DescribeTimeSeries
<a name="API_DescribeTimeSeries"></a>

Retrieves information about a time series (data stream).

To identify a time series, do one of the following:
+ If the time series isn't associated with an asset property, specify the `alias` of the time series.
+ If the time series is associated with an asset property, specify one of the following:
  + The `alias` of the time series.
  + The `assetId` and `propertyId` that identifies the asset property.

## Request Syntax
<a name="API_DescribeTimeSeries_RequestSyntax"></a>

```
GET /timeseries/describe/?alias={{alias}}&assetId={{assetId}}&propertyId={{propertyId}}&workspaceName={{workspaceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTimeSeries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [alias](#API_DescribeTimeSeries_RequestSyntax) **   <a name="iotsitewise-DescribeTimeSeries-request-uri-alias"></a>
The alias that identifies the time series.
Length Constraints: Minimum length of 1.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetId](#API_DescribeTimeSeries_RequestSyntax) **   <a name="iotsitewise-DescribeTimeSeries-request-uri-assetId"></a>
The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`

 ** [propertyId](#API_DescribeTimeSeries_RequestSyntax) **   <a name="iotsitewise-DescribeTimeSeries-request-uri-propertyId"></a>
The ID of the asset property. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`

 ** [workspaceName](#API_DescribeTimeSeries_RequestSyntax) **   <a name="iotsitewise-DescribeTimeSeries-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Request Body
<a name="API_DescribeTimeSeries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTimeSeries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "alias": "string",
   "assetId": "string",
   "dataType": "string",
   "dataTypeSpec": "string",
   "propertyId": "string",
   "timeSeriesArn": "string",
   "timeSeriesCreationDate": number,
   "timeSeriesId": "string",
   "timeSeriesLastUpdateDate": number,
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_DescribeTimeSeries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [alias](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-alias"></a>
The alias that identifies the time series.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetId](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-assetId"></a>
The ID of the asset in which the asset property was created.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [dataType](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-dataType"></a>
The data type of the time series.
If you specify `STRUCT`, you must also specify `dataTypeSpec` to identify the type of the structure for this time series.
Type: String
Valid Values: `STRING | INTEGER | DOUBLE | BOOLEAN | STRUCT | VIDEO | ANNOTATION | JSON`

 ** [dataTypeSpec](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-dataTypeSpec"></a>
The data type of the structure for this time series. This parameter is required for time series that have the `STRUCT` data type.
The options for this parameter depend on the type of the composite model in which you created the asset property that is associated with your time series. Use `AWS/ALARM_STATE` for alarm state in alarm composite models.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [propertyId](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-propertyId"></a>
The ID of the asset property, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [timeSeriesArn](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-timeSeriesArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the time series, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:time-series/${TimeSeriesId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [timeSeriesCreationDate](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-timeSeriesCreationDate"></a>
The date that the time series was created, in Unix epoch time.
Type: Timestamp

 ** [timeSeriesId](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-timeSeriesId"></a>
The ID of the time series.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.

 ** [timeSeriesLastUpdateDate](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-timeSeriesLastUpdateDate"></a>
The date that the time series was last updated, in Unix epoch time.
Type: Timestamp

 ** [workspaceName](#API_DescribeTimeSeries_ResponseSyntax) **   <a name="iotsitewise-DescribeTimeSeries-response-workspaceName"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_DescribeTimeSeries_Errors"></a>

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
<a name="API_DescribeTimeSeries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeTimeSeries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeTimeSeries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeTimeSeries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeTimeSeries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeTimeSeries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeTimeSeries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeTimeSeries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeTimeSeries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeTimeSeries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeTimeSeries)
