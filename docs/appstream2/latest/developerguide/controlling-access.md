---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-access.html
---

# Identity and Access Management for Amazon WorkSpaces Applications
<a name="controlling-access"></a>

Your security credentials identify you to services in AWS and grant you unlimited use of your AWS resources, such as your WorkSpaces Applications resources. You can use features of WorkSpaces Applications and AWS Identity and Access Management (IAM) to allow other users, services, and applications to use your WorkSpaces Applications resources without sharing your security credentials.

You can use IAM to control how other users use resources in your Amazon Web Services account, and you can use security groups to control access to your WorkSpaces Applications streaming instances. You can allow full use or limited use of your WorkSpaces Applications resources.

**Topics**
+ [Network Access to Your Streaming Instance](network-access-to-streaming-instances.md)
+ [Using AWS Managed Policies and Linked Roles to Manage Administrator Access to WorkSpaces Applications Resources](controlling-administrator-access-with-policies-roles.md)
+ [Using IAM Policies to Manage Administrator Access to Application Auto Scaling](autoscaling-iam-policy.md)
+ [Using IAM Policies to Manage Administrator Access to the Amazon S3 Bucket for Home Folders and Application Settings Persistence](s3-iam-policy.md)
+ [Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances](using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.md)
+ [SELinux on Red Hat Enterprise Linux and Rocky Linux](selinux.md)
+ [Cookie-Based Authentication in Amazon WorkSpaces Applications](cookie-auth.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
