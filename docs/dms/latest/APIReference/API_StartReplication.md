---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplication.html
---

# StartReplication
<a name="API_StartReplication"></a>

For a given AWS DMS Serverless replication configuration, AWS DMS connects to the source endpoint and collects the metadata to analyze the replication workload. Using this metadata, AWS DMS then computes and provisions the required capacity and starts replicating to the target endpoint using the server resources that AWS DMS has provisioned for the AWS DMS Serverless replication.

## Request Syntax
<a name="API_StartReplication_RequestSyntax"></a>

```
{
   "CdcStartPosition": "{{string}}",
   "CdcStartTime": {{number}},
   "CdcStopPosition": "{{string}}",
   "PremigrationAssessmentSettings": "{{string}}",
   "ReplicationConfigArn": "{{string}}",
   "StartReplicationType": "{{string}}"
}
```

## Request Parameters
<a name="API_StartReplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CdcStartPosition](#API_StartReplication_RequestSyntax) **   <a name="DMS-StartReplication-request-CdcStartPosition"></a>
Indicates when you want a change data capture (CDC) operation to start. Use either `CdcStartPosition` or `CdcStartTime` to specify when you want a CDC operation to start. Specifying both values results in an error.
The value can be in date, checkpoint, or LSN/SCN format.
Type: String
Required: No

 ** [CdcStartTime](#API_StartReplication_RequestSyntax) **   <a name="DMS-StartReplication-request-CdcStartTime"></a>
Indicates the start time for a change data capture (CDC) operation. Use either `CdcStartTime` or `CdcStartPosition` to specify when you want a CDC operation to start. Specifying both values results in an error.
Type: Timestamp
Required: No

 ** [CdcStopPosition](#API_StartReplication_RequestSyntax) **   <a name="DMS-StartReplication-request-CdcStopPosition"></a>
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Type: String
Required: No

 ** [PremigrationAssessmentSettings](#API_StartReplication_RequestSyntax) **   <a name="DMS-StartReplication-request-PremigrationAssessmentSettings"></a>
User-defined settings for the premigration assessment. The possible values are:
+  `ResultLocationFolder`: The folder within an Amazon S3 bucket where you want AWS DMS to store the results of this assessment run.
+  `ResultEncryptionMode`: The supported values are `SSE_KMS` and `SSE_S3`. If these values are not provided, then the files are not encrypted at rest. For more information, see [Creating AWS KMS keys to encrypt Amazon S3 target objects](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.KMSKeys).
+  `ResultKmsKeyArn`: The ARN of a customer KMS encryption key that you specify when you set `ResultEncryptionMode` to `SSE_KMS`.
+  `IncludeOnly`: A space-separated list of names for specific individual assessments that you want to include. These names come from the default list of individual assessments that AWS Database Migration Service supports for the associated migration.
+  `Exclude`: A space-separated list of names for specific individual assessments that you want to exclude. These names come from the default list of individual assessments that AWS Database Migration Service supports for the associated migration.
+  `FailOnAssessmentFailure`: A configurable setting you can set to `true` (the default setting) or `false`. Use this setting to to stop the replication from starting automatically if the assessment fails. This can help you evaluate the issue that is preventing the replication from running successfully.
Type: String
Required: No

 ** [ReplicationConfigArn](#API_StartReplication_RequestSyntax) **   <a name="DMS-StartReplication-request-ReplicationConfigArn"></a>
The Amazon Resource Name of the replication for which to start replication.
Type: String
Required: Yes

 ** [StartReplicationType](#API_StartReplication_RequestSyntax) **   <a name="DMS-StartReplication-request-StartReplicationType"></a>
The replication type.
When the replication type is `full-load` or `full-load-and-cdc`, the only valid value for the first run of the replication is `start-replication`. This option will start the replication.
You can also use [ReloadTables](API_ReloadTables.md) to reload specific tables that failed during replication instead of restarting the replication.
The `resume-processing` option isn't applicable for a full-load replication, because you can't resume partially loaded tables during the full load phase.
For a `full-load-and-cdc` replication, AWS DMS migrates table data, and then applies data changes that occur on the source. To load all the tables again, and start capturing source changes, use `reload-target`. Otherwise use `resume-processing`, to replicate the changes from the last stop position.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartReplication_ResponseSyntax"></a>

```
{
   "Replication": {
      "CdcStartPosition": "string",
      "CdcStartTime": number,
      "CdcStopPosition": "string",
      "FailureMessages": [ "string" ],
      "IsReadOnly": boolean,
      "PremigrationAssessmentStatuses": [
         {
            "AssessmentProgress": {
               "IndividualAssessmentCompletedCount": number,
               "IndividualAssessmentCount": number
            },
            "FailOnAssessmentFailure": boolean,
            "LastFailureMessage": "string",
            "PremigrationAssessmentRunArn": "string",
            "PremigrationAssessmentRunCreationDate": number,
            "ResultEncryptionMode": "string",
            "ResultKmsKeyArn": "string",
            "ResultLocationBucket": "string",
            "ResultLocationFolder": "string",
            "ResultStatistic": {
               "Cancelled": number,
               "Error": number,
               "Failed": number,
               "Passed": number,
               "Skipped": number,
               "Warning": number
            },
            "Status": "string"
         }
      ],
      "ProvisionData": {
         "DateNewProvisioningDataAvailable": number,
         "DateProvisioned": number,
         "IsNewProvisioningAvailable": boolean,
         "ProvisionedCapacityUnits": number,
         "ProvisionState": "string",
         "ReasonForNewProvisioningData": "string"
      },
      "RecoveryCheckpoint": "string",
      "ReplicationConfigArn": "string",
      "ReplicationConfigIdentifier": "string",
      "ReplicationCreateTime": number,
      "ReplicationDeprovisionTime": number,
      "ReplicationLastStopTime": number,
      "ReplicationStats": {
         "ElapsedTimeMillis": number,
         "FreshStartDate": number,
         "FullLoadFinishDate": number,
         "FullLoadProgressPercent": number,
         "FullLoadStartDate": number,
         "StartDate": number,
         "StopDate": number,
         "TablesErrored": number,
         "TablesLoaded": number,
         "TablesLoading": number,
         "TablesQueued": number
      },
      "ReplicationType": "string",
      "ReplicationUpdateTime": number,
      "SourceEndpointArn": "string",
      "StartReplicationType": "string",
      "Status": "string",
      "StopReason": "string",
      "TargetEndpointArn": "string"
   }
}
```

## Response Elements
<a name="API_StartReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Replication](#API_StartReplication_ResponseSyntax) **   <a name="DMS-StartReplication-response-Replication"></a>
The replication that AWS DMS started.
Type: [Replication](API_Replication.md) object

## Errors
<a name="API_StartReplication_Errors"></a>

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
<a name="API_StartReplication_Examples"></a>

### Example
<a name="API_StartReplication_Example_1"></a>

This example illustrates one usage of StartReplication.

#### Sample Request
<a name="API_StartReplication_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.StartReplication
{
   "ReplicationConfigArn":"arn:aws:dms:us-east
1:123456789012:replication-config:RALPZGYI3IUSJCBKKIRBEURKDY",
   "StartReplicationTaskType":"reload-target",
   "CdcStartTime":null
}
```

#### Sample Response
<a name="API_StartReplication_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "Replication": {
      {
         "SourceEndpointArn": "arn:aws:dms:us-west-
2:123456789012:endpoint:5OFSBLSONLVVSYQAY7IBDSMCEHD6NU4FJQ5L7XY",
         "Status": "created",
         "ReplicationConfigIdentifier": "serverless-kms-0",
         "ReplicationStats": {
            "TablesLoading": 0,
            "TablesQueued": 0,
            "TablesErrored": 0,
            "FullLoadProgressPercent": 0,
            "TablesLoaded": 0,
            "ElapsedTimeMillis": 0
         },
         "ReplicationCreateTime": 1679665872.025,
         "ReplicationConfigArn": "arn:aws:dms:us-east
1:123456789012:replication-config:RALPZGYI3IUSJCBKKIRBEURKDY",
         "ReplicationType": "full-load-and-cdc",
         "ReplicationUpdateTime": 1679665872.025,
         "ProvisionData": {
            "IsNewProvisioningAvailable": false,
            "ProvisionedCapacityUnits": 0
         },
         "TargetEndpointArn": "arn:aws:dms:us-west-
2:123456789012:endpoint:WTMG7G6X5TQ5GOQG46WGEBNMPDSH47J5JZHXUFI",
         "FailureMessages": []
      }
   }
}
```

## See Also
<a name="API_StartReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartReplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
