---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationInstance.html
---

# ModifyReplicationInstance
<a name="API_ModifyReplicationInstance"></a>

Modifies the replication instance to apply new settings. You can change one or more parameters by specifying these parameters and the new values in the request.

Some settings are applied during the maintenance window.

## Request Syntax
<a name="API_ModifyReplicationInstance_RequestSyntax"></a>

```
{
   "AllocatedStorage": {{number}},
   "AllowMajorVersionUpgrade": {{boolean}},
   "ApplyImmediately": {{boolean}},
   "AutoMinorVersionUpgrade": {{boolean}},
   "EngineVersion": "{{string}}",
   "KerberosAuthenticationSettings": {
      "KeyCacheSecretIamArn": "{{string}}",
      "KeyCacheSecretId": "{{string}}",
      "Krb5FileContents": "{{string}}"
   },
   "MultiAZ": {{boolean}},
   "NetworkType": "{{string}}",
   "PreferredMaintenanceWindow": "{{string}}",
   "ReplicationInstanceArn": "{{string}}",
   "ReplicationInstanceClass": "{{string}}",
   "ReplicationInstanceIdentifier": "{{string}}",
   "VpcSecurityGroupIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ModifyReplicationInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllocatedStorage](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-AllocatedStorage"></a>
The amount of storage (in gigabytes) to be allocated for the replication instance.
Type: Integer
Required: No

 ** [AllowMajorVersionUpgrade](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-AllowMajorVersionUpgrade"></a>
Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible.
This parameter must be set to `true` when specifying a value for the `EngineVersion` parameter that is a different major version than the replication instance's current version.
Type: Boolean
Required: No

 ** [ApplyImmediately](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-ApplyImmediately"></a>
Indicates whether the changes should be applied immediately or during the next maintenance window.
Type: Boolean
Required: No

 ** [AutoMinorVersionUpgrade](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-AutoMinorVersionUpgrade"></a>
A value that indicates that minor version upgrades are applied automatically to the replication instance during the maintenance window. Changing this parameter doesn't result in an outage, except in the case described following. The change is asynchronously applied as soon as possible.
An outage does result if these factors apply:
+ This parameter is set to `true` during the maintenance window.
+ A newer minor version is available.
+  AWS DMS has enabled automatic patching for the given engine version.
Type: Boolean
Required: No

 ** [EngineVersion](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-EngineVersion"></a>
The engine version number of the replication instance.
When modifying a major engine version of an instance, also set `AllowMajorVersionUpgrade` to `true`.
Type: String
Required: No

 ** [KerberosAuthenticationSettings](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-KerberosAuthenticationSettings"></a>
Specifies the settings required for kerberos authentication when modifying a replication instance.
Type: [KerberosAuthenticationSettings](API_KerberosAuthenticationSettings.md) object
Required: No

 ** [MultiAZ](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-MultiAZ"></a>
 Specifies whether the replication instance is a Multi-AZ deployment. You can't set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to `true`.
Type: Boolean
Required: No

 ** [NetworkType](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-NetworkType"></a>
The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.
Type: String
Required: No

 ** [PreferredMaintenanceWindow](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-PreferredMaintenanceWindow"></a>
The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter does not result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.
Default: Uses existing setting
Format: ddd:hh24:mi-ddd:hh24:mi
Valid Days: Mon \| Tue \| Wed \| Thu \| Fri \| Sat \| Sun
Constraints: Must be at least 30 minutes
Type: String
Required: No

 ** [ReplicationInstanceArn](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the replication instance.
Type: String
Required: Yes

 ** [ReplicationInstanceClass](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-ReplicationInstanceClass"></a>
The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to `"dms.c4.large"`.
For more information on the settings and capacities for the available replication instance classes, see [ Selecting the right AWS DMS replication instance for your migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth).
Type: String
Length Constraints: Maximum length of 30.
Required: No

 ** [ReplicationInstanceIdentifier](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-ReplicationInstanceIdentifier"></a>
The replication instance identifier. This parameter is stored as a lowercase string.
Type: String
Required: No

 ** [VpcSecurityGroupIds](#API_ModifyReplicationInstance_RequestSyntax) **   <a name="DMS-ModifyReplicationInstance-request-VpcSecurityGroupIds"></a>
 Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_ModifyReplicationInstance_ResponseSyntax"></a>

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
<a name="API_ModifyReplicationInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationInstance](#API_ModifyReplicationInstance_ResponseSyntax) **   <a name="DMS-ModifyReplicationInstance-response-ReplicationInstance"></a>
The modified replication instance.
Type: [ReplicationInstance](API_ReplicationInstance.md) object

## Errors
<a name="API_ModifyReplicationInstance_Errors"></a>

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

 ** ResourceAlreadyExistsFault **
The resource you are attempting to create already exists.
 ** message **

 ** resourceArn **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** StorageQuotaExceededFault **
The storage quota has been exceeded.
 ** message **

HTTP Status Code: 400

 ** UpgradeDependencyFailureFault **
An upgrade dependency is preventing the database migration.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ModifyReplicationInstance_Examples"></a>

### Example
<a name="API_ModifyReplicationInstance_Example_1"></a>

This example illustrates one usage of ModifyReplicationInstance.

#### Sample Request
<a name="API_ModifyReplicationInstance_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.ModifyReplicationInstance
{
   "ReplicationInstanceArn":"arn:aws:dms:us-east-
1:123456789012:rep:PWEBBEUNOLU7VEB2OHTEH4I4GQ",
   "AllocatedStorage":0,
   "NetworkType":"IPv4",
   "ApplyImmediately":true,
   "ReplicationInstanceClass":"dms.t3.small",
   "PreferredMaintenanceWindow":"",
   "EngineVersion":"",
   "AllowMajorVersionUpgrade":true,
   "AutoMinorVersionUpgrade":true,
   "ReplicationInstanceIdentifier":""
}
```

#### Sample Response
<a name="API_ModifyReplicationInstance_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationInstance":{
      "AvailabilityZone":"us-east-1c",
      "ReplicationInstancePrivateIpAddress":"172.31.6.45",
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
      "ReplicationInstanceStatus":"available",
      "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:key/4dc17316-5543-
4ded-b1e3-d53a7cfb411d",
      "InstanceCreateTime":1457645140.38,
      "ReplicationInstancePublicIpAddress":"52.87.66.36",
      "AllocatedStorage":5,
      "EngineVersion":"1.5.0",
      "ReplicationInstanceIdentifier":"test-rep-1",
      "PubliclyAccessible":true,
      "PreferredMaintenanceWindow":"sun:06:00-sun:14:00",
      "PendingModifiedValues":{
         "ReplicationInstanceClass":"dms.t2.small"
      }
   }
}
```

## See Also
<a name="API_ModifyReplicationInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ModifyReplicationInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ModifyReplicationInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ModifyReplicationInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ModifyReplicationInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ModifyReplicationInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ModifyReplicationInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ModifyReplicationInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ModifyReplicationInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ModifyReplicationInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ModifyReplicationInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
