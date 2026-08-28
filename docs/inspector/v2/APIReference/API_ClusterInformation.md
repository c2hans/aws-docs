---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ClusterInformation.html
---

# ClusterInformation
<a name="API_ClusterInformation"></a>

Information about the cluster.

## Contents
<a name="API_ClusterInformation_Contents"></a>

 ** clusterArn **   <a name="inspector2-Type-ClusterInformation-clusterArn"></a>
The cluster ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-[a-z0-9-]+)?:(?:ecs|eks):[a-z0-9-]+:[0-9]{12}:cluster/[a-zA-Z0-9_-]+`
Required: Yes

 ** clusterDetails **   <a name="inspector2-Type-ClusterInformation-clusterDetails"></a>
Details about the cluster.
Type: Array of [ClusterDetails](API_ClusterDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_ClusterInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ClusterInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ClusterInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ClusterInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
