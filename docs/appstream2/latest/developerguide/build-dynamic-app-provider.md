---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/build-dynamic-app-provider.html
---

# Use the WorkSpaces Applications Dynamic Application Framework to Build a Dynamic App Provider
<a name="build-dynamic-app-provider"></a>

The WorkSpaces Applications dynamic application framework provides API operations within an WorkSpaces Applications streaming instance that you can use to build a dynamic app provider. Dynamic app providers can use the API operations provided to modify the catalog of applications that your users can access in real time. The applications managed by the dynamic app providers can be within the image, or they can be off-instance, such as from a Windows file share or an application virtualization technology.

**Note**
This feature requires an WorkSpaces Applications Always-On or On-Demand fleet that is joined to a Microsoft Active Directory domain. For more information, see [Using Active Directory with WorkSpaces Applications](active-directory.md).

**Topics**
+ [About the Dynamic Application Framework](about-dynamic-framework.md)
+ [Dynamic Application Framework Thrift Definitions and Named Pipe Name](dynamic-application-framework-thrift-definitions.md)
+ [API Actions for Managing App Entitlement for WorkSpaces Applications](manage-app-entitlement-api-actions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
