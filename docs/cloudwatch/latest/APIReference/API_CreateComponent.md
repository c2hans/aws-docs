---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateComponent.html
---

# CreateComponent
<a name="API_CreateComponent"></a>

Creates a custom component by grouping similar standalone instances to monitor.

## Request Syntax
<a name="API_CreateComponent_RequestSyntax"></a>

```
{
   "ComponentName": "{{string}}",
   "ResourceGroupName": "{{string}}",
   "ResourceList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComponentName](#API_CreateComponent_RequestSyntax) **   <a name="appinsights-CreateComponent-request-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\d\w\-_\.+]*$`
Required: Yes

 ** [ResourceGroupName](#API_CreateComponent_RequestSyntax) **   <a name="appinsights-CreateComponent-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [ResourceList](#API_CreateComponent_RequestSyntax) **   <a name="appinsights-CreateComponent-request-ResourceList"></a>
The list of resource ARNs that belong to the component.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
Required: Yes

## Response Elements
<a name="API_CreateComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateComponent_Errors"></a>

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
<a name="API_CreateComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/CreateComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/CreateComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/CreateComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/CreateComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/CreateComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/CreateComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/CreateComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/CreateComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/CreateComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/CreateComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
