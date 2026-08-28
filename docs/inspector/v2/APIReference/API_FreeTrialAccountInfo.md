---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FreeTrialAccountInfo.html
---

# FreeTrialAccountInfo
<a name="API_FreeTrialAccountInfo"></a>

Information about the Amazon Inspector free trial for an account.

## Contents
<a name="API_FreeTrialAccountInfo_Contents"></a>

 ** accountId **   <a name="inspector2-Type-FreeTrialAccountInfo-accountId"></a>
The account associated with the Amazon Inspector free trial information.
Type: String
Pattern: `.*[0-9]{12}.*`
Required: Yes

 ** freeTrialInfo **   <a name="inspector2-Type-FreeTrialAccountInfo-freeTrialInfo"></a>
Contains information about the Amazon Inspector free trial for an account.
Type: Array of [FreeTrialInfo](API_FreeTrialInfo.md) objects
Required: Yes

## See Also
<a name="API_FreeTrialAccountInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FreeTrialAccountInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FreeTrialAccountInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FreeTrialAccountInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
