---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_Source.html
---

# Source
<a name="API_Source"></a>

The source of collected metrics for a scraper.

## Contents
<a name="API_Source_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** eksConfiguration **   <a name="prometheus-Type-Source-eksConfiguration"></a>
The Amazon EKS cluster from which a scraper collects metrics.
Type: [EksConfiguration](API_EksConfiguration.md) object
Required: No

 ** vpcConfiguration **   <a name="prometheus-Type-Source-vpcConfiguration"></a>
The Amazon VPC configuration for the Prometheus collector when connecting to Amazon MSK clusters. This configuration enables secure, private network connectivity between the collector and your Amazon MSK cluster within your Amazon VPC.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

## See Also
<a name="API_Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/Source)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
