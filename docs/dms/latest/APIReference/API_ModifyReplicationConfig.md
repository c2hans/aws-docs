---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationConfig.html
---

# ModifyReplicationConfig
<a name="API_ModifyReplicationConfig"></a>

Modifies an existing AWS DMS Serverless replication configuration that you can use to start a replication. This command includes input validation and logic to check the state of any replication that uses this configuration. You can only modify a replication configuration before any replication that uses it has started. As soon as you have initially started a replication with a given configuiration, you can't modify that configuration, even if you stop it.

Other run statuses that allow you to run this command include FAILED and CREATED. A provisioning state that allows you to run this command is FAILED\_PROVISION.

## Request Syntax
<a name="API_ModifyReplicationConfig_RequestSyntax"></a>

```
{
   "ComputeConfig": {
      "AvailabilityZone": "{{string}}",
      "DnsNameServers": "{{string}}",
      "KmsKeyId": "{{string}}",
      "MaxCapacityUnits": {{number}},
      "MinCapacityUnits": {{number}},
      "MultiAZ": {{boolean}},
      "PreferredMaintenanceWindow": "{{string}}",
      "ReplicationSubnetGroupId": "{{string}}",
      "VpcSecurityGroupIds": [ "{{string}}" ]
   },
   "ReplicationConfigArn": "{{string}}",
   "ReplicationConfigIdentifier": "{{string}}",
   "ReplicationSettings": "{{string}}",
   "ReplicationType": "{{string}}",
   "SourceEndpointArn": "{{string}}",
   "SupplementalSettings": "{{string}}",
   "TableMappings": "{{string}}",
   "TargetEndpointArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ModifyReplicationConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComputeConfig](#API_ModifyReplicationConfig_RequestSyntax) **   <a name="DMS-ModifyReplicationConfig-request-ComputeConfig"></a>
Configuration parameters for provisioning an AWS DMS Serverless replication.
Type: [ComputeConfig](API_ComputeConfig.md) object
Required: No

 ** [ReplicationConfigArn](#API_ModifyReplicationConfig_RequestSyntax) **   <a name="DMS-ModifyReplicationConfig-request-ReplicationConfigArn"></a>
The Amazon Resource Name of the replication to modify.
Type: String
Required: Yes

 ** [ReplicationConfigIdentifier](#API_ModifyReplicationConfig_RequestSyntax) **   <a name="DMS-ModifyReplicationConfig-request-ReplicationConfigIdentifier"></a>
The new replication config to apply to the replication.
Type: String
Required: No

 ** [ReplicationSettings](#API_ModifyReplicationConfig_RequestSyntax) **   <a name="DMS-ModifyReplicationConfig-request-ReplicationSettings"></a>
The settings for the replication.
Type: String
Required: No

 ** [ReplicationType](#API_ModifyReplicationConfig_RequestSyntax) **   <a name="DMS-ModifyReplicationConfig-request-ReplicationType"></a>
The type of replication.
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: No

 ** [SourceEndpointArn](#API_ModifyReplicationConfig_RequestSyntax) **   <a name="DMS-ModifyReplicationConfig-request-SourceEndpointArn"></a>
The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS serverless replication configuration.
Type: String
Required: No

 ** [SupplementalSettings](#API_ModifyReplicationConfig_RequestSyntax) **   <a name="DMS-ModifyReplicationConfig-request-SupplementalSettings"></a>
Additional settings for the replication.
Type: String
Required: No

 ** [TableMappings](#API_ModifyReplicationConfig_RequestSyntax) **   <a name="DMS-ModifyReplicationConfig-request-TableMappings"></a>
Table mappings specified in the replication.
Type: String
Required: No

 ** [TargetEndpointArn](#API_ModifyReplicationConfig_RequestSyntax) **   <a name="DMS-ModifyReplicationConfig-request-TargetEndpointArn"></a>
The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS serverless replication configuration.
Type: String
Required: No

## Response Syntax
<a name="API_ModifyReplicationConfig_ResponseSyntax"></a>

```
{
   "ReplicationConfig": {
      "ComputeConfig": {
         "AvailabilityZone": "string",
         "DnsNameServers": "string",
         "KmsKeyId": "string",
         "MaxCapacityUnits": number,
         "MinCapacityUnits": number,
         "MultiAZ": boolean,
         "PreferredMaintenanceWindow": "string",
         "ReplicationSubnetGroupId": "string",
         "VpcSecurityGroupIds": [ "string" ]
      },
      "IsReadOnly": boolean,
      "ReplicationConfigArn": "string",
      "ReplicationConfigCreateTime": number,
      "ReplicationConfigIdentifier": "string",
      "ReplicationConfigUpdateTime": number,
      "ReplicationSettings": "string",
      "ReplicationType": "string",
      "SourceEndpointArn": "string",
      "SupplementalSettings": "string",
      "TableMappings": "string",
      "TargetEndpointArn": "string"
   }
}
```

## Response Elements
<a name="API_ModifyReplicationConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationConfig](#API_ModifyReplicationConfig_ResponseSyntax) **   <a name="DMS-ModifyReplicationConfig-response-ReplicationConfig"></a>
Information about the serverless replication config that was modified.
Type: [ReplicationConfig](API_ReplicationConfig.md) object

## Errors
<a name="API_ModifyReplicationConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
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

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ModifyReplicationConfig_Examples"></a>

### Example
<a name="API_ModifyReplicationConfig_Example_1"></a>

This example illustrates one usage of ModifyReplicationConfig.

#### Sample Request
<a name="API_ModifyReplicationConfig_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
 SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.ModifyReplicationConfig
{
    "ReplicationConfigIdentifier":"test-replication-config",
    "ReplicationConfigArn":"arn:aws:dms:us-east-1:123456789012:replication-config:UX6OL6MHMMJKFFOXE3H7LLJCMEKBDUG4ZV7DRSI"
}
```

#### Sample Response
<a name="API_ModifyReplicationConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "ReplicationConfig":"{
        "ReplicationConfigIdentifier":"test-replication-config",
        "ReplicationConfigArn":"arn:aws:dms:us-east-
1:123456789012:replication-config:UX6OL6MHMMJKFFOXE3H7LLJCMEKBDUG4ZV7DRSI",
        "SourceEndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE",
        "TargetEndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:GVBUJQXJZASXWHTWCLN2WNT57E",
        "ReplicationConfigCreateTime":1677683717.524,
        "TableMappings":"{\n \"TableMappings\":
            [\n
                {\n \"Type\": \"Include\",\n \"SourceSchema\": \"/\",
                    \n \"SourceTable\": \"/ \"\n
                }\n
            ]\n
        }\n\n",
        "ReplicationTaskSettings":"{\"TargetMetadata\":
            {\"TargetSchema\":\"\",\"SupportLobs\":true,\"FullLobMode\":
                true,\"LobChunkSize\":64,\"LimitedSizeLobMode\":
                false,\"LobMaxSize\":0
            },
            \"FullLoadSettings\":{
                \"FullLoadEnabled\":true,
                \"TargetTablePrepMode\":\"DROP_AND_CREATE\",
                \"CreatePkAfterFullLoad\":false,
                \"StopTaskCachedChangesApplied\":false,
                \"StopTaskCachedChangesNotApplied\":false,
                \"ResumeEnabled\":false,
                \"ResumeMinTableSize\":100000,
                \"ResumeOnlyClusteredPKTables\":true,
                \"MaxFullLoadSubTasks\":8,
                \"TransactionConsistencyTimeout\":600,
                \"CommitRate\":10000
            },
            \"Logging\":{
                \"EnableLogging\":false
            }
        }"
    }"
}
```

## See Also
<a name="API_ModifyReplicationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ModifyReplicationConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ModifyReplicationConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ModifyReplicationConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ModifyReplicationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ModifyReplicationConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ModifyReplicationConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ModifyReplicationConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ModifyReplicationConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ModifyReplicationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ModifyReplicationConfig)
