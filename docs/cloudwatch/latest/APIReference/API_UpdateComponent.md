---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponent.html
---

# UpdateComponent
<a name="API_UpdateComponent"></a>

Updates the custom component name and/or the list of resources that make up the component.

## Request Syntax
<a name="API_UpdateComponent_RequestSyntax"></a>

```
{
   "ComponentName": "{{string}}",
   "NewComponentName": "{{string}}",
   "ResourceGroupName": "{{string}}",
   "ResourceList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComponentName](#API_UpdateComponent_RequestSyntax) **   <a name="appinsights-UpdateComponent-request-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\d\w\-_\.+]*$`
Required: Yes

 ** [NewComponentName](#API_UpdateComponent_RequestSyntax) **   <a name="appinsights-UpdateComponent-request-NewComponentName"></a>
The new name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\d\w\-_\.+]*$`
Required: No

 ** [ResourceGroupName](#API_UpdateComponent_RequestSyntax) **   <a name="appinsights-UpdateComponent-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [ResourceList](#API_UpdateComponent_RequestSyntax) **   <a name="appinsights-UpdateComponent-request-ResourceList"></a>
The list of resource ARNs that belong to the component.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
Required: No

## Response Elements
<a name="API_UpdateComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is already created or in use.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/UpdateComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/UpdateComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/UpdateComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/UpdateComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/UpdateComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/UpdateComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/UpdateComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/UpdateComponent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/UpdateComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/UpdateComponent)
