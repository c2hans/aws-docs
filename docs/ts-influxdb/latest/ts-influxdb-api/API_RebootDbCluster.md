---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_RebootDbCluster.html
---

# RebootDbCluster
<a name="API_RebootDbCluster"></a>

Reboots a Timestream for InfluxDB cluster.

## Request Syntax
<a name="API_RebootDbCluster_RequestSyntax"></a>

```
{
   "dbClusterId": "{{string}}",
   "instanceIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_RebootDbCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dbClusterId](#API_RebootDbCluster_RequestSyntax) **   <a name="tsinfluxdb-RebootDbCluster-request-dbClusterId"></a>
Service-generated unique identifier of the DB cluster to reboot.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** [instanceIds](#API_RebootDbCluster_RequestSyntax) **   <a name="tsinfluxdb-RebootDbCluster-request-instanceIds"></a>
A list of service-generated unique DB Instance Ids belonging to the DB Cluster to reboot.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: No

## Response Syntax
<a name="API_RebootDbCluster_ResponseSyntax"></a>

```
{
   "dbClusterStatus": "string"
}
```

## Response Elements
<a name="API_RebootDbCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbClusterStatus](#API_RebootDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbCluster-response-dbClusterStatus"></a>
The status of the DB Cluster.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | AVAILABLE | FAILED | DELETED | MAINTENANCE | UPDATING_INSTANCE_TYPE | REBOOTING | REBOOT_FAILED | PARTIALLY_AVAILABLE`

## Errors
<a name="API_RebootDbCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request conflicts with an existing resource in Timestream for InfluxDB.
 ** resourceId **
The identifier for the Timestream for InfluxDB resource associated with the request.
 ** resourceType **
The type of Timestream for InfluxDB resource associated with the request.
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
<a name="API_RebootDbCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-influxdb-2023-01-27/RebootDbCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-influxdb-2023-01-27/RebootDbCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/RebootDbCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-influxdb-2023-01-27/RebootDbCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/RebootDbCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-influxdb-2023-01-27/RebootDbCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-influxdb-2023-01-27/RebootDbCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-influxdb-2023-01-27/RebootDbCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-influxdb-2023-01-27/RebootDbCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/RebootDbCluster)
