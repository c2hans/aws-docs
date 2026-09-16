---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeSourceServers.html
---

# DescribeSourceServers
<a name="API_DescribeSourceServers"></a>

Retrieves all SourceServers or multiple SourceServers by ID.

## Request Syntax
<a name="API_DescribeSourceServers_RequestSyntax"></a>

```
POST /DescribeSourceServers HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "filters": {
      "applicationIDs": [ "{{string}}" ],
      "isArchived": {{boolean}},
      "lifeCycleStates": [ "{{string}}" ],
      "replicationTypes": [ "{{string}}" ],
      "sourceServerIDs": [ "{{string}}" ]
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

 ** [accountID](#API_DescribeSourceServers_RequestSyntax) **   <a name="mgn-DescribeSourceServers-request-accountID"></a>
Request to filter Source Servers list by Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [filters](#API_DescribeSourceServers_RequestSyntax) **   <a name="mgn-DescribeSourceServers-request-filters"></a>
Request to filter Source Servers list.
Type: [DescribeSourceServersRequestFilters](API_DescribeSourceServersRequestFilters.md) object
Required: No

 ** [maxResults](#API_DescribeSourceServers_RequestSyntax) **   <a name="mgn-DescribeSourceServers-request-maxResults"></a>
Request to filter Source Servers list by maximum results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeSourceServers_RequestSyntax) **   <a name="mgn-DescribeSourceServers-request-nextToken"></a>
Request to filter Source Servers list by next token.
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeSourceServers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeSourceServers_ResponseSyntax) **   <a name="mgn-DescribeSourceServers-response-items"></a>
The list of returned Source Servers.
Type: Array of [SourceServer](API_SourceServer.md) objects

 ** [nextToken](#API_DescribeSourceServers_ResponseSyntax) **   <a name="mgn-DescribeSourceServers-response-nextToken"></a>
The token of the next Source Server to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeSourceServers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeSourceServers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DescribeSourceServers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DescribeSourceServers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DescribeSourceServers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DescribeSourceServers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DescribeSourceServers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DescribeSourceServers)
