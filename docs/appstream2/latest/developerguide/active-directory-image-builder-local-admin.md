---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-image-builder-local-admin.html
---

# Granting Local Administrator Rights on Image Builders
<a name="active-directory-image-builder-local-admin"></a>

By default, Active Directory domain users do not have local administrator rights on image builder instances. You can grant these rights by using Group Policy preferences in your directory, or manually, by using the local administrator account on an image builder. Granting local administrator rights to a domain user allows that user to install applications on and create images in an WorkSpaces Applications image builder.

**Topics**
+ [Using Group Policy preferences](group-policy.md)
+ [Using the local Administrators group on the image builder](manual-procedure.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
