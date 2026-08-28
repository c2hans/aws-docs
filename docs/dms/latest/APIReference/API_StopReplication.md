---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplication.html
---

# StopReplication
<a name="API_StopReplication"></a>

For a given AWS DMS Serverless replication configuration, AWS DMS stops any and all ongoing AWS DMS Serverless replications. This command doesn't deprovision the stopped replications.

## Request Syntax
<a name="API_StopReplication_RequestSyntax"></a>

```
{
   "ReplicationConfigArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StopReplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplicationConfigArn](#API_StopReplication_RequestSyntax) **   <a name="DMS-StopReplication-request-ReplicationConfigArn"></a>
The Amazon Resource Name of the replication to stop.
Type: String
Required: Yes

## Response Syntax
<a name="API_StopReplication_ResponseSyntax"></a>

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
<a name="API_StopReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Replication](#API_StopReplication_ResponseSyntax) **   <a name="DMS-StopReplication-response-Replication"></a>
The replication that AWS DMS stopped.
Type: [Replication](API_Replication.md) object

## Errors
<a name="API_StopReplication_Errors"></a>

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
<a name="API_StopReplication_Examples"></a>

### Example
<a name="API_StopReplication_Example_1"></a>

This example illustrates one usage of StopReplication.

#### Sample Request
<a name="API_StopReplication_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.StopReplication
{
   "ReplicationConfigArn":"arn:aws:dms:us-east
1:123456789012:replication-config:RALPZGYI3IUSJCBKKIRBEURKDY"
}
```

#### Sample Response
<a name="API_StopReplication_Example_1_Response"></a>

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
<a name="API_StopReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StopReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StopReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StopReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StopReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StopReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StopReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StopReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StopReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StopReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StopReplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
