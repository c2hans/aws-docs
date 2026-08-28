---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RootCause.html
---

# RootCause
<a name="API_RootCause"></a>

The combination of AWS service, linked account, linked account name, Region, and usage type where a cost anomaly is observed, along with the dollar and percentage amount of the anomaly impact. The linked account name will only be available when the account name can be identified.

## Contents
<a name="API_RootCause_Contents"></a>

 ** Impact **   <a name="awscostmanagement-Type-RootCause-Impact"></a>
The dollar impact for the root cause.
Type: [RootCauseImpact](API_RootCauseImpact.md) object
Required: No

 ** LinkedAccount **   <a name="awscostmanagement-Type-RootCause-LinkedAccount"></a>
The member account value that's associated with the cost anomaly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** LinkedAccountName **   <a name="awscostmanagement-Type-RootCause-LinkedAccountName"></a>
The member account name value that's associated with the cost anomaly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Region **   <a name="awscostmanagement-Type-RootCause-Region"></a>
The AWS Region that's associated with the cost anomaly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Service **   <a name="awscostmanagement-Type-RootCause-Service"></a>
The AWS service name that's associated with the cost anomaly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** UsageType **   <a name="awscostmanagement-Type-RootCause-UsageType"></a>
The `UsageType` value that's associated with the cost anomaly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_RootCause_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/RootCause)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/RootCause)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/RootCause)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
