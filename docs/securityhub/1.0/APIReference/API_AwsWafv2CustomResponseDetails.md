---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2CustomResponseDetails.html
---

# AwsWafv2CustomResponseDetails
<a name="API_AwsWafv2CustomResponseDetails"></a>

 A custom response to send to the client. You can define a custom response for rule actions and default web ACL actions that are set to block.

## Contents
<a name="API_AwsWafv2CustomResponseDetails_Contents"></a>

 ** CustomResponseBodyKey **   <a name="securityhub-Type-AwsWafv2CustomResponseDetails-CustomResponseBodyKey"></a>
 References the response body that you want AWS WAF to return to the web request client. You can define a custom response for a rule action or a default web ACL action that is set to block.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResponseCode **   <a name="securityhub-Type-AwsWafv2CustomResponseDetails-ResponseCode"></a>
 The HTTP status code to return to the client. For a list of status codes that you can use in your custom responses, see [Supported status codes for custom response](https://docs.aws.amazon.com/waf/latest/developerguide/customizing-the-response-status-codes.html) in the * AWS WAF Developer Guide.*
Type: Integer
Required: No

 ** ResponseHeaders **   <a name="securityhub-Type-AwsWafv2CustomResponseDetails-ResponseHeaders"></a>
 The HTTP headers to use in the response.
Type: Array of [AwsWafv2CustomHttpHeader](API_AwsWafv2CustomHttpHeader.md) objects
Required: No

## See Also
<a name="API_AwsWafv2CustomResponseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2CustomResponseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2CustomResponseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2CustomResponseDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
