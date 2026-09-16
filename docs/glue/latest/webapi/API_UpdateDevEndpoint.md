---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateDevEndpoint.html
---

# UpdateDevEndpoint
<a name="API_UpdateDevEndpoint"></a>

Updates a specified development endpoint.

## Request Syntax
<a name="API_UpdateDevEndpoint_RequestSyntax"></a>

```
{
   "AddArguments": {
      "{{string}}" : "{{string}}"
   },
   "AddPublicKeys": [ "{{string}}" ],
   "CustomLibraries": {
      "ExtraJarsS3Path": "{{string}}",
      "ExtraPythonLibsS3Path": "{{string}}"
   },
   "DeleteArguments": [ "{{string}}" ],
   "DeletePublicKeys": [ "{{string}}" ],
   "EndpointName": "{{string}}",
   "PublicKey": "{{string}}",
   "UpdateEtlLibraries": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateDevEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddArguments](#API_UpdateDevEndpoint_RequestSyntax) **   <a name="Glue-UpdateDevEndpoint-request-AddArguments"></a>
The map of arguments to add the map of arguments used to configure the `DevEndpoint`.
Valid arguments are:
+  `"--enable-glue-datacatalog": ""`
You can specify a version of Python support for development endpoints by using the `Arguments` parameter in the `CreateDevEndpoint` or `UpdateDevEndpoint` APIs. If no arguments are provided, the version defaults to Python 2.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [AddPublicKeys](#API_UpdateDevEndpoint_RequestSyntax) **   <a name="Glue-UpdateDevEndpoint-request-AddPublicKeys"></a>
The list of public keys for the `DevEndpoint` to use.
Type: Array of strings
Array Members: Maximum number of 5 items.
Required: No

 ** [CustomLibraries](#API_UpdateDevEndpoint_RequestSyntax) **   <a name="Glue-UpdateDevEndpoint-request-CustomLibraries"></a>
Custom Python or Java libraries to be loaded in the `DevEndpoint`.
Type: [DevEndpointCustomLibraries](API_DevEndpointCustomLibraries.md) object
Required: No

 ** [DeleteArguments](#API_UpdateDevEndpoint_RequestSyntax) **   <a name="Glue-UpdateDevEndpoint-request-DeleteArguments"></a>
The list of argument keys to be deleted from the map of arguments used to configure the `DevEndpoint`.
Type: Array of strings
Required: No

 ** [DeletePublicKeys](#API_UpdateDevEndpoint_RequestSyntax) **   <a name="Glue-UpdateDevEndpoint-request-DeletePublicKeys"></a>
The list of public keys to be deleted from the `DevEndpoint`.
Type: Array of strings
Array Members: Maximum number of 5 items.
Required: No

 ** [EndpointName](#API_UpdateDevEndpoint_RequestSyntax) **   <a name="Glue-UpdateDevEndpoint-request-EndpointName"></a>
The name of the `DevEndpoint` to be updated.
Type: String
Required: Yes

 ** [PublicKey](#API_UpdateDevEndpoint_RequestSyntax) **   <a name="Glue-UpdateDevEndpoint-request-PublicKey"></a>
The public key for the `DevEndpoint` to use.
Type: String
Required: No

 ** [UpdateEtlLibraries](#API_UpdateDevEndpoint_RequestSyntax) **   <a name="Glue-UpdateDevEndpoint-request-UpdateEtlLibraries"></a>
 `True` if the list of custom libraries to be loaded in the development endpoint needs to be updated, or `False` if otherwise.
Type: Boolean
Required: No

## Response Elements
<a name="API_UpdateDevEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDevEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDevEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateDevEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateDevEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateDevEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateDevEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateDevEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateDevEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateDevEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateDevEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateDevEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateDevEndpoint)
