---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteProxyConfiguration.html
---

# DeleteProxyConfiguration
<a name="API_DeleteProxyConfiguration"></a>

Deletes the specified [ProxyConfiguration](API_ProxyConfiguration.md).

## Request Syntax
<a name="API_DeleteProxyConfiguration_RequestSyntax"></a>

```
{
   "ProxyConfigurationArn": "{{string}}",
   "ProxyConfigurationName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteProxyConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProxyConfigurationArn](#API_DeleteProxyConfiguration_RequestSyntax) **   <a name="networkfirewall-DeleteProxyConfiguration-request-ProxyConfigurationArn"></a>
The Amazon Resource Name (ARN) of a proxy configuration.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** [ProxyConfigurationName](#API_DeleteProxyConfiguration_RequestSyntax) **   <a name="networkfirewall-DeleteProxyConfiguration-request-ProxyConfigurationName"></a>
The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

## Response Syntax
<a name="API_DeleteProxyConfiguration_ResponseSyntax"></a>

```
{
   "ProxyConfigurationArn": "string",
   "ProxyConfigurationName": "string"
}
```

## Response Elements
<a name="API_DeleteProxyConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProxyConfigurationArn](#API_DeleteProxyConfiguration_ResponseSyntax) **   <a name="networkfirewall-DeleteProxyConfiguration-response-ProxyConfigurationArn"></a>
The Amazon Resource Name (ARN) of a proxy configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`

 ** [ProxyConfigurationName](#API_DeleteProxyConfiguration_ResponseSyntax) **   <a name="networkfirewall-DeleteProxyConfiguration-response-ProxyConfigurationName"></a>
The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`

## Errors
<a name="API_DeleteProxyConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
The operation failed because of a problem with your request. Examples include:
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Unable to locate a resource using the parameters that you provided.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

## See Also
<a name="API_DeleteProxyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DeleteProxyConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DeleteProxyConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DeleteProxyConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DeleteProxyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DeleteProxyConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DeleteProxyConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DeleteProxyConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DeleteProxyConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DeleteProxyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DeleteProxyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
