---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SessionFilter.html
---

# SessionFilter
<a name="API_SessionFilter"></a>

Describes a filter for Session Manager information.

## Contents
<a name="API_SessionFilter_Contents"></a>

 ** key **   <a name="systemsmanager-Type-SessionFilter-key"></a>
The name of the filter.
Type: String
Valid Values: `InvokedAfter | InvokedBefore | Target | Owner | Status | SessionId | AccessType`
Required: Yes

 ** value **   <a name="systemsmanager-Type-SessionFilter-value"></a>
The filter value. Valid values for each filter key are as follows:
+ InvokedAfter: Specify a timestamp to limit your results. For example, specify 2024-08-29T00:00:00Z to see sessions that started August 29, 2024, and later.
+ InvokedBefore: Specify a timestamp to limit your results. For example, specify 2024-08-29T00:00:00Z to see sessions that started before August 29, 2024.
+ Target: Specify a managed node to which session connections have been made.
+ Owner: Specify an Amazon Web Services user to see a list of sessions started by that user.
+ Status: Specify a valid session status to see a list of all sessions with that status. Status values you can specify include:
  + Connected
  + Connecting
  + Disconnected
  + Terminated
  + Terminating
  + Failed
+ SessionId: Specify a session ID to return details about the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: Yes

## See Also
<a name="API_SessionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/SessionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/SessionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/SessionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
