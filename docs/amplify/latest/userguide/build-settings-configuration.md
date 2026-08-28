---
source_url: https://docs.aws.amazon.com/amplify/latest/userguide/build-settings-configuration.html
---

# Managing the build configuration for an Amplify application
<a name="build-settings-configuration"></a>

You can customize the build settings and configuration for your Amplify deployments. When you deploy an application, Amplify automatically detects the frontend framework and the associated build settings. You can customize the build settings in the application's build specification (buildspec) to add environment variables, run build commands, and specify build dependencies.

Amplify's default build image comes with several packages and dependencies pre-installed, but you can also use the live package updates feature to specify either a specific version, or ensure that the latest version is always installed. If you have specific dependencies that take a long time to install during a build using Amplify's default container, you can create your own custom build image. You can also customize the build instance size to provide your application deployment with the CPU, memory, and disk space resources it needs.

Builds are initiated automatically with each commit to your Git repository and with each new deployment. You can set up the incoming webhooks feature to initiate a build without a commit to your Git repository.

The build notifications feature allows you to share information with team members about build successes and failures.

**Topics**
+ [Configuring the build settings for an Amplify application](build-settings.md)
+ [Customizing the build image](custom-build-image.md)
+ [Configuring the build instance for an Amplify application](custom-build-instance.md)
+ [Creating an incoming webhook to start a build](create-incoming-webhook.md)
+ [Setting up email notifications for builds](notifications.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
