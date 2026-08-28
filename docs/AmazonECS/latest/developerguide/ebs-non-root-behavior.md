---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-non-root-behavior.html
---

# Non-root user behavior
<a name="ebs-non-root-behavior"></a>

When you specify a non-root user in your container definition, Amazon ECS automatically configures the Amazon EBS volume with group-based permissions that allow the specified user to read and write to the volume. The volume is mounted with the following characteristics:
+ The volume is owned by the root user and root group.
+ Group permissions are set to allow read and write access.
+ The non-root user is added to the appropriate group to access the volume.

Follow these best practices when using Amazon EBS volumes with non-root containers:
+ Use consistent user IDs (UIDs) and group IDs (GIDs) across your container images to ensure consistent permissions.
+ Pre-create mount point directories in your container image and set appropriate ownership and permissions.
+ Test your containers with Amazon EBS volumes in a development environment to confirm that file system permissions work as expected.
+ If multiple containers in the same task share a volume, ensure they either use compatible UIDs/GIDs or mount the volume with consistent access expectations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
