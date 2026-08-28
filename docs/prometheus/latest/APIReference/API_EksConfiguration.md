---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_EksConfiguration.html
---

# EksConfiguration
<a name="API_EksConfiguration"></a>

The `EksConfiguration` structure describes the connection to the Amazon EKS cluster from which a scraper collects metrics.

## Contents
<a name="API_EksConfiguration_Contents"></a>

 ** clusterArn **   <a name="prometheus-Type-EksConfiguration-clusterArn"></a>
ARN of the Amazon EKS cluster.
Type: String
Pattern: `arn:aws[-a-z]*:eks:[-a-z0-9]+:[0-9]{12}:cluster/.+`
Required: Yes

 ** subnetIds **   <a name="prometheus-Type-EksConfiguration-subnetIds"></a>
A list of subnet IDs for the Amazon EKS cluster VPC configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-z]+`
Required: Yes

 ** securityGroupIds **   <a name="prometheus-Type-EksConfiguration-securityGroupIds"></a>
A list of the security group IDs for the Amazon EKS cluster VPC configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-z]+`
Required: No

## See Also
<a name="API_EksConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/EksConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/EksConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/EksConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
