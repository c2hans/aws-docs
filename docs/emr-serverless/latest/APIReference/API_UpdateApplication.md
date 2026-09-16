---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

Updates a specified application. An application has to be in a stopped or created state in order to be updated.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
PATCH /applications/{{applicationId}} HTTP/1.1
Content-type: application/json

{
   "architecture": "{{string}}",
   "autoStartConfiguration": {
      "enabled": {{boolean}}
   },
   "autoStopConfiguration": {
      "enabled": {{boolean}},
      "idleTimeoutMinutes": {{number}}
   },
   "clientToken": "{{string}}",
   "diskEncryptionConfiguration": {
      "encryptionContext": {
         "{{string}}" : "{{string}}"
      },
      "encryptionKeyArn": "{{string}}"
   },
   "identityCenterConfiguration": {
      "identityCenterInstanceArn": "{{string}}",
      "userBackgroundSessionsEnabled": {{boolean}}
   },
   "imageConfiguration": {
      "applicationLevelDigestResolution": {{boolean}},
      "imageUri": "{{string}}"
   },
   "initialCapacity": {
      "{{string}}" : {
         "workerConfiguration": {
            "cpu": "{{string}}",
            "disk": "{{string}}",
            "diskType": "{{string}}",
            "memory": "{{string}}"
         },
         "workerCount": {{number}}
      }
   },
   "interactiveConfiguration": {
      "livyEndpointEnabled": {{boolean}},
      "sessionEnabled": {{boolean}},
      "studioEnabled": {{boolean}}
   },
   "jobLevelCostAllocationConfiguration": {
      "enabled": {{boolean}}
   },
   "maximumCapacity": {
      "cpu": "{{string}}",
      "disk": "{{string}}",
      "memory": "{{string}}"
   },
   "monitoringConfiguration": {
      "cloudWatchLoggingConfiguration": {
         "enabled": {{boolean}},
         "encryptionKeyArn": "{{string}}",
         "logGroupName": "{{string}}",
         "logStreamNamePrefix": "{{string}}",
         "logTypes": {
            "{{string}}" : [ "{{string}}" ]
         }
      },
      "managedPersistenceMonitoringConfiguration": {
         "enabled": {{boolean}},
         "encryptionKeyArn": "{{string}}"
      },
      "prometheusMonitoringConfiguration": {
         "remoteWriteUrl": "{{string}}"
      },
      "s3MonitoringConfiguration": {
         "encryptionKeyArn": "{{string}}",
         "logUri": "{{string}}"
      }
   },
   "networkConfiguration": {
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ]
   },
   "releaseLabel": "{{string}}",
   "runtimeConfiguration": [
      {
         "classification": "{{string}}",
         "configurations": [
            "Configuration"
         ],
         "properties": {
            "{{string}}" : "{{string}}"
         }
      }
   ],
   "schedulerConfiguration": {
      "maxConcurrentRuns": {{number}},
      "queueTimeoutMinutes": {{number}}
   },
   "workerTypeSpecifications": {
      "{{string}}" : {
         "imageConfiguration": {
            "applicationLevelDigestResolution": {{boolean}},
            "imageUri": "{{string}}"
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-uri-applicationId"></a>
The ID of the application to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_UpdateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [architecture](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-architecture"></a>
The CPU architecture of an application.
Type: String
Valid Values: `ARM64 | X86_64`
Required: No

 ** [autoStartConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-autoStartConfiguration"></a>
The configuration for an application to automatically start on job submission.
Type: [AutoStartConfig](API_AutoStartConfig.md) object
Required: No

 ** [autoStopConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-autoStopConfiguration"></a>
The configuration for an application to automatically stop after a certain amount of time being idle.
Type: [AutoStopConfig](API_AutoStopConfig.md) object
Required: No

 ** [clientToken](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-clientToken"></a>
The client idempotency token of the application to update. Its value must be unique for each request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._-]+`
Required: Yes

 ** [diskEncryptionConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-diskEncryptionConfiguration"></a>
The configuration object that allows encrypting local disks.
Type: [DiskEncryptionConfiguration](API_DiskEncryptionConfiguration.md) object
Required: No

 ** [identityCenterConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-identityCenterConfiguration"></a>
Specifies the IAM Identity Center configuration used to enable or disable trusted identity propagation. When provided, this configuration determines how the application interacts with IAM Identity Center for user authentication and access control.
Type: [IdentityCenterConfigurationInput](API_IdentityCenterConfigurationInput.md) object
Required: No

 ** [imageConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-imageConfiguration"></a>
The image configuration to be used for all worker types. You can either set this parameter or `imageConfiguration` for each worker type in `WorkerTypeSpecificationInput`.
Type: [ImageConfigurationInput](API_ImageConfigurationInput.md) object
Required: No

 ** [initialCapacity](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-initialCapacity"></a>
The capacity to initialize when the application is updated.
Type: String to [InitialCapacityConfig](API_InitialCapacityConfig.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `[a-zA-Z]+[-_]*[a-zA-Z]+`
Required: No

 ** [interactiveConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-interactiveConfiguration"></a>
The interactive configuration object that contains new interactive use cases when the application is updated.
Type: [InteractiveConfiguration](API_InteractiveConfiguration.md) object
Required: No

 ** [jobLevelCostAllocationConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-jobLevelCostAllocationConfiguration"></a>
The configuration object that enables job level cost allocation.
Type: [JobLevelCostAllocationConfiguration](API_JobLevelCostAllocationConfiguration.md) object
Required: No

 ** [maximumCapacity](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-maximumCapacity"></a>
The maximum capacity to allocate when the application is updated. This is cumulative across all workers at any given point in time during the lifespan of the application. No new resources will be created once any one of the defined limits is hit.
Type: [MaximumAllowedResources](API_MaximumAllowedResources.md) object
Required: No

 ** [monitoringConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-monitoringConfiguration"></a>
The configuration setting for monitoring.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

 ** [networkConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-networkConfiguration"></a>
The network configuration for customer VPC connectivity.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [releaseLabel](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-releaseLabel"></a>
The Amazon EMR release label for the application. You can change the release label to use a different release of Amazon EMR.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/-]+`
Required: No

 ** [runtimeConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-runtimeConfiguration"></a>
The [Configuration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html) specifications to use when updating an application. Each configuration consists of a classification and properties. This configuration is applied across all the job runs submitted under the application.
Type: Array of [Configuration](API_Configuration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [schedulerConfiguration](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-schedulerConfiguration"></a>
The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.
Type: [SchedulerConfiguration](API_SchedulerConfiguration.md) object
Required: No

 ** [workerTypeSpecifications](#API_UpdateApplication_RequestSyntax) **   <a name="emrserverless-UpdateApplication-request-workerTypeSpecifications"></a>
The key-value pairs that specify worker type to `WorkerTypeSpecificationInput`. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include `Driver` and `Executor` for Spark applications and `HiveDriver` and `TezTask` for Hive applications. You can either set image details in this parameter for each worker type, or in `imageConfiguration` for all worker types.
Type: String to [WorkerTypeSpecificationInput](API_WorkerTypeSpecificationInput.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `[a-zA-Z]+[-_]*[a-zA-Z]+`
Required: No

## Response Syntax
<a name="API_UpdateApplication_ResponseSyntax"></a>

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
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [application](#API_UpdateApplication_ResponseSyntax) **   <a name="emrserverless-UpdateApplication-response-application"></a>
Information about the updated application.
Type: [Application](API_Application.md) object

## Errors
<a name="API_UpdateApplication_Errors"></a>

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
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/UpdateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/UpdateApplication)
