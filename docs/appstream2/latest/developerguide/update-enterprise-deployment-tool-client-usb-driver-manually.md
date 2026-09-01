---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/update-enterprise-deployment-tool-client-usb-driver-manually.html
---

# Update the WorkSpaces Applications Enterprise Deployment Tool, Client, and USB Driver Manually
<a name="update-enterprise-deployment-tool-client-usb-driver-manually"></a>

By default, the WorkSpaces Applications client and USB driver update automatically when we release a new client version. If you used the Enterprise Deployment Tool to install the WorkSpaces Applications client and disabled automatic updates, you must update the client and USB driver manually. To do so, run the following PowerShell commands on your users' computers.

**Note**
To run these commands, you must either be logged in to the applicable computer as Administrator, or you can run the script remotely under the SYSTEM account on startup.
Using the Enterprise Deployment Tool to manage the WorkSpaces Applications macOS client is not supported.

1. Install the new version of the WorkSpaces Applications client over the existing version:

   ```
   Start-Process msiexec.exe -Wait -ArgumentList '/i AmazonWorkSpacesApplicationsClientSetup_<new_version>.msi ALLUSERS=1 /quiet'
   ```
**Note**
You don't need to uninstall the previous version or reboot. The new version automatically replaces the previous version.

1. (Optional) Update the WorkSpaces Applications USB driver:

   ```
   Start-Process AmazonAppStreamUsbDriverSetup_<new_version>.exe -Wait -ArgumentList '/quiet'
   ```

**Upgrading from versions 1.2.1830 and earlier**
If you previously installed the client using the Enterprise Deployment Tool (versions 1.2.1830 and earlier), the new MSI automatically removes the legacy installation during upgrade. No manual uninstall or reboot is required. The install location changes from `C:\Program Files (x86)\Amazon WorkSpaces Applications Client Installer\` to `C:\Program Files\Amazon Web Services, Inc\Amazon WorkSpaces Applications\`. The MSI requires a 64-bit version of Windows.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
