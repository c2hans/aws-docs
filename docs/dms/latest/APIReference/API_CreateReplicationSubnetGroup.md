---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationSubnetGroup.html
---

# CreateReplicationSubnetGroup
<a name="API_CreateReplicationSubnetGroup"></a>

Creates a replication subnet group given a list of the subnet IDs in a VPC.

The VPC needs to have at least one subnet in at least two availability zones in the AWS Region, otherwise the service will throw a `ReplicationSubnetGroupDoesNotCoverEnoughAZs` exception.

If a replication subnet group exists in your AWS account, the CreateReplicationSubnetGroup action returns the following error message: The Replication Subnet Group already exists. In this case, delete the existing replication subnet group. To do so, use the [DeleteReplicationSubnetGroup](https://docs.aws.amazon.com/en_us/dms/latest/APIReference/API_DeleteReplicationSubnetGroup.html) action. Optionally, choose Subnet groups in the AWS DMS console, then choose your subnet group. Next, choose Delete from Actions.

## Request Syntax
<a name="API_CreateReplicationSubnetGroup_RequestSyntax"></a>

```
{
   "ReplicationSubnetGroupDescription": "{{string}}",
   "ReplicationSubnetGroupIdentifier": "{{string}}",
   "SubnetIds": [ "{{string}}" ],
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateReplicationSubnetGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplicationSubnetGroupDescription](#API_CreateReplicationSubnetGroup_RequestSyntax) **   <a name="DMS-CreateReplicationSubnetGroup-request-ReplicationSubnetGroupDescription"></a>
The description for the subnet group.
Constraints: This parameter Must not contain non-printable control characters.
Type: String
Required: Yes

 ** [ReplicationSubnetGroupIdentifier](#API_CreateReplicationSubnetGroup_RequestSyntax) **   <a name="DMS-CreateReplicationSubnetGroup-request-ReplicationSubnetGroupIdentifier"></a>
The name for the replication subnet group. This value is stored as a lowercase string.
Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, or hyphens. Must not be "default".
Example: `mySubnetgroup`
Type: String
Required: Yes

 ** [SubnetIds](#API_CreateReplicationSubnetGroup_RequestSyntax) **   <a name="DMS-CreateReplicationSubnetGroup-request-SubnetIds"></a>
Two or more subnet IDs to be assigned to the subnet group.
Type: Array of strings
Required: Yes

 ** [Tags](#API_CreateReplicationSubnetGroup_RequestSyntax) **   <a name="DMS-CreateReplicationSubnetGroup-request-Tags"></a>
One or more tags to be assigned to the subnet group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateReplicationSubnetGroup_ResponseSyntax"></a>

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
<a name="API_CreateReplicationSubnetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationSubnetGroup](#API_CreateReplicationSubnetGroup_ResponseSyntax) **   <a name="DMS-CreateReplicationSubnetGroup-response-ReplicationSubnetGroup"></a>
The replication subnet group that was created.
Type: [ReplicationSubnetGroup](API_ReplicationSubnetGroup.md) object

## Errors
<a name="API_CreateReplicationSubnetGroup_Errors"></a>

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

 ** ResourceAlreadyExistsFault **
The resource you are attempting to create already exists.
 ** message **

 ** resourceArn **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_CreateReplicationSubnetGroup_Examples"></a>

### Example
<a name="API_CreateReplicationSubnetGroup_Example_1"></a>

This example illustrates one usage of CreateReplicationSubnetGroup.

#### Sample Request
<a name="API_CreateReplicationSubnetGroup_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.CreateReplicationSubnetGroup
{
   "ReplicationSubnetGroupIdentifier":"test-subnet-group",
   "ReplicationSubnetGroupDescription":"dms testing",
   "SubnetIds":[
      "subnet-f6dd91af",
      "subnet-3605751d",
      "subnet-c2daefb5"
   ],
   "Tags":[
      {
         "Key":"",
         "Value":""
      }
   ]
}
```

#### Sample Response
<a name="API_CreateReplicationSubnetGroup_Example_1_Response"></a>

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
}
```

## See Also
<a name="API_CreateReplicationSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CreateReplicationSubnetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CreateReplicationSubnetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CreateReplicationSubnetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CreateReplicationSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CreateReplicationSubnetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CreateReplicationSubnetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CreateReplicationSubnetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CreateReplicationSubnetGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CreateReplicationSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CreateReplicationSubnetGroup)
