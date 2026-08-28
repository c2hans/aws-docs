---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_StartReplication.html
---

# StartReplication
<a name="API_StartReplication"></a>

Starts replication for a stopped Source Server. This action would make the Source Server protected again and restart billing for it.

## Request Syntax
<a name="API_StartReplication_RequestSyntax"></a>

```
POST /StartReplication HTTP/1.1
Content-type: application/json

{
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartReplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartReplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sourceServerID](#API_StartReplication_RequestSyntax) **   <a name="drs-StartReplication-request-sourceServerID"></a>
The ID of the Source Server to start replication for.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_StartReplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "sourceServer": {
      "agentVersion": "string",
      "arn": "string",
      "dataReplicationInfo": {
         "dataReplicationError": {
            "error": "string",
            "rawError": "string"
         },
         "dataReplicationInitiation": {
            "nextAttemptDateTime": "string",
            "startDateTime": "string",
            "steps": [
               {
                  "name": "string",
                  "status": "string"
               }
            ]
         },
         "dataReplicationState": "string",
         "etaDateTime": "string",
         "lagDuration": "string",
         "replicatedDisks": [
            {
               "backloggedStorageBytes": number,
               "deviceName": "string",
               "replicatedStorageBytes": number,
               "rescannedStorageBytes": number,
               "totalStorageBytes": number,
               "volumeStatus": "string"
            }
         ],
         "stagingAvailabilityZone": "string",
         "stagingOutpostArn": "string"
      },
      "lastLaunchResult": "string",
      "lifeCycle": {
         "addedToServiceDateTime": "string",
         "elapsedReplicationDuration": "string",
         "firstByteDateTime": "string",
         "lastLaunch": {
            "initiated": {
               "apiCallDateTime": "string",
               "jobID": "string",
               "type": "string"
            },
            "status": "string"
         },
         "lastSeenByServiceDateTime": "string"
      },
      "recoveryInstanceId": "string",
      "replicationDirection": "string",
      "reversedDirectionSourceServerArn": "string",
      "sourceCloudProperties": {
         "originAccountID": "string",
         "originAvailabilityZone": "string",
         "originRegion": "string",
         "sourceOutpostArn": "string"
      },
      "sourceNetworkID": "string",
      "sourceProperties": {
         "cpus": [
            {
               "cores": number,
               "modelName": "string"
            }
         ],
         "disks": [
            {
               "bytes": number,
               "deviceName": "string"
            }
         ],
         "identificationHints": {
            "awsInstanceID": "string",
            "fqdn": "string",
            "hostname": "string",
            "vmWareUuid": "string"
         },
         "lastUpdatedDateTime": "string",
         "networkInterfaces": [
            {
               "ips": [ "string" ],
               "isPrimary": boolean,
               "macAddress": "string"
            }
         ],
         "os": {
            "fullString": "string"
         },
         "ramBytes": number,
         "recommendedInstanceType": "string",
         "supportsNitroInstances": boolean
      },
      "sourceServerID": "string",
      "stagingArea": {
         "errorMessage": "string",
         "stagingAccountID": "string",
         "stagingSourceServerArn": "string",
         "status": "string"
      },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_StartReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sourceServer](#API_StartReplication_ResponseSyntax) **   <a name="drs-StartReplication-response-sourceServer"></a>
The Source Server that this action was targeted on.
Type: [SourceServer](API_SourceServer.md) object

## Errors
<a name="API_StartReplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

## See Also
<a name="API_StartReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/StartReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/StartReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/StartReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/StartReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/StartReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/StartReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/StartReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/StartReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/StartReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/StartReplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
