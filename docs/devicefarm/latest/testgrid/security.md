---
source_url: https://docs.aws.amazon.com/devicefarm/latest/testgrid/security.html
---

# Security in Device Farm desktop browser testing
<a name="security"></a>

This section describes data collection and how to control access to resources when you use browser testing in AWS Device Farm.

**Topics**
+ [Your data in Device Farm desktop browser testing](#security-your-data)
+ [Access control and IAM](security-acl-iam.md)
+ [Using service-linked roles for Device Farm](using-service-linked-roles.md)

## Your data in Device Farm desktop browser testing
<a name="security-your-data"></a>

Device Farm does not collect the content of your web application except what's required to run the service.

Your tests are run in isolated instances. They are not shared by any other user or test.

Artifacts (logs, video, and so on) are associated with your account. Files that you download in your tests are not collected. Any content that is saved in the browser (for example, cookies or LocalDB storage) is lost when your session ends.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
