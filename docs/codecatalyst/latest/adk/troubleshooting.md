---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/adk/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

The following information can help you troubleshoot common issues in the Amazon CodeCatalyst ADK.

**Topics**
+ [Handling errors](#handling-errors)
+ [Running action workflows for third-party repositories](#3p-repository-actions)

## Handling errors
<a name="handling-errors"></a>

**Problem:** I see "Internal Error" when running my test workflow but I'm not sure what the issue is.

**Possible fixes:** Your action definition YAML file may have an error. Run the following command to catch errors in the `action.yml` file: `adk validate`.

## Running action workflows for third-party repositories
<a name="3p-repository-actions"></a>

**Problem:** My workflow run fails with a custom action's source code that is in a third-party repository (GitHub).

**Possible fixes:** Your custom action's source code can only be in a Amazon CodeCatalyst source repository. You can create a new repository in CodeCatalyst, move your source code to that repository, and run your workflow again with the action. For more information, see [Step 1: Set up your project and Dev Environment](getting-started.md#set-up-workspace-first-action).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
