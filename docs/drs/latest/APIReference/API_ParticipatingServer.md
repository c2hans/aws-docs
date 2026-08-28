---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ParticipatingServer.html
---

# ParticipatingServer
<a name="API_ParticipatingServer"></a>

Represents a server participating in an asynchronous Job.

## Contents
<a name="API_ParticipatingServer_Contents"></a>

 ** launchActionsStatus **   <a name="drs-Type-ParticipatingServer-launchActionsStatus"></a>
The post-launch action runs of a participating server.
Type: [LaunchActionsStatus](API_LaunchActionsStatus.md) object
Required: No

 ** launchStatus **   <a name="drs-Type-ParticipatingServer-launchStatus"></a>
The launch status of a participating server.
Type: String
Valid Values: `PENDING | IN_PROGRESS | LAUNCHED | FAILED | TERMINATED`
Required: No

 ** recoveryInstanceID **   <a name="drs-Type-ParticipatingServer-recoveryInstanceID"></a>
The Recovery Instance ID of a participating server.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

 ** sourceServerID **   <a name="drs-Type-ParticipatingServer-sourceServerID"></a>
The Source Server ID of a participating server.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_ParticipatingServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ParticipatingServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ParticipatingServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ParticipatingServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
