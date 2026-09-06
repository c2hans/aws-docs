---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateExtendedSourceServer.html
---

# CreateExtendedSourceServer
<a name="API_CreateExtendedSourceServer"></a>

Create an extended source server in the target Account based on the source server in staging account.

## Request Syntax
<a name="API_CreateExtendedSourceServer_RequestSyntax"></a>

```
POST /CreateExtendedSourceServer HTTP/1.1
Content-type: application/json

{
   "sourceServerArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateExtendedSourceServer_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateExtendedSourceServer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sourceServerArn](#API_CreateExtendedSourceServer_RequestSyntax) **   <a name="drs-CreateExtendedSourceServer-request-sourceServerArn"></a>
This defines the ARN of the source server in staging Account based on which you want to create an extended source server.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:[0-9a-zA-Z_-]+:){3}([0-9]{12,}):source-server/(s-[0-9a-zA-Z]{17})`
Required: Yes

 ** [tags](#API_CreateExtendedSourceServer_RequestSyntax) **   <a name="drs-CreateExtendedSourceServer-request-tags"></a>
A list of tags associated with the extended source server.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateExtendedSourceServer_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateExtendedSourceServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [sourceServer](#API_CreateExtendedSourceServer_ResponseSyntax) **   <a name="drs-CreateExtendedSourceServer-response-sourceServer"></a>
Created extended source server.
Type: [SourceServer](API_SourceServer.md) object

## Errors
<a name="API_CreateExtendedSourceServer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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

 ** ServiceQuotaExceededException **
The request could not be completed because its exceeded the service quota.
 ** quotaCode **
Quota code.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
 ** serviceCode **
Service code.
HTTP Status Code: 402

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

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_CreateExtendedSourceServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/CreateExtendedSourceServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/CreateExtendedSourceServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/CreateExtendedSourceServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/CreateExtendedSourceServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/CreateExtendedSourceServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/CreateExtendedSourceServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/CreateExtendedSourceServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/CreateExtendedSourceServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/CreateExtendedSourceServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/CreateExtendedSourceServer)
