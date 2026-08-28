---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/appguide/share-data.html
---

The SiteWise Monitor feature is not available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html)

# Share data with AWS IoT SiteWise Monitor projects
<a name="share-data"></a>

In AWS IoT SiteWise Monitor, you share data by inviting viewers to a project. Viewers can view all assets, asset properties, alarms, and dashboards in the project. You can create multiple projects to give groups of viewers access to different sets of assets and dashboards. Only portal administrators can create and update projects and associate assets with projects. Project owners create and update dashboards and invite viewers to projects.

Your AWS administrator chooses the portal administrators. Your portal administrators assign assets to projects and assign owners to those projects. The project owner invites viewers to a project. At each step, these users decide who has access to your data and what type of access they have.

You can perform the following data sharing tasks:

| Task | Roles that can perform the task |
| --- | --- |
| [Create projects in an AWS IoT SiteWise Monitor portal](create-projects.md) | Only portal administrators can create projects. |
| [View project details](view-project-details.md) | Portal administrators can view details for all projects. Project owners and project viewers can view details for projects to which they have been invited. |
| [Add assets to projects](add-assets-to-projects-sd.md) | Only a portal administrator can add assets to a project. |
| [Assign project owners](assign-project-owners.md) | Only a portal administrator can assign project owners to a project. |
| [Assign project viewers](assign-project-viewers.md) | Portal administrators can invite viewers to any project in the portal. Project owners can invite viewers to projects that they administer. |
| [Change project details](edit-project-details.md) | Only portal administrators can update the name and description for a project. |
| [Delete projects in AWS IoT SiteWise Monitor](delete-projects.md) | Only portal administrators can delete projects. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
