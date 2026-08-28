---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UsageTotal.html
---

# UsageTotal
<a name="API_UsageTotal"></a>

The total of usage for an account ID.

## Contents
<a name="API_UsageTotal_Contents"></a>

 ** accountId **   <a name="inspector2-Type-UsageTotal-accountId"></a>
The account ID of the account that usage data was retrieved for.
Type: String
Pattern: `.*[0-9]{12}.*`
Required: No

 ** usage **   <a name="inspector2-Type-UsageTotal-usage"></a>
An object representing the total usage for an account.
Type: Array of [Usage](API_Usage.md) objects
Required: No

## See Also
<a name="API_UsageTotal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UsageTotal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UsageTotal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UsageTotal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
