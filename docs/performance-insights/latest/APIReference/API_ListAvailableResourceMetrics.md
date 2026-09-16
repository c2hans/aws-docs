---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListAvailableResourceMetrics.html
---

# ListAvailableResourceMetrics
<a name="API_ListAvailableResourceMetrics"></a>

Retrieve metrics of the specified types that can be queried for a specified DB instance.

## Request Syntax
<a name="API_ListAvailableResourceMetrics_RequestSyntax"></a>

```
{
   "Identifier": "{{string}}",
   "MaxResults": {{number}},
   "MetricTypes": [ "{{string}}" ],
   "NextToken": "{{string}}",
   "ServiceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAvailableResourceMetrics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Identifier](#API_ListAvailableResourceMetrics_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceMetrics-request-Identifier"></a>
An immutable identifier for a data source that is unique within an AWS Region. Performance Insights gathers metrics from this data source. To use an Amazon RDS DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VWZ`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [MetricTypes](#API_ListAvailableResourceMetrics_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceMetrics-request-MetricTypes"></a>
The types of metrics to return in the response. Valid values in the array include the following:
+  `os` (OS counter metrics) - All engines
+  `db` (DB load metrics) - All engines except for Amazon DocumentDB
+  `db.sql.stats` (per-SQL metrics) - All engines except for Amazon DocumentDB
+  `db.sql_tokenized.stats` (per-SQL digest metrics) - All engines except for Amazon DocumentDB
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-_\.:/*)( ]+$`
Required: Yes

 ** [ServiceType](#API_ListAvailableResourceMetrics_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceMetrics-request-ServiceType"></a>
The AWS service for which Performance Insights returns metrics.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [MaxResults](#API_ListAvailableResourceMetrics_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceMetrics-request-MaxResults"></a>
The maximum number of items to return. If the `MaxRecords` value is less than the number of existing items, the response includes a pagination token.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No

 ** [NextToken](#API_ListAvailableResourceMetrics_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceMetrics-request-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`
Required: No

## Response Syntax
<a name="API_ListAvailableResourceMetrics_ResponseSyntax"></a>

```
{
   "Metrics": [
      {
         "Description": "string",
         "Metric": "string",
         "Unit": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAvailableResourceMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Metrics](#API_ListAvailableResourceMetrics_ResponseSyntax) **   <a name="performanceinsights-ListAvailableResourceMetrics-response-Metrics"></a>
An array of metrics available to query. Each array element contains the full name, description, and unit of the metric.
Type: Array of [ResponseResourceMetric](API_ResponseResourceMetric.md) objects

 ** [NextToken](#API_ListAvailableResourceMetrics_ResponseSyntax) **   <a name="performanceinsights-ListAvailableResourceMetrics-response-NextToken"></a>
A pagination token that indicates the response didn’t return all available records because `MaxRecords` was specified in the previous request. To get the remaining records, specify `NextToken` in a separate request with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`

## Errors
<a name="API_ListAvailableResourceMetrics_Errors"></a>

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
<a name="API_ListAvailableResourceMetrics_Examples"></a>

### List specified metrics
<a name="API_ListAvailableResourceMetrics_Example_1"></a>

The following example requests the metrics for metric types `os` and `db`.

#### Sample Request
<a name="API_ListAvailableResourceMetrics_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.ListAvailableResourceMetrics
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "ServiceType": "RDS",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "MetricTypes": [ "os", "db" ]
}
```

#### Sample Response
<a name="API_ListAvailableResourceMetrics_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive

{
    "Metrics": [
        {
            "Description": "The number of virtual CPUs for the DB instance",
            "Metric": "os.general.numVCPUs",
            "Unit": "vCPUs"
        },
        ......,
        {
            "Description": "Time spent reading data file blocks by backends in this instance",
            "Metric": "db.IO.read_latency",
            "Unit": "Milliseconds per block"
        },
        ......
    ]
}
```

## See Also
<a name="API_ListAvailableResourceMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/ListAvailableResourceMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/ListAvailableResourceMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/ListAvailableResourceMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/ListAvailableResourceMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/ListAvailableResourceMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/ListAvailableResourceMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/ListAvailableResourceMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/ListAvailableResourceMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/ListAvailableResourceMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/ListAvailableResourceMetrics)
