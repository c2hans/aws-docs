---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyEndpointEncryptionMode.html
---

# ModifyEndpointEncryptionMode
<a name="API_ModifyEndpointEncryptionMode"></a>

Modifies the endpoint encryption mode that allows you to configure the specified directory between Standard TLS and FIPS 140-2 validated mode.

## Request Syntax
<a name="API_ModifyEndpointEncryptionMode_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "EndpointEncryptionMode": "{{string}}"
}
```

## Request Parameters
<a name="API_ModifyEndpointEncryptionMode_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_ModifyEndpointEncryptionMode_RequestSyntax) **   <a name="WorkSpaces-ModifyEndpointEncryptionMode-request-DirectoryId"></a>
 The identifier of the directory.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** [EndpointEncryptionMode](#API_ModifyEndpointEncryptionMode_RequestSyntax) **   <a name="WorkSpaces-ModifyEndpointEncryptionMode-request-EndpointEncryptionMode"></a>
The encryption mode used for endpoint connections when streaming to WorkSpaces Personal or WorkSpace Pools.
Type: String
Valid Values: `STANDARD_TLS | FIPS_VALIDATED`
Required: Yes

## Response Elements
<a name="API_ModifyEndpointEncryptionMode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifyEndpointEncryptionMode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** OperationNotSupportedException **
This operation is not supported.
 ** message **
The exception error message.
 ** reason **
The exception error reason.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_ModifyEndpointEncryptionMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModifyEndpointEncryptionMode)
