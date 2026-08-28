---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AccountState.html
---

# AccountState
<a name="API_AccountState"></a>

An object with details the status of an AWS account within your Amazon Inspector environment.

## Contents
<a name="API_AccountState_Contents"></a>

 ** accountId **   <a name="inspector2-Type-AccountState-accountId"></a>
The AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** resourceState **   <a name="inspector2-Type-AccountState-resourceState"></a>
An object detailing which resources Amazon Inspector is enabled to scan for the account.
Type: [ResourceState](API_ResourceState.md) object
Required: Yes

 ** state **   <a name="inspector2-Type-AccountState-state"></a>
An object detailing the status of Amazon Inspector for the account.
Type: [State](API_State.md) object
Required: Yes

## See Also
<a name="API_AccountState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AccountState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AccountState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AccountState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
