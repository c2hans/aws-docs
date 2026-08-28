---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeSourceServers.html
---

# DescribeSourceServers
<a name="API_DescribeSourceServers"></a>

Lists all Source Servers or multiple Source Servers filtered by ID.

## Request Syntax
<a name="API_DescribeSourceServers_RequestSyntax"></a>

```
POST /DescribeSourceServers HTTP/1.1
Content-type: application/json

{
   "filters": {
      "hardwareId": "{{string}}",
      "sourceServerIDs": [ "{{string}}" ],
      "stagingAccountIDs": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeSourceServers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeSourceServers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeSourceServers_RequestSyntax) **   <a name="drs-DescribeSourceServers-request-filters"></a>
A set of filters by which to return Source Servers.
Type: [DescribeSourceServersRequestFilters](API_DescribeSourceServersRequestFilters.md) object
Required: No

 ** [maxResults](#API_DescribeSourceServers_RequestSyntax) **   <a name="drs-DescribeSourceServers-request-maxResults"></a>
Maximum number of Source Servers to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_DescribeSourceServers_RequestSyntax) **   <a name="drs-DescribeSourceServers-request-nextToken"></a>
The token of the next Source Server to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeSourceServers_ResponseSyntax"></a>

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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeSourceServers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeSourceServers_ResponseSyntax) **   <a name="drs-DescribeSourceServers-response-items"></a>
An array of Source Servers.
Type: Array of [SourceServer](API_SourceServer.md) objects

 ** [nextToken](#API_DescribeSourceServers_ResponseSyntax) **   <a name="drs-DescribeSourceServers-response-nextToken"></a>
The token of the next Source Server to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeSourceServers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSourceServers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DescribeSourceServers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DescribeSourceServers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeSourceServers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DescribeSourceServers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeSourceServers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
