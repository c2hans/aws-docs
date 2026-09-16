---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyClientProperties.html
---

# ModifyClientProperties
<a name="API_ModifyClientProperties"></a>

Modifies the properties of the specified Amazon WorkSpaces clients.

## Request Syntax
<a name="API_ModifyClientProperties_RequestSyntax"></a>

```
{
   "ClientProperties": {
      "ClientExperiencePolicy": "{{string}}",
      "LogUploadEnabled": "{{string}}",
      "ReconnectEnabled": "{{string}}"
   },
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ModifyClientProperties_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ClientProperties](#API_ModifyClientProperties_RequestSyntax) **   <a name="WorkSpaces-ModifyClientProperties-request-ClientProperties"></a>
Information about the Amazon WorkSpaces client.
Type: [ClientProperties](API_ClientProperties.md) object
Required: Yes

 ** [ResourceId](#API_ModifyClientProperties_RequestSyntax) **   <a name="WorkSpaces-ModifyClientProperties-request-ResourceId"></a>
The resource identifiers, in the form of directory IDs.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Elements
<a name="API_ModifyClientProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifyClientProperties_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
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
<a name="API_ModifyClientProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ModifyClientProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ModifyClientProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModifyClientProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ModifyClientProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModifyClientProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ModifyClientProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ModifyClientProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ModifyClientProperties)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ModifyClientProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModifyClientProperties)
