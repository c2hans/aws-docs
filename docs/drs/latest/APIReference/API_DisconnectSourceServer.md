---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DisconnectSourceServer.html
---

# DisconnectSourceServer
<a name="API_DisconnectSourceServer"></a>

Disconnects a specific Source Server from Elastic Disaster Recovery. Data replication is stopped immediately. All AWS resources created by Elastic Disaster Recovery for enabling the replication of the Source Server will be terminated / deleted within 90 minutes. You cannot disconnect a Source Server if it has a Recovery Instance. If the agent on the Source Server has not been prevented from communicating with the Elastic Disaster Recovery service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.

## Request Syntax
<a name="API_DisconnectSourceServer_RequestSyntax"></a>

```
POST /DisconnectSourceServer HTTP/1.1
Content-type: application/json

{
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisconnectSourceServer_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisconnectSourceServer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sourceServerID](#API_DisconnectSourceServer_RequestSyntax) **   <a name="drs-DisconnectSourceServer-request-sourceServerID"></a>
The ID of the Source Server to disconnect.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_DisconnectSourceServer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
      "architecture": "string",
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
```

## Response Elements
<a name="API_DisconnectSourceServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentVersion](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-agentVersion"></a>
The version of the DRS agent installed on the source server
Type: String
Pattern: `[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}(.[0-9]{4}.[0-9]{3}.[0-9]{4})?`

 ** [arn](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-arn"></a>
The ARN of the Source Server.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`

 ** [dataReplicationInfo](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-dataReplicationInfo"></a>
The Data Replication Info of the Source Server.
Type: [DataReplicationInfo](API_DataReplicationInfo.md) object

 ** [lastLaunchResult](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-lastLaunchResult"></a>
The status of the last recovery launch of this Source Server.
Type: String
Valid Values: `NOT_STARTED | PENDING | SUCCEEDED | FAILED`

 ** [lifeCycle](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-lifeCycle"></a>
The lifecycle information of this Source Server.
Type: [LifeCycle](API_LifeCycle.md) object

 ** [recoveryInstanceId](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-recoveryInstanceId"></a>
The ID of the Recovery Instance associated with this Source Server.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`

 ** [replicationDirection](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-replicationDirection"></a>
Replication direction of the Source Server.
Type: String
Valid Values: `FAILOVER | FAILBACK`

 ** [reversedDirectionSourceServerArn](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-reversedDirectionSourceServerArn"></a>
For EC2-originated Source Servers which have been failed over and then failed back, this value will mean the ARN of the Source Server on the opposite replication direction.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:[0-9a-zA-Z_-]+:){3}([0-9]{12,}):source-server/(s-[0-9a-zA-Z]{17})`

 ** [sourceCloudProperties](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-sourceCloudProperties"></a>
Source cloud properties of the Source Server.
Type: [SourceCloudProperties](API_SourceCloudProperties.md) object

 ** [sourceNetworkID](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-sourceNetworkID"></a>
ID of the Source Network which is protecting this Source Server's network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-zA-Z]{17}`

 ** [sourceProperties](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-sourceProperties"></a>
The source properties of the Source Server.
Type: [SourceProperties](API_SourceProperties.md) object

 ** [sourceServerID](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-sourceServerID"></a>
The ID of the Source Server.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`

 ** [stagingArea](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-stagingArea"></a>
The staging area of the source server.
Type: [StagingArea](API_StagingArea.md) object

 ** [tags](#API_DisconnectSourceServer_ResponseSyntax) **   <a name="drs-DisconnectSourceServer-response-tags"></a>
The tags associated with the Source Server.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_DisconnectSourceServer_Errors"></a>

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
<a name="API_DisconnectSourceServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DisconnectSourceServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DisconnectSourceServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DisconnectSourceServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DisconnectSourceServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DisconnectSourceServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DisconnectSourceServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DisconnectSourceServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DisconnectSourceServer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DisconnectSourceServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DisconnectSourceServer)
