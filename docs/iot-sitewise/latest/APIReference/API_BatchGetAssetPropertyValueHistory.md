---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValueHistory.html
---

# BatchGetAssetPropertyValueHistory
<a name="API_BatchGetAssetPropertyValueHistory"></a>

Gets the historical values for one or more asset properties. For more information, see [Querying historical values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values) in the * AWS IoT SiteWise User Guide*.

## Request Syntax
<a name="API_BatchGetAssetPropertyValueHistory_RequestSyntax"></a>

```
POST /properties/batch/history HTTP/1.1
Content-type: application/json

{
   "entries": [
      {
         "assetId": "{{string}}",
         "endDate": {{number}},
         "entryId": "{{string}}",
         "propertyAlias": "{{string}}",
         "propertyId": "{{string}}",
         "qualities": [ "{{string}}" ],
         "startDate": {{number}},
         "timeOrdering": "{{string}}"
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchGetAssetPropertyValueHistory_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetAssetPropertyValueHistory_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [entries](#API_BatchGetAssetPropertyValueHistory_RequestSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValueHistory-request-entries"></a>
The list of asset property historical value entries for the batch get request. You can specify up to 16 entries per request.
Type: Array of [BatchGetAssetPropertyValueHistoryEntry](API_BatchGetAssetPropertyValueHistoryEntry.md) objects
Required: Yes

 ** [maxResults](#API_BatchGetAssetPropertyValueHistory_RequestSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValueHistory-request-maxResults"></a>
The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.
+ The size of the result set is equal to 4 MB.
+ The number of data points in the result set is equal to the value of `maxResults`. The maximum value of `maxResults` is 20000.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_BatchGetAssetPropertyValueHistory_RequestSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValueHistory-request-nextToken"></a>
The token to be used for the next set of paginated results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_BatchGetAssetPropertyValueHistory_ResponseSyntax"></a>

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
         "assetPropertyValueHistory": [
            {
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
         ],
         "entryId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetAssetPropertyValueHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorEntries](#API_BatchGetAssetPropertyValueHistory_ResponseSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValueHistory-response-errorEntries"></a>
A list of the errors (if any) associated with the batch request. Each error entry contains the `entryId` of the entry that failed.
Type: Array of [BatchGetAssetPropertyValueHistoryErrorEntry](API_BatchGetAssetPropertyValueHistoryErrorEntry.md) objects

 ** [nextToken](#API_BatchGetAssetPropertyValueHistory_ResponseSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValueHistory-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [skippedEntries](#API_BatchGetAssetPropertyValueHistory_ResponseSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValueHistory-response-skippedEntries"></a>
A list of entries that were not processed by this batch request. because these entries had been completely processed by previous paginated requests. Each skipped entry contains the `entryId` of the entry that skipped.
Type: Array of [BatchGetAssetPropertyValueHistorySkippedEntry](API_BatchGetAssetPropertyValueHistorySkippedEntry.md) objects

 ** [successEntries](#API_BatchGetAssetPropertyValueHistory_ResponseSyntax) **   <a name="iotsitewise-BatchGetAssetPropertyValueHistory-response-successEntries"></a>
A list of entries that were processed successfully by this batch request. Each success entry contains the `entryId` of the entry that succeeded and the latest query result.
Type: Array of [BatchGetAssetPropertyValueHistorySuccessEntry](API_BatchGetAssetPropertyValueHistorySuccessEntry.md) objects

## Errors
<a name="API_BatchGetAssetPropertyValueHistory_Errors"></a>

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
<a name="API_BatchGetAssetPropertyValueHistory_Examples"></a>

### Example
<a name="API_BatchGetAssetPropertyValueHistory_Example_1"></a>

The following example uses the AWS Command Line Interface (AWS CLI) to retrieve the historical temperature values for two wind turbines between April 26, 2021 at midnight and May 3, 2021 at midnight in Pacific Time (PT). The following also shows the contents of the `batch-get-asset-property-value-history.json` file.

#### Sample Request
<a name="API_BatchGetAssetPropertyValueHistory_Example_1_Request"></a>

```
aws iotsitewise batch-get-asset-property-value-history --cli-input-json file://batch-get-asset-property-value-history.json
```

```
{
   "entries":[
      {
         "entryId":"1",
         "assetId":"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
         "propertyId":"a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
         "startDate":1619420400,
         "endDate":1620025200
      },
      {
         "entryId":"2",
         "assetId":"a1b2c3d4-5678-90ab-cdef-33333EXAMPLE",
         "propertyId":"a1b2c3d4-5678-90ab-cdef-44444EXAMPLE",
         "startDate":1619420400,
         "endDate":1620025200
      }
   ]
}
```

#### Sample Response
<a name="API_BatchGetAssetPropertyValueHistory_Example_1_Response"></a>

```
{
   "errorEntries":[],
   "successEntries":[
      {
         "entryId":"1",
         "assetPropertyValueHistory":[
            {
               "value":{
                  "doubleValue":1426.55
               },
               "timestamp":{
                  "timeInSeconds":1619420400,
                  "offsetInNanos":0
               },
               "quality":"GOOD"
            },
            {
               "value":{
                  "doubleValue":1429.23
               },
               "timestamp":{
                  "timeInSeconds":1619620700,
                  "offsetInNanos":0
               },
               "quality":"GOOD"
            },
            {
               "value":{
                  "doubleValue":1431.43
               },
               "timestamp":{
                  "timeInSeconds":1619820400,
                  "offsetInNanos":0
               },
               "quality":"GOOD"
            },
            {
               "value":{
                  "doubleValue":1435.66
               },
               "timestamp":{
                  "timeInSeconds":1620025200,
                  "offsetInNanos":0
               },
               "quality":"GOOD"
            }
         ]
      },
      {
         "entryId":"2",
         "assetPropertyValueHistory":[
            {
               "value":{
                  "doubleValue":1424.17
               },
               "timestamp":{
                  "timeInSeconds":1619420400,
                  "offsetInNanos":0
               },
               "quality":"GOOD"
            },
            {
               "value":{
                  "doubleValue":1424.23
               },
               "timestamp":{
                  "timeInSeconds":1619620700,
                  "offsetInNanos":0
               },
               "quality":"GOOD"
            },
            {
               "value":{
                  "doubleValue":1425.24
               },
               "timestamp":{
                  "timeInSeconds":1619820400,
                  "offsetInNanos":0
               },
               "quality":"GOOD"
            },
            {
               "value":{
                  "doubleValue":1430.17
               },
               "timestamp":{
                  "timeInSeconds":1620025200,
                  "offsetInNanos":0
               },
               "quality":"GOOD"
            }
         ]
      }
   ],
   "skippedEntries":[]
}
```

## See Also
<a name="API_BatchGetAssetPropertyValueHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistory)
