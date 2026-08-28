---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/updating-the-global-config.html
---

# Configure solution settings in the web application
<a name="updating-the-global-config"></a>

Innovation Sandbox on AWS stores its global configuration settings in an Amazon DynamoDB table. You manage the settings on the **Settings** page of the solution web UI. The solution no longer manages these settings through the AWS AppConfig console.

New deployments start with every configuration section set to its built-in default values, and with maintenance mode turned **ON**. Innovation Sandbox is fully operational with the default values in the meantime. When maintenance mode is on, only Admins have access to the solution web application. Managers and sandbox users cannot access the web application until an Admin turns maintenance mode off.

To complete first-run configuration:

1. Sign in to the solution web UI as an Admin (a member of the `<NAMESPACE>_IsbAdminsGroup` group). For more information, see [Logging into the web UI](log-in-webui.md).

1. From the left navigation pane, choose **Settings**, and review each section on the **Leases & Cost**, **Cleanup**, and **General** tabs. Save each section to apply its values to your deployment, whether you keep the defaults or customize them. For instructions on viewing and modifying settings, see [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings).

1. On the **General** tab, in the **Notification** section, enter the **Email from address** used to send lease and account notification emails, and save the section. The address (or its parent domain) must already be a verified identity in Amazon Simple Email Service in the Hub account. For more information, see [the prerequisites](prerequisites.md) section. The solution validates the address when you save the section, and the save fails if Amazon SES has not verified the address. Leave this field empty to disable email notifications.

1. When you finish reviewing settings, turn off maintenance mode so Managers and users can access the solution. For instructions, see [Managing maintenance mode](administrator-guide.md#maintenance-mode).

**Note**
Changes you save on the **Settings** page take effect immediately. You do not need to start an AWS AppConfig deployment.

**Note**
If you upgraded to v1.3.0 or later from an earlier version, your existing settings were migrated automatically to the **Settings** page during the stack update. The **GlobalConfig** and **ReportingConfig** configuration profiles that remain in AWS AppConfig are no longer used, and editing them has no effect. The account cleanup configuration—the AWS Nuke configuration and the cleanup validator exclusion configuration—remains in AWS AppConfig, unaffected by this change.

**Note**
The Innovation Sandbox on AWS solution is now ready for use. You can now [log in to the web UI](log-in-webui.md) and start using the solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
