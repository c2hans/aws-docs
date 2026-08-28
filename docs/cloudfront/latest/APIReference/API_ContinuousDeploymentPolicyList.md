---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ContinuousDeploymentPolicyList.html
---

# ContinuousDeploymentPolicyList
<a name="API_ContinuousDeploymentPolicyList"></a>

Contains a list of continuous deployment policies.

## Contents
<a name="API_ContinuousDeploymentPolicyList_Contents"></a>

 ** MaxItems **   <a name="cloudfront-Type-ContinuousDeploymentPolicyList-MaxItems"></a>
The maximum number of continuous deployment policies that were specified in your request.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-ContinuousDeploymentPolicyList-Quantity"></a>
The total number of continuous deployment policies in your AWS account, regardless of the `MaxItems` value.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-ContinuousDeploymentPolicyList-Items"></a>
A list of continuous deployment policy items.
Type: Array of [ContinuousDeploymentPolicySummary](API_ContinuousDeploymentPolicySummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-ContinuousDeploymentPolicyList-NextMarker"></a>
Indicates the next page of continuous deployment policies. To get the next page of the list, use this value in the `Marker` field of your request.
Type: String
Required: No

## See Also
<a name="API_ContinuousDeploymentPolicyList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentPolicyList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentPolicyList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentPolicyList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
