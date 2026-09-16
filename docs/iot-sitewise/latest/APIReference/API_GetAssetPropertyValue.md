---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html
---

# GetAssetPropertyValue
<a name="API_GetAssetPropertyValue"></a>

Gets an asset property's current value. For more information, see [Querying current values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values) in the * AWS IoT SiteWise User Guide*.

To identify an asset property, you must specify one of the following:
+ The `assetId` and `propertyId` of an asset property.
+ A `propertyAlias`, which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature`). To define an asset property's alias, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html).

## Request Syntax
<a name="API_GetAssetPropertyValue_RequestSyntax"></a>

```
GET /properties/latest?assetId={{assetId}}&propertyAlias={{propertyAlias}}&propertyId={{propertyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAssetPropertyValue_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetId](#API_GetAssetPropertyValue_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyValue-request-uri-assetId"></a>
The ID of the asset, in UUID format.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [propertyAlias](#API_GetAssetPropertyValue_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyValue-request-uri-propertyAlias"></a>
The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature`). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [propertyId](#API_GetAssetPropertyValue_RequestSyntax) **   <a name="iotsitewise-GetAssetPropertyValue-request-uri-propertyId"></a>
The ID of the asset property, in UUID format.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Request Body
<a name="API_GetAssetPropertyValue_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAssetPropertyValue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "propertyValue": {
      "quality": "string",
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
}
```

## Response Elements
<a name="API_GetAssetPropertyValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [propertyValue](#API_GetAssetPropertyValue_ResponseSyntax) **   <a name="iotsitewise-GetAssetPropertyValue-response-propertyValue"></a>
The current asset property value.
Type: [AssetPropertyValue](API_AssetPropertyValue.md) object

## Errors
<a name="API_GetAssetPropertyValue_Errors"></a>

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
<a name="API_GetAssetPropertyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/GetAssetPropertyValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/GetAssetPropertyValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/GetAssetPropertyValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/GetAssetPropertyValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/GetAssetPropertyValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/GetAssetPropertyValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/GetAssetPropertyValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/GetAssetPropertyValue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/GetAssetPropertyValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/GetAssetPropertyValue)
