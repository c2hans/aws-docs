---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationSubnetGroup.html
---

# ModifyReplicationSubnetGroup
<a name="API_ModifyReplicationSubnetGroup"></a>

Modifies the settings for the specified replication subnet group.

## Request Syntax
<a name="API_ModifyReplicationSubnetGroup_RequestSyntax"></a>

```
{
   "ReplicationSubnetGroupDescription": "{{string}}",
   "ReplicationSubnetGroupIdentifier": "{{string}}",
   "SubnetIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ModifyReplicationSubnetGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplicationSubnetGroupDescription](#API_ModifyReplicationSubnetGroup_RequestSyntax) **   <a name="DMS-ModifyReplicationSubnetGroup-request-ReplicationSubnetGroupDescription"></a>
A description for the replication instance subnet group.
Type: String
Required: No

 ** [ReplicationSubnetGroupIdentifier](#API_ModifyReplicationSubnetGroup_RequestSyntax) **   <a name="DMS-ModifyReplicationSubnetGroup-request-ReplicationSubnetGroupIdentifier"></a>
The name of the replication instance subnet group.
Type: String
Required: Yes

 ** [SubnetIds](#API_ModifyReplicationSubnetGroup_RequestSyntax) **   <a name="DMS-ModifyReplicationSubnetGroup-request-SubnetIds"></a>
A list of subnet IDs.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_ModifyReplicationSubnetGroup_ResponseSyntax"></a>

```
{
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
   }
}
```

## Response Elements
<a name="API_ModifyReplicationSubnetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationSubnetGroup](#API_ModifyReplicationSubnetGroup_ResponseSyntax) **   <a name="DMS-ModifyReplicationSubnetGroup-response-ReplicationSubnetGroup"></a>
The modified replication subnet group.
Type: [ReplicationSubnetGroup](API_ReplicationSubnetGroup.md) object

## Errors
<a name="API_ModifyReplicationSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidSubnet **
The subnet provided isn't valid.
 ** message **

HTTP Status Code: 400

 ** ReplicationSubnetGroupDoesNotCoverEnoughAZs **
The replication subnet group does not cover enough Availability Zones (AZs). Edit the replication subnet group and add more AZs.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

 ** SubnetAlreadyInUse **
The specified subnet is already in use.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ModifyReplicationSubnetGroup_Examples"></a>

### Example
<a name="API_ModifyReplicationSubnetGroup_Example_1"></a>

This example illustrates one usage of ModifyReplicationSubnetGroup.

#### Sample Request
<a name="API_ModifyReplicationSubnetGroup_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.ModifyReplicationSubnetGroup
{
   "ReplicationSubnetGroupIdentifier":"test-subnet-group",
   "ReplicationSubnetGroupDescription":"",
   "SubnetIds":[
      "subnet-f6dd91af",
      "subnet-3605751d "
   ]
}
```

#### Sample Response
<a name="API_ModifyReplicationSubnetGroup_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationSubnetGroup":{
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
         }
      ],
      "VpcId":"vpc-6741a603",
      "SubnetGroupStatus":"Complete",
      "ReplicationSubnetGroupIdentifier":"test-subnet-group"
   }
}
```

## See Also
<a name="API_ModifyReplicationSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ModifyReplicationSubnetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ModifyReplicationSubnetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ModifyReplicationSubnetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ModifyReplicationSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ModifyReplicationSubnetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ModifyReplicationSubnetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ModifyReplicationSubnetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ModifyReplicationSubnetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ModifyReplicationSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ModifyReplicationSubnetGroup)
