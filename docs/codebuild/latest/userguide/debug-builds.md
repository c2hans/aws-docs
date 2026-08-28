---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/debug-builds.html
---

# Debug builds in AWS CodeBuild
<a name="debug-builds"></a>

AWS CodeBuild provides two methods for debugging builds during development and troubleshooting. You can use the CodeBuild Sandbox environment to investigate issues and validate fixes in real-time, or you can use AWS Systems Manager Session Manager to connect to the build container and view the container state.

## Debug builds with CodeBuild sandbox
<a name="debug-codebuild-sandbox"></a>

The CodeBuild sandbox environment provides an interactive debug session in a secure and isolated environment. You can interact with the environment directly through the AWS Management Console or AWS CLI, execute commands, and validate your build process step by step. It uses a cost-effective per-second billing model and supports the same native integration with source providers and AWS services as your build environment. You can also connect to a sandbox environment using SSH clients or from your integrated development environments (IDEs).

To learn more about the CodeBuild sandbox pricing, visit the [CodeBuild pricing documentation](https://aws.amazon.com/codebuild/pricing/#Sandbox). For detailed instructions, visit the [Debug builds with CodeBuild sandbox](sandbox.md) documentation.

## Debug builds with Session Manager
<a name="debug-codebuild-session-manager"></a>

AWS Systems Manager Session Manager enables direct access to running builds in their actual execution environment. This approach allows you to connect to active build containers and inspect the build process in real-time. You can examine the file system, monitor running processes, and troubleshoot issues as they occur.

For detailed instructions, visit the [Debug builds with Session Manager](session-manager.md) documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
