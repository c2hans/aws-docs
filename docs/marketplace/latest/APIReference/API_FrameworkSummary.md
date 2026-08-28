---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_FrameworkSummary.html
---

# FrameworkSummary
<a name="API_FrameworkSummary"></a>

The framework-specific details of the assessed resource. Exactly one member is set, corresponding to the framework that was assessed.

## Contents
<a name="API_FrameworkSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AMISecuritySummary **   <a name="AWSMarketplaceService-Type-FrameworkSummary-AMISecuritySummary"></a>
The details of the resource assessed under the AMI Security framework.
Type: [AMISecuritySummary](API_AMISecuritySummary.md) object
Required: No

 ** ContainerSecuritySummary **   <a name="AWSMarketplaceService-Type-FrameworkSummary-ContainerSecuritySummary"></a>
The details of the resource assessed under the Container Security framework.
Type: [ContainerSecuritySummary](API_ContainerSecuritySummary.md) object
Required: No

## See Also
<a name="API_FrameworkSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/FrameworkSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/FrameworkSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/FrameworkSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
