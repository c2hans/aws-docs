---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetDimensionKeyDetails.html
---

# GetDimensionKeyDetails
<a name="API_GetDimensionKeyDetails"></a>

Get the attributes of the specified dimension group for a DB instance or data source. For example, if you specify a SQL ID, `GetDimensionKeyDetails` retrieves the full text of the dimension `db.sql.statement` associated with this ID. This operation is useful because `GetResourceMetrics` and `DescribeDimensionKeys` don't support retrieval of large SQL statement text, lock snapshots, and execution plans.

## Request Syntax
<a name="API_GetDimensionKeyDetails_RequestSyntax"></a>

```
{
   "Group": "{{string}}",
   "GroupIdentifier": "{{string}}",
   "Identifier": "{{string}}",
   "RequestedDimensions": [ "{{string}}" ],
   "ServiceType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDimensionKeyDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Group](#API_GetDimensionKeyDetails_RequestSyntax) **   <a name="performanceinsights-GetDimensionKeyDetails-request-Group"></a>
The name of the dimension group. Performance Insights searches the specified group for the dimension group ID. The following group name values are valid:
+  `db.execution_plan` (Amazon RDS and Aurora only)
+  `db.lock_snapshot` (Aurora only)
+  `db.query` (Amazon DocumentDB only)
+  `db.sql` (Amazon RDS and Aurora only)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** [GroupIdentifier](#API_GetDimensionKeyDetails_RequestSyntax) **   <a name="performanceinsights-GetDimensionKeyDetails-request-GroupIdentifier"></a>
The ID of the dimension group from which to retrieve dimension details. For dimension group `db.sql`, the group ID is `db.sql.id`. The following group ID values are valid:
+  `db.execution_plan.id` for dimension group `db.execution_plan` (Aurora and RDS only)
+  `db.sql.id` for dimension group `db.sql` (Aurora and RDS only)
+  `db.query.id` for dimension group `db.query` (DocumentDB only)
+ For the dimension group `db.lock_snapshot`, the `GroupIdentifier` is the epoch timestamp when Performance Insights captured the snapshot, in seconds. You can retrieve this value with the `GetResourceMetrics` operation for a 1 second period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** [Identifier](#API_GetDimensionKeyDetails_RequestSyntax) **   <a name="performanceinsights-GetDimensionKeyDetails-request-Identifier"></a>
The ID for a data source from which to gather dimension data. This ID must be immutable and unique within an AWS Region. When a DB instance is the data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [ServiceType](#API_GetDimensionKeyDetails_RequestSyntax) **   <a name="performanceinsights-GetDimensionKeyDetails-request-ServiceType"></a>
The AWS service for which Performance Insights returns data. The only valid value is `RDS`.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [RequestedDimensions](#API_GetDimensionKeyDetails_RequestSyntax) **   <a name="performanceinsights-GetDimensionKeyDetails-request-RequestedDimensions"></a>
A list of dimensions to retrieve the detail data for within the given dimension group. If you don't specify this parameter, Performance Insights returns all dimension data within the specified dimension group. Specify dimension names for the following dimension groups:
+  `db.execution_plan` - Specify the dimension name `db.execution_plan.raw_plan` or the short dimension name `raw_plan` (Amazon RDS and Aurora only)
+  `db.lock_snapshot` - Specify the dimension name `db.lock_snapshot.lock_trees` or the short dimension name `lock_trees`. (Aurora only)
+  `db.sql` - Specify either the full dimension name `db.sql.statement` or the short dimension name `statement` (Aurora and RDS only).
+  `db.query` - Specify either the full dimension name `db.query.statement` or the short dimension name `statement` (DocumentDB only).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-_\.:/*)( ]+$`
Required: No

## Response Syntax
<a name="API_GetDimensionKeyDetails_ResponseSyntax"></a>

```
{
   "Dimensions": [
      {
         "Dimension": "string",
         "Status": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetDimensionKeyDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Dimensions](#API_GetDimensionKeyDetails_ResponseSyntax) **   <a name="performanceinsights-GetDimensionKeyDetails-response-Dimensions"></a>
The details for the requested dimensions.
Type: Array of [DimensionKeyDetail](API_DimensionKeyDetail.md) objects

## Errors
<a name="API_GetDimensionKeyDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
The request failed due to an unknown error.
HTTP Status Code: 500

 ** InvalidArgumentException **
One of the arguments provided is invalid for this request.
HTTP Status Code: 400

 ** NotAuthorizedException **
The user is not authorized to perform this request.
HTTP Status Code: 400

## Examples
<a name="API_GetDimensionKeyDetails_Examples"></a>

### Retrieve the full SQL text for a query
<a name="API_GetDimensionKeyDetails_Example_1"></a>

The following example requests the full text for the SQL query with the ID `example-group-identifier`, which is a placeholder for a SQL ID that you retrieved by calling `GetResourceMetrics` or `DescribeDimensionKeys`. Because the dimension details are available, the response shows the full SQL text.

#### Sample Request
<a name="API_GetDimensionKeyDetails_Example_1_Request"></a>

```
{
    "ServiceType":"RDS",
    "Identifier":"db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "Group": "db.sql",
    "GroupIdentifier": "example-group-identifier",
    "RequestedDimensions": ["statement"]
}
```

#### Sample Response
<a name="API_GetDimensionKeyDetails_Example_1_Response"></a>

```
{
    "Dimensions":[
    {
        "Value": "SELECT e.last_name, d.department_name FROM employees e, departments d WHERE e.department_id=d.department_id",
        "Dimension": "db.sql.statement",
        "Status": "AVAILABLE"
    },
    ...
    ]
}
```

### Retrieve locking data for a database at a point in time
<a name="API_GetDimensionKeyDetails_Example_2"></a>

The following example requests locking data at the epoch timestamp `1730231303`. You can retrieve the epoch timestamp with the `GetResourceMetrics` operation for a 1 second period.

Note that Performance Insights uses the comma-separated values format for the response. Each column value is enclosed in double quotation marks (" ") and separated by a comma. Each line is separated by a new line. The first line in the response describes the column names, and each of the following lines represents session data from a blocking or blocked session. The value `level` is the level of the session in the blocking tree hierarchy. For example, the session at level 0 is blocking the sessions at level 1.

#### Sample Request
<a name="API_GetDimensionKeyDetails_Example_2_Request"></a>

```
{
    "ServiceType":"RDS",
    "Identifier":"db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "Group": "db.lock_snapshot",
    "GroupIdentifier": "1730231303",
    "RequestedDimensions": ["lock_trees"]
}
```

#### Sample Response
<a name="API_GetDimensionKeyDetails_Example_2_Response"></a>

```
{
    "Dimensions":[
    {
        "Value": "\"level\",\"blocked_sessions_count\",\"pid\",\"session_id\",\"blocking_mode\",\"waiting_mode\",\"last_query_executed\",\"application\",\"blocking_txn_start_time\",\"waiting_start_time\",\"session_start_time\",\"state\",\"wait_event_type\",\"wait_event\",\"last_query_exec_time\",\"user\",\"host\",\"port\",\"client_address\",\"granted\",\"waiting_tuple\",\"waiting_page\",\"waiting_transaction_id\",\"waiting_relation\",\"waiting_object_id\",\"waiting_database_id\",\"waiting_database_name\",\"waiting_locktype\",\"blocking_time_(In_Seconds)\"\n\"0\",\"4\",\"28599\",\"63bcb300.6fb7\",\"\",\"\",\"update sbtest1 set id = 200000 where id=1;\",\"psql\",\"\",\"\",\"1672533380000\",\"idle in transaction\",\"Client\",\"ClientRead\",\"1672533380000\",\"postgres\",\"\",\"37444\",\"34.222.155.102\",\"t\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"42\"\n\"1\",\"3\",\"30877\",\"63bcbc21.789d\",\"ExclusiveLock\",\"ShareLock\",\"update sbtest1 set id=20000 where id=1;\",\"psql\",\"1672533380000\",\"1672535758000\",\"1672535758000\",\"active\",\"Lock\",\"transactionid\",\"1672535758000\",\"postgres\",\"\",\"35064\",\"34.222.155.102\",\"f\",\"\",\"\",\"569470\",\"\",\"\",\"\",\"sbtest\",\"transactionid\",\"2430\"\n\"2\",\"2\",\"30937\",\"63bcbc5c.78d9\",\"AccessExclusiveLock\",\"AccessExclusiveLock\",\"update sbtest1 set id = 200000 where id=1;\",\"psql\",\"1672535758000\",\"1672533370000\",\"1672533370000\",\"active\",\"Lock\",\"tuple\",\"1672533370000\",\"postgres\",\"\",\"37398\",\"34.222.155.102\",\"f\",\"1\",\"0\",\"\",\"16946\",\"\",\"16839\",\"sbtest\",\"tuple\",\"2470\"\n\"3\",\"1\",\"31029\",\"63bcbcbf.7935\",\"AccessExclusiveLock\",\"AccessExclusiveLock\",\"update sbtest1 set id = 200000 where id=1;\",\"psql\",\"1672533370000\",\"1672533330000\",\"1672533330000\",\"active\",\"Lock\",\"tuple\",\"1672533330000\",\"postgres\",\"\",\"36266\",\"34.222.155.102\",\"f\",\"1\",\"0\",\"\",\"16946\",\"\",\"16839\",\"sbtest\",\"tuple\",\"2440\"\n\"4\",\"0\",\"31062\",\"63bcbcd8.7956\",\"AccessExclusiveLock\",\"AccessExclusiveLock\",\"update sbtest1 set id = 200000 where id=1;\",\"psql\",\"1672533330000\",\"1672533360000\",\"1672533360000\",\"active\",\"Lock\",\"tuple\",\"1672533360000\",\"postgres\",\"\",\"56694\",\"34.222.155.102\",\"f\",\"1\",\"0\",\"\",\"16946\",\"\",\"16839\",\"sbtest\",\"tuple\",\"\"\n",
        "Dimension": "db.lock_snapshot",
        "Status": "AVAILABLE"
    },
    ...
    ]
}
```

### Retrieve execution plans for a database
<a name="API_GetDimensionKeyDetails_Example_3"></a>

The following example requests execution plans for a database, where the plan ID is `435345209`.

#### Sample Request
<a name="API_GetDimensionKeyDetails_Example_3_Request"></a>

```
{
      "ServiceType": "RDS",
      "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
      "GroupIdentifier": "435345209",
      "Group": "db.execution_plan",
      "RequestedDimensions": ["raw_plan"]
}
```

#### Sample Response
<a name="API_GetDimensionKeyDetails_Example_3_Response"></a>

```
{
      "Dimensions":[
      {
         "Value": "Update on orders  (cost=0.43..8.46 rows=0 width=0)\n  ->  Index Scan using orders_pk on orders  (cost=0.43..8.46 rows=1 width=14)\n        Index Cond: (order_id = 200)"
         "Dimension": "db.execution_plan.raw_plan",
         "Status": "AVAILABLE",
      }
      ]
}
```

## See Also
<a name="API_GetDimensionKeyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/GetDimensionKeyDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/GetDimensionKeyDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/GetDimensionKeyDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/GetDimensionKeyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/GetDimensionKeyDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/GetDimensionKeyDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/GetDimensionKeyDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/GetDimensionKeyDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/GetDimensionKeyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/GetDimensionKeyDetails)
