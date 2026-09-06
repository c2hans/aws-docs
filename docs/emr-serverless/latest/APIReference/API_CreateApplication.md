---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates an application.

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
POST /applications HTTP/1.1
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
   "name": "{{string}}",
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
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}",
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
<a name="API_CreateApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [architecture](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-architecture"></a>
The CPU architecture of an application.
Type: String
Valid Values: `ARM64 | X86_64`
Required: No

 ** [autoStartConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-autoStartConfiguration"></a>
The configuration for an application to automatically start on job submission.
Type: [AutoStartConfig](API_AutoStartConfig.md) object
Required: No

 ** [autoStopConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-autoStopConfiguration"></a>
The configuration for an application to automatically stop after a certain amount of time being idle.
Type: [AutoStopConfig](API_AutoStopConfig.md) object
Required: No

 ** [clientToken](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-clientToken"></a>
The client idempotency token of the application to create. Its value must be unique for each request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._-]+`
Required: Yes

 ** [diskEncryptionConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-diskEncryptionConfiguration"></a>
The configuration object that allows encrypting local disks.
Type: [DiskEncryptionConfiguration](API_DiskEncryptionConfiguration.md) object
Required: No

 ** [identityCenterConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-identityCenterConfiguration"></a>
The IAM Identity Center Configuration accepts the Identity Center instance parameter required to enable trusted identity propagation. This configuration allows identity propagation between integrated services and the Identity Center instance.
Type: [IdentityCenterConfigurationInput](API_IdentityCenterConfigurationInput.md) object
Required: No

 ** [imageConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-imageConfiguration"></a>
The image configuration for all worker types. You can either set this parameter or `imageConfiguration` for each worker type in `workerTypeSpecifications`.
Type: [ImageConfigurationInput](API_ImageConfigurationInput.md) object
Required: No

 ** [initialCapacity](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-initialCapacity"></a>
The capacity to initialize when the application is created.
Type: String to [InitialCapacityConfig](API_InitialCapacityConfig.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `[a-zA-Z]+[-_]*[a-zA-Z]+`
Required: No

 ** [interactiveConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-interactiveConfiguration"></a>
The interactive configuration object that enables the interactive use cases to use when running an application.
Type: [InteractiveConfiguration](API_InteractiveConfiguration.md) object
Required: No

 ** [jobLevelCostAllocationConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-jobLevelCostAllocationConfiguration"></a>
The configuration object that enables job level cost allocation.
Type: [JobLevelCostAllocationConfiguration](API_JobLevelCostAllocationConfiguration.md) object
Required: No

 ** [maximumCapacity](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-maximumCapacity"></a>
The maximum capacity to allocate when the application is created. This is cumulative across all workers at any given point in time, not just when an application is created. No new resources will be created once any one of the defined limits is hit.
Type: [MaximumAllowedResources](API_MaximumAllowedResources.md) object
Required: No

 ** [monitoringConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-monitoringConfiguration"></a>
The configuration setting for monitoring.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

 ** [name](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/#-]+`
Required: No

 ** [networkConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-networkConfiguration"></a>
The network configuration for customer VPC connectivity.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [releaseLabel](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-releaseLabel"></a>
The Amazon EMR release associated with the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/-]+`
Required: Yes

 ** [runtimeConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-runtimeConfiguration"></a>
The [Configuration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html) specifications to use when creating an application. Each configuration consists of a classification and properties. This configuration is applied to all the job runs submitted under the application.
Type: Array of [Configuration](API_Configuration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [schedulerConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-schedulerConfiguration"></a>
The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.
Type: [SchedulerConfiguration](API_SchedulerConfiguration.md) object
Required: No

 ** [tags](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-tags"></a>
The tags assigned to the application.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[A-Za-z0-9 /_.:=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 /_.:=+@-]*`
Required: No

 ** [type](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-type"></a>
The type of application you want to start, such as Spark or Hive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [workerTypeSpecifications](#API_CreateApplication_RequestSyntax) **   <a name="emrserverless-CreateApplication-request-workerTypeSpecifications"></a>
The key-value pairs that specify worker type to `WorkerTypeSpecificationInput`. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include `Driver` and `Executor` for Spark applications and `HiveDriver` and `TezTask` for Hive applications. You can either set image details in this parameter for each worker type, or in `imageConfiguration` for all worker types.
Type: String to [WorkerTypeSpecificationInput](API_WorkerTypeSpecificationInput.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `[a-zA-Z]+[-_]*[a-zA-Z]+`
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "arn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_CreateApplication_ResponseSyntax) **   <a name="emrserverless-CreateApplication-response-applicationId"></a>
The output contains the application ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [arn](#API_CreateApplication_ResponseSyntax) **   <a name="emrserverless-CreateApplication-response-arn"></a>
The output contains the ARN of the application.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+`

 ** [name](#API_CreateApplication_ResponseSyntax) **   <a name="emrserverless-CreateApplication-response-name"></a>
The output contains the name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/#-]+`

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

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
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/CreateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/CreateApplication)
