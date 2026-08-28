---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/collecting-a-workspaces-support-log-bundle-for-debugging.html
---

# Collecting a WorkSpaces support log bundle for debugging
<a name="collecting-a-workspaces-support-log-bundle-for-debugging"></a>

 When troubleshooting WorkSpaces issues, it is necessary to gather the log bundle from the affected WorkSpace and the host where the WorkSpaces client is installed. There are two fundamental categories of logs:
+  **Server-side logs**: The WorkSpace is the server in this scenario, so these are logs that live on the WorkSpace itself.
+  **Client-side logs**: Logs on the device that the end user is using to connect to the WorkSpace.
+  Only Windows and macOS clients write logs locally.
+  Zero clients and iOS clients do not log.
+  Android logs are encrypted on the local storage and uploaded automatically to the WorkSpaces client engineering team. Only that team can review the logs for Android devices.

## WSP server-side logs
<a name="wsp-server-side-logs"></a>

All of the WSP components write their log files into one of two folders:
+ **Primary location:** `C:\ProgramData\Amazon\WSP\` and `C:\ProgramData\NICE\dcv\log\`
+ **Archive location:** `C:\ProgramData\Amazon\WSP\TRANSMITTED\`

### Changing log file verbosity on Windows
<a name="changing-log-file-verbosity-windows"></a>

 You can configure the log file verbosity level for WSP Windows WorkSpaces **at scale** by configuring the [log verbosity level Group Policy setting](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#log_verbosity).

 To change the log file verbosity for individual WorkSpaces, configure the `h_log_verbosity_options` key using the Windows Registry Editor:

1.  Open Windows Registry Editor as an administrator.

1.  Navigate to `\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Amazon`.

1.  If the `WSP` key doesn't exist, right-click and choose **New** > **Key** and name it `WSP`.

1.  Navigate to `\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Amazon\WSP`.

1.  If the `h_log_verbosity_options` value doesn't exist, right-click and choose **New** > **DWORD** and name it `h_log_verbosity_options`.

1.  Click the new `h_log_verbosity_options` **DWORD** and change the **Value** to one of the following numbers depending on the required verbosity level:
   +  0 — Error
   +  1 — Warning
   +  2 — Info
   +  3 — Debug

1.  Choose **OK** and close the Windows Registry Editor.

1.  Restart the WorkSpace.

## PCoIP server-side logs
<a name="pcoip-server-side-logs"></a>

 All of the PCoIP components write their log files into one of two folders:
+  **Primary location**: `C:\ProgramData\Teradici\PCoIPAgent\logs`
+  **Archive location**: `C:\ProgramData\Teradici\logs`

 Sometimes when working with AWS Support on a complex issue, it is necessary to put the PCoIP Server agent into verbose logging mode. To enable this:

1. Open the following registry key: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Teradici\PCoIP\pcoip_admin_defaults`

1.  In the `pcoip_admin_defaults` key, create the following 32-bit DWORD: `pcoip.event_filter_mode`

1.  Set the value for `pcoip.event_filter_mode` to “`3`” (Dec or Hex).

 For reference, these are the log thresholds which can be defined in this DWORD.
+  0 — (CRITICAL)
+  1 — (ERROR)
+  2 — (INFO)
+  3 — (Debug)

 If the `pcoip_admin_default` DWORD doesn’t exist, the log level is `2` by default. It is recommended to restore a value of `2` to the DWORD after it no longer need verbose logs, as they are much larger and will consume disk space unnecessarily.

## WebAccess server-side logs
<a name="webaccess-server-side-logs"></a>

For PCoIP and WSP (version 1.0\+) WorkSpaces, the WorkSpaces Web Access client uses the STXHD service. The logs for WorkSpaces Web Access are stored at `C:\ProgramData\Amazon\Stxhd\Logs`.

For WSP (version 2.0\+) WorkSpaces, the logs for WorkSpaces Web Access are stored at `C:\ProgramData\Amazon\WSP\`.

## Client-side logs
<a name="client-side-logs"></a>

 These logs come from the WorkSpaces client that the user connects with, so the logs are on the end user’s computer. The log file locations for Windows and Mac are:
+  **Windows**: `"%LOCALAPPDATA%\Amazon Web Services\Amazon WorkSpaces\Logs"`
+  **macOS**: `~/Library/"Application Support"/"Amazon Web Services"/"Amazon WorkSpaces"/logs`
+  **Linux**: `~/.local/share/Amazon Web Services/Amazon WorkSpaces/logs`

 To help troubleshoot issues that users might experience, enable advanced logging that can be used on any Amazon WorkSpaces client. Advanced logging is enabled for every subsequent client session until it is disabled.

1.  Before connecting to the WorkSpace, the end user should [enable advanced logging](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-troubleshooting.html#advanced-logging) for their WorkSpaces client.

1.  The end user should then connect as usual, use their WorkSpace, and attempt to reproduce the issue.

1.  Advanced logging generates log files that contain diagnostic information and debugging-level details, including verbose performance data.

 This setting persists until explicitly turned off. After the user has successfully reproduced the issue with verbose logging on, this setting should be disabled, as it generates large log files.

## Automated server-side log bundle collection for Windows
<a name="automated-server-side-log-bundle-collection-for-windows"></a>

 The `Get-WorkSpaceLogs.ps1` script is helpful for quickly gathering a server-side log bundle for AWS Support. The script can be requested from AWS Support by requesting it in a support case:

1.  Connect to the WorkSpace using the client or using Remote Desktop Protocol (RDP).

1.  Start an administrative Command Prompt (run as administrator). You must have permission to access the `C:` drive (WorkSpaces Root Volume).

1.  Launch the script from the Command Prompt with the following command:

   ```
   powershell.exe -NoLogo -ExecutionPolicy RemoteSigned -NoProfile -File "C:\Program Files\Amazon\WorkSpacesConfig\Scripts\Get-WorkSpaceLogs.ps1"
   ```

1.  The script creates a log bundle on the user's desktop.

    The script creates a zip file with the following folders:
   +  **C** — Contains the files from Program Files, Program Files (x86), ProgramData, and Windows related to Skylight, EC2Config, Teradici, Event viewer, and Windows logs (Panther and others).
   +  **CliXML** — Contains XML files that can be imported in Powershell by using `Import-CliXML` for interactive filtering. Refer to [Import-Clixml](https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.utility/import-clixml).
   +  **Config** — Detailed logs for each check that is performed
   +  **ScriptLogs** — Logs about the script execution (not relevant to the investigation, but useful to debug what the script does).
   +  **tmp** —Temporary folder (it should be empty).
   +  **Traces** — Packet capture done during the log collection.

We try to ensure this script doesn't collect AWS-related credentials. However, it does collect environmental variables that help AWS with troubleshooting issues. Make sure you review the output before submitting the script to AWS to ensure you don't expose confidential credentials.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
