---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBulkOperation.html
---

# DescribeBulkOperation
<a name="API_DescribeBulkOperation"></a>

Describes the specified bulk operation.

## Request Syntax
<a name="API_DescribeBulkOperation_RequestSyntax"></a>

```
{
   "BulkOperationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBulkOperation_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BulkOperationArn](#API_DescribeBulkOperation_RequestSyntax) **   <a name="DDB-DescribeBulkOperation-request-BulkOperationArn"></a>
The Amazon Resource Name (ARN) of the bulk operation to describe.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_DescribeBulkOperation_ResponseSyntax"></a>

```
{
   "BulkOperationDescription": {
      "BulkOperationArn": "string",
      "BulkOperationStatus": "string",
      "BulkOperationUsage": [
         {
            "BulkPutBytes": number,
            "GlobalSecondaryIndexes": {
               "string" : {
                  "BulkPutBytes": number
               }
            },
            "LocalSecondaryIndexes": {
               "string" : {
                  "BulkPutBytes": number
               }
            },
            "Table": {
               "BulkPutBytes": number
            },
            "TableName": "string",
            "VectorIndexes": {
               "string" : {
                  "BulkPutVectorBytes": number
               }
            }
         }
      ],
      "ClientToken": "string",
      "EndTime": number,
      "FailedItemCount": number,
      "FailureCode": "string",
      "FailureMessage": "string",
      "InputS3Configuration": {
         "InputCompressionType": "string",
         "InputFormat": "string",
         "S3Bucket": "string",
         "S3BucketOwner": "string",
         "S3KeyPrefix": "string"
      },
      "MaxWriteRequestUnits": number,
      "OutputS3Configuration": {
         "OutputType": [ "string" ],
         "S3Bucket": "string",
         "S3BucketOwner": "string",
         "S3KeyPrefix": "string",
         "S3SseAlgorithm": "string",
         "S3SseKmsKeyId": "string"
      },
      "PerformanceTier": "string",
      "ProcessedInputBytes": number,
      "ProcessedItemCount": number,
      "StartTime": number,
      "TableDetails": [
         {
            "TableId": "string",
            "TableName": "string"
         }
      ],
      "TotalInputBytes": number
   }
}
```

## Response Elements
<a name="API_DescribeBulkOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BulkOperationDescription](#API_DescribeBulkOperation_ResponseSyntax) **   <a name="DDB-DescribeBulkOperation-response-BulkOperationDescription"></a>
Contains detailed information about the bulk operation.
Type: [BulkOperationDescription](API_BulkOperationDescription.md) object

## Errors
<a name="API_DescribeBulkOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeBulkOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DescribeBulkOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DescribeBulkOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DescribeBulkOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DescribeBulkOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeBulkOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DescribeBulkOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DescribeBulkOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DescribeBulkOperation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DescribeBulkOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DescribeBulkOperation)
