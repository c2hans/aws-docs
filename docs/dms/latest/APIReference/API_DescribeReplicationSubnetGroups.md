---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationSubnetGroups.html
---

# DescribeReplicationSubnetGroups
<a name="API_DescribeReplicationSubnetGroups"></a>

Returns information about the replication subnet groups.

## Request Syntax
<a name="API_DescribeReplicationSubnetGroups_RequestSyntax"></a>

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
<a name="API_DescribeReplicationSubnetGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeReplicationSubnetGroups_RequestSyntax) **   <a name="DMS-DescribeReplicationSubnetGroups-request-Filters"></a>
Filters applied to replication subnet groups.
Valid filter names: replication-subnet-group-id
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeReplicationSubnetGroups_RequestSyntax) **   <a name="DMS-DescribeReplicationSubnetGroups-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeReplicationSubnetGroups_RequestSyntax) **   <a name="DMS-DescribeReplicationSubnetGroups-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeReplicationSubnetGroups_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "ReplicationSubnetGroups": [
      {
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
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReplicationSubnetGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeReplicationSubnetGroups_ResponseSyntax) **   <a name="DMS-DescribeReplicationSubnetGroups-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [ReplicationSubnetGroups](#API_DescribeReplicationSubnetGroups_ResponseSyntax) **   <a name="DMS-DescribeReplicationSubnetGroups-response-ReplicationSubnetGroups"></a>
A description of the replication subnet groups.
Type: Array of [ReplicationSubnetGroup](API_ReplicationSubnetGroup.md) objects

## Errors
<a name="API_DescribeReplicationSubnetGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeReplicationSubnetGroups_Examples"></a>

### Example
<a name="API_DescribeReplicationSubnetGroups_Example_1"></a>

This example illustrates one usage of DescribeReplicationSubnetGroups.

#### Sample Request
<a name="API_DescribeReplicationSubnetGroups_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeReplicationSubnetGroups
{
   "Filters":[
      {
         "Name":"replication-subnet-group-id",
         "Values":[
            "test-subnet-group"
         ]
      }
   ],
   "MaxRecords":0,
   "Marker":""
}
```

#### Sample Response
<a name="API_DescribeReplicationSubnetGroups_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationSubnetGroups":[
      {
         "ReplicationSubnetGroupDescription":"dms testing",
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
            }
         ],
         "VpcId":"vpc-6741a603",
         "SubnetGroupStatus":"Complete",
         "ReplicationSubnetGroupIdentifier":"test-subnet-group"
      }
   ]
}
```

## See Also
<a name="API_DescribeReplicationSubnetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeReplicationSubnetGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeReplicationSubnetGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeReplicationSubnetGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeReplicationSubnetGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeReplicationSubnetGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeReplicationSubnetGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeReplicationSubnetGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeReplicationSubnetGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeReplicationSubnetGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeReplicationSubnetGroups)
