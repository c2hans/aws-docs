---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateComponentVersion.html
---

# CreateComponentVersion
<a name="API_CreateComponentVersion"></a>

Creates a component. Components are software that run on Greengrass core devices. After you develop and test a component on your core device, you can use this operation to upload your component to AWS IoT Greengrass. Then, you can deploy the component to other core devices.

You can use this operation to do the following:
+  **Create components from recipes**

  Create a component from a recipe, which is a file that defines the component's metadata, parameters, dependencies, lifecycle, artifacts, and platform capability. For more information, see [AWS IoT Greengrass component recipe reference](https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html) in the * AWS IoT Greengrass V2 Developer Guide*.

  To create a component from a recipe, specify `inlineRecipe` when you call this operation.
+  **Create components from Lambda functions**

  Create a component from an AWS Lambda function that runs on AWS IoT Greengrass. This creates a recipe and artifacts from the Lambda function's deployment package. You can use this operation to migrate Lambda functions from AWS IoT Greengrass V1 to AWS IoT Greengrass V2.

  This function accepts Lambda functions in all supported versions of Python, Node.js, and Java runtimes. AWS IoT Greengrass doesn't apply any additional restrictions on deprecated Lambda runtime versions.

  To create a component from a Lambda function, specify `lambdaFunction` when you call this operation.
**Note**
 AWS IoT Greengrass currently supports Lambda functions on only Linux core devices.

## Request Syntax
<a name="API_CreateComponentVersion_RequestSyntax"></a>

```
POST /greengrass/v2/createComponentVersion HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "inlineRecipe": {{blob}},
   "lambdaFunction": {
      "componentDependencies": {
         "{{string}}" : {
            "dependencyType": "{{string}}",
            "versionRequirement": "{{string}}"
         }
      },
      "componentLambdaParameters": {
         "environmentVariables": {
            "{{string}}" : "{{string}}"
         },
         "eventSources": [
            {
               "topic": "{{string}}",
               "type": "{{string}}"
            }
         ],
         "execArgs": [ "{{string}}" ],
         "inputPayloadEncodingType": "{{string}}",
         "linuxProcessParams": {
            "containerParams": {
               "devices": [
                  {
                     "addGroupOwner": {{boolean}},
                     "path": "{{string}}",
                     "permission": "{{string}}"
                  }
               ],
               "memorySizeInKB": {{number}},
               "mountROSysfs": {{boolean}},
               "volumes": [
                  {
                     "addGroupOwner": {{boolean}},
                     "destinationPath": "{{string}}",
                     "permission": "{{string}}",
                     "sourcePath": "{{string}}"
                  }
               ]
            },
            "isolationMode": "{{string}}"
         },
         "maxIdleTimeInSeconds": {{number}},
         "maxInstancesCount": {{number}},
         "maxQueueSize": {{number}},
         "pinned": {{boolean}},
         "statusTimeoutInSeconds": {{number}},
         "timeoutInSeconds": {{number}}
      },
      "componentName": "{{string}}",
      "componentPlatforms": [
         {
            "attributes": {
               "{{string}}" : "{{string}}"
            },
            "name": "{{string}}"
         }
      ],
      "componentVersion": "{{string}}",
      "lambdaArn": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateComponentVersion_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateComponentVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateComponentVersion_RequestSyntax) **   <a name="greengrassv2-CreateComponentVersion-request-clientToken"></a>
A unique, case-sensitive identifier that you can provide to ensure that the request is idempotent. Idempotency means that the request is successfully processed only once, even if you send the request multiple times. When a request succeeds, and you specify the same client token for subsequent successful requests, the AWS IoT Greengrass V2 service returns the successful response that it caches from the previous request. AWS IoT Greengrass V2 caches successful responses for idempotent requests for up to 8 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [inlineRecipe](#API_CreateComponentVersion_RequestSyntax) **   <a name="greengrassv2-CreateComponentVersion-request-inlineRecipe"></a>
The recipe to use to create the component. The recipe defines the component's metadata, parameters, dependencies, lifecycle, artifacts, and platform compatibility.
You must specify either `inlineRecipe` or `lambdaFunction`.
Type: Base64-encoded binary data object
Required: No

 ** [lambdaFunction](#API_CreateComponentVersion_RequestSyntax) **   <a name="greengrassv2-CreateComponentVersion-request-lambdaFunction"></a>
The parameters to create a component from a Lambda function.
You must specify either `inlineRecipe` or `lambdaFunction`.
Type: [LambdaFunctionRecipeSource](API_LambdaFunctionRecipeSource.md) object
Required: No

 ** [tags](#API_CreateComponentVersion_RequestSyntax) **   <a name="greengrassv2-CreateComponentVersion-request-tags"></a>
A list of key-value pairs that contain metadata for the resource. For more information, see [Tag your resources](https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html) in the * AWS IoT Greengrass V2 Developer Guide*.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateComponentVersion_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "componentName": "string",
   "componentVersion": "string",
   "creationTimestamp": number,
   "status": {
      "componentState": "string",
      "errors": {
         "string" : "string"
      },
      "message": "string",
      "vendorGuidance": "string",
      "vendorGuidanceMessage": "string"
   }
}
```

## Response Elements
<a name="API_CreateComponentVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateComponentVersion_ResponseSyntax) **   <a name="greengrassv2-CreateComponentVersion-response-arn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the component version.
Type: String
Pattern: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):components:[^:]+:versions:[^:]+`

 ** [componentName](#API_CreateComponentVersion_ResponseSyntax) **   <a name="greengrassv2-CreateComponentVersion-response-componentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [componentVersion](#API_CreateComponentVersion_ResponseSyntax) **   <a name="greengrassv2-CreateComponentVersion-response-componentVersion"></a>
The version of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [creationTimestamp](#API_CreateComponentVersion_ResponseSyntax) **   <a name="greengrassv2-CreateComponentVersion-response-creationTimestamp"></a>
The time at which the component was created, expressed in ISO 8601 format.
Type: Timestamp

 ** [status](#API_CreateComponentVersion_ResponseSyntax) **   <a name="greengrassv2-CreateComponentVersion-response-status"></a>
The status of the component version in AWS IoT Greengrass V2. This status is different from the status of the component on a core device.
Type: [CloudComponentStatus](API_CloudComponentStatus.md) object

## Errors
<a name="API_CreateComponentVersion_Errors"></a>

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

 ** ServiceQuotaExceededException **
Your request exceeds a service quota. For example, you might have the maximum number of components that you can create.
 ** quotaCode **
The code for the quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** resourceId **
The ID of the resource that exceeds the service quota.
 ** resourceType **
The type of the resource that exceeds the service quota.
 ** serviceCode **
The code for the service in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 402

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
<a name="API_CreateComponentVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/CreateComponentVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/CreateComponentVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/CreateComponentVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/CreateComponentVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/CreateComponentVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/CreateComponentVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/CreateComponentVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/CreateComponentVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/CreateComponentVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/CreateComponentVersion)
