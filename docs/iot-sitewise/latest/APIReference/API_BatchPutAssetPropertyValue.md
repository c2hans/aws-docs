---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html
---

# BatchPutAssetPropertyValue
<a name="API_BatchPutAssetPropertyValue"></a>

Sends a list of asset property values to AWS IoT SiteWise. Each value is a timestamp-quality-value (TQV) data point. For more information, see [Ingesting data using the API](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html) in the * AWS IoT SiteWise User Guide*.

To identify an asset property, you must specify one of the following:
+ The `assetId` and `propertyId` of an asset property.
+ A `propertyAlias`, which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature`). To define an asset property's alias, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html).

**Important**
With respect to Unix epoch time, AWS IoT SiteWise accepts only TQVs that have a timestamp of no more than 7 days in the past and no more than 10 minutes in the future. AWS IoT SiteWise rejects timestamps outside of the inclusive range of [-7 days, \+10 minutes] and returns a `TimestampOutOfRangeException` error.
For each asset property, AWS IoT SiteWise overwrites TQVs with duplicate timestamps unless the newer TQV has a different quality. For example, if you store a TQV `{T1, GOOD, V1}`, then storing `{T1, GOOD, V2}` replaces the existing TQV.

 AWS IoT SiteWise authorizes access to each `BatchPutAssetPropertyValue` entry individually. For more information, see [BatchPutAssetPropertyValue authorization](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action) in the * AWS IoT SiteWise User Guide*.

## Request Syntax
<a name="API_BatchPutAssetPropertyValue_RequestSyntax"></a>

```
POST /properties HTTP/1.1
Content-type: application/json

{
   "enablePartialEntryProcessing": {{boolean}},
   "entries": [
      {
         "assetId": "{{string}}",
         "entryId": "{{string}}",
         "propertyAlias": "{{string}}",
         "propertyId": "{{string}}",
         "propertyValues": [
            {
               "quality": "{{string}}",
               "timestamp": {
                  "offsetInNanos": {{number}},
                  "timeInSeconds": {{number}}
               },
               "value": {
                  "booleanValue": {{boolean}},
                  "doubleValue": {{number}},
                  "integerValue": {{number}},
                  "nullValue": {
                     "valueType": "{{string}}"
                  },
                  "stringValue": "{{string}}"
               }
            }
         ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchPutAssetPropertyValue_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchPutAssetPropertyValue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [enablePartialEntryProcessing](#API_BatchPutAssetPropertyValue_RequestSyntax) **   <a name="iotsitewise-BatchPutAssetPropertyValue-request-enablePartialEntryProcessing"></a>
This setting enables partial ingestion at entry-level. If set to `true`, we ingest all TQVs not resulting in an error. If set to `false`, an invalid TQV fails ingestion of the entire entry that contains it.
Type: Boolean
Required: No

 ** [entries](#API_BatchPutAssetPropertyValue_RequestSyntax) **   <a name="iotsitewise-BatchPutAssetPropertyValue-request-entries"></a>
The list of asset property value entries for the batch put request. You can specify up to 10 entries per request.
Type: Array of [PutAssetPropertyValueEntry](API_PutAssetPropertyValueEntry.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchPutAssetPropertyValue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errorEntries": [
      {
         "entryId": "string",
         "errors": [
            {
               "errorCode": "string",
               "errorMessage": "string",
               "timestamps": [
                  {
                     "offsetInNanos": number,
                     "timeInSeconds": number
                  }
               ]
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchPutAssetPropertyValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorEntries](#API_BatchPutAssetPropertyValue_ResponseSyntax) **   <a name="iotsitewise-BatchPutAssetPropertyValue-response-errorEntries"></a>
A list of the errors (if any) associated with the batch put request. Each error entry contains the `entryId` of the entry that failed.
Type: Array of [BatchPutAssetPropertyErrorEntry](API_BatchPutAssetPropertyErrorEntry.md) objects

## Errors
<a name="API_BatchPutAssetPropertyValue_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

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
<a name="API_BatchPutAssetPropertyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)
