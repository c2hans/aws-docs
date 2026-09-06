---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModifySamlProperties.html
---

# ModifySamlProperties
<a name="API_ModifySamlProperties"></a>

Modifies multiple properties related to SAML 2.0 authentication, including the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.

## Request Syntax
<a name="API_ModifySamlProperties_RequestSyntax"></a>

```
{
   "PropertiesToDelete": [ "{{string}}" ],
   "ResourceId": "{{string}}",
   "SamlProperties": {
      "RelayStateParameterName": "{{string}}",
      "Status": "{{string}}",
      "UserAccessUrl": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ModifySamlProperties_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [PropertiesToDelete](#API_ModifySamlProperties_RequestSyntax) **   <a name="WorkSpaces-ModifySamlProperties-request-PropertiesToDelete"></a>
The SAML properties to delete as part of your request.
Specify one of the following options:
+  `SAML_PROPERTIES_USER_ACCESS_URL` to delete the user access URL.
+  `SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME` to delete the relay state parameter name.
Type: Array of strings
Valid Values: `SAML_PROPERTIES_USER_ACCESS_URL | SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME`
Required: No

 ** [ResourceId](#API_ModifySamlProperties_RequestSyntax) **   <a name="WorkSpaces-ModifySamlProperties-request-ResourceId"></a>
The directory identifier for which you want to configure SAML properties.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** [SamlProperties](#API_ModifySamlProperties_RequestSyntax) **   <a name="WorkSpaces-ModifySamlProperties-request-SamlProperties"></a>
The properties for configuring SAML 2.0 authentication.
Type: [SamlProperties](API_SamlProperties.md) object
Required: No

## Response Elements
<a name="API_ModifySamlProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifySamlProperties_Errors"></a>

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
<a name="API_ModifySamlProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ModifySamlProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ModifySamlProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModifySamlProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ModifySamlProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModifySamlProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ModifySamlProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ModifySamlProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ModifySamlProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ModifySamlProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModifySamlProperties)
