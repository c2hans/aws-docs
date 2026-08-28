---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-cfn-starter-farm.html
---

# Deploy a starter Deadline Cloud farm with CloudFormation
<a name="examples-cfn-starter-farm"></a>

The [starter\_farm](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/starter_farm) CloudFormation template deploys a Deadline Cloud farm that you can use to run jobs that render images, reconstruct 3D scenes, or transform data. The deployed farm includes:
+ One or more [service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-manage.html) that you select during deployment.
+ A production queue with conda virtual environments for the applications that jobs need.
+ A package build queue that you can use to build conda packages.
+ Two conda channels by default: a private channel on an Amazon S3 bucket you provide and the [deadline-cloud channel](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html#conda-queue-environment), which provides applications such as Blender, Houdini, Maya, and Nuke.

To deploy the template, you need an Amazon S3 bucket to hold job attachments and the conda channel, and a Deadline Cloud monitor with IAM Identity Center to view and manage jobs.

From the CloudFormation console, choose *Create Stack*, upload `deadline-cloud-starter-farm-template.yaml`, enter a stack name and the Amazon S3 bucket name, and proceed through stack creation. To use the [conda-forge channel](https://conda-forge.org/), set the `ProdCondaChannels` parameter to `deadline-cloud conda-forge`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
