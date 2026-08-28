---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/applications-list.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Manage applications
<a name="applications-list"></a>

The **Applications** page lists all the applications that have been added to AWS Transform MGN. The **Applications** page allows you to manage your applications and perform a variety of commands for one or more applications (such as controlling replication and launching test and cutover instances).

## Interacting with the Applications page
<a name="applications-list-interacting"></a>

The **Applications** page shows a list of applications. Each row on the list represents a single application.

The **Applications** page provides key information for each application under each of the columns on the page.

The columns include:
+  **Selector column** – This blank checkbox selector column allows you to select one or more applications. When an application is selected, you can interact with the application through the **Actions** menu, **Edit**, and **Delete** buttons. Selected applications are highlighted.
+  **Application name** – This column shows the unique application name for each application.
+  **Wave name** – This column shows the name of the wave the application is associated with. An application cannot be associated with more than one wave at a time.

  This column is hidden by default.
+  **Migration status** – This column shows the migration status for each application.
  +  **Not started** – None of the application associated servers has started replication yet.
  +  **In progress** – At least one of the application associated servers has started replication and not all of its servers completed migration.
  +  **Completed** – All the application associated servers completed migration (have been cut over).
+  **Alerts** – This column shows whether any alerts exist for the application.
  + **Stalled** – An application that has at least one server that is experiencing significant issues, such as a stall.
  + **Lagging** – An application that has at least one server that is experiencing a temporary issue such as lag or backlog.
  + **Healthy** – A healthy active application.

  Archived applications do not display any alerts.
+  **Number of servers** – This column shows the total number of servers associated with each application.

**Topics**
+ [Interacting with the Applications page](#applications-list-interacting)
+ [Add application](add-application.md)
+ [Edit application](edit-application.md)
+ [Delete application](delete-application.md)
+ [Manage applications](application-actions-menu.md)
+ [Filtering the Applications page](applications-filtering.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
