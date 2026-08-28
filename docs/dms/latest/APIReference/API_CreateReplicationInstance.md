---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationInstance.html
---

# CreateReplicationInstance
<a name="API_CreateReplicationInstance"></a>

Creates the replication instance using the specified parameters.

 AWS DMS requires that your account have certain roles with appropriate permissions before you can create a replication instance. For information on the required roles, see [Creating the IAM Roles to Use With the AWS CLI and AWS DMS API](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.APIRole). For information on the required permissions, see [IAM Permissions Needed to Use AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions).

**Note**
If you don't specify a version when creating a replication instance, AWS DMS will create the instance using the default engine version. For information about the default engine version, see [Release Notes](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReleaseNotes.html).

## Request Syntax
<a name="API_CreateReplicationInstance_RequestSyntax"></a>

```
{
   "AllocatedStorage": {{number}},
   "AutoMinorVersionUpgrade": {{boolean}},
   "AvailabilityZone": "{{string}}",
   "DnsNameServers": "{{string}}",
   "EngineVersion": "{{string}}",
   "KerberosAuthenticationSettings": {
      "KeyCacheSecretIamArn": "{{string}}",
      "KeyCacheSecretId": "{{string}}",
      "Krb5FileContents": "{{string}}"
   },
   "KmsKeyId": "{{string}}",
   "MultiAZ": {{boolean}},
   "NetworkType": "{{string}}",
   "PreferredMaintenanceWindow": "{{string}}",
   "PubliclyAccessible": {{boolean}},
   "ReplicationInstanceClass": "{{string}}",
   "ReplicationInstanceIdentifier": "{{string}}",
   "ReplicationSubnetGroupIdentifier": "{{string}}",
   "ResourceIdentifier": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcSecurityGroupIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateReplicationInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllocatedStorage](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-AllocatedStorage"></a>
The amount of storage (in gigabytes) to be initially allocated for the replication instance.
Type: Integer
Required: No

 ** [AutoMinorVersionUpgrade](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-AutoMinorVersionUpgrade"></a>
A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to `true`.
Default: `true`
Type: Boolean
Required: No

 ** [AvailabilityZone](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-AvailabilityZone"></a>
The Availability Zone where the replication instance will be created. The default value is a random, system-chosen Availability Zone in the endpoint's AWS Region, for example: `us-east-1d`.
Type: String
Required: No

 ** [DnsNameServers](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-DnsNameServers"></a>
A list of custom DNS name servers supported for the replication instance to access your on-premise source or target database. This list overrides the default name servers supported by the replication instance. You can specify a comma-separated list of internet addresses for up to four on-premise DNS name servers. For example: `"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"`
Type: String
Required: No

 ** [EngineVersion](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-EngineVersion"></a>
The engine version number of the replication instance.
If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.
Type: String
Required: No

 ** [KerberosAuthenticationSettings](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-KerberosAuthenticationSettings"></a>
Specifies the settings required for kerberos authentication when creating the replication instance.
Type: [KerberosAuthenticationSettings](API_KerberosAuthenticationSettings.md) object
Required: No

 ** [KmsKeyId](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-KmsKeyId"></a>
An AWS KMS key identifier that is used to encrypt the data on the replication instance.
If you don't specify a value for the `KmsKeyId` parameter, then AWS DMS uses your default encryption key.
 AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Required: No

 ** [MultiAZ](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-MultiAZ"></a>
 Specifies whether the replication instance is a Multi-AZ deployment. You can't set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to `true`.
Type: Boolean
Required: No

 ** [NetworkType](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-NetworkType"></a>
The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.
Type: String
Required: No

 ** [PreferredMaintenanceWindow](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-PreferredMaintenanceWindow"></a>
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
 Format: `ddd:hh24:mi-ddd:hh24:mi`
Default: A 30-minute window selected at random from an 8-hour block of time per AWS Region, occurring on a random day of the week.
Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
Constraints: Minimum 30-minute window.
Type: String
Required: No

 ** [PubliclyAccessible](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-PubliclyAccessible"></a>
 Specifies the accessibility options for the replication instance. A value of `true` represents an instance with a public IP address. A value of `false` represents an instance with a private IP address. The default value is `true`.
Type: Boolean
Required: No

 ** [ReplicationInstanceClass](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-ReplicationInstanceClass"></a>
The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to `"dms.c4.large"`.
For more information on the settings and capacities for the available replication instance classes, see [ Choosing the right AWS DMS replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Types.html ); and, [Selecting the best size for a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.SizingReplicationInstance.html).
Type: String
Length Constraints: Maximum length of 30.
Required: Yes

 ** [ReplicationInstanceIdentifier](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-ReplicationInstanceIdentifier"></a>
The replication instance identifier. This parameter is stored as a lowercase string.
Constraints:
+ Must contain 1-63 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `myrepinstance`
Type: String
Required: Yes

 ** [ReplicationSubnetGroupIdentifier](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-ReplicationSubnetGroupIdentifier"></a>
A subnet group to associate with the replication instance.
Type: String
Required: No

 ** [ResourceIdentifier](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-ResourceIdentifier"></a>
A friendly name for the resource identifier at the end of the `EndpointArn` response parameter that is returned in the created `Endpoint` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as `Example-App-ARN1`. For example, this value might result in the `EndpointArn` value `arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`. If you don't specify a `ResourceIdentifier` value, AWS DMS generates a default identifier value for the end of `EndpointArn`.
Type: String
Required: No

 ** [Tags](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-Tags"></a>
One or more tags to be assigned to the replication instance.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [VpcSecurityGroupIds](#API_CreateReplicationInstance_RequestSyntax) **   <a name="DMS-CreateReplicationInstance-request-VpcSecurityGroupIds"></a>
 Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_CreateReplicationInstance_ResponseSyntax"></a>

```
{
   "ReplicationInstance": {
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
}
```

## Response Elements
<a name="API_CreateReplicationInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationInstance](#API_CreateReplicationInstance_ResponseSyntax) **   <a name="DMS-CreateReplicationInstance-response-ReplicationInstance"></a>
The replication instance that was created.
Type: [ReplicationInstance](API_ReplicationInstance.md) object

## Errors
<a name="API_CreateReplicationInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InsufficientResourceCapacityFault **
There are not enough resources allocated to the database migration.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** InvalidSubnet **
The subnet provided isn't valid.
 ** message **

HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
 AWS DMS cannot access the KMS key.
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

 ** StorageQuotaExceededFault **
The storage quota has been exceeded.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_CreateReplicationInstance_Examples"></a>

### Example
<a name="API_CreateReplicationInstance_Example_1"></a>

This example illustrates one usage of CreateReplicationInstance.

#### Sample Request
<a name="API_CreateReplicationInstance_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.CreateReplicationInstance
{
   "ReplicationInstanceIdentifier":"test-rep-1",
   "AllocatedStorage":5,
   "ReplicationInstanceClass":"dms.t2.micro",
   "AvailabilityZone":"",
   "ReplicationSubnetGroupIdentifier":"default",
   "PreferredMaintenanceWindow":"",
   "EngineVersion":"1.5.0",
   "AutoMinorVersionUpgrade":true,
   "NetworkType":"IPv4",
   "Tags":[
      {
         "Key":"",
         "Value":""
      }
   ],
   "KmsKeyId":"",
   "PubliclyAccessible":true
}
```

#### Sample Response
<a name="API_CreateReplicationInstance_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationInstance":{
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
      "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:key/4dc17316-5543-
4ded-b1e3-d53a7cfb411d",
      "AllocatedStorage":5,
      "NetworkType":"IPv4",
      "EngineVersion":"1.5.0",
      "ReplicationInstanceIdentifier":"test-rep-1",
      "PreferredMaintenanceWindow":"sun:06:00-sun:14:00",
      "PendingModifiedValues":{

      }
   }
}
```

## See Also
<a name="API_CreateReplicationInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CreateReplicationInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CreateReplicationInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CreateReplicationInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CreateReplicationInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CreateReplicationInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CreateReplicationInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CreateReplicationInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CreateReplicationInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CreateReplicationInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CreateReplicationInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
