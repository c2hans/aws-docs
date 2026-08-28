---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFrontDistributionOriginSslProtocols.html
---

# AwsCloudFrontDistributionOriginSslProtocols
<a name="API_AwsCloudFrontDistributionOriginSslProtocols"></a>

A complex type that contains information about the SSL/TLS protocols that CloudFront can use when establishing an HTTPS connection with your origin.

## Contents
<a name="API_AwsCloudFrontDistributionOriginSslProtocols_Contents"></a>

 ** Items **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginSslProtocols-Items"></a>
A list that contains allowed SSL/TLS protocols for this distribution.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Quantity **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginSslProtocols-Quantity"></a>
The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
Type: Integer
Required: No

## See Also
<a name="API_AwsCloudFrontDistributionOriginSslProtocols_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudFrontDistributionOriginSslProtocols)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudFrontDistributionOriginSslProtocols)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudFrontDistributionOriginSslProtocols)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
