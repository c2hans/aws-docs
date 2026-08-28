---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ParticipatingServer.html
---

# ParticipatingServer
<a name="API_ParticipatingServer"></a>

Server participating in Job.

## Contents
<a name="API_ParticipatingServer_Contents"></a>

 ** sourceServerID **   <a name="mgn-Type-ParticipatingServer-sourceServerID"></a>
Participating server Source Server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

 ** launchedEc2InstanceID **   <a name="mgn-Type-ParticipatingServer-launchedEc2InstanceID"></a>
Participating server's launched ec2 instance ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

 ** launchStatus **   <a name="mgn-Type-ParticipatingServer-launchStatus"></a>
Participating server launch status.
Type: String
Valid Values: `PENDING | IN_PROGRESS | LAUNCHED | FAILED | TERMINATED`
Required: No

 ** postLaunchActionsStatus **   <a name="mgn-Type-ParticipatingServer-postLaunchActionsStatus"></a>
Participating server's Post Launch Actions Status.
Type: [PostLaunchActionsStatus](API_PostLaunchActionsStatus.md) object
Required: No

## See Also
<a name="API_ParticipatingServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ParticipatingServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ParticipatingServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ParticipatingServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
