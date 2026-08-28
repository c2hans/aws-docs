---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/troubleshooting.html
---

# Troubleshooting AWS CodeArtifact
<a name="troubleshooting"></a>

The following information might help you troubleshoot common issues with CodeArtifact.

For information about troubleshooting format-specific issues, see the following topics:
+ [Maven troubleshooting](maven-troubleshooting.md)
+ [Swift troubleshooting](swift-troubleshooting.md)

## I cannot view notifications
<a name="troubleshooting-notifications"></a>

**Problem:** When you are in the Developer Tools console and choose **Notifications** under **Settings**, you see a permissions error.

**Possible fixes:** While notifications are a feature of the Developer Tools console, CodeArtifact does not currently support notifications. None of the managed policies for CodeArtifact include permissions that allow users to view or manage notifications. If you use other services in the Developer Tools console, and those services support notifications, the managed policies for those services include the permissions required to view and manage notifications for those services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
