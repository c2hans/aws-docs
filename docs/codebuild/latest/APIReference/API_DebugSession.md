---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DebugSession.html
---

# DebugSession
<a name="API_DebugSession"></a>

Contains information about the debug session for a build. For more information, see [Viewing a running build in Session Manager](https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html).

## Contents
<a name="API_DebugSession_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** sessionEnabled **   <a name="CodeBuild-Type-DebugSession-sessionEnabled"></a>
Specifies if session debugging is enabled for this build.
Type: Boolean
Required: No

 ** sessionTarget **   <a name="CodeBuild-Type-DebugSession-sessionTarget"></a>
Contains the identifier of the Session Manager session used for the build. To work with the paused build, you open this session to examine, control, and resume the build.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_DebugSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/DebugSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/DebugSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/DebugSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
