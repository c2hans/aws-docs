---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsMskClusterClusterInfoClientAuthenticationTlsDetails.html
---

# AwsMskClusterClusterInfoClientAuthenticationTlsDetails
<a name="API_AwsMskClusterClusterInfoClientAuthenticationTlsDetails"></a>

 Provides details for client authentication using TLS.

## Contents
<a name="API_AwsMskClusterClusterInfoClientAuthenticationTlsDetails_Contents"></a>

 ** CertificateAuthorityArnList **   <a name="securityhub-Type-AwsMskClusterClusterInfoClientAuthenticationTlsDetails-CertificateAuthorityArnList"></a>
 List of AWS Private CA Amazon Resource Names (ARNs). AWS Private CA enables creation of private certificate authority (CA) hierarchies, including root and subordinate CAs, without the investment and maintenance costs of operating an on-premises CA.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Enabled **   <a name="securityhub-Type-AwsMskClusterClusterInfoClientAuthenticationTlsDetails-Enabled"></a>
 Indicates whether TLS authentication is enabled or not.
Type: Boolean
Required: No

## See Also
<a name="API_AwsMskClusterClusterInfoClientAuthenticationTlsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsMskClusterClusterInfoClientAuthenticationTlsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsMskClusterClusterInfoClientAuthenticationTlsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsMskClusterClusterInfoClientAuthenticationTlsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
