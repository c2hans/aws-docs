---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeImport.html
---

# DescribeImport
<a name="API_DescribeImport"></a>

 Represents the properties of the import.

## Request Syntax
<a name="API_DescribeImport_RequestSyntax"></a>

```
{
   "ImportArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeImport_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ImportArn](#API_DescribeImport_RequestSyntax) **   <a name="DDB-DescribeImport-request-ImportArn"></a>
 The Amazon Resource Name (ARN) associated with the table you're importing to.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_DescribeImport_ResponseSyntax"></a>

```
{
   "ImportTableDescription": {
      "ClientToken": "string",
      "CloudWatchLogGroupArn": "string",
      "EndTime": number,
      "ErrorCount": number,
      "FailureCode": "string",
      "FailureMessage": "string",
      "ImportArn": "string",
      "ImportedItemCount": number,
      "ImportStatus": "string",
      "InputCompressionType": "string",
      "InputFormat": "string",
      "InputFormatOptions": {
         "Csv": {
            "Delimiter": "string",
            "HeaderList": [ "string" ]
         }
      },
      "ProcessedItemCount": number,
      "ProcessedSizeBytes": number,
      "S3BucketSource": {
         "S3Bucket": "string",
         "S3BucketOwner": "string",
         "S3KeyPrefix": "string"
      },
      "StartTime": number,
      "TableArn": "string",
      "TableCreationParameters": {
         "AttributeDefinitions": [
            {
               "AttributeName": "string",
               "AttributeType": "string"
            }
         ],
         "BillingMode": "string",
         "GlobalSecondaryIndexes": [
            {
               "IndexName": "string",
               "KeySchema": [
                  {
                     "AttributeName": "string",
                     "KeyType": "string"
                  }
               ],
               "OnDemandThroughput": {
                  "MaxReadRequestUnits": number,
                  "MaxWriteRequestUnits": number
               },
               "Projection": {
                  "NonKeyAttributes": [ "string" ],
                  "ProjectionType": "string"
               },
               "ProvisionedThroughput": {
                  "ReadCapacityUnits": number,
                  "WriteCapacityUnits": number
               },
               "WarmThroughput": {
                  "ReadUnitsPerSecond": number,
                  "WriteUnitsPerSecond": number
               }
            }
         ],
         "KeySchema": [
            {
               "AttributeName": "string",
               "KeyType": "string"
            }
         ],
         "OnDemandThroughput": {
            "MaxReadRequestUnits": number,
            "MaxWriteRequestUnits": number
         },
         "ProvisionedThroughput": {
            "ReadCapacityUnits": number,
            "WriteCapacityUnits": number
         },
         "SSESpecification": {
            "Enabled": boolean,
            "KMSMasterKeyId": "string",
            "SSEType": "string"
         },
         "TableName": "string",
         "VectorIndexes": [
            {
               "Dimensions": number,
               "DistanceFunction": "string",
               "IndexName": "string",
               "Projection": {
                  "NonKeyAttributes": [ "string" ],
                  "ProjectionType": "string"
               },
               "SearchSchema": [
                  {
                     "AttributeName": "string",
                     "SearchSchemaElementType": "string"
                  }
               ],
               "VectorAttribute": {
                  "AttributeName": "string"
               }
            }
         ]
      },
      "TableId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImportTableDescription](#API_DescribeImport_ResponseSyntax) **   <a name="DDB-DescribeImport-response-ImportTableDescription"></a>
 Represents the properties of the table created for the import, and parameters of the import. The import parameters include import status, how many items were processed, and how many errors were encountered.
Type: [ImportTableDescription](API_ImportTableDescription.md) object

## Errors
<a name="API_DescribeImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ImportNotFoundException **
 The specified import was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DescribeImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DescribeImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DescribeImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DescribeImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DescribeImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DescribeImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DescribeImport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DescribeImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DescribeImport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
