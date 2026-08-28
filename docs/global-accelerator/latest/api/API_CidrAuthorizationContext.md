---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_CidrAuthorizationContext.html
---

# CidrAuthorizationContext
<a name="API_CidrAuthorizationContext"></a>

Provides authorization for Amazon to bring a specific IP address range to a specific AWS account using bring your own IP addresses (BYOIP).

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the * AWS Global Accelerator Developer Guide*.

## Contents
<a name="API_CidrAuthorizationContext_Contents"></a>

 ** Message **   <a name="globalaccelerator-Type-CidrAuthorizationContext-Message"></a>
The plain-text authorization message for the prefix and account.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** Signature **   <a name="globalaccelerator-Type-CidrAuthorizationContext-Signature"></a>
The signed authorization message for the prefix and account.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## See Also
<a name="API_CidrAuthorizationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CidrAuthorizationContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CidrAuthorizationContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CidrAuthorizationContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
