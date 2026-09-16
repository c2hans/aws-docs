---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_CreateAppBundle.html
---

# CreateAppBundle
<a name="API_CreateAppBundle"></a>

Creates an app bundle to collect data from an application using AppFabric.

## Request Syntax
<a name="API_CreateAppBundle_RequestSyntax"></a>

```
POST /appbundles HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "customerManagedKeyIdentifier": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAppBundle_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAppBundle_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAppBundle_RequestSyntax) **   <a name="appfabric-CreateAppBundle-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [customerManagedKeyIdentifier](#API_CreateAppBundle_RequestSyntax) **   <a name="appfabric-CreateAppBundle-request-customerManagedKeyIdentifier"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key to use to encrypt the application data. If this is not specified, an AWS owned key is used for encryption.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [tags](#API_CreateAppBundle_RequestSyntax) **   <a name="appfabric-CreateAppBundle-request-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAppBundle_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "appBundle": {
      "arn": "string",
      "customerManagedKeyArn": "string"
   }
}
```

## Response Elements
<a name="API_CreateAppBundle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [appBundle](#API_CreateAppBundle_ResponseSyntax) **   <a name="appfabric-CreateAppBundle-response-appBundle"></a>
Contains information about an app bundle.
Type: [AppBundle](API_AppBundle.md) object

## Errors
<a name="API_CreateAppBundle_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
The request has created a conflict. Check the request parameters and try again.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
 ** quotaCode **
The code for the quota exceeded.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
 ** serviceCode **
The code of the service.
HTTP Status Code: 402

 ** ThrottlingException **
The request rate exceeds the limit.
 ** quotaCode **
The code for the quota exceeded.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
 ** serviceCode **
The code of the service.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
 ** fieldList **
The field list.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateAppBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appfabric-2023-05-19/CreateAppBundle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appfabric-2023-05-19/CreateAppBundle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/CreateAppBundle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appfabric-2023-05-19/CreateAppBundle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/CreateAppBundle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appfabric-2023-05-19/CreateAppBundle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appfabric-2023-05-19/CreateAppBundle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appfabric-2023-05-19/CreateAppBundle)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appfabric-2023-05-19/CreateAppBundle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/CreateAppBundle)
