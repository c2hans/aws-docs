---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ResolveComponentCandidates.html
---

# ResolveComponentCandidates
<a name="API_ResolveComponentCandidates"></a>

Retrieves a list of components that meet the component, version, and platform requirements of a deployment. Greengrass core devices call this operation when they receive a deployment to identify the components to install.

This operation identifies components that meet all dependency requirements for a deployment. If the requirements conflict, then this operation returns an error and the deployment fails. For example, this occurs if component `A` requires version `>2.0.0` and component `B` requires version `<2.0.0` of a component dependency.

When you specify the component candidates to resolve, AWS IoT Greengrass compares each component's digest from the core device with the component's digest in the AWS Cloud. If the digests don't match, then AWS IoT Greengrass specifies to use the version from the AWS Cloud.

**Important**
To use this operation, you must use the data plane API endpoint and authenticate with an AWS IoT device certificate. For more information, see [AWS IoT Greengrass endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/greengrass.html).

## Request Syntax
<a name="API_ResolveComponentCandidates_RequestSyntax"></a>

```
POST /greengrass/v2/resolveComponentCandidates HTTP/1.1
Content-type: application/json

{
   "componentCandidates": [
      {
         "componentName": "{{string}}",
         "componentVersion": "{{string}}",
         "versionRequirements": {
            "{{string}}" : "{{string}}"
         }
      }
   ],
   "platform": {
      "attributes": {
         "{{string}}" : "{{string}}"
      },
      "name": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ResolveComponentCandidates_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ResolveComponentCandidates_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [componentCandidates](#API_ResolveComponentCandidates_RequestSyntax) **   <a name="greengrassv2-ResolveComponentCandidates-request-componentCandidates"></a>
The list of components to resolve.
Type: Array of [ComponentCandidate](API_ComponentCandidate.md) objects
Required: No

 ** [platform](#API_ResolveComponentCandidates_RequestSyntax) **   <a name="greengrassv2-ResolveComponentCandidates-request-platform"></a>
The platform to use to resolve compatible components.
Type: [ComponentPlatform](API_ComponentPlatform.md) object
Required: No

## Response Syntax
<a name="API_ResolveComponentCandidates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "resolvedComponentVersions": [
      {
         "arn": "string",
         "componentName": "string",
         "componentVersion": "string",
         "message": "string",
         "recipe": blob,
         "vendorGuidance": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ResolveComponentCandidates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resolvedComponentVersions](#API_ResolveComponentCandidates_ResponseSyntax) **   <a name="greengrassv2-ResolveComponentCandidates-response-resolvedComponentVersions"></a>
A list of components that meet the requirements that you specify in the request. This list includes each component's recipe that you can use to install the component.
Type: Array of [ResolvedComponentVersion](API_ResolvedComponentVersion.md) objects

## Errors
<a name="API_ResolveComponentCandidates_Errors"></a>

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
<a name="API_ResolveComponentCandidates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/ResolveComponentCandidates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/ResolveComponentCandidates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ResolveComponentCandidates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/ResolveComponentCandidates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ResolveComponentCandidates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/ResolveComponentCandidates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/ResolveComponentCandidates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/ResolveComponentCandidates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ResolveComponentCandidates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ResolveComponentCandidates)
