---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTable.html
---

# DescribeGlobalTable
<a name="API_DescribeGlobalTable"></a>

Returns information about the specified global table.

**Important**
This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use [Global Tables version 2019.11.21 (Current)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).
To determine which version you're using, see [Determining the global table version you are using](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html). To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see [Upgrading global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html).

## Request Syntax
<a name="API_DescribeGlobalTable_RequestSyntax"></a>

```
{
   "GlobalTableName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGlobalTable_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GlobalTableName](#API_DescribeGlobalTable_RequestSyntax) **   <a name="DDB-DescribeGlobalTable-request-GlobalTableName"></a>
The name of the global table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeGlobalTable_ResponseSyntax"></a>

```
{
   "GlobalTableDescription": {
      "CreationDateTime": number,
      "GlobalTableArn": "string",
      "GlobalTableName": "string",
      "GlobalTableStatus": "string",
      "ReplicationGroup": [
         {
            "GlobalSecondaryIndexes": [
               {
                  "IndexName": "string",
                  "OnDemandThroughputOverride": {
                     "MaxReadRequestUnits": number
                  },
                  "ProvisionedThroughputOverride": {
                     "ReadCapacityUnits": number
                  },
                  "WarmThroughput": {
                     "ReadUnitsPerSecond": number,
                     "Status": "string",
                     "WriteUnitsPerSecond": number
                  }
               }
            ],
            "GlobalTableSettingsReplicationMode": "string",
            "KMSMasterKeyId": "string",
            "OnDemandThroughputOverride": {
               "MaxReadRequestUnits": number
            },
            "ProvisionedThroughputOverride": {
               "ReadCapacityUnits": number
            },
            "RegionName": "string",
            "ReplicaArn": "string",
            "ReplicaInaccessibleDateTime": number,
            "ReplicaStatus": "string",
            "ReplicaStatusDescription": "string",
            "ReplicaStatusPercentProgress": "string",
            "ReplicaTableClassSummary": {
               "LastUpdateDateTime": number,
               "TableClass": "string"
            },
            "WarmThroughput": {
               "ReadUnitsPerSecond": number,
               "Status": "string",
               "WriteUnitsPerSecond": number
            }
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeGlobalTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GlobalTableDescription](#API_DescribeGlobalTable_ResponseSyntax) **   <a name="DDB-DescribeGlobalTable-response-GlobalTableDescription"></a>
Contains the details of the global table.
Type: [GlobalTableDescription](API_GlobalTableDescription.md) object

## Errors
<a name="API_DescribeGlobalTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalTableNotFoundException **
The specified global table does not exist.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

## See Also
<a name="API_DescribeGlobalTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DescribeGlobalTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DescribeGlobalTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DescribeGlobalTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DescribeGlobalTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeGlobalTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DescribeGlobalTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DescribeGlobalTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DescribeGlobalTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DescribeGlobalTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DescribeGlobalTable)
