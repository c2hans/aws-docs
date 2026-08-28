---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks-disassociate.html
---

# Disassociate an App Block in Amazon WorkSpaces Applications
<a name="appstream-app-blocks-disassociate"></a>

If all your app block builders are associated with other app blocks, and you want to test, create, or activate another app block, then you can either create a new app block builder, or disassociate an existing app block builder from the app block and use it with the new app block.

**Note**
Associating and disassociating an app block is only supported for app blocks with WorkSpaces Applications packaging.
Disassociation is allowed only if an app block builder is in the **STOPPED** state.

**Disassociate an app block from an app block builder**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. From the left-hand navigation menu, choose **Applications Manager**, **App blocks**.

1. Select an app block, and choose **Disassociate** from the **Actions** menu.

1. Select an already associated app block builder, and choose **Disassociate app block builder**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
