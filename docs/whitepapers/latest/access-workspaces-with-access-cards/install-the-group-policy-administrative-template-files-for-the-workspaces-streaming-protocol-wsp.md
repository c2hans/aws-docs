---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/install-the-group-policy-administrative-template-files-for-the-workspaces-streaming-protocol-wsp.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Install the Group Policy Administrative Template files for the WorkSpaces Streaming Protocol (WSP)
<a name="install-the-group-policy-administrative-template-files-for-the-workspaces-streaming-protocol-wsp"></a>

 To use the Group Policy settings that are specific to Amazon WorkSpaces when using the WorkSpaces Streaming Protocol (WSP), you must add the Group Policy administrative template wsp.admx and wsp.adml files for WSP to the Central Store of the domain controller for your WorkSpaces directory. For more information about .admx and .adml files, see [How to create and manage the Central Store for Group Policy Administrative Templates in Windows](https://support.microsoft.com/help/3087759/how-to-create-and-manage-the-central-store-for-group-policy-administra).

 The following procedure describes how to create the Central Store and add the administrative template files to it. Perform the following procedure on a directory administration WorkSpace or Amazon EC2 instance that is joined to your WorkSpaces directory.

 **To install the Group Policy administrative template files for WSP**:

1.  From a running Windows WorkSpace, make a copy of the `wsp.admx` and `wsp.adml` files in the `C:\Program Files\Amazon\WSP` directory.

1.  On a directory administration WorkSpace or [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instance that is joined to your WorkSpaces directory, navigate to the domain's shared network folder. This folder will have your organization's fully qualified domain name (`FQDN`), such as \\\\example.com.

1.  In Windows File Explorer or the Finder, go to **Network** > **FQDN**.

1.  Open the **SYSVOL** folder.

1.  Open the **FQDN** folder.

1.  Open the **Policies** folder. You should now be in `\\FQDN\SYSVOL\FQDN\Policies`.

1.  If it doesn't already exist, create a folder named **PolicyDefinitions**.

1.  Open the **PolicyDefinitions** folder.

1.  Copy the wsp.admx file into the `\\FQDN\SYSVOL\FQDN\Policies\PolicyDefinitions` folder.

1.  Create a folder named **en-US** in the **PolicyDefinitions** folder.

1.  Open the **en-US** folder.

1.  Copy the wsp.adml file into the `\\FQDN\SYSVOL\FQDN\Policies\PolicyDefinitions\en-US` folder.

 **To verify that the administrative template files are correctly installed**:

1.  On your directory administration WorkSpace or Amazon EC2 instance that is joined to your WorkSpaces directory, open the **Group Policy Management** tool (`gpmc.msc`).

1.  Expand the forest (`Forest:FQDN`).

1.  Expand **Domains**.

1.  Expand your **FQDN** (for example, example.com).

1.  Expand **Group Policy Objects**.

1.  Select **Default Domain Policy**, open the context (**right-click**) menu, and choose **Edit**.

1.  In the **Group Policy Management** **Editor**, choose **Computer Configuration, Policies, Administrative Templates**, **Amazon**, and **WSP**.

1.  You can now use this WSP Group Policy object to modify the Group Policy settings that are specific to Amazon WorkSpaces when using WSP.

 **To enable or disable smart card redirection for Windows WorkSpaces**:

By default, Amazon WorkSpaces are not enabled to support the use of smart cards for in-session authentication. If needed, you can enable in-session authentication for Windows WorkSpaces by using Group Policy settings.

1.  Ensure that the most recent Amazon WorkSpaces Group Policy administrative template for WSP is installed in the Central Store of the domain controller for your WorkSpaces directory.

1.  On your directory administration WorkSpace or Amazon EC2 instance that is joined to your WorkSpaces directory, open the **Group Policy Management** tool (`gpmc.msc`).

1.  Expand the forest (`Forest:FQDN`).

1.  Expand **Domains**.

1.  Expand your **FQDN** (for example, `example.com`).

1.  Expand **Group Policy Objects**.

1.  Select **Default Domain Policy**, open the context (**right-click**) menu, and choose **Edit**.

1.  In the **Group Policy Management** Editor, choose **Computer Configuration, Policies, Administrative Templates**, **Amazon**, and **WSP**.

1.  Open the **Enable/disable smart card redirection** setting.

1.  In the **Enable/disable smart card redirection** dialog box, choose **Enabled**.

1.  Choose **OK**.

1.  The Group Policy setting change takes effect after the next Group Policy update for the WorkSpace and after the WorkSpace session is restarted. To apply the Group Policy changes, do one of the following:
+  Reboot the WorkSpace (in the Amazon WorkSpaces console, select the WorkSpace, then choose **Actions** > **Reboot WorkSpaces**).
+  From an administrative command prompt, enter `gpupdate /force`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
