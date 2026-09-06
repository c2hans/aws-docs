---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationConfig.html
---

# CreateReplicationConfig
<a name="API_CreateReplicationConfig"></a>

Creates a configuration that you can later provide to configure and start an AWS DMS Serverless replication. You can also provide options to validate the configuration inputs before you start the replication.

## Request Syntax
<a name="API_CreateReplicationConfig_RequestSyntax"></a>

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
   "ReplicationConfigIdentifier": "{{string}}",
   "ReplicationSettings": "{{string}}",
   "ReplicationType": "{{string}}",
   "ResourceIdentifier": "{{string}}",
   "SourceEndpointArn": "{{string}}",
   "SupplementalSettings": "{{string}}",
   "TableMappings": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetEndpointArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateReplicationConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComputeConfig](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-ComputeConfig"></a>
Configuration parameters for provisioning an AWS DMS Serverless replication.
Type: [ComputeConfig](API_ComputeConfig.md) object
Required: Yes

 ** [ReplicationConfigIdentifier](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-ReplicationConfigIdentifier"></a>
A unique identifier that you want to use to create a `ReplicationConfigArn` that is returned as part of the output from this action. You can then pass this output `ReplicationConfigArn` as the value of the `ReplicationConfigArn` option for other actions to identify both AWS DMS Serverless replications and replication configurations that you want those actions to operate on. For some actions, you can also use either this unique identifier or a corresponding ARN in action filters to identify the specific replication and replication configuration to operate on.
Type: String
Required: Yes

 ** [ReplicationSettings](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-ReplicationSettings"></a>
Optional JSON settings for AWS DMS Serverless replications that are provisioned using this replication configuration. For example, see [ Change processing tuning settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ChangeProcessingTuning.html).
Type: String
Required: No

 ** [ReplicationType](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-ReplicationType"></a>
The type of AWS DMS Serverless replication to provision using this replication configuration.
Possible values:
+  `"full-load"`
+  `"cdc"`
+  `"full-load-and-cdc"`
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: Yes

 ** [ResourceIdentifier](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-ResourceIdentifier"></a>
Optional unique value or name that you set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource. For more information, see [ Fine-grained access control using resource names and tags](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.FineGrainedAccess).
Type: String
Required: No

 ** [SourceEndpointArn](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-SourceEndpointArn"></a>
The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration.
Type: String
Required: Yes

 ** [SupplementalSettings](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-SupplementalSettings"></a>
Optional JSON settings for specifying supplemental data. For more information, see [ Specifying supplemental data for task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html).
Type: String
Required: No

 ** [TableMappings](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-TableMappings"></a>
JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration. For more information, see [ Specifying table selection and transformations rules using JSON](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.html).
Type: String
Required: Yes

 ** [Tags](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-Tags"></a>
One or more optional tags associated with resources used by the AWS DMS Serverless replication. For more information, see [ Tagging resources in AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [TargetEndpointArn](#API_CreateReplicationConfig_RequestSyntax) **   <a name="DMS-CreateReplicationConfig-request-TargetEndpointArn"></a>
The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS serverless replication configuration.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateReplicationConfig_ResponseSyntax"></a>

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
<a name="API_CreateReplicationConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationConfig](#API_CreateReplicationConfig_ResponseSyntax) **   <a name="DMS-CreateReplicationConfig-response-ReplicationConfig"></a>
Configuration parameters returned from the AWS DMS Serverless replication after it is created.
Type: [ReplicationConfig](API_ReplicationConfig.md) object

## Errors
<a name="API_CreateReplicationConfig_Errors"></a>

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
<a name="API_CreateReplicationConfig_Examples"></a>

### Example
<a name="API_CreateReplicationConfig_Example_1"></a>

This example illustrates one usage of CreateReplicationConfig.

#### Sample Request
<a name="API_CreateReplicationConfig_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.CreateReplicationConfig
{
    "ReplicationConfigIdentifier":"test-replication-config",
    "SourceEndpointArn":"arn:aws:dms:us-east-1:123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE",
    "TargetEndpointArn":"arn:aws:dms:us-east-1:123456789012:endpoint:GVBUJQXJZASXWHTWCLN2WNT57E",
    "ComputeConfig": "{\"MaxCapacityUnits\":2}",
    "ReplicationType": "full-load",
    "TableMappings":"{\n \"TableMappings\": [ \n
        {\n \"Type\": \"Include\",\n \"SourceSchema\": \"/\",
            \n \"SourceTable\": \"/ \"\n }\n ]\n
        }\n\n",
    "ReplicationTaskSettings":"",
    "Tags":[
        {
            "Key":"",
            "Value":""
        }
    ]
}
```

#### Sample Response
<a name="API_CreateReplicationConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "ReplicationConfigIdentifier":"test-replication-config",
    "ReplicationConfigArn":"arn:aws:dms:us-east-
1:123456789012:replication-config:UX6OL6MHMMJKFFOXE3H7LLJCMEKBDUG4ZV7DRSI",
    "SourceEndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE",
    "TargetEndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:GVBUJQXJZASXWHTWCLN2WNT57E",
    "ReplicationConfigCreateTime":1677683717.524,
    "TableMappings":"{\n \"TableMappings\": [ \n
        {\n \"Type\": \"Include\",\n \"SourceSchema\": \"/\",
            \n \"SourceTable\": \"/ \"\n }\n ]\n
        }\n\n",
    "ReplicationTaskSettings":"{\"TargetMetadata\":
    {
        \"TargetSchema\":\"\",\"SupportLobs\":true,\"FullLobMode\":
        true,\"LobChunkSize\":64,\"LimitedSizeLobMode\":
        false,\"LobMaxSize\":0},\"FullLoadSettings\":{
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
}
```

## See Also
<a name="API_CreateReplicationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CreateReplicationConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CreateReplicationConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CreateReplicationConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CreateReplicationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CreateReplicationConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CreateReplicationConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CreateReplicationConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CreateReplicationConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CreateReplicationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CreateReplicationConfig)
