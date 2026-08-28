---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBackup.html
---

# DescribeBackup
<a name="API_DescribeBackup"></a>

Describes an existing backup of a table.

You can call `DescribeBackup` at a maximum rate of 10 times per second.

## Request Syntax
<a name="API_DescribeBackup_RequestSyntax"></a>

```
{
   "BackupArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBackup_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BackupArn](#API_DescribeBackup_RequestSyntax) **   <a name="DDB-DescribeBackup-request-BackupArn"></a>
The Amazon Resource Name (ARN) associated with the backup.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_DescribeBackup_ResponseSyntax"></a>

```
{
   "BackupDescription": {
      "BackupDetails": {
         "BackupArn": "string",
         "BackupCreationDateTime": number,
         "BackupExpiryDateTime": number,
         "BackupName": "string",
         "BackupSizeBytes": number,
         "BackupStatus": "string",
         "BackupType": "string"
      },
      "SourceTableDetails": {
         "BillingMode": "string",
         "ItemCount": number,
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
         "TableArn": "string",
         "TableCreationDateTime": number,
         "TableId": "string",
         "TableName": "string",
         "TableSizeBytes": number
      },
      "SourceTableFeatureDetails": {
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
               }
            }
         ],
         "LocalSecondaryIndexes": [
            {
               "IndexName": "string",
               "KeySchema": [
                  {
                     "AttributeName": "string",
                     "KeyType": "string"
                  }
               ],
               "Projection": {
                  "NonKeyAttributes": [ "string" ],
                  "ProjectionType": "string"
               }
            }
         ],
         "SSEDescription": {
            "InaccessibleEncryptionDateTime": number,
            "KMSMasterKeyArn": "string",
            "SSEType": "string",
            "Status": "string"
         },
         "StreamDescription": {
            "StreamEnabled": boolean,
            "StreamViewType": "string"
         },
         "TimeToLiveDescription": {
            "AttributeName": "string",
            "TimeToLiveStatus": "string"
         },
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
      }
   }
}
```

## Response Elements
<a name="API_DescribeBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupDescription](#API_DescribeBackup_ResponseSyntax) **   <a name="DDB-DescribeBackup-response-BackupDescription"></a>
Contains the description of the backup created for the table.
Type: [BackupDescription](API_BackupDescription.md) object

## Errors
<a name="API_DescribeBackup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BackupNotFoundException **
Backup not found for the given BackupARN.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

## See Also
<a name="API_DescribeBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DescribeBackup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DescribeBackup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DescribeBackup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DescribeBackup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeBackup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DescribeBackup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DescribeBackup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DescribeBackup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DescribeBackup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DescribeBackup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
