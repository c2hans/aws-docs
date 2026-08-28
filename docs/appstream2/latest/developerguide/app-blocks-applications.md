---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/app-blocks-applications.html
---

# Applications Manager
<a name="app-blocks-applications"></a>

When using an Elastic fleet, you can create app blocks and applications. *App blocks* represent a virtual hard disk (VHD) that is stored within an Amazon S3 bucket within your account that contains the application files and binaries necessary to launch the applications that your users will use. *Applications* contain the details necessary to launch your application after the VHD has been mounted. The following sections describe how to create and manage these resources.

**Topics**
+ [App Blocks](app-blocks.md)
+ [App Block Builder](app-block-builder.md)
+ [Applications](applications-elastic.md)
+ [Store Application Icon, Setup Script, Session Script, and VHD in an S3 Bucket](store-s3-bucket.md)
+ [Associate Applications to Elastic Fleets](associate-elastic.md)
+ [Additional Resources](additional-resources-app-blocks.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
