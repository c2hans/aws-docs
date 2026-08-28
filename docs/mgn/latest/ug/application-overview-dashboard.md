---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/application-overview-dashboard.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Review overall application status
<a name="application-overview-dashboard"></a>

The **Overview** dashboard provides an overview of the overall application status, including:
+  **Description** – The description of the application.
+  **State** – The state of the application. **State** can be in one of two states: **Active** or **Archived**.
+  **Last status update** – Time stamp of when application status was updated (update occurs every five minutes).
+  **Wave name** – Name of the wave that the application is associated with.
+  **Migration status** – The application migration status.

   Application **Migration status** can have one of the following values:

   **Not started** – If none of its servers has started replication yet.

   **Completed** – If all of its servers completed migration (have been cutover).

   **In progress** – At least one of its servers has started replication and not all of its servers completed migration.
+  **Alerts** – The application alert.

   An application that has at least one server that is experiencing significant issues, such as a stall, will display a **Stalled** status.

   An application that has at least one server that is experiencing a temporary issue such as lag or backlog will display a **Lagging** status.

   A healthy active application will display a **Healthy** status.

   An archived application will not display a status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
