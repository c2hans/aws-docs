---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_RetryBuildBatch.html
---

# RetryBuildBatch
<a name="API_RetryBuildBatch"></a>

Restarts a failed batch build. Only batch builds that have failed can be retried.

## Request Syntax
<a name="API_RetryBuildBatch_RequestSyntax"></a>

```
{
   "id": "{{string}}",
   "idempotencyToken": "{{string}}",
   "retryType": "{{string}}"
}
```

## Request Parameters
<a name="API_RetryBuildBatch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [id](#API_RetryBuildBatch_RequestSyntax) **   <a name="CodeBuild-RetryBuildBatch-request-id"></a>
Specifies the identifier of the batch build to restart.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [idempotencyToken](#API_RetryBuildBatch_RequestSyntax) **   <a name="CodeBuild-RetryBuildBatch-request-idempotencyToken"></a>
A unique, case sensitive identifier you provide to ensure the idempotency of the `RetryBuildBatch` request. The token is included in the `RetryBuildBatch` request and is valid for five minutes. If you repeat the `RetryBuildBatch` request with the same token, but change a parameter, AWS CodeBuild returns a parameter mismatch error.
Type: String
Required: No

 ** [retryType](#API_RetryBuildBatch_RequestSyntax) **   <a name="CodeBuild-RetryBuildBatch-request-retryType"></a>
Specifies the type of retry to perform.
Type: String
Valid Values: `RETRY_ALL_BUILDS | RETRY_FAILED_BUILDS`
Required: No

## Response Syntax
<a name="API_RetryBuildBatch_ResponseSyntax"></a>

```
{
   "buildBatch": {
      "arn": "string",
      "artifacts": {
         "artifactIdentifier": "string",
         "bucketOwnerAccess": "string",
         "encryptionDisabled": boolean,
         "location": "string",
         "md5sum": "string",
         "overrideArtifactName": boolean,
         "sha256sum": "string"
      },
      "buildBatchConfig": {
         "batchReportMode": "string",
         "combineArtifacts": boolean,
         "restrictions": {
            "computeTypesAllowed": [ "string" ],
            "fleetsAllowed": [ "string" ],
            "maximumBuildsAllowed": number
         },
         "serviceRole": "string",
         "timeoutInMins": number
      },
      "buildBatchNumber": number,
      "buildBatchStatus": "string",
      "buildGroups": [
         {
            "currentBuildSummary": {
               "arn": "string",
               "buildStatus": "string",
               "primaryArtifact": {
                  "identifier": "string",
                  "location": "string",
                  "type": "string"
               },
               "requestedOn": number,
               "secondaryArtifacts": [
                  {
                     "identifier": "string",
                     "location": "string",
                     "type": "string"
                  }
               ]
            },
            "dependsOn": [ "string" ],
            "identifier": "string",
            "ignoreFailure": boolean,
            "priorBuildSummaryList": [
               {
                  "arn": "string",
                  "buildStatus": "string",
                  "primaryArtifact": {
                     "identifier": "string",
                     "location": "string",
                     "type": "string"
                  },
                  "requestedOn": number,
                  "secondaryArtifacts": [
                     {
                        "identifier": "string",
                        "location": "string",
                        "type": "string"
                     }
                  ]
               }
            ]
         }
      ],
      "buildTimeoutInMinutes": number,
      "cache": {
         "cacheNamespace": "string",
         "location": "string",
         "modes": [ "string" ],
         "type": "string"
      },
      "complete": boolean,
      "currentPhase": "string",
      "debugSessionEnabled": boolean,
      "encryptionKey": "string",
      "endTime": number,
      "environment": {
         "certificate": "string",
         "computeConfiguration": {
            "disk": number,
            "instanceType": "string",
            "machineType": "string",
            "memory": number,
            "vCpu": number
         },
         "computeType": "string",
         "dockerServer": {
            "computeType": "string",
            "securityGroupIds": [ "string" ],
            "status": {
               "message": "string",
               "status": "string"
            }
         },
         "environmentVariables": [
            {
               "name": "string",
               "type": "string",
               "value": "string"
            }
         ],
         "fleet": {
            "fleetArn": "string"
         },
         "hostKernel": "string",
         "image": "string",
         "imagePullCredentialsType": "string",
         "privilegedMode": boolean,
         "registryCredential": {
            "credential": "string",
            "credentialProvider": "string"
         },
         "type": "string"
      },
      "fileSystemLocations": [
         {
            "identifier": "string",
            "location": "string",
            "mountOptions": "string",
            "mountPoint": "string",
            "type": "string"
         }
      ],
      "id": "string",
      "initiator": "string",
      "logConfig": {
         "cloudWatchLogs": {
            "groupName": "string",
            "status": "string",
            "streamName": "string"
         },
         "s3Logs": {
            "bucketOwnerAccess": "string",
            "encryptionDisabled": boolean,
            "location": "string",
            "status": "string"
         }
      },
      "phases": [
         {
            "contexts": [
               {
                  "message": "string",
                  "statusCode": "string"
               }
            ],
            "durationInSeconds": number,
            "endTime": number,
            "phaseStatus": "string",
            "phaseType": "string",
            "startTime": number
         }
      ],
      "projectName": "string",
      "queuedTimeoutInMinutes": number,
      "reportArns": [ "string" ],
      "resolvedSourceVersion": "string",
      "secondaryArtifacts": [
         {
            "artifactIdentifier": "string",
            "bucketOwnerAccess": "string",
            "encryptionDisabled": boolean,
            "location": "string",
            "md5sum": "string",
            "overrideArtifactName": boolean,
            "sha256sum": "string"
         }
      ],
      "secondarySources": [
         {
            "auth": {
               "resource": "string",
               "type": "string"
            },
            "buildspec": "string",
            "buildStatusConfig": {
               "context": "string",
               "targetUrl": "string"
            },
            "gitCloneDepth": number,
            "gitSubmodulesConfig": {
               "fetchSubmodules": boolean
            },
            "insecureSsl": boolean,
            "location": "string",
            "reportBuildStatus": boolean,
            "sourceIdentifier": "string",
            "type": "string"
         }
      ],
      "secondarySourceVersions": [
         {
            "sourceIdentifier": "string",
            "sourceVersion": "string"
         }
      ],
      "serviceRole": "string",
      "source": {
         "auth": {
            "resource": "string",
            "type": "string"
         },
         "buildspec": "string",
         "buildStatusConfig": {
            "context": "string",
            "targetUrl": "string"
         },
         "gitCloneDepth": number,
         "gitSubmodulesConfig": {
            "fetchSubmodules": boolean
         },
         "insecureSsl": boolean,
         "location": "string",
         "reportBuildStatus": boolean,
         "sourceIdentifier": "string",
         "type": "string"
      },
      "sourceVersion": "string",
      "startTime": number,
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnets": [ "string" ],
         "vpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_RetryBuildBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [buildBatch](#API_RetryBuildBatch_ResponseSyntax) **   <a name="CodeBuild-RetryBuildBatch-response-buildBatch"></a>
Contains information about a batch build.
Type: [BuildBatch](API_BuildBatch.md) object

## Errors
<a name="API_RetryBuildBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_RetryBuildBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/RetryBuildBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/RetryBuildBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/RetryBuildBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/RetryBuildBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/RetryBuildBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/RetryBuildBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/RetryBuildBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/RetryBuildBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/RetryBuildBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/RetryBuildBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
