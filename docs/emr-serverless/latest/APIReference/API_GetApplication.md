---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html
---

# GetApplication
<a name="API_GetApplication"></a>

Displays detailed information about a specified application.

## Request Syntax
<a name="API_GetApplication_RequestSyntax"></a>

```
GET /applications/{{applicationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetApplication_RequestSyntax) **   <a name="emrserverless-GetApplication-request-uri-applicationId"></a>
The ID of the application that will be described.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_GetApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "application": {
      "applicationId": "string",
      "architecture": "string",
      "arn": "string",
      "autoStartConfiguration": {
         "enabled": boolean
      },
      "autoStopConfiguration": {
         "enabled": boolean,
         "idleTimeoutMinutes": number
      },
      "createdAt": number,
      "diskEncryptionConfiguration": {
         "encryptionContext": {
            "string" : "string"
         },
         "encryptionKeyArn": "string"
      },
      "identityCenterConfiguration": {
         "identityCenterApplicationArn": "string",
         "identityCenterInstanceArn": "string",
         "userBackgroundSessionsEnabled": boolean
      },
      "imageConfiguration": {
         "applicationLevelDigestResolution": boolean,
         "imageUri": "string",
         "resolvedImageDigest": "string"
      },
      "initialCapacity": {
         "string" : {
            "workerConfiguration": {
               "cpu": "string",
               "disk": "string",
               "diskType": "string",
               "memory": "string"
            },
            "workerCount": number
         }
      },
      "interactiveConfiguration": {
         "livyEndpointEnabled": boolean,
         "sessionEnabled": boolean,
         "studioEnabled": boolean
      },
      "jobLevelCostAllocationConfiguration": {
         "enabled": boolean
      },
      "maximumCapacity": {
         "cpu": "string",
         "disk": "string",
         "memory": "string"
      },
      "monitoringConfiguration": {
         "cloudWatchLoggingConfiguration": {
            "enabled": boolean,
            "encryptionKeyArn": "string",
            "logGroupName": "string",
            "logStreamNamePrefix": "string",
            "logTypes": {
               "string" : [ "string" ]
            }
         },
         "managedPersistenceMonitoringConfiguration": {
            "enabled": boolean,
            "encryptionKeyArn": "string"
         },
         "prometheusMonitoringConfiguration": {
            "remoteWriteUrl": "string"
         },
         "s3MonitoringConfiguration": {
            "encryptionKeyArn": "string",
            "logUri": "string"
         }
      },
      "name": "string",
      "networkConfiguration": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ]
      },
      "releaseLabel": "string",
      "runtimeConfiguration": [
         {
            "classification": "string",
            "configurations": [
               "Configuration"
            ],
            "properties": {
               "string" : "string"
            }
         }
      ],
      "schedulerConfiguration": {
         "maxConcurrentRuns": number,
         "queueTimeoutMinutes": number
      },
      "state": "string",
      "stateDetails": "string",
      "tags": {
         "string" : "string"
      },
      "type": "string",
      "updatedAt": number,
      "workerTypeSpecifications": {
         "string" : {
            "imageConfiguration": {
               "applicationLevelDigestResolution": boolean,
               "imageUri": "string",
               "resolvedImageDigest": "string"
            }
         }
      }
   }
}
```

## Response Elements
<a name="API_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [application](#API_GetApplication_ResponseSyntax) **   <a name="emrserverless-GetApplication-response-application"></a>
The output displays information about the specified application.
Type: [Application](API_Application.md) object

## Errors
<a name="API_GetApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/GetApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/GetApplication)
