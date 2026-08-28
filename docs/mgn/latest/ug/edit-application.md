---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/edit-application.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Edit application
<a name="edit-application"></a>

To edit an application, choose **Edit**. When the **Edit application** prompt opens, edit the application name, description, and tags, as well as associate or disassociate source servers.
+ **Application name** – Application name is mandatory, with a limit of up to 256 characters. The name must be unique per account per region. Uniqueness verification for application name in Migration Application Service is case-insensitive.
+  **Description** – Application description is optional, with a limit of 600 characters.
+  **Servers** – You can add up to 200 servers to an application. Checking a server in the dropdown list will associate it with the application. Unchecking an associated server will disassociate it from the application.
+  **Tags** – You can add up to 50 tags to an application.

To finalize your changes, choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
