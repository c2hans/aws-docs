---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CountsSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CountsSummary
<a name="API_CountsSummary"></a>

Summary counts of each AWS Proton resource type.

## Contents
<a name="API_CountsSummary_Contents"></a>

 ** components **   <a name="proton-Type-CountsSummary-components"></a>
The total number of components in the AWS account.
The semantics of the `components` field are different from the semantics of results for other infrastructure-provisioning resources. That's because at this time components don't have associated templates, therefore they don't have the concept of staleness. The `components` object will only contain `total` and `failed` members.
Type: [ResourceCountsSummary](API_ResourceCountsSummary.md) object
Required: No

 ** environments **   <a name="proton-Type-CountsSummary-environments"></a>
The staleness counts for AWS Proton environments in the AWS account. The `environments` object will only contain `total` members.
Type: [ResourceCountsSummary](API_ResourceCountsSummary.md) object
Required: No

 ** environmentTemplates **   <a name="proton-Type-CountsSummary-environmentTemplates"></a>
The total number of environment templates in the AWS account. The `environmentTemplates` object will only contain `total` members.
Type: [ResourceCountsSummary](API_ResourceCountsSummary.md) object
Required: No

 ** pipelines **   <a name="proton-Type-CountsSummary-pipelines"></a>
The staleness counts for AWS Proton pipelines in the AWS account.
Type: [ResourceCountsSummary](API_ResourceCountsSummary.md) object
Required: No

 ** serviceInstances **   <a name="proton-Type-CountsSummary-serviceInstances"></a>
The staleness counts for AWS Proton service instances in the AWS account.
Type: [ResourceCountsSummary](API_ResourceCountsSummary.md) object
Required: No

 ** services **   <a name="proton-Type-CountsSummary-services"></a>
The staleness counts for AWS Proton services in the AWS account.
Type: [ResourceCountsSummary](API_ResourceCountsSummary.md) object
Required: No

 ** serviceTemplates **   <a name="proton-Type-CountsSummary-serviceTemplates"></a>
The total number of service templates in the AWS account. The `serviceTemplates` object will only contain `total` members.
Type: [ResourceCountsSummary](API_ResourceCountsSummary.md) object
Required: No

## See Also
<a name="API_CountsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CountsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CountsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CountsSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
