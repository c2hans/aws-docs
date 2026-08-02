---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbClusters.html
---

# ListDbClusters
<a name="API_ListDbClusters"></a>

Returns a list of Timestream for InfluxDB DB clusters.

## Request Syntax
<a name="API_ListDbClusters_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDbClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListDbClusters_RequestSyntax) **   <a name="tsinfluxdb-ListDbClusters-request-maxResults"></a>
The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListDbClusters_RequestSyntax) **   <a name="tsinfluxdb-ListDbClusters-request-nextToken"></a>
The pagination token. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListDbClusters_ResponseSyntax"></a>

```
{
   "items": [
      {
         "allocatedStorage": number,
         "arn": "string",
         "dbInstanceType": "string",
         "dbStorageType": "string",
         "deploymentType": "string",
         "endpoint": "string",
         "engineType": "string",
         "id": "string",
         "name": "string",
         "networkType": "string",
         "port": number,
         "readerEndpoint": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDbClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListDbClusters_ResponseSyntax) **   <a name="tsinfluxdb-ListDbClusters-response-items"></a>
A list of Timestream for InfluxDB cluster summaries.
Type: Array of [DbClusterSummary](API_DbClusterSummary.md) objects

 ** [nextToken](#API_ListDbClusters_ResponseSyntax) **   <a name="tsinfluxdb-ListDbClusters-response-nextToken"></a>
Token from a previous call of the operation. When this value is provided, the service returns results from where the previous response left off.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListDbClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found or does not exist.
 ** resourceId **
The identifier for the Timestream for InfluxDB resource associated with the request.
 ** resourceType **
The type of Timestream for InfluxDB resource associated with the request.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by Timestream for InfluxDB.
 ** reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListDbClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-influxdb-2023-01-27/ListDbClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-influxdb-2023-01-27/ListDbClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/ListDbClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-influxdb-2023-01-27/ListDbClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/ListDbClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-influxdb-2023-01-27/ListDbClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-influxdb-2023-01-27/ListDbClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-influxdb-2023-01-27/ListDbClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-influxdb-2023-01-27/ListDbClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/ListDbClusters)
