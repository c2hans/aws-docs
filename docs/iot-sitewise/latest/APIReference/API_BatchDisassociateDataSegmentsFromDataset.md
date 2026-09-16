---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchDisassociateDataSegmentsFromDataset.html
---

# BatchDisassociateDataSegmentsFromDataset
<a name="API_BatchDisassociateDataSegmentsFromDataset"></a>

Disassociates a batch of data segments from a curated dataset. Disassociating a data segment doesn't delete the underlying data in the source session dataset.

## Request Syntax
<a name="API_BatchDisassociateDataSegmentsFromDataset_RequestSyntax"></a>

```
POST /datasets/{{datasetId}}/data-segments/disassociate HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "disassociateDataSegmentEntries": [
      {
         "endTimestamp": {
            "offsetInNanos": {{number}},
            "timeInSeconds": {{number}}
         },
         "sourceDatasetId": "{{string}}",
         "startTimestamp": {
            "offsetInNanos": {{number}},
            "timeInSeconds": {{number}}
         },
         "timeSeriesId": "{{string}}"
      }
   ],
   "workspaceName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchDisassociateDataSegmentsFromDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_BatchDisassociateDataSegmentsFromDataset_RequestSyntax) **   <a name="iotsitewise-BatchDisassociateDataSegmentsFromDataset-request-uri-datasetId"></a>
The ID of the curated dataset to disassociate data segments from.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_BatchDisassociateDataSegmentsFromDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_BatchDisassociateDataSegmentsFromDataset_RequestSyntax) **   <a name="iotsitewise-BatchDisassociateDataSegmentsFromDataset-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [disassociateDataSegmentEntries](#API_BatchDisassociateDataSegmentsFromDataset_RequestSyntax) **   <a name="iotsitewise-BatchDisassociateDataSegmentsFromDataset-request-disassociateDataSegmentEntries"></a>
The list of data segment entries to disassociate from the dataset.
Type: Array of [DisassociateDataSegmentEntry](API_DisassociateDataSegmentEntry.md) objects
Required: Yes

 ** [workspaceName](#API_BatchDisassociateDataSegmentsFromDataset_RequestSyntax) **   <a name="iotsitewise-BatchDisassociateDataSegmentsFromDataset-request-workspaceName"></a>
The name of the workspace that contains the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Response Syntax
<a name="API_BatchDisassociateDataSegmentsFromDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasetId": "string",
   "datasetVersion": "string",
   "failedDisassociations": [
      {
         "endTimestamp": {
            "offsetInNanos": number,
            "timeInSeconds": number
         },
         "errorCode": "string",
         "errorMessage": "string",
         "sourceDatasetId": "string",
         "startTimestamp": {
            "offsetInNanos": number,
            "timeInSeconds": number
         },
         "timeSeriesId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDisassociateDataSegmentsFromDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasetId](#API_BatchDisassociateDataSegmentsFromDataset_ResponseSyntax) **   <a name="iotsitewise-BatchDisassociateDataSegmentsFromDataset-response-datasetId"></a>
The ID of the dataset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [datasetVersion](#API_BatchDisassociateDataSegmentsFromDataset_ResponseSyntax) **   <a name="iotsitewise-BatchDisassociateDataSegmentsFromDataset-response-datasetVersion"></a>
The version of the dataset after disassociation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [failedDisassociations](#API_BatchDisassociateDataSegmentsFromDataset_ResponseSyntax) **   <a name="iotsitewise-BatchDisassociateDataSegmentsFromDataset-response-failedDisassociations"></a>
A list of data segment disassociations that failed.
Type: Array of [FailedDataSegmentDisassociation](API_FailedDataSegmentDisassociation.md) objects

## Errors
<a name="API_BatchDisassociateDataSegmentsFromDataset_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_BatchDisassociateDataSegmentsFromDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchDisassociateDataSegmentsFromDataset)
