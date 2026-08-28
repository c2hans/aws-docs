---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteProxyRuleGroup.html
---

# DeleteProxyRuleGroup
<a name="API_DeleteProxyRuleGroup"></a>

Deletes the specified [ProxyRuleGroup](API_ProxyRuleGroup.md).

## Request Syntax
<a name="API_DeleteProxyRuleGroup_RequestSyntax"></a>

```
{
   "ProxyRuleGroupArn": "{{string}}",
   "ProxyRuleGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteProxyRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProxyRuleGroupArn](#API_DeleteProxyRuleGroup_RequestSyntax) **   <a name="networkfirewall-DeleteProxyRuleGroup-request-ProxyRuleGroupArn"></a>
The Amazon Resource Name (ARN) of a proxy rule group.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** [ProxyRuleGroupName](#API_DeleteProxyRuleGroup_RequestSyntax) **   <a name="networkfirewall-DeleteProxyRuleGroup-request-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

## Response Syntax
<a name="API_DeleteProxyRuleGroup_ResponseSyntax"></a>

```
{
   "ProxyRuleGroupArn": "string",
   "ProxyRuleGroupName": "string"
}
```

## Response Elements
<a name="API_DeleteProxyRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProxyRuleGroupArn](#API_DeleteProxyRuleGroup_ResponseSyntax) **   <a name="networkfirewall-DeleteProxyRuleGroup-response-ProxyRuleGroupArn"></a>
The Amazon Resource Name (ARN) of a proxy rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`

 ** [ProxyRuleGroupName](#API_DeleteProxyRuleGroup_ResponseSyntax) **   <a name="networkfirewall-DeleteProxyRuleGroup-response-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`

## Errors
<a name="API_DeleteProxyRuleGroup_Errors"></a>

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
<a name="API_DeleteProxyRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DeleteProxyRuleGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DeleteProxyRuleGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DeleteProxyRuleGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DeleteProxyRuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DeleteProxyRuleGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DeleteProxyRuleGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DeleteProxyRuleGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DeleteProxyRuleGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DeleteProxyRuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DeleteProxyRuleGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
