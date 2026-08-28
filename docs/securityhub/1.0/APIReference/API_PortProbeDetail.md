---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_PortProbeDetail.html
---

# PortProbeDetail
<a name="API_PortProbeDetail"></a>

A port scan that was part of the port probe. For each scan, PortProbeDetails provides information about the local IP address and port that were scanned, and the remote IP address that the scan originated from.

## Contents
<a name="API_PortProbeDetail_Contents"></a>

 ** LocalIpDetails **   <a name="securityhub-Type-PortProbeDetail-LocalIpDetails"></a>
Provides information about the IP address where the scanned port is located.
Type: [ActionLocalIpDetails](API_ActionLocalIpDetails.md) object
Required: No

 ** LocalPortDetails **   <a name="securityhub-Type-PortProbeDetail-LocalPortDetails"></a>
Provides information about the port that was scanned.
Type: [ActionLocalPortDetails](API_ActionLocalPortDetails.md) object
Required: No

 ** RemoteIpDetails **   <a name="securityhub-Type-PortProbeDetail-RemoteIpDetails"></a>
Provides information about the remote IP address that performed the scan.
Type: [ActionRemoteIpDetails](API_ActionRemoteIpDetails.md) object
Required: No

## See Also
<a name="API_PortProbeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/PortProbeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/PortProbeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/PortProbeDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
