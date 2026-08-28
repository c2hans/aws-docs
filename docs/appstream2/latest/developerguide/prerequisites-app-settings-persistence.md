---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/prerequisites-app-settings-persistence.html
---

# Prerequisites for Enabling Application Settings Persistence
<a name="prerequisites-app-settings-persistence"></a>

To enable application settings persistence, you must first do the following:
+ Check that you have the correct AWS Identity and Access Management (IAM) permissions for Amazon S3 actions. For more information, see the *IAM Policies and the Amazon S3 Bucket for Home Folders* section in [Identity and Access Management for Amazon WorkSpaces Applications](controlling-access.md).
+ Use an image that was created from a base image published by AWS on or after December 7, 2017. For a current list of released AWS base images, see [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md).
+ Associate the stack on which you plan to enable this feature with a fleet based on an image that uses a version of the WorkSpaces Applications agent released on or after August 29, 2018. For more information, see [WorkSpaces Applications Agent Release Notes](agent-software-versions.md).
+ Enable network connectivity to Amazon S3 from your virtual private cloud (VPC) by configuring internet access or a VPC endpoint for Amazon S3. For more information, see the *Home Folders and VPC Endpoints* section in [Networking and Access for Amazon WorkSpaces Applications](managing-network.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
