---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RebootReplicationInstance.html
---

# RebootReplicationInstance
<a name="API_RebootReplicationInstance"></a>

Reboots a replication instance. Rebooting results in a momentary outage, until the replication instance becomes available again.

## Request Syntax
<a name="API_RebootReplicationInstance_RequestSyntax"></a>

```
{
   "ForceFailover": {{boolean}},
   "ForcePlannedFailover": {{boolean}},
   "ReplicationInstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_RebootReplicationInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ForceFailover](#API_RebootReplicationInstance_RequestSyntax) **   <a name="DMS-RebootReplicationInstance-request-ForceFailover"></a>
If this parameter is `true`, the reboot is conducted through a Multi-AZ failover. If the instance isn't configured for Multi-AZ, then you can't specify `true`. ( `--force-planned-failover` and `--force-failover` can't both be set to `true`.)
Type: Boolean
Required: No

 ** [ForcePlannedFailover](#API_RebootReplicationInstance_RequestSyntax) **   <a name="DMS-RebootReplicationInstance-request-ForcePlannedFailover"></a>
If this parameter is `true`, the reboot is conducted through a planned Multi-AZ failover where resources are released and cleaned up prior to conducting the failover. If the instance isn''t configured for Multi-AZ, then you can't specify `true`. ( `--force-planned-failover` and `--force-failover` can't both be set to `true`.)
Type: Boolean
Required: No

 ** [ReplicationInstanceArn](#API_RebootReplicationInstance_RequestSyntax) **   <a name="DMS-RebootReplicationInstance-request-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the replication instance.
Type: String
Required: Yes

## Response Syntax
<a name="API_RebootReplicationInstance_ResponseSyntax"></a>

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
<a name="API_RebootReplicationInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationInstance](#API_RebootReplicationInstance_ResponseSyntax) **   <a name="DMS-RebootReplicationInstance-response-ReplicationInstance"></a>
The replication instance that is being rebooted.
Type: [ReplicationInstance](API_ReplicationInstance.md) object

## Errors
<a name="API_RebootReplicationInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_RebootReplicationInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/RebootReplicationInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/RebootReplicationInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RebootReplicationInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/RebootReplicationInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RebootReplicationInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/RebootReplicationInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/RebootReplicationInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/RebootReplicationInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/RebootReplicationInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RebootReplicationInstance)
