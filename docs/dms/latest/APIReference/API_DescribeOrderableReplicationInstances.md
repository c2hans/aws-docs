---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeOrderableReplicationInstances.html
---

# DescribeOrderableReplicationInstances
<a name="API_DescribeOrderableReplicationInstances"></a>

Returns information about the replication instance types that can be created in the specified region.

## Request Syntax
<a name="API_DescribeOrderableReplicationInstances_RequestSyntax"></a>

```
{
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeOrderableReplicationInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_DescribeOrderableReplicationInstances_RequestSyntax) **   <a name="DMS-DescribeOrderableReplicationInstances-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeOrderableReplicationInstances_RequestSyntax) **   <a name="DMS-DescribeOrderableReplicationInstances-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeOrderableReplicationInstances_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "OrderableReplicationInstances": [
      {
         "AvailabilityZones": [ "string" ],
         "DefaultAllocatedStorage": number,
         "EngineVersion": "string",
         "IncludedAllocatedStorage": number,
         "MaxAllocatedStorage": number,
         "MinAllocatedStorage": number,
         "ReleaseStatus": "string",
         "ReplicationInstanceClass": "string",
         "StorageType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeOrderableReplicationInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeOrderableReplicationInstances_ResponseSyntax) **   <a name="DMS-DescribeOrderableReplicationInstances-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [OrderableReplicationInstances](#API_DescribeOrderableReplicationInstances_ResponseSyntax) **   <a name="DMS-DescribeOrderableReplicationInstances-response-OrderableReplicationInstances"></a>
The order-able replication instances available.
Type: Array of [OrderableReplicationInstance](API_OrderableReplicationInstance.md) objects

## Errors
<a name="API_DescribeOrderableReplicationInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeOrderableReplicationInstances_Examples"></a>

### Example
<a name="API_DescribeOrderableReplicationInstances_Example_1"></a>

This example illustrates one usage of DescribeOrderableReplicationInstances.

#### Sample Request
<a name="API_DescribeOrderableReplicationInstances_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256
Credential=<Credential>,
SignedHeaders=contenttype;date;host;user-
agent;x-amz-date;x-amz-target;x-amzn-
requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.DescribeOrderableReplicationInstances
{
"MaxRecords": 0,
"Marker": ""
}
```

#### Sample Response
<a name="API_DescribeOrderableReplicationInstances_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "OrderableReplicationInstances":[
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.2xlarge",
         "EngineVersion":"1.3.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.4xlarge",
         "EngineVersion":"1.3.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.large",
         "EngineVersion":"1.3.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.xlarge",
         "EngineVersion":"1.3.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.large",
         "EngineVersion":"1.3.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.medium",
         "EngineVersion":"1.3.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.micro",
         "EngineVersion":"1.3.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.small",
         "EngineVersion":"1.3.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.2xlarge",
         "EngineVersion":"1.4.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.4xlarge",
         "EngineVersion":"1.4.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.large",
         "EngineVersion":"1.4.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.xlarge",
         "EngineVersion":"1.4.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.large",
         "EngineVersion":"1.4.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.medium",
         "EngineVersion":"1.4.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.micro",
         "EngineVersion":"1.4.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.small",
         "EngineVersion":"1.4.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.2xlarge",
         "EngineVersion":"1.5.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.4xlarge",
         "EngineVersion":"1.5.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.large",
         "EngineVersion":"1.5.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.c4.xlarge",
         "EngineVersion":"1.5.0",
         "IncludedAllocatedStorage":100,
         "DefaultAllocatedStorage":100,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.large",
         "EngineVersion":"1.5.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.medium",
         "EngineVersion":"1.5.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.micro",
         "EngineVersion":"1.5.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "StorageType":"gp2",
         "ReplicationInstanceClass":"dms.t2.small",
         "EngineVersion":"1.5.0",
         "IncludedAllocatedStorage":50,
         "DefaultAllocatedStorage":50,
         "MinAllocatedStorage":5,
         "MaxAllocatedStorage":6144
      },
      {
         "MaxAllocatedStorage": 6144,
         "AvailabilityZones": [
             "us-east-1a",
             "us-east-1b",
             "us-east-1c",
             "us-east-1d",
             "us-east-1e"
         ],
         "ReleaseStatus": "BETA",
         "DefaultAllocatedStorage": 100,
         "ReplicationInstanceClass": "dms.c4.2xlarge",
         "MinAllocatedStorage": 5,
         "EngineVersion": "3.3.0",
         "StorageType": "gp2",
         "IncludedAllocatedStorage": 100
      }
   ]
}
```

## See Also
<a name="API_DescribeOrderableReplicationInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeOrderableReplicationInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeOrderableReplicationInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeOrderableReplicationInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeOrderableReplicationInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeOrderableReplicationInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeOrderableReplicationInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeOrderableReplicationInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeOrderableReplicationInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeOrderableReplicationInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeOrderableReplicationInstances)
