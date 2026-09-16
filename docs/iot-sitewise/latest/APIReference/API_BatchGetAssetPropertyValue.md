---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValue.html
---

# BatchGetAssetPropertyValue
<a name="API_BatchGetAssetPropertyValue"></a>

Gets the current value for one or more asset properties. For more information, see [Querying current values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values) in the * AWS IoT SiteWise User Guide*.

## Request Syntax
<a name="API_BatchGetAssetPropertyValue_RequestSyntax"></a>

```
POST /properties/batch/latest HTTP/1.1
Content-type: application/json

{
   "entries": [
      {
         "assetId": "{{string}}",
         "entryId": "{{string}}",
         "propertyAlias": "{{string}}",
         "propertyId": "{{string}}"
      }
   ],
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchGetAssetPropertyValue_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetAssetPropertyValue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [entries](#API_BatchGetAssetPropertyValue_RequestSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValue-request-entries"></a>
The list of asset property value entries for the batch get request. You can specify up to 128 entries per request.
Type: Array of [BatchGetAssetPropertyValueEntry](API_BatchGetAssetPropertyValueEntry.md) objects
Required: Yes

 ** [nextToken](#API_BatchGetAssetPropertyValue_RequestSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValue-request-nextToken"></a>
The token to be used for the next set of paginated results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_BatchGetAssetPropertyValue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errorEntries": [
      {
         "entryId": "string",
         "errorCode": "string",
         "errorMessage": "string"
      }
   ],
   "nextToken": "string",
   "skippedEntries": [
      {
         "completionStatus": "string",
         "entryId": "string",
         "errorInfo": {
            "errorCode": "string",
            "errorTimestamp": number
         }
      }
   ],
   "successEntries": [
      {
         "assetPropertyValue": {
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
         },
         "entryId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetAssetPropertyValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorEntries](#API_BatchGetAssetPropertyValue_ResponseSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValue-response-errorEntries"></a>
A list of the errors (if any) associated with the batch request. Each error entry contains the `entryId` of the entry that failed.
Type: Array of [BatchGetAssetPropertyValueErrorEntry](API_BatchGetAssetPropertyValueErrorEntry.md) objects

 ** [nextToken](#API_BatchGetAssetPropertyValue_ResponseSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValue-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [skippedEntries](#API_BatchGetAssetPropertyValue_ResponseSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValue-response-skippedEntries"></a>
A list of entries that were not processed by this batch request. because these entries had been completely processed by previous paginated requests. Each skipped entry contains the `entryId` of the entry that skipped.
Type: Array of [BatchGetAssetPropertyValueSkippedEntry](API_BatchGetAssetPropertyValueSkippedEntry.md) objects

 ** [successEntries](#API_BatchGetAssetPropertyValue_ResponseSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValue-response-successEntries"></a>
A list of entries that were processed successfully by this batch request. Each success entry contains the `entryId` of the entry that succeeded and the latest query result.
Type: Array of [BatchGetAssetPropertyValueSuccessEntry](API_BatchGetAssetPropertyValueSuccessEntry.md) objects

## Errors
<a name="API_BatchGetAssetPropertyValue_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The requested service is unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## Examples
<a name="API_BatchGetAssetPropertyValue_Examples"></a>

### Example
<a name="API_BatchGetAssetPropertyValue_Example_1"></a>

The following example uses the AWS Command Line Interface (AWS CLI) to retrieve the current temperature value for two wind turbines. The following also shows the contents of the `batch-get-asset-property-value.json` file.

#### Sample Request
<a name="API_BatchGetAssetPropertyValue_Example_1_Request"></a>

```
aws iotsitewise batch-get-asset-property-value --cli-input-json file://batch-get-asset-property-value.json
```

```
{
   "entries":[
      {
         "entryId":"1",
         "assetId":"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
         "propertyId":"a1b2c3d4-5678-90ab-cdef-22222EXAMPLE"
      },
      {
         "entryId":"2",
         "assetId":"a1b2c3d4-5678-90ab-cdef-33333EXAMPLE",
         "propertyId":"a1b2c3d4-5678-90ab-cdef-44444EXAMPLE"
      }
   ]
}
```

#### Sample Response
<a name="API_BatchGetAssetPropertyValue_Example_1_Response"></a>

```
{
   "errorEntries":[

   ],
   "successEntries":[
      {
         "entryId":"1",
         "propertyValue":{
            "value":{
               "doubleValue":1426.66
            },
            "timestamp":{
               "timeInSeconds":1580853000,
               "offsetInNanos":0
            },
            "quality":"GOOD"
         }
      },
      {
         "entryId":"2",
         "propertyValue":{
            "value":{
               "doubleValue":1429.44
            },
            "timestamp":{
               "timeInSeconds":1580853000,
               "offsetInNanos":0
            },
            "quality":"GOOD"
         }
      }
   ]
}
```

## See Also
<a name="API_BatchGetAssetPropertyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValue)
