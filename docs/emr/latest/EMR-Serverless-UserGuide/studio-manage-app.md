---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/studio-manage-app.html
---

# Manage applications from the EMR Studio console
<a name="studio-manage-app"></a>

You can perform the following actions on an application from either the **List applications** page or from a specific application’s **Details** page.

****Start application****
Choose this option to manually start an application.

****Stop application****
Choose this option to manually stop an application. An application must have no running jobs to be stopped. To learn more about application state transitions, refer to [Application states](applications.md#application-states).

****Configure application****
Edit the optional settings for an application from the **Configure application** page. You can change most application settings. For example, change the release label for an application to upgrade it to a different version of Amazon EMR, or switch the architecture from x86\_64 to arm64. The other optional settings are the same as those that are in the **Custom settings** section on the **Create application** page. For more information about the application settings, refer to [Create an application](studio.md#studio-create-app).

****Delete application****
Choose this option to manually delete an application. You must stop an application to delete it. To learn more about application state transitions, refer to [Application states](applications.md#application-states).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
