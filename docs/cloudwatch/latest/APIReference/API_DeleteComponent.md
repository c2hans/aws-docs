---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteComponent.html
---

# DeleteComponent
<a name="API_DeleteComponent"></a>

Ungroups a custom component. When you ungroup custom components, all applicable monitors that are set up for the component are removed and the instances revert to their standalone status.

## Request Syntax
<a name="API_DeleteComponent_RequestSyntax"></a>

```
{
   "ComponentName": "{{string}}",
   "ResourceGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComponentName](#API_DeleteComponent_RequestSyntax) **   <a name="appinsights-DeleteComponent-request-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\d\w\-_\.+]*$`
Required: Yes

 ** [ResourceGroupName](#API_DeleteComponent_RequestSyntax) **   <a name="appinsights-DeleteComponent-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

## Response Elements
<a name="API_DeleteComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/DeleteComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/DeleteComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/DeleteComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/DeleteComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/DeleteComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/DeleteComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/DeleteComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/DeleteComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/DeleteComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/DeleteComponent)
