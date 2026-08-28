---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/add-application.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Add application
<a name="add-application"></a>

To add an application, choose **Add application**. When the **Add application** prompt opens, configure the application name, add a description (optional), associate source servers (optional), and add tags (optional).
+  **Application name** – Application name is mandatory, with a limit of 256 characters. The name must be unique per account per region. Uniqueness verification for application name in Migration Application Service is case-insensitive.
+  **Description** – Application description is optional, with a limit of 600 characters.
+  **Servers** – You can add up to 200 servers to an application. Checking a server in the drop-down list will associate it with the application.
+  **Tags** – You can add up to 50 tags to an application.

When you are done configuring your application settings, choose **Add application** to create the application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
