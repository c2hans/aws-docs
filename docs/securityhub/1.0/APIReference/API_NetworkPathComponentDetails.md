---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_NetworkPathComponentDetails.html
---

# NetworkPathComponentDetails
<a name="API_NetworkPathComponentDetails"></a>

Information about the destination of the next component in the network path.

## Contents
<a name="API_NetworkPathComponentDetails_Contents"></a>

 ** Address **   <a name="securityhub-Type-NetworkPathComponentDetails-Address"></a>
The IP addresses of the destination.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** PortRanges **   <a name="securityhub-Type-NetworkPathComponentDetails-PortRanges"></a>
A list of port ranges for the destination.
Type: Array of [PortRange](API_PortRange.md) objects
Required: No

## See Also
<a name="API_NetworkPathComponentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/NetworkPathComponentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/NetworkPathComponentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/NetworkPathComponentDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
