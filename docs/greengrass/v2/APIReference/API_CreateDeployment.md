---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateDeployment.html
---

# CreateDeployment
<a name="API_CreateDeployment"></a>

Creates a continuous deployment for a target, which is a Greengrass core device or group of core devices. When you add a new core device to a group of core devices that has a deployment, AWS IoT Greengrass deploys that group's deployment to the new device.

You can define one deployment for each target. When you create a new deployment for a target that has an existing deployment, you replace the previous deployment. AWS IoT Greengrass applies the new deployment to the target devices.

Every deployment has a revision number that indicates how many deployment revisions you define for a target. Use this operation to create a new revision of an existing deployment.

For more information, see the [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) in the * AWS IoT Greengrass V2 Developer Guide*.

## Request Syntax
<a name="API_CreateDeployment_RequestSyntax"></a>

```
POST /greengrass/v2/deployments HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "components": {
      "{{string}}" : {
         "componentVersion": "{{string}}",
         "configurationUpdate": {
            "merge": "{{string}}",
            "reset": [ "{{string}}" ]
         },
         "runWith": {
            "posixUser": "{{string}}",
            "systemResourceLimits": {
               "cpus": {{number}},
               "memory": {{number}}
            },
            "windowsUser": "{{string}}"
         }
      }
   },
   "deploymentName": "{{string}}",
   "deploymentPolicies": {
      "componentUpdatePolicy": {
         "action": "{{string}}",
         "timeoutInSeconds": {{number}}
      },
      "configurationValidationPolicy": {
         "timeoutInSeconds": {{number}}
      },
      "failureHandlingPolicy": "{{string}}"
   },
   "iotJobConfiguration": {
      "abortConfig": {
         "criteriaList": [
            {
               "action": "{{string}}",
               "failureType": "{{string}}",
               "minNumberOfExecutedThings": {{number}},
               "thresholdPercentage": {{number}}
            }
         ]
      },
      "jobExecutionsRolloutConfig": {
         "exponentialRate": {
            "baseRatePerMinute": {{number}},
            "incrementFactor": {{number}},
            "rateIncreaseCriteria": {
               "numberOfNotifiedThings": {{number}},
               "numberOfSucceededThings": {{number}}
            }
         },
         "maximumPerMinute": {{number}}
      },
      "timeoutConfig": {
         "inProgressTimeoutInMinutes": {{number}}
      }
   },
   "parentTargetArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targetArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDeployment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDeployment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDeployment_RequestSyntax) **   <a name="greengrassv2-CreateDeployment-request-clientToken"></a>
A unique, case-sensitive identifier that you can provide to ensure that the request is idempotent. Idempotency means that the request is successfully processed only once, even if you send the request multiple times. When a request succeeds, and you specify the same client token for subsequent successful requests, the AWS IoT Greengrass V2 service returns the successful response that it caches from the previous request. AWS IoT Greengrass V2 caches successful responses for idempotent requests for up to 8 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [components](#API_CreateDeployment_RequestSyntax) **   <a name="greengrassv2-CreateDeployment-request-components"></a>
The components to deploy. This is a dictionary, where each key is the name of a component, and each key's value is the version and configuration to deploy for that component.
Type: String to [ComponentDeploymentSpecification](API_ComponentDeploymentSpecification.md) object map
Key Length Constraints: Minimum length of 1.
Required: No

 ** [deploymentName](#API_CreateDeployment_RequestSyntax) **   <a name="greengrassv2-CreateDeployment-request-deploymentName"></a>
The name of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [deploymentPolicies](#API_CreateDeployment_RequestSyntax) **   <a name="greengrassv2-CreateDeployment-request-deploymentPolicies"></a>
The deployment policies for the deployment. These policies define how the deployment updates components and handles failure.
Type: [DeploymentPolicies](API_DeploymentPolicies.md) object
Required: No

 ** [iotJobConfiguration](#API_CreateDeployment_RequestSyntax) **   <a name="greengrassv2-CreateDeployment-request-iotJobConfiguration"></a>
The job configuration for the deployment configuration. The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.
Type: [DeploymentIoTJobConfiguration](API_DeploymentIoTJobConfiguration.md) object
Required: No

 ** [parentTargetArn](#API_CreateDeployment_RequestSyntax) **   <a name="greengrassv2-CreateDeployment-request-parentTargetArn"></a>
The parent deployment's target [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) within a subdeployment.
Type: String
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:thinggroup/.+`
Required: No

 ** [tags](#API_CreateDeployment_RequestSyntax) **   <a name="greengrassv2-CreateDeployment-request-tags"></a>
A list of key-value pairs that contain metadata for the resource. For more information, see [Tag your resources](https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html) in the * AWS IoT Greengrass V2 Developer Guide*.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

 ** [targetArn](#API_CreateDeployment_RequestSyntax) **   <a name="greengrassv2-CreateDeployment-request-targetArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the target AWS IoT thing or thing group. When creating a subdeployment, the targetARN can only be a thing group.
Type: String
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:(thing|thinggroup)/.+`
Required: Yes

## Response Syntax
<a name="API_CreateDeployment_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "deploymentId": "string",
   "iotJobArn": "string",
   "iotJobId": "string"
}
```

## Response Elements
<a name="API_CreateDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [deploymentId](#API_CreateDeployment_ResponseSyntax) **   <a name="greengrassv2-CreateDeployment-response-deploymentId"></a>
The ID of the deployment.
Type: String
Length Constraints: Minimum length of 1.

 ** [iotJobArn](#API_CreateDeployment_ResponseSyntax) **   <a name="greengrassv2-CreateDeployment-response-iotJobArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS IoT job that applies the deployment to target devices.
Type: String
Pattern: `arn:[^:]*:iot:[^:]+:[0-9]+:job/.+`

 ** [iotJobId](#API_CreateDeployment_ResponseSyntax) **   <a name="greengrassv2-CreateDeployment-response-iotJobId"></a>
The ID of the AWS IoT job that applies the deployment to target devices.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_CreateDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
HTTP Status Code: 403

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceId **
The ID of the resource that conflicts with the request.
 ** resourceType **
The type of the resource that conflicts with the request.
HTTP Status Code: 409

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

 ** RequestAlreadyInProgressException **
The request is already in progress. This exception occurs when you use a client token for multiple requests while AWS IoT Greengrass is still processing an earlier request that uses the same client token.
HTTP Status Code: 400

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
<a name="API_CreateDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/CreateDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/CreateDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/CreateDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/CreateDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/CreateDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/CreateDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/CreateDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/CreateDeployment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/CreateDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/CreateDeployment)
