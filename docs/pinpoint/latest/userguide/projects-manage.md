---
source_url: https://docs.aws.amazon.com/pinpoint/latest/userguide/projects-manage.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Managing Amazon Pinpoint projects
<a name="projects-manage"></a>

You can use the Amazon Pinpoint console to create, view, edit, and delete projects. Within a project, you can also [import endpoints](segments-importing.md), [build segments](segments-building.md), [create campaigns](campaigns.md), [create journeys](journeys-create.md), and [view analytics data](analytics-charts.md) for that project.

Use the **General settings** page to specify when Amazon Pinpoint can send messages for campaigns and journeys in the current project and how many messages Amazon Pinpoint can send for those campaigns and journeys. This includes settings such as the time frame for sending messages and the maximum number of messages to send to each endpoint. You can also use the **General settings** page to delete a project.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
