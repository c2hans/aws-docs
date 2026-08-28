---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2CustomRequestHandlingDetails.html
---

# AwsWafv2CustomRequestHandlingDetails
<a name="API_AwsWafv2CustomRequestHandlingDetails"></a>

 Custom request handling behavior that inserts custom headers into a web request. AWS WAF uses custom request handling when the rule action doesn't block the request.

## Contents
<a name="API_AwsWafv2CustomRequestHandlingDetails_Contents"></a>

 ** InsertHeaders **   <a name="securityhub-Type-AwsWafv2CustomRequestHandlingDetails-InsertHeaders"></a>
 The HTTP headers to insert into the request.
Type: Array of [AwsWafv2CustomHttpHeader](API_AwsWafv2CustomHttpHeader.md) objects
Required: No

## See Also
<a name="API_AwsWafv2CustomRequestHandlingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2CustomRequestHandlingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2CustomRequestHandlingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2CustomRequestHandlingDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
