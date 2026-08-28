---
source_url: https://docs.aws.amazon.com/amplify/latest/userguide/build-settings.html
---

# Configuring the build settings for an Amplify application
<a name="build-settings"></a>

When you deploy an application, Amplify automatically detects the frontend framework and associated build settings by inspecting the app's `package.json` file in your Git repository. You have the following options for storing your app's build settings:
+ Save the build settings in the Amplify console - The Amplify console autodetects build settings and saves them so that they can be accessed by the Amplify console. Amplify applies these settings to all of your branches unless there is an `amplify.yml` file stored in your repository.
+ Save the build settings in your repository - Download the `amplify.yml` file and add it to the root of your repository.

**Note**
**Build settings** is visible in the Amplify console's **Hosting** menu only when an app is set up for continuous deployment and connected to a git repository. For instructions on this type of deployment, see [Getting started](getting-started.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
