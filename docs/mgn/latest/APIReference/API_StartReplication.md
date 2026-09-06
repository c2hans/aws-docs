---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartReplication.html
---

# StartReplication
<a name="API_StartReplication"></a>

Start replication for source server irrespective of its replication type.

## Request Syntax
<a name="API_StartReplication_RequestSyntax"></a>

```
POST /StartReplication HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartReplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartReplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_StartReplication_RequestSyntax) **   <a name="mgn-StartReplication-request-accountID"></a>
Account ID on which to start replication.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [sourceServerID](#API_StartReplication_RequestSyntax) **   <a name="mgn-StartReplication-request-sourceServerID"></a>
ID of source server on which to start replication.
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
   "applicationID": "string",
   "arn": "string",
   "connectorAction": {
      "connectorArn": "string",
      "credentialsSecretArn": "string"
   },
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
      "lastSnapshotDateTime": "string",
      "replicatedDisks": [
         {
            "backloggedStorageBytes": number,
            "deviceName": "string",
            "replicatedStorageBytes": number,
            "rescannedStorageBytes": number,
            "totalStorageBytes": number
         }
      ],
      "replicatorId": "string"
   },
   "fqdnForActionFramework": "string",
   "isArchived": boolean,
   "launchedInstance": {
      "ec2InstanceID": "string",
      "firstBoot": "string",
      "jobID": "string",
      "lastKnownChecks": [
         {
            "checkedAt": number,
            "error": "string",
            "name": "string",
            "status": "string",
            "type": "string"
         }
      ],
      "lastKnownFsxChecksStatus": "string"
   },
   "lifeCycle": {
      "addedToServiceDateTime": "string",
      "elapsedReplicationDuration": "string",
      "firstByteDateTime": "string",
      "lastCutover": {
         "finalized": {
            "apiCallDateTime": "string"
         },
         "initiated": {
            "apiCallDateTime": "string",
            "jobID": "string"
         },
         "reverted": {
            "apiCallDateTime": "string"
         }
      },
      "lastSeenByServiceDateTime": "string",
      "lastTest": {
         "finalized": {
            "apiCallDateTime": "string"
         },
         "initiated": {
            "apiCallDateTime": "string",
            "jobID": "string"
         },
         "reverted": {
            "apiCallDateTime": "string"
         }
      },
      "state": "string"
   },
   "replicationType": "string",
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
         "vmPath": "string",
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
      "recommendedInstanceType": "string"
   },
   "sourceServerID": "string",
   "tags": {
      "string" : "string"
   },
   "userProvidedID": "string",
   "vcenterClientID": "string"
}
```

## Response Elements
<a name="API_StartReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationID](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-applicationID"></a>
Source server application ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `app-[0-9a-zA-Z]{17}`

 ** [arn](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-arn"></a>
Source server ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [connectorAction](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-connectorAction"></a>
Source Server connector action.
Type: [SourceServerConnectorAction](API_SourceServerConnectorAction.md) object

 ** [dataReplicationInfo](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-dataReplicationInfo"></a>
Source server data replication info.
Type: [DataReplicationInfo](API_DataReplicationInfo.md) object

 ** [fqdnForActionFramework](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-fqdnForActionFramework"></a>
Source server fqdn for action framework.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [isArchived](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-isArchived"></a>
Source server archived status.
Type: Boolean

 ** [launchedInstance](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-launchedInstance"></a>
Source server launched instance.
Type: [LaunchedInstance](API_LaunchedInstance.md) object

 ** [lifeCycle](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-lifeCycle"></a>
Source server lifecycle state.
Type: [LifeCycle](API_LifeCycle.md) object

 ** [replicationType](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-replicationType"></a>
Source server replication type.
Type: String
Valid Values: `AGENT_BASED | SNAPSHOT_SHIPPING`

 ** [sourceProperties](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-sourceProperties"></a>
Source server properties.
Type: [SourceProperties](API_SourceProperties.md) object

 ** [sourceServerID](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-sourceServerID"></a>
Source server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`

 ** [tags](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-tags"></a>
Source server Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userProvidedID](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-userProvidedID"></a>
Source server user provided ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`

 ** [vcenterClientID](#API_StartReplication_ResponseSyntax) **   <a name="mgn-StartReplication-response-vcenterClientID"></a>
Source server vCenter client id.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `vcc-[0-9a-zA-Z]{17}`

## Errors
<a name="API_StartReplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request could not be completed because it exceeded the service quota.
 ** quotaCode **
Exceeded the service quota code.
 ** quotaValue **
Exceeded the service quota value.
 ** resourceId **
Exceeded the service quota resource ID.
 ** resourceType **
Exceeded the service quota resource type.
 ** serviceCode **
Exceeded the service quota service code.
HTTP Status Code: 402

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_StartReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/StartReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/StartReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/StartReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/StartReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/StartReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/StartReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/StartReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/StartReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/StartReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/StartReplication)
