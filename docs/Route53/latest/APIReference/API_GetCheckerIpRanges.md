---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetCheckerIpRanges.html
---

# GetCheckerIpRanges
<a name="API_GetCheckerIpRanges"></a>

Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.

**Important**
 `GetCheckerIpRanges` still works, but we recommend that you download ip-ranges.json, which includes IP address ranges for all AWS services. For more information, see [IP Address Ranges of Amazon Route 53 Servers](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-ip-addresses.html) in the *Amazon Route 53 Developer Guide*.

## Request Syntax
<a name="API_GetCheckerIpRanges_RequestSyntax"></a>

```
GET /2013-04-01/checkeripranges HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCheckerIpRanges_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetCheckerIpRanges_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCheckerIpRanges_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetCheckerIpRangesResponse>
   <CheckerIpRanges>
      <member>string</member>
   </CheckerIpRanges>
</GetCheckerIpRangesResponse>
```

## Response Elements
<a name="API_GetCheckerIpRanges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetCheckerIpRangesResponse](#API_GetCheckerIpRanges_ResponseSyntax) **   <a name="Route53-GetCheckerIpRanges-response-GetCheckerIpRangesResponse"></a>
Root level tag for the GetCheckerIpRangesResponse parameters.
Required: Yes

 ** [CheckerIpRanges](#API_GetCheckerIpRanges_ResponseSyntax) **   <a name="Route53-GetCheckerIpRanges-response-CheckerIpRanges"></a>
A complex type that contains sorted list of IP ranges in CIDR format for Amazon Route 53 health checkers.
Type: Array of strings

## Errors
<a name="API_GetCheckerIpRanges_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetCheckerIpRanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetCheckerIpRanges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetCheckerIpRanges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetCheckerIpRanges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetCheckerIpRanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetCheckerIpRanges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetCheckerIpRanges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetCheckerIpRanges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetCheckerIpRanges)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetCheckerIpRanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetCheckerIpRanges)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
