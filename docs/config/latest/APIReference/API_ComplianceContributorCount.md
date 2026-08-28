---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ComplianceContributorCount.html
---

# ComplianceContributorCount
<a name="API_ComplianceContributorCount"></a>

The number of AWS resources or AWS Config rules responsible for the current compliance of the item, up to a maximum number.

## Contents
<a name="API_ComplianceContributorCount_Contents"></a>

 ** CapExceeded **   <a name="config-Type-ComplianceContributorCount-CapExceeded"></a>
Indicates whether the maximum count is reached.
Type: Boolean
Required: No

 ** CappedCount **   <a name="config-Type-ComplianceContributorCount-CappedCount"></a>
The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
Type: Integer
Required: No

## See Also
<a name="API_ComplianceContributorCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ComplianceContributorCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ComplianceContributorCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ComplianceContributorCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
