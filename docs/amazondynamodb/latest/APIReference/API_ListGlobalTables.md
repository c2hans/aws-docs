---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListGlobalTables.html
---

# ListGlobalTables
<a name="API_ListGlobalTables"></a>

Lists all global tables that have a replica in the specified Region.

**Important**
This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use [Global Tables version 2019.11.21 (Current)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).
To determine which version you're using, see [Determining the global table version you are using](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html). To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see [Upgrading global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html).

## Request Syntax
<a name="API_ListGlobalTables_RequestSyntax"></a>

```
{
   "ExclusiveStartGlobalTableName": "{{string}}",
   "Limit": {{number}},
   "RegionName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListGlobalTables_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ExclusiveStartGlobalTableName](#API_ListGlobalTables_RequestSyntax) **   <a name="DDB-ListGlobalTables-request-ExclusiveStartGlobalTableName"></a>
The first global table name that this operation will evaluate.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [Limit](#API_ListGlobalTables_RequestSyntax) **   <a name="DDB-ListGlobalTables-request-Limit"></a>
The maximum number of table names to return, if the parameter is not specified DynamoDB defaults to 100.
If the number of global tables DynamoDB finds reaches this limit, it stops the operation and returns the table names collected up to that point, with a table name in the `LastEvaluatedGlobalTableName` to apply in a subsequent operation to the `ExclusiveStartGlobalTableName` parameter.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [RegionName](#API_ListGlobalTables_RequestSyntax) **   <a name="DDB-ListGlobalTables-request-RegionName"></a>
Lists the global tables in a specific Region.
Type: String
Required: No

## Response Syntax
<a name="API_ListGlobalTables_ResponseSyntax"></a>

```
{
   "GlobalTables": [
      {
         "GlobalTableName": "string",
         "ReplicationGroup": [
            {
               "RegionName": "string"
            }
         ]
      }
   ],
   "LastEvaluatedGlobalTableName": "string"
}
```

## Response Elements
<a name="API_ListGlobalTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GlobalTables](#API_ListGlobalTables_ResponseSyntax) **   <a name="DDB-ListGlobalTables-response-GlobalTables"></a>
List of global table names.
Type: Array of [GlobalTable](API_GlobalTable.md) objects

 ** [LastEvaluatedGlobalTableName](#API_ListGlobalTables_ResponseSyntax) **   <a name="DDB-ListGlobalTables-response-LastEvaluatedGlobalTableName"></a>
Last evaluated global table name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_ListGlobalTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

## See Also
<a name="API_ListGlobalTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/ListGlobalTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/ListGlobalTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ListGlobalTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/ListGlobalTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ListGlobalTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/ListGlobalTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/ListGlobalTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/ListGlobalTables)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/ListGlobalTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ListGlobalTables)
