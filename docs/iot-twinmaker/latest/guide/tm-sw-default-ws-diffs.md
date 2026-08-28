---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-default-ws-diffs.html
---

# Differences between custom and default workspaces
<a name="tm-sw-default-ws-diffs"></a>

**Important**
New AWS IoT SiteWise features, such as [`CompositionModel`](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html), are only available in `IoTSiteWiseDefaultWorkspace`. We encourage you to use a default workspace instead of custom workspace.

When using the `IoTSiteWiseDefaultWorkspace`, there are a few notable differences from using a custom workspace with asset sync.
+ When you create a default workspace, the Amazon S3 location and IAM role are optional.
**Note**
You can use `UpdateWorkspace` to provide the Amazon S3 location and IAM role.
+ The `IoTSiteWiseDefaultWorkspace` doesn't have a resource count limit to sync AWS IoT SiteWise resources to AWS IoT TwinMaker.
+ When you sync resources from AWS IoT SiteWise, their `SyncSource` will be `SITEWISE_MANAGED`. This includes `Entities` and `ComponentTypes`.
+ New AWS IoT SiteWise features, such as `CompositionModel` are only available in the `IoTSiteWiseDefaultWorkspace`.

There are a few limitations specific to `IoTSiteWiseDefaultWorkspace`, they are:
+ The default workspace can't be deleted.
+ To delete resources, you must delete the AWS IoT SiteWise resources first, then the corresponding resources in AWS IoT TwinMaker are deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
