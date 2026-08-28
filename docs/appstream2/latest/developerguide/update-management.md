---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/update-management.html
---

# Update Management in Amazon WorkSpaces Applications
<a name="update-management"></a>

WorkSpaces Applications provides an automated way to update your image builder with newer WorkSpaces Applications software. When your images are configured to always use the latest WorkSpaces Applications agent version, your streaming instances are automatically updated with the latest features, performance improvements, and security updates that are available from AWS. For information about how to manage WorkSpaces Applications agent versions, see [Manage WorkSpaces Applications Agent Versions](base-images-agent.md).

You are responsible for installing and maintaining the updates for the Windows operating system, your applications, and their dependencies. For more information, see [Keep Your Amazon WorkSpaces Applications Image Up-to-Date](keep-image-updated.md).

You can keep your WorkSpaces Applications image up-to-date by using managed WorkSpaces Applications image updates. This update method provides the latest Windows operating system updates and driver updates, and the latest WorkSpaces Applications agent software. For more information, see [Update an Image by Using Managed WorkSpaces Applications Image Updates](keep-image-updated-managed-image-updates.md).

To manage updates for applications on your streaming instances, you can use any automatic update services provided. You can also follow the recommendations for installing updates provided by the application vendor.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
