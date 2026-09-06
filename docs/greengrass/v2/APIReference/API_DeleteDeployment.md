---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeleteDeployment.html
---

# DeleteDeployment
<a name="API_DeleteDeployment"></a>

Deletes a deployment. To delete an active deployment, you must first cancel it. For more information, see [CancelDeployment](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelDeployment.html).

Deleting a deployment doesn't affect core devices that run that deployment, because core devices store the deployment's configuration on the device. Additionally, core devices can roll back to a previous deployment that has been deleted.

Deleting the AWS IoT job associated with a deployment may take time. While the job is being deleted, the status of the job will be shown as "DELETION\_IN\_PROGRESS". Only 10 jobs may have status "DELETION\_IN\_PROGRESS" at the same time. If Greengrass is unable to delete a job because of this limit, the DeleteDeployment operation will return `ThrottlingException`.

## Request Syntax
<a name="API_DeleteDeployment_RequestSyntax"></a>

```
DELETE /greengrass/v2/deployments/{{deploymentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [deploymentId](#API_DeleteDeployment_RequestSyntax) **   <a name="greengrassv2-DeleteDeployment-request-uri-deploymentId"></a>
The ID of the deployment.
Length Constraints: Minimum length of 1.
Required: Yes

## Request Body
<a name="API_DeleteDeployment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDeployment_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteDeployment_Errors"></a>

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
<a name="API_DeleteDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/DeleteDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/DeleteDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/DeleteDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/DeleteDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/DeleteDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/DeleteDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/DeleteDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/DeleteDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/DeleteDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/DeleteDeployment)
