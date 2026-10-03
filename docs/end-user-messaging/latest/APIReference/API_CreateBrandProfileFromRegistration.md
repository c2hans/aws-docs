---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CreateBrandProfileFromRegistration.html
---

# CreateBrandProfileFromRegistration
<a name="API_CreateBrandProfileFromRegistration"></a>

Creates a brand profile and populates its attributes from an existing registration. This operation runs asynchronously. Use the GetJob operation to track its progress.

## Request Syntax
<a name="API_CreateBrandProfileFromRegistration_RequestSyntax"></a>

```
POST /v1/brand-profiles/create-from-registration HTTP/1.1
Content-type: application/json

{
   "brandProfileName": "{{string}}",
   "clientToken": "{{string}}",
   "registrationId": "{{string}}",
   "smartMatch": {{boolean}},
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateBrandProfileFromRegistration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateBrandProfileFromRegistration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [brandProfileName](#API_CreateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfileFromRegistration-request-brandProfileName"></a>
The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** [clientToken](#API_CreateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfileFromRegistration-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [registrationId](#API_CreateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfileFromRegistration-request-registrationId"></a>
The identifier or Amazon Resource Name (ARN) of the registration to populate the brand profile from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [smartMatch](#API_CreateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfileFromRegistration-request-smartMatch"></a>
Specifies whether to use semantic field mapping between brand profile attributes and registration fields. The default is true. When false, the service maps fields using a fixed set of standard field types.
Type: Boolean
Required: No

 ** [tags](#API_CreateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfileFromRegistration-request-tags"></a>
An array of key and value pair tags that are associated with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateBrandProfileFromRegistration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "results": [
      {
         "jobId": "string",
         "resourceIdentifier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateBrandProfileFromRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [results](#API_CreateBrandProfileFromRegistration_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfileFromRegistration-response-results"></a>
The results of the operation. Each result pairs a requested item with the asynchronous job that processes it.
Type: Array of [JobResult](API_JobResult.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

## Errors
<a name="API_CreateBrandProfileFromRegistration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
The identifier of the resource that the request conflicts with.
 ** resourceType **
The type of the resource that the request conflicts with.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.
 ** resourceId **
The identifier of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed a service quota for your account.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateBrandProfileFromRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/CreateBrandProfileFromRegistration)
