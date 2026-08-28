---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-images.html
---

# Images
<a name="managing-images"></a>

You can create Amazon WorkSpaces Applications images that contain applications you can stream to your users and default system and application settings to enable your users to get started with those applications quickly. However, after you create an image, you can't change it. To add other applications, update existing applications, or change image settings, you must start and reconnect to the image builder that you used to create the image. If you deleted that image builder, launch a new image builder that is based on your image. Then make your changes and create a new image. For more information, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md) and [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md).

Images that are available to you are listed in the **Image Registry** in the WorkSpaces Applications console. They are categorized as public, private, or shared. You can use any of these image types to launch an image builder and set up an WorkSpaces Applications fleet. Shared images are owned by other Amazon Web Services accounts and shared with you. Permissions set on images that are shared with you may limit what you can do with those images. For more information, see [Administer Your Amazon WorkSpaces Applications Images](administer-images.md).

**Topics**
+ [Default Application and Windows Settings and Application Launch Performance in Amazon WorkSpaces Applications](customizing-appstream-images.md)
+ [Manage WorkSpaces Applications Agent Versions](base-images-agent.md)
+ [WorkSpaces Applications Agent Release Notes](agent-software-versions.md)
+ [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md)
+ [Administer Your Amazon WorkSpaces Applications Images](administer-images.md)
+ [Create Your Amazon WorkSpaces Applications Image Programmatically by Using the Image Assistant CLI Operations](programmatically-create-image.md)
+ [Create Your Linux-Based Images](create-linux-based-images.md)
+ [Use Session Scripts to Manage Your Amazon WorkSpaces Applications Users' Streaming Experience](use-session-scripts.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
