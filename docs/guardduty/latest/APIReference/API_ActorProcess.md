---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ActorProcess.html
---

# ActorProcess
<a name="API_ActorProcess"></a>

Contains information about a process involved in a GuardDuty finding, including process identification, execution details, and file information.

## Contents
<a name="API_ActorProcess_Contents"></a>

 ** name **   <a name="guardduty-Type-ActorProcess-name"></a>
The name of the process as it appears in the system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: Yes

 ** path **   <a name="guardduty-Type-ActorProcess-path"></a>
The full file path to the process executable on the system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: Yes

 ** sha256 **   <a name="guardduty-Type-ActorProcess-sha256"></a>
The SHA256 hash of the process executable file, which can be used for identification and verification purposes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ActorProcess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ActorProcess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ActorProcess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ActorProcess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
