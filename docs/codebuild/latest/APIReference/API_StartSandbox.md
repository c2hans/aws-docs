---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartSandbox.html
---

# StartSandbox
<a name="API_StartSandbox"></a>

Starts a sandbox.

## Request Syntax
<a name="API_StartSandbox_RequestSyntax"></a>

```
{
   "idempotencyToken": "{{string}}",
   "projectName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartSandbox_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [idempotencyToken](#API_StartSandbox_RequestSyntax) **   <a name="CodeBuild-StartSandbox-request-idempotencyToken"></a>
A unique client token.
Type: String
Required: No

 ** [projectName](#API_StartSandbox_RequestSyntax) **   <a name="CodeBuild-StartSandbox-request-projectName"></a>
The AWS CodeBuild project name.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_StartSandbox_ResponseSyntax"></a>

```
{
   "sandbox": {
      "arn": "string",
      "currentSession": {
         "currentPhase": "string",
         "endTime": number,
         "id": "string",
         "logs": {
            "cloudWatchLogs": {
               "groupName": "string",
               "status": "string",
               "streamName": "string"
            },
            "cloudWatchLogsArn": "string",
            "deepLink": "string",
            "groupName": "string",
            "s3DeepLink": "string",
            "s3Logs": {
               "bucketOwnerAccess": "string",
               "encryptionDisabled": boolean,
               "location": "string",
               "status": "string"
            },
            "s3LogsArn": "string",
            "streamName": "string"
         },
         "networkInterface": {
            "networkInterfaceId": "string",
            "subnetId": "string"
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
         "resolvedSourceVersion": "string",
         "startTime": number,
         "status": "string"
      },
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
      "projectName": "string",
      "queuedTimeoutInMinutes": number,
      "requestTime": number,
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
      "status": "string",
      "timeoutInMinutes": number,
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnets": [ "string" ],
         "vpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_StartSandbox_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sandbox](#API_StartSandbox_ResponseSyntax) **   <a name="CodeBuild-StartSandbox-response-sandbox"></a>
Information about the requested sandbox.
Type: [Sandbox](API_Sandbox.md) object

## Errors
<a name="API_StartSandbox_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountSuspendedException **
The CodeBuild access has been suspended for the calling Amazon Web Services account.
HTTP Status Code: 400

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_StartSandbox_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/StartSandbox)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/StartSandbox)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/StartSandbox)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/StartSandbox)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/StartSandbox)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/StartSandbox)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/StartSandbox)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/StartSandbox)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/StartSandbox)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/StartSandbox)
