---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_RangedConnectionDetails.html
---

# RangedConnectionDetails
<a name="API_RangedConnectionDetails"></a>

Ingress address of AgentEndpoint with a port range and an optional mtu.

## Contents
<a name="API_RangedConnectionDetails_Contents"></a>

 ** socketAddress **   <a name="groundstation-Type-RangedConnectionDetails-socketAddress"></a>
A ranged socket address.
Type: [RangedSocketAddress](API_RangedSocketAddress.md) object
Required: Yes

 ** mtu **   <a name="groundstation-Type-RangedConnectionDetails-mtu"></a>
Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.
Type: Integer
Valid Range: Minimum value of 1400. Maximum value of 1500.
Required: No

## See Also
<a name="API_RangedConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/RangedConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/RangedConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/RangedConnectionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
