---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/server-details.html
---

# View server details with AWS DRS
<a name="server-details"></a>

To access the server details view, click the **Hostname** of any server on the **Source servers** page.

![Source servers table with hostname 22: ready_for_recovery highlighted in red box.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-ss11-details.png)

You can also access the server details view by checking the box to the left of any single source server on the **Source servers** page and choosing **Actions > View server details**.

![Actions menu with View server details option highlighted.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-ss11-details2.png)

The server details view shows information and options for an individual server. Here, you can fully control and monitor the individual server.

![Recovery dashboard tab showing server status as Ready with last recovery result Pending from 3 days ago.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-ss12-details.png)

You can also perform a variety of actions, control replication, and launch Recovery instances for the individual server from the server details view.

The **Overview** box provides a basic overview of the server's status, including whether the server is ready for recovery, any pending actions, the last recovery result (if any), and a link to the Recovery instance (if one was launched for the server).

![Overview box showing Ready status, no pending actions, Successful last recovery result, and recovery instance ID.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-ss12-details-overview.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
