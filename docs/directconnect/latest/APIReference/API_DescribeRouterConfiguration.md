---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeRouterConfiguration.html
---

# DescribeRouterConfiguration
<a name="API_DescribeRouterConfiguration"></a>

 Details about the router.

## Request Syntax
<a name="API_DescribeRouterConfiguration_RequestSyntax"></a>

```
{
   "routerTypeIdentifier": "{{string}}",
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRouterConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [routerTypeIdentifier](#API_DescribeRouterConfiguration_RequestSyntax) **   <a name="DX-DescribeRouterConfiguration-request-routerTypeIdentifier"></a>
Identifies the router by a combination of vendor, platform, and software version. For example, `CiscoSystemsInc-2900SeriesRouters-IOS124`.
Type: String
Required: No

 ** [virtualInterfaceId](#API_DescribeRouterConfiguration_RequestSyntax) **   <a name="DX-DescribeRouterConfiguration-request-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeRouterConfiguration_ResponseSyntax"></a>

```
{
   "customerRouterConfig": "string",
   "router": {
      "platform": "string",
      "routerTypeIdentifier": "string",
      "software": "string",
      "vendor": "string",
      "xsltTemplateName": "string",
      "xsltTemplateNameForMacSec": "string"
   },
   "virtualInterfaceId": "string",
   "virtualInterfaceName": "string"
}
```

## Response Elements
<a name="API_DescribeRouterConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [customerRouterConfig](#API_DescribeRouterConfiguration_ResponseSyntax) **   <a name="DX-DescribeRouterConfiguration-response-customerRouterConfig"></a>
The customer router configuration.
Type: String

 ** [router](#API_DescribeRouterConfiguration_ResponseSyntax) **   <a name="DX-DescribeRouterConfiguration-response-router"></a>
The details about the router.
Type: [RouterType](API_RouterType.md) object

 ** [virtualInterfaceId](#API_DescribeRouterConfiguration_ResponseSyntax) **   <a name="DX-DescribeRouterConfiguration-response-virtualInterfaceId"></a>
The ID assigned to the virtual interface.
Type: String

 ** [virtualInterfaceName](#API_DescribeRouterConfiguration_ResponseSyntax) **   <a name="DX-DescribeRouterConfiguration-response-virtualInterfaceName"></a>
Provides the details about a virtual interface's router.
Type: String

## Errors
<a name="API_DescribeRouterConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRouterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeRouterConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeRouterConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeRouterConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeRouterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeRouterConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeRouterConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeRouterConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeRouterConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeRouterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeRouterConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
