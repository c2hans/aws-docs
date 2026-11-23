---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetAvailableModule.html
---

# GetAvailableModule

Returns a module that you can attach. If you can't attach the module, the operation returns ResourceNotFoundException, the same as for a missing one.

## Request Syntax
<a name="API_GetAvailableModule_RequestSyntax"></a>

```
GET /available-modules/{{moduleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAvailableModule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [moduleId](#API_GetAvailableModule_RequestSyntax) **   <a name="rtbfabric-GetAvailableModule-request-uri-moduleId"></a>
The module's ID.
Pattern: `module-[a-zA-Z0-9]{1,25}`
Required: Yes

## Request Body
<a name="API_GetAvailableModule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAvailableModule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "description": "string",
   "marketplaceProductId": "string",
   "moduleArn": "string",
   "moduleId": "string",
   "moduleName": "string",
   "subscriptionStatus": "string",
   "subscriptionType": "string"
}
```

## Response Elements
<a name="API_GetAvailableModule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetAvailableModule_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModule-response-createdAt"></a>
The time when the module was created.
Type: Timestamp

 ** [description](#API_GetAvailableModule_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModule-response-description"></a>
The module's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [marketplaceProductId](#API_GetAvailableModule_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModule-response-marketplaceProductId"></a>
The Marketplace product the module is sold under. Present only when subscriptionType is MARKETPLACE.
Type: String

 ** [moduleArn](#API_GetAvailableModule_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModule-response-moduleArn"></a>
The module's ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1011.
Pattern: `arn:aws[a-zA-Z-]*:rtbfabric:[a-z0-9-]+::modules/module-[a-zA-Z0-9]{1,25}`

 ** [moduleId](#API_GetAvailableModule_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModule-response-moduleId"></a>
The module's ID.
Type: String
Pattern: `module-[a-zA-Z0-9]{1,25}`

 ** [moduleName](#API_GetAvailableModule_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModule-response-moduleName"></a>
A label, not unique: modules can share a name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9-]*`

 ** [subscriptionStatus](#API_GetAvailableModule_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModule-response-subscriptionStatus"></a>
The status of your access to the module. ACTIVE for every module returned. A module that you no longer have access to isn't returned.
Type: String
Valid Values: `ACTIVE | EXPIRED`

 ** [subscriptionType](#API_GetAvailableModule_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModule-response-subscriptionType"></a>
The type of access that you have to the module.
Type: String
Valid Values: `MARKETPLACE | PRIVATE | AWS_BUILT_IN`

## Errors
<a name="API_GetAvailableModule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_GetAvailableModule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/GetAvailableModule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/GetAvailableModule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/GetAvailableModule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/GetAvailableModule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/GetAvailableModule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/GetAvailableModule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/GetAvailableModule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/GetAvailableModule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/GetAvailableModule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/GetAvailableModule)
