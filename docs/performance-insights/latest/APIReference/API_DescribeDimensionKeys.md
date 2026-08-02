---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DescribeDimensionKeys.html
---

# DescribeDimensionKeys
<a name="API_DescribeDimensionKeys"></a>

For a specific time period, retrieve the top `N` dimension keys for a metric.

**Note**
Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.

## Request Syntax
<a name="API_DescribeDimensionKeys_RequestSyntax"></a>

```
{
   "AdditionalMetrics": [ "{{string}}" ],
   "EndTime": {{number}},
   "Filter": {
      "{{string}}" : "{{string}}"
   },
   "GroupBy": {
      "Dimensions": [ "{{string}}" ],
      "Group": "{{string}}",
      "Limit": {{number}}
   },
   "Identifier": "{{string}}",
   "MaxResults": {{number}},
   "Metric": "{{string}}",
   "NextToken": "{{string}}",
   "PartitionBy": {
      "Dimensions": [ "{{string}}" ],
      "Group": "{{string}}",
      "Limit": {{number}}
   },
   "PeriodInSeconds": {{number}},
   "ServiceType": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_DescribeDimensionKeys_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [EndTime](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-EndTime"></a>
The date and time specifying the end of the requested time series data. The value specified is *exclusive*, which means that data points less than (but not equal to) `EndTime` are returned.
The value for `EndTime` must be later than the value for `StartTime`.
Type: Timestamp
Required: Yes

 ** [GroupBy](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-GroupBy"></a>
A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights returns all dimensions within this group, unless you provide the names of specific dimensions within this group. You can also request that Performance Insights return a limited number of values for a dimension.
Type: [DimensionGroup](API_DimensionGroup.md) object
Required: Yes

 ** [Identifier](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-Identifier"></a>
An immutable, AWS Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.
To use an Amazon RDS instance as a data source, you specify its `DbiResourceId` value. For example, specify `db-FAIHNTYBKTGAUSUZQYPDS2GW4A`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [Metric](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-Metric"></a>
The name of a Performance Insights metric to be measured.
Valid values for `Metric` are:
+  `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
+  `db.sampledload.avg` - The raw number of active sessions for the database engine.
If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg`. For most use cases, you can query `db.load.avg` only.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** [ServiceType](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-ServiceType"></a>
The AWS service for which Performance Insights will return metrics. Valid values are as follows:
+  `RDS`
+  `DOCDB`
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [StartTime](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-StartTime"></a>
The date and time specifying the beginning of the requested time series data. You must specify a `StartTime` within the past 7 days. The value specified is *inclusive*, which means that data points equal to or greater than `StartTime` are returned.
The value for `StartTime` must be earlier than the value for `EndTime`.
Type: Timestamp
Required: Yes

 ** [AdditionalMetrics](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-AdditionalMetrics"></a>
Additional metrics for the top `N` dimension keys. If the specified dimension group in the `GroupBy` parameter is `db.sql_tokenized`, you can specify per-SQL metrics to get the values for the top `N` SQL digests. The response syntax is as follows: `"AdditionalMetrics" : { "string" : "string" }`.
The only supported statistic function is `.avg`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-_\.:/*)( ]+$`
Required: No

 ** [Filter](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-Filter"></a>
One or more filters to apply in the request. Restrictions:
+ Any number of filters by the same dimension, as specified in the `GroupBy` or `Partition` parameters.
+ A single filter for any other dimension in this dimension group.
The `db.sql.db_id` filter isn't available for RDS for SQL Server DB instances.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `^[a-zA-Z0-9-_\.:/*)( ]+$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

 ** [MaxResults](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-MaxResults"></a>
The maximum number of items to return in the response. If more items exist than the specified `MaxRecords` value, a pagination token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`
Required: No

 ** [PartitionBy](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-PartitionBy"></a>
For each dimension specified in `GroupBy`, specify a secondary dimension to further subdivide the partition keys in the response.
Type: [DimensionGroup](API_DimensionGroup.md) object
Required: No

 ** [PeriodInSeconds](#API_DescribeDimensionKeys_RequestSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-request-PeriodInSeconds"></a>
The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:
+  `1` (one second)
+  `60` (one minute)
+  `300` (five minutes)
+  `3600` (one hour)
+  `86400` (twenty-four hours)
If you don't specify `PeriodInSeconds`, then Performance Insights chooses a value for you, with a goal of returning roughly 100-200 data points in the response.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeDimensionKeys_ResponseSyntax"></a>

```
{
   "AlignedEndTime": number,
   "AlignedStartTime": number,
   "Keys": [
      {
         "AdditionalMetrics": {
            "string" : number
         },
         "Dimensions": {
            "string" : "string"
         },
         "Partitions": [ number ],
         "Total": number
      }
   ],
   "NextToken": "string",
   "PartitionKeys": [
      {
         "Dimensions": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeDimensionKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlignedEndTime](#API_DescribeDimensionKeys_ResponseSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-response-AlignedEndTime"></a>
The end time for the returned dimension keys, after alignment to a granular boundary (as specified by `PeriodInSeconds`). `AlignedEndTime` will be greater than or equal to the value of the user-specified `Endtime`.
Type: Timestamp

 ** [AlignedStartTime](#API_DescribeDimensionKeys_ResponseSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-response-AlignedStartTime"></a>
The start time for the returned dimension keys, after alignment to a granular boundary (as specified by `PeriodInSeconds`). `AlignedStartTime` will be less than or equal to the value of the user-specified `StartTime`.
Type: Timestamp

 ** [Keys](#API_DescribeDimensionKeys_ResponseSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-response-Keys"></a>
The dimension keys that were requested.
Type: Array of [DimensionKeyDescription](API_DimensionKeyDescription.md) objects

 ** [NextToken](#API_DescribeDimensionKeys_ResponseSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-response-NextToken"></a>
A pagination token that indicates the response didn’t return all available records because `MaxRecords` was specified in the previous request. To get the remaining records, specify `NextToken` in a separate request with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`

 ** [PartitionKeys](#API_DescribeDimensionKeys_ResponseSyntax) **   <a name="performanceinsights-DescribeDimensionKeys-response-PartitionKeys"></a>
If `PartitionBy` was present in the request, `PartitionKeys` contains the breakdown of dimension keys by the specified partitions.
Type: Array of [ResponsePartitionKey](API_ResponsePartitionKey.md) objects

## Errors
<a name="API_DescribeDimensionKeys_Errors"></a>

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
<a name="API_DescribeDimensionKeys_Examples"></a>

### Retrieve top dimension keys
<a name="API_DescribeDimensionKeys_Example_1"></a>

The following example retrieves the top 10 dimension keys for metrics `db.load.avg`, `db.sql_tokenized.stats.calls_per_sec.avg`, and `db.sql_tokenized.statement` over a specific 5-minute time range. The request returns the metrics in dimension groups `db.sql_tokenized.id` and `db.sql_tokenized.statement`. For both of these dimension groups, the request subdivides the partition keys by `db.user.id` and `db.user.name`.

#### Sample Request
<a name="API_DescribeDimensionKeys_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.DescribeDimensionKeys
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
   "ServiceType": "RDS",
   "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
   "StartTime": 1603915200,
   "EndTime": 1603918800,
   "PeriodInSeconds": 300,
   "Metric": "db.load.avg",
   "GroupBy": {
      "Dimensions": [ "db.sql_tokenized.id", "db.sql_tokenized.statement" ],
      "Group": "db.sql_tokenized",
      "Limit": 5
   },
   "Filter": {
      "db.user.name" : "example-user"
   },
   "PartitionBy": {
      "Dimensions": [ "db.user.id", "db.user.name" ],
      "Group": "db.user",
      "Limit": 5
   },
   "MaxResults": 10,
   "AdditionalMetrics": [
      "db.sql_tokenized.stats.calls_per_sec.avg",
      "db.sql_tokenized.stats.rows_per_sec.avg"
   ]
}
```

#### Sample Response
<a name="API_DescribeDimensionKeys_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive

{
   "AlignedEndTime": 1.6244895E9,
   "AlignedStartTime": 1.6244889E9,
   "Keys": [
      {
         "Dimensions": {
            "db.sql_tokenized.id" : "12A345BCDE67F8G9H012I3IJKI4J5675K8L912M",
            "db.sql_tokenized.statement" : "INSERT INTO pgbench_history (tid, bid, aid, delta, mtime) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP);"
         },
         "Partitions": [ 2.1333333333333333 ],
         "Total": 2.1333333333333333,
         "AdditionalMetrics" : {
            "db.sql_tokenized.stats.calls_per_sec.avg": 1.0,
            "db.sql_tokenized.stats.rows_per_sec.avg": 3.0
         }
      },
      ......
   ],
   "PartitionKeys": [
     {
        "Dimensions": {
          "db.user.name": "example-user",
          "db.user.id": "A12B3456C7D8E890F123F45G67HIJ8K9LM0N1O2"
        }
     }
   ]
}
}
```

## See Also
<a name="API_DescribeDimensionKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/DescribeDimensionKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/DescribeDimensionKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/DescribeDimensionKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/DescribeDimensionKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/DescribeDimensionKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/DescribeDimensionKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/DescribeDimensionKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/DescribeDimensionKeys)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/DescribeDimensionKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/DescribeDimensionKeys)
