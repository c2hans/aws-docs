---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_EventParameters.html
---

# EventParameters
<a name="API_EventParameters"></a>

 **[Event-based policies only]** Specifies an event that activates an event-based policy.

## Contents
<a name="API_EventParameters_Contents"></a>

 ** DescriptionRegex **   <a name="dlm-Type-EventParameters-DescriptionRegex"></a>
The snapshot description that can trigger the policy. The description pattern is specified using a regular expression. The policy runs only if a snapshot with a description that matches the specified pattern is shared with your account.
For example, specifying `^.*Created for policy: policy-1234567890abcdef0.*$` configures the policy to run only if snapshots created by policy `policy-1234567890abcdef0` are shared with your account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\p{all}]*`
Required: Yes

 ** EventType **   <a name="dlm-Type-EventParameters-EventType"></a>
The type of event. Currently, only snapshot sharing events are supported.
Type: String
Valid Values: `shareSnapshot`
Required: Yes

 ** SnapshotOwner **   <a name="dlm-Type-EventParameters-SnapshotOwner"></a>
The IDs of the AWS accounts that can trigger policy by sharing snapshots with your account. The policy only runs if one of the specified AWS accounts shares a snapshot with your account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## See Also
<a name="API_EventParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/EventParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/EventParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/EventParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
