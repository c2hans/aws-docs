---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorResourceDetail.html
---

# TrustedAdvisorResourceDetail
<a name="API_TrustedAdvisorResourceDetail"></a>

Contains information about a resource identified by a Trusted Advisor check.

## Contents
<a name="API_TrustedAdvisorResourceDetail_Contents"></a>

 ** metadata **   <a name="AWSSupport-Type-TrustedAdvisorResourceDetail-metadata"></a>
Additional information about the identified resource. The exact metadata and its order can be obtained by inspecting the [TrustedAdvisorCheckDescription](API_TrustedAdvisorCheckDescription.md) object returned by the call to [DescribeTrustedAdvisorChecks](API_DescribeTrustedAdvisorChecks.md). **Metadata** contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data.
Type: Array of strings

 ** resourceId **   <a name="AWSSupport-Type-TrustedAdvisorResourceDetail-resourceId"></a>
The unique identifier for the identified resource.
Type: String

 ** status **   <a name="AWSSupport-Type-TrustedAdvisorResourceDetail-status"></a>
The status code for the resource identified in the Trusted Advisor check.
Type: String

 ** isSuppressed **   <a name="AWSSupport-Type-TrustedAdvisorResourceDetail-isSuppressed"></a>
Specifies whether the AWS resource was ignored by Trusted Advisor because it was marked as suppressed by the user.
Type: Boolean

 ** region **   <a name="AWSSupport-Type-TrustedAdvisorResourceDetail-region"></a>
The AWS Region in which the identified resource is located.
Type: String

## See Also
<a name="API_TrustedAdvisorResourceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/TrustedAdvisorResourceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/TrustedAdvisorResourceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/TrustedAdvisorResourceDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
