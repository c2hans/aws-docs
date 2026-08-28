---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-images.html
---

# Image Builder output image resources
<a name="manage-images"></a>

After you have created image resources for AMI or container images with Image Builder, you can manage them using the Image Builder console, through the Image Builder API, or with **imagebuilder** commands in the AWS CLI.

**Tip**
When you have multiple resources of the same type, tagging helps you to identify a specific resource based on the tags you've assigned to it. For more information about tagging your resources using Image Builder commands in the AWS CLI, see the [Tag resources](tag-resources.md) section of this guide.

This section covers how to list, view, and create images. For information about image workflows and how to manage them, see [Manage build, test, and distribution workflows for Image Builder images](manage-image-workflows.md).

**Topics**
+ [List images and build versions](image-details-list.md)
+ [View image resource details](view-image-details.md)
+ [Create custom images with Image Builder](create-images.md)
+ [Import and export virtual machine images with Image Builder](vm-import-export.md)
+ [Import verified Windows ISO disk images with Image Builder](import-iso-disk.md)
+ [Manage security findings for Image Builder images](image-security-findings.md)
+ [Clean up Image Builder resources](#images-cleanup)

## Clean up Image Builder resources
<a name="images-cleanup"></a>

To avoid unexpected charges, make sure to clean up resources and pipelines that you created from the examples in this guide. For more information about deleting resources in Image Builder, see [Delete outdated or unused Image Builder resources](delete-resources.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
