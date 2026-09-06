---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetDeployment.html
---

# GetDeployment
<a name="API_GetDeployment"></a>

Gets a deployment. Deployments define the components that run on Greengrass core devices.

## Request Syntax
<a name="API_GetDeployment_RequestSyntax"></a>

```
GET /greengrass/v2/deployments/{{deploymentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [deploymentId](#API_GetDeployment_RequestSyntax) **   <a name="greengrassv2-GetDeployment-request-uri-deploymentId"></a>
The ID of the deployment.
Length Constraints: Minimum length of 1.
Required: Yes

## Request Body
<a name="API_GetDeployment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDeployment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "components": {
      "string" : {
         "componentVersion": "string",
         "configurationUpdate": {
            "merge": "string",
            "reset": [ "string" ]
         },
         "runWith": {
            "posixUser": "string",
            "systemResourceLimits": {
               "cpus": number,
               "memory": number
            },
            "windowsUser": "string"
         }
      }
   },
   "creationTimestamp": number,
   "deploymentId": "string",
   "deploymentName": "string",
   "deploymentPolicies": {
      "componentUpdatePolicy": {
         "action": "string",
         "timeoutInSeconds": number
      },
      "configurationValidationPolicy": {
         "timeoutInSeconds": number
      },
      "failureHandlingPolicy": "string"
   },
   "deploymentStatus": "string",
   "iotJobArn": "string",
   "iotJobConfiguration": {
      "abortConfig": {
         "criteriaList": [
            {
               "action": "string",
               "failureType": "string",
               "minNumberOfExecutedThings": number,
               "thresholdPercentage": number
            }
         ]
      },
      "jobExecutionsRolloutConfig": {
         "exponentialRate": {
            "baseRatePerMinute": number,
            "incrementFactor": number,
            "rateIncreaseCriteria": {
               "numberOfNotifiedThings": number,
               "numberOfSucceededThings": number
            }
         },
         "maximumPerMinute": number
      },
      "timeoutConfig": {
         "inProgressTimeoutInMinutes": number
      }
   },
   "iotJobId": "string",
   "isLatestForTarget": boolean,
   "parentTargetArn": "string",
   "revisionId": "string",
   "tags": {
      "string" : "string"
   },
   "targetArn": "string"
}
```

## Response Elements
<a name="API_GetDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [components](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-components"></a>
The components to deploy. This is a dictionary, where each key is the name of a component, and each key's value is the version and configuration to deploy for that component.
Type: String to [ComponentDeploymentSpecification](API_ComponentDeploymentSpecification.md) object map
Key Length Constraints: Minimum length of 1.

 ** [creationTimestamp](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-creationTimestamp"></a>
The time at which the deployment was created, expressed in ISO 8601 format.
Type: Timestamp

 ** [deploymentId](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-deploymentId"></a>
The ID of the deployment.
Type: String
Length Constraints: Minimum length of 1.

 ** [deploymentName](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-deploymentName"></a>
The name of the deployment.
Type: String

 ** [deploymentPolicies](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-deploymentPolicies"></a>
The deployment policies for the deployment. These policies define how the deployment updates components and handles failure.
Type: [DeploymentPolicies](API_DeploymentPolicies.md) object

 ** [deploymentStatus](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-deploymentStatus"></a>
The status of the deployment.
Type: String
Valid Values: `ACTIVE | COMPLETED | CANCELED | FAILED | INACTIVE`

 ** [iotJobArn](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-iotJobArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS IoT job that applies the deployment to target devices.
Type: String
Pattern: `arn:[^:]*:iot:[^:]+:[0-9]+:job/.+`

 ** [iotJobConfiguration](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-iotJobConfiguration"></a>
The job configuration for the deployment configuration. The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.
Type: [DeploymentIoTJobConfiguration](API_DeploymentIoTJobConfiguration.md) object

 ** [iotJobId](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-iotJobId"></a>
The ID of the AWS IoT job that applies the deployment to target devices.
Type: String

 ** [isLatestForTarget](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-isLatestForTarget"></a>
Whether or not the deployment is the latest revision for its target.
Type: Boolean

 ** [parentTargetArn](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-parentTargetArn"></a>
The parent deployment's target [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) within a subdeployment.
Type: String
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:(thing|thinggroup)/.+`

 ** [revisionId](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-revisionId"></a>
The revision number of the deployment.
Type: String
Length Constraints: Minimum length of 1.

 ** [tags](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-tags"></a>
A list of key-value pairs that contain metadata for the resource. For more information, see [Tag your resources](https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html) in the * AWS IoT Greengrass V2 Developer Guide*.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.

 ** [targetArn](#API_GetDeployment_ResponseSyntax) **   <a name="greengrassv2-GetDeployment-response-targetArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the target AWS IoT thing or thing group.
Type: String
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:(thing|thinggroup)/.+`

## Errors
<a name="API_GetDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
HTTP Status Code: 403

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** resourceId **
The ID of the resource that isn't found.
 ** resourceType **
The type of the resource that isn't found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.
 ** quotaCode **
The code for the quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
 ** serviceCode **
The code for the service in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** fields **
The list of fields that failed to validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_GetDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/GetDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/GetDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/GetDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/GetDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/GetDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/GetDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/GetDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/GetDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/GetDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/GetDeployment)
