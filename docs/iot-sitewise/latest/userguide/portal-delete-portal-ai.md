---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/portal-delete-portal-ai.html
---

# Delete a portal
<a name="portal-delete-portal-ai"></a>

You might delete a portal if you created it for testing purposes or if you created a duplicate of a portal that already exists.

**Note**
You must first manually delete all dashboards and projects in a portal before you can delete a portal.

1. On the portal details page, choose **Delete**.
**Important**
When you delete a portal, you lose all projects that the portal contains, and all dashboards in each project. This action can't be undone. Your asset data isn't affected.
![Portal details page with Delete highlighted.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-sitewise-delete-portal-console.png)

1. In the **Delete portal** dialog box, choose **Remove admins and users**.

   You must remove the administrators and users from a portal before you can delete it. If your portal doesn't have administrators or users, the button doesn't appear, and you can skip to the next step.

1. If you're sure that you want to delete the entire portal, enter **confirm** in the field to confirm deletion.

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
