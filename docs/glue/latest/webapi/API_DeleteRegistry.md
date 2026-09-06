---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DeleteRegistry.html
---

# DeleteRegistry
<a name="API_DeleteRegistry"></a>

Delete the entire registry including schema and all of its versions. To get the status of the delete operation, you can call the `GetRegistry` API after the asynchronous call. Deleting a registry will deactivate all online operations for the registry such as the `UpdateRegistry`, `CreateSchema`, `UpdateSchema`, and `RegisterSchemaVersion` APIs.

## Request Syntax
<a name="API_DeleteRegistry_RequestSyntax"></a>

```
{
   "RegistryId": {
      "RegistryArn": "{{string}}",
      "RegistryName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_DeleteRegistry_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RegistryId](#API_DeleteRegistry_RequestSyntax) **   <a name="Glue-DeleteRegistry-request-RegistryId"></a>
This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN).
Type: [RegistryId](API_RegistryId.md) object
Required: Yes

## Response Syntax
<a name="API_DeleteRegistry_ResponseSyntax"></a>

```
{
   "RegistryArn": "string",
   "RegistryName": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DeleteRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RegistryArn](#API_DeleteRegistry_ResponseSyntax) **   <a name="Glue-DeleteRegistry-response-RegistryArn"></a>
The Amazon Resource Name (ARN) of the registry being deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

 ** [RegistryName](#API_DeleteRegistry_ResponseSyntax) **   <a name="Glue-DeleteRegistry-response-RegistryName"></a>
The name of the registry being deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`

 ** [Status](#API_DeleteRegistry_ResponseSyntax) **   <a name="Glue-DeleteRegistry-response-Status"></a>
The status of the registry. A successful operation will return the `Deleting` status.
Type: String
Valid Values: `AVAILABLE | DELETING`

## Errors
<a name="API_DeleteRegistry_Errors"></a>

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

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRegistry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/DeleteRegistry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/DeleteRegistry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DeleteRegistry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/DeleteRegistry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DeleteRegistry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/DeleteRegistry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/DeleteRegistry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/DeleteRegistry)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/DeleteRegistry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DeleteRegistry)
