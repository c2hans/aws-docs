---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationInstances.html
---

# DescribeReplicationInstances
<a name="API_DescribeReplicationInstances"></a>

Returns information about replication instances for your account in the current region.

## Request Syntax
<a name="API_DescribeReplicationInstances_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeReplicationInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeReplicationInstances_RequestSyntax) **   <a name="DMS-DescribeReplicationInstances-request-Filters"></a>
Filters applied to replication instances.
Valid filter names: replication-instance-arn \| replication-instance-id \| replication-instance-class \| engine-version
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeReplicationInstances_RequestSyntax) **   <a name="DMS-DescribeReplicationInstances-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeReplicationInstances_RequestSyntax) **   <a name="DMS-DescribeReplicationInstances-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeReplicationInstances_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "ReplicationInstances": [
      {
         "AllocatedStorage": number,
         "AutoMinorVersionUpgrade": boolean,
         "AvailabilityZone": "string",
         "DnsNameServers": "string",
         "EngineVersion": "string",
         "FreeUntil": number,
         "InstanceCreateTime": number,
         "KerberosAuthenticationSettings": {
            "KeyCacheSecretIamArn": "string",
            "KeyCacheSecretId": "string",
            "Krb5FileContents": "string"
         },
         "KmsKeyId": "string",
         "MultiAZ": boolean,
         "NetworkType": "string",
         "PendingModifiedValues": {
            "AllocatedStorage": number,
            "EngineVersion": "string",
            "MultiAZ": boolean,
            "NetworkType": "string",
            "ReplicationInstanceClass": "string"
         },
         "PreferredMaintenanceWindow": "string",
         "PubliclyAccessible": boolean,
         "ReplicationInstanceArn": "string",
         "ReplicationInstanceClass": "string",
         "ReplicationInstanceIdentifier": "string",
         "ReplicationInstanceIpv6Addresses": [ "string" ],
         "ReplicationInstancePrivateIpAddress": "string",
         "ReplicationInstancePrivateIpAddresses": [ "string" ],
         "ReplicationInstancePublicIpAddress": "string",
         "ReplicationInstancePublicIpAddresses": [ "string" ],
         "ReplicationInstanceStatus": "string",
         "ReplicationSubnetGroup": {
            "IsReadOnly": boolean,
            "ReplicationSubnetGroupDescription": "string",
            "ReplicationSubnetGroupIdentifier": "string",
            "SubnetGroupStatus": "string",
            "Subnets": [
               {
                  "SubnetAvailabilityZone": {
                     "Name": "string"
                  },
                  "SubnetIdentifier": "string",
                  "SubnetStatus": "string"
               }
            ],
            "SupportedNetworkTypes": [ "string" ],
            "VpcId": "string"
         },
         "SecondaryAvailabilityZone": "string",
         "VpcSecurityGroups": [
            {
               "Status": "string",
               "VpcSecurityGroupId": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReplicationInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeReplicationInstances_ResponseSyntax) **   <a name="DMS-DescribeReplicationInstances-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [ReplicationInstances](#API_DescribeReplicationInstances_ResponseSyntax) **   <a name="DMS-DescribeReplicationInstances-response-ReplicationInstances"></a>
The replication instances described.
Type: Array of [ReplicationInstance](API_ReplicationInstance.md) objects

## Errors
<a name="API_DescribeReplicationInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeReplicationInstances_Examples"></a>

### Example
<a name="API_DescribeReplicationInstances_Example_1"></a>

This example illustrates one usage of DescribeReplicationInstances.

#### Sample Request
<a name="API_DescribeReplicationInstances_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeReplicationInstances
{
   "Filters":[
      {
         "Name":"rep-instance-arn",
         "Values":[
            "arn:aws:dms:us-east-
1:123456789012:rep:PWEBBEUNOLU7VEB2OHTEH4I4GQ"
         ]
      }
   ],
   "MaxRecords":0,
   "Marker":""
}
```

#### Sample Response
<a name="API_DescribeReplicationInstances_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationInstances":[
      {
         "AvailabilityZone":"us-east-1c",
         "PubliclyAccessible":true,
         "ReplicationInstanceArn":"arn:aws:dms:us-east-
1:123456789012:rep:PWEBBEUNOLU7VEB2OHTEH4I4GQ",
         "ReplicationInstanceClass":"dms.t2.micro",
         "ReplicationSubnetGroup":{
            "ReplicationSubnetGroupDescription":"default",
            "Subnets":[
               {
                  "SubnetStatus":"Active",
                  "SubnetIdentifier":"subnet-f6dd91af",
                  "SubnetAvailabilityZone":{
                     "Name":"us-east-1d"
                  }
               },
               {
                  "SubnetStatus":"Active",
                  "SubnetIdentifier":"subnet-3605751d",
                  "SubnetAvailabilityZone":{
                     "Name":"us-east-1b"
                  }
               },
               {
                  "SubnetStatus":"Active",
                  "SubnetIdentifier":"subnet-c2daefb5",
                  "SubnetAvailabilityZone":{
                     "Name":"us-east-1c"
                  }
               },
               {
                  "SubnetStatus":"Active",
                  "SubnetIdentifier":"subnet-85e90cb8",
                  "SubnetAvailabilityZone":{
                     "Name":"us-east-1e"
                  }
               }
            ],
            "VpcId":"vpc-6741a603",
            "SubnetGroupStatus":"Complete",
            "ReplicationSubnetGroupIdentifier":"default"
         },
         "AutoMinorVersionUpgrade":true,
         "ReplicationInstanceStatus":"creating",
         "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:key/4dc17316-
5543-4ded-b1e3-d53a7cfb411d",
         "AllocatedStorage":5,
         "EngineVersion":"1.5.0",
         "ReplicationInstanceIdentifier":"test-rep-1",
         "PreferredMaintenanceWindow":"sun:06:00-sun:14:00",
         "PendingModifiedValues":{

         }
      }
   ]
}
```

## See Also
<a name="API_DescribeReplicationInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeReplicationInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeReplicationInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeReplicationInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeReplicationInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeReplicationInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeReplicationInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeReplicationInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeReplicationInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeReplicationInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeReplicationInstances)
