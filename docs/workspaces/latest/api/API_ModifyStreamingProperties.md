---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyStreamingProperties.html
---

# ModifyStreamingProperties
<a name="API_ModifyStreamingProperties"></a>

Modifies the specified streaming properties.

## Request Syntax
<a name="API_ModifyStreamingProperties_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "StreamingProperties": {
      "GlobalAccelerator": {
         "Mode": "{{string}}",
         "PreferredProtocol": "{{string}}"
      },
      "StorageConnectors": [
         {
            "ConnectorType": "{{string}}",
            "Status": "{{string}}"
         }
      ],
      "StreamingExperiencePreferredProtocol": "{{string}}",
      "UserSettings": [
         {
            "Action": "{{string}}",
            "MaximumLength": {{number}},
            "Permission": "{{string}}"
         }
      ]
   }
}
```

## Request Parameters
<a name="API_ModifyStreamingProperties_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceId](#API_ModifyStreamingProperties_RequestSyntax) **   <a name="WorkSpaces-ModifyStreamingProperties-request-ResourceId"></a>
The identifier of the resource.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** [StreamingProperties](#API_ModifyStreamingProperties_RequestSyntax) **   <a name="WorkSpaces-ModifyStreamingProperties-request-StreamingProperties"></a>
The streaming properties to configure.
Type: [StreamingProperties](API_StreamingProperties.md) object
Required: No

## Response Elements
<a name="API_ModifyStreamingProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifyStreamingProperties_Errors"></a>

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
<a name="API_ModifyStreamingProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ModifyStreamingProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ModifyStreamingProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModifyStreamingProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ModifyStreamingProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModifyStreamingProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ModifyStreamingProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ModifyStreamingProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ModifyStreamingProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ModifyStreamingProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModifyStreamingProperties)
