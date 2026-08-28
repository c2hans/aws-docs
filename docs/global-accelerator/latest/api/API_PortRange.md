---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_PortRange.html
---

# PortRange
<a name="API_PortRange"></a>

A complex type for a range of ports for a listener.

## Contents
<a name="API_PortRange_Contents"></a>

 ** FromPort **   <a name="globalaccelerator-Type-PortRange-FromPort"></a>
The first port in the range of ports, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** ToPort **   <a name="globalaccelerator-Type-PortRange-ToPort"></a>
The last port in the range of ports, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_PortRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/PortRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/PortRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/PortRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
