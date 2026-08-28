---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationConfig.html
---

# DeleteReplicationConfig
<a name="API_DeleteReplicationConfig"></a>

Deletes an AWS DMS Serverless replication configuration. This effectively deprovisions any and all replications that use this configuration. You can't delete the configuration for an AWS DMS Serverless replication that is ongoing. You can delete the configuration when the replication is in a non-RUNNING and non-STARTING state.

## Request Syntax
<a name="API_DeleteReplicationConfig_RequestSyntax"></a>

```
{
   "ReplicationConfigArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteReplicationConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplicationConfigArn](#API_DeleteReplicationConfig_RequestSyntax) **   <a name="DMS-DeleteReplicationConfig-request-ReplicationConfigArn"></a>
The replication config to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteReplicationConfig_ResponseSyntax"></a>

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
<a name="API_DeleteReplicationConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationConfig](#API_DeleteReplicationConfig_ResponseSyntax) **   <a name="DMS-DeleteReplicationConfig-response-ReplicationConfig"></a>
Configuration parameters returned for the AWS DMS Serverless replication after it is deleted.
Type: [ReplicationConfig](API_ReplicationConfig.md) object

## Errors
<a name="API_DeleteReplicationConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DeleteReplicationConfig_Examples"></a>

### Example
<a name="API_DeleteReplicationConfig_Example_1"></a>

This example illustrates one usage of DeleteReplicationConfig.

#### Sample Request
<a name="API_DeleteReplicationConfig_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DeleteReplicationConfig
{
   "ReplicationConfigArn":"arn:aws:dms:us-east-
1:123456789012:replication-config:UX6OL6MHMMJKFFOXE3H7LLJCMEKBDUG4ZV7DRSI"
}
```

#### Sample Response
<a name="API_DeleteReplicationConfig_Example_1_Response"></a>

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
<a name="API_DeleteReplicationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DeleteReplicationConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DeleteReplicationConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DeleteReplicationConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DeleteReplicationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DeleteReplicationConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DeleteReplicationConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DeleteReplicationConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DeleteReplicationConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DeleteReplicationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DeleteReplicationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
