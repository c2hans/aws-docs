---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetProjects.html
---

# BatchGetProjects
<a name="API_BatchGetProjects"></a>

Gets information about one or more build projects.

## Request Syntax
<a name="API_BatchGetProjects_RequestSyntax"></a>

```
{
   "names": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetProjects_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [names](#API_BatchGetProjects_RequestSyntax) **   <a name="CodeBuild-BatchGetProjects-request-names"></a>
The names or ARNs of the build projects. To get information about a project shared with your AWS account, its ARN must be specified. You cannot specify a shared project using its name.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_BatchGetProjects_ResponseSyntax"></a>

```
{
   "projects": [
      {
         "arn": "string",
         "artifacts": {
            "artifactIdentifier": "string",
            "bucketOwnerAccess": "string",
            "encryptionDisabled": boolean,
            "location": "string",
            "name": "string",
            "namespaceType": "string",
            "overrideArtifactName": boolean,
            "packaging": "string",
            "path": "string",
            "type": "string"
         },
         "autoRetryLimit": number,
         "badge": {
            "badgeEnabled": boolean,
            "badgeRequestUrl": "string"
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
         "cache": {
            "cacheNamespace": "string",
            "location": "string",
            "modes": [ "string" ],
            "type": "string"
         },
         "concurrentBuildLimit": number,
         "created": number,
         "description": "string",
         "encryptionKey": "string",
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
         "lastModified": number,
         "logsConfig": {
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
         "name": "string",
         "projectVisibility": "string",
         "publicProjectAlias": "string",
         "queuedTimeoutInMinutes": number,
         "resourceAccessRole": "string",
         "secondaryArtifacts": [
            {
               "artifactIdentifier": "string",
               "bucketOwnerAccess": "string",
               "encryptionDisabled": boolean,
               "location": "string",
               "name": "string",
               "namespaceType": "string",
               "overrideArtifactName": boolean,
               "packaging": "string",
               "path": "string",
               "type": "string"
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
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "timeoutInMinutes": number,
         "vpcConfig": {
            "securityGroupIds": [ "string" ],
            "subnets": [ "string" ],
            "vpcId": "string"
         },
         "webhook": {
            "branchFilter": "string",
            "buildType": "string",
            "filterGroups": [
               [
                  {
                     "excludeMatchedPattern": boolean,
                     "pattern": "string",
                     "type": "string"
                  }
               ]
            ],
            "lastModifiedSecret": number,
            "manualCreation": boolean,
            "payloadUrl": "string",
            "pullRequestBuildPolicy": {
               "approverRoles": [ "string" ],
               "requiresCommentApproval": "string"
            },
            "scopeConfiguration": {
               "domain": "string",
               "name": "string",
               "scope": "string"
            },
            "secret": "string",
            "status": "string",
            "statusMessage": "string",
            "url": "string"
         }
      }
   ],
   "projectsNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetProjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [projects](#API_BatchGetProjects_ResponseSyntax) **   <a name="CodeBuild-BatchGetProjects-response-projects"></a>
Information about the requested build projects.
Type: Array of [Project](API_Project.md) objects

 ** [projectsNotFound](#API_BatchGetProjects_ResponseSyntax) **   <a name="CodeBuild-BatchGetProjects-response-projectsNotFound"></a>
The names of build projects for which information could not be found.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

## Errors
<a name="API_BatchGetProjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetProjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/BatchGetProjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/BatchGetProjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BatchGetProjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/BatchGetProjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BatchGetProjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/BatchGetProjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/BatchGetProjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/BatchGetProjects)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/BatchGetProjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BatchGetProjects)
