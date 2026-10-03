---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateBrandProfileFromRegistration.html
---

# UpdateBrandProfileFromRegistration
<a name="API_UpdateBrandProfileFromRegistration"></a>

Imports or refreshes the attributes of an existing brand profile from an existing registration. This operation runs asynchronously. Use the GetJob operation to track its progress.

## Request Syntax
<a name="API_UpdateBrandProfileFromRegistration_RequestSyntax"></a>

```
POST /v1/brand-profiles/{{brandProfileId}}/update-from-registration HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "onAttributeConflict": "{{string}}",
   "registrationId": "{{string}}",
   "smartMatch": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateBrandProfileFromRegistration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [brandProfileId](#API_UpdateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileFromRegistration-request-uri-brandProfileId"></a>
The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Request Body
<a name="API_UpdateBrandProfileFromRegistration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileFromRegistration-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [onAttributeConflict](#API_UpdateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileFromRegistration-request-onAttributeConflict"></a>
Specifies how the service resolves an attribute that already exists. REPLACE overwrites the existing value with the incoming value. PRESERVE keeps the existing value.
Type: String
Valid Values: `REPLACE | PRESERVE`
Required: No

 ** [registrationId](#API_UpdateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileFromRegistration-request-registrationId"></a>
The identifier or Amazon Resource Name (ARN) of the registration to import attributes from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [smartMatch](#API_UpdateBrandProfileFromRegistration_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileFromRegistration-request-smartMatch"></a>
Specifies whether to use semantic field mapping between brand profile attributes and registration fields. The default is true. When false, the service maps fields using a fixed set of standard field types.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateBrandProfileFromRegistration_ResponseSyntax"></a>

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
<a name="API_UpdateBrandProfileFromRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [results](#API_UpdateBrandProfileFromRegistration_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileFromRegistration-response-results"></a>
The results of the operation. Each result pairs a requested item with the asynchronous job that processes it.
Type: Array of [JobResult](API_JobResult.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

## Errors
<a name="API_UpdateBrandProfileFromRegistration_Errors"></a>

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

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateBrandProfileFromRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/UpdateBrandProfileFromRegistration)
