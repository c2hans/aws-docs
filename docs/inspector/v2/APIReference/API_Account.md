---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Account.html
---

# Account
<a name="API_Account"></a>

An AWS account within your environment that Amazon Inspector has been enabled for.

## Contents
<a name="API_Account_Contents"></a>

 ** accountId **   <a name="inspector2-Type-Account-accountId"></a>
The ID of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** resourceStatus **   <a name="inspector2-Type-Account-resourceStatus"></a>
Details of the status of Amazon Inspector scans by resource type.
Type: [ResourceStatus](API_ResourceStatus.md) object
Required: Yes

 ** status **   <a name="inspector2-Type-Account-status"></a>
The status of Amazon Inspector for the account.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | SUSPENDING | SUSPENDED`
Required: Yes

## See Also
<a name="API_Account_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Account)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Account)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Account)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
