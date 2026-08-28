---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoveryInstances.html
---

# DescribeRecoveryInstances
<a name="API_DescribeRecoveryInstances"></a>

Lists all Recovery Instances or multiple Recovery Instances by ID.

## Request Syntax
<a name="API_DescribeRecoveryInstances_RequestSyntax"></a>

```
POST /DescribeRecoveryInstances HTTP/1.1
Content-type: application/json

{
   "filters": {
      "recoveryInstanceIDs": [ "{{string}}" ],
      "sourceServerIDs": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeRecoveryInstances_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeRecoveryInstances_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeRecoveryInstances_RequestSyntax) **   <a name="drs-DescribeRecoveryInstances-request-filters"></a>
A set of filters by which to return Recovery Instances.
Type: [DescribeRecoveryInstancesRequestFilters](API_DescribeRecoveryInstancesRequestFilters.md) object
Required: No

 ** [maxResults](#API_DescribeRecoveryInstances_RequestSyntax) **   <a name="drs-DescribeRecoveryInstances-request-maxResults"></a>
Maximum number of Recovery Instances to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_DescribeRecoveryInstances_RequestSyntax) **   <a name="drs-DescribeRecoveryInstances-request-nextToken"></a>
The token of the next Recovery Instance to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeRecoveryInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "agentVersion": "string",
         "arn": "string",
         "dataReplicationInfo": {
            "dataReplicationError": {
               "error": "string",
               "rawError": "string"
            },
            "dataReplicationInitiation": {
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
                  "totalStorageBytes": number
               }
            ],
            "stagingAvailabilityZone": "string",
            "stagingOutpostArn": "string"
         },
         "ec2InstanceID": "string",
         "ec2InstanceState": "string",
         "failback": {
            "agentLastSeenByServiceDateTime": "string",
            "elapsedReplicationDuration": "string",
            "failbackClientID": "string",
            "failbackClientLastSeenByServiceDateTime": "string",
            "failbackInitiationTime": "string",
            "failbackJobID": "string",
            "failbackLaunchType": "string",
            "failbackToOriginalServer": boolean,
            "firstByteDateTime": "string",
            "state": "string"
         },
         "isDrill": boolean,
         "jobID": "string",
         "originAvailabilityZone": "string",
         "originEnvironment": "string",
         "pointInTimeSnapshotDateTime": "string",
         "recoveryInstanceID": "string",
         "recoveryInstanceProperties": {
            "cpus": [
               {
                  "cores": number,
                  "modelName": "string"
               }
            ],
            "disks": [
               {
                  "bytes": number,
                  "ebsVolumeID": "string",
                  "internalDeviceName": "string"
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
            "ramBytes": number
         },
         "sourceOutpostArn": "string",
         "sourceServerID": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeRecoveryInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeRecoveryInstances_ResponseSyntax) **   <a name="drs-DescribeRecoveryInstances-response-items"></a>
An array of Recovery Instances.
Type: Array of [RecoveryInstance](API_RecoveryInstance.md) objects

 ** [nextToken](#API_DescribeRecoveryInstances_ResponseSyntax) **   <a name="drs-DescribeRecoveryInstances-response-nextToken"></a>
The token of the next Recovery Instance to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeRecoveryInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

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
<a name="API_DescribeRecoveryInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DescribeRecoveryInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DescribeRecoveryInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeRecoveryInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DescribeRecoveryInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeRecoveryInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DescribeRecoveryInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DescribeRecoveryInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DescribeRecoveryInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DescribeRecoveryInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeRecoveryInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
