---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateRegistry.html
---

# UpdateRegistry
<a name="API_UpdateRegistry"></a>

Updates an existing registry which is used to hold a collection of schemas. The updated properties relate to the registry, and do not modify any of the schemas within the registry.

## Request Syntax
<a name="API_UpdateRegistry_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "RegistryId": {
      "RegistryArn": "{{string}}",
      "RegistryName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateRegistry_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateRegistry_RequestSyntax) **   <a name="Glue-UpdateRegistry-request-Description"></a>
A description of the registry. If description is not provided, this field will not be updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** [RegistryId](#API_UpdateRegistry_RequestSyntax) **   <a name="Glue-UpdateRegistry-request-RegistryId"></a>
This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN).
Type: [RegistryId](API_RegistryId.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateRegistry_ResponseSyntax"></a>

```
{
   "RegistryArn": "string",
   "RegistryName": "string"
}
```

## Response Elements
<a name="API_UpdateRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RegistryArn](#API_UpdateRegistry_ResponseSyntax) **   <a name="Glue-UpdateRegistry-response-RegistryArn"></a>
The Amazon Resource name (ARN) of the updated registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

 ** [RegistryName](#API_UpdateRegistry_ResponseSyntax) **   <a name="Glue-UpdateRegistry-response-RegistryName"></a>
The name of the updated registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`

## Errors
<a name="API_UpdateRegistry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRegistry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateRegistry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateRegistry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateRegistry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateRegistry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateRegistry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateRegistry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateRegistry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateRegistry)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateRegistry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateRegistry)
