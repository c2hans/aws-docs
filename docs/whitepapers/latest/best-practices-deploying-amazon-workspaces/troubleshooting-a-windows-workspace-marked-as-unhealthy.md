---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/troubleshooting-a-windows-workspace-marked-as-unhealthy.html
---

# Troubleshooting a Windows WorkSpace marked as unhealthy
<a name="troubleshooting-a-windows-workspace-marked-as-unhealthy"></a>

 The Amazon WorkSpaces service periodically checks the health of a WorkSpace by sending it a status request. The WorkSpace is marked as Unhealthy if a response isn’t received from the WorkSpace in a timely manner. Common causes for this problem are:
+  An application on the WorkSpace is blocking network connection between the Amazon WorkSpaces service and the WorkSpace.
+  High CPU utilization on the WorkSpace.
+  The computer name of the WorkSpace is changed.
+  The agent or service that responds to the Amazon WorkSpaces service isn't in running state.

 The following troubleshooting steps can return the WorkSpace to a healthy state:
+  First, [reboot the WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/reboot-workspaces.html) from the [Amazon WorkSpaces console](https://docs.aws.amazon.com/workspaces/latest/adminguide/reboot-workspaces.html). If rebooting the WorkSpace doesn't resolve the issue, either use [RDP](https://aws.amazon.com/premiumsupport/knowledge-center/connect-workspace-rdp/), or connect to an [Amazon Linux WorkSpace using SSH](https://docs.aws.amazon.com/workspaces/latest/adminguide/connect-to-linux-workspaces-with-ssh.html).
+  If the WorkSpace is unreachable by a different protocol, [rebuild the WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/reset-workspace.html) from the Amazon WorkSpaces console.
+  If a WorkSpaces connection cannot be established, verify the following:

## Verify CPU utilization
<a name="verify-cpu-utilization"></a>

 Use Open Task Manager to determine if the WorkSpace is experiencing high CPU utilization. If it is, try any of the following troubleshooting steps to resolve the issue:

1.  Stop any service that is consuming a high amount of CPU.

1.  Resize the WorkSpace to a compute type greater than what is currently used.

1.  Reboot the WorkSpace.

**Note**
 To diagnose high CPU utilization, and for guidance if the above steps don't resolve the high CPU utilization issue, refer to [How do I diagnose high CPU utilization on my EC2 Windows instance when my CPU is not throttled?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-cpu-utilization-not-throttled/)

## Verify the computer name of the WorkSpace
<a name="verify-the-computer-name-of-the-workspace"></a>

 If the computer name of the Workspace was changed, change it back to the original name:

1.  Open the Amazon WorkSpaces console, and then expand the Unhealthy WorkSpace to show details.

1.  Copy the Computer Name.

1.  Connect to the WorkSpace using RDP.

1.  Open a command prompt, and then enter hostname to view the current computer name.

   1.  If the name matches the Computer Name from step 2, skip to the next troubleshooting section.

   1.  If the names don’t match, enter sysdm.cpl to open system properties, and then follow the remaining steps in this section.

1.  Choose **Change**, and then paste the Computer Name from step 2.

1.  Enter the domain user credentials if prompted.

1.  Confirm that **SkyLightWorkspaceConfigService** is in Running State

   1.  From **Services**, verify that the WorkSpace service SkyLightWorkspaceConfigService is in running state. If it’s not, start the service.

## Verify Firewall rules
<a name="verify-firewall-rules"></a>

 Confirm that the Windows Firewall and any third-party firewall that is running have rules to allow the following ports:
+  Inbound TCP on port 4172: Establish the streaming connection.
+  Inbound UDP on port 4172: Stream user input.
+  Inbound TCP on port 8200: Manage and configure the WorkSpace.
+  Outbound UDP on port 55002: PCoIP streaming.

 If the firewall uses stateless filtering, then open ephemeral ports 49152-65535 to allow return communication.

 If the firewall uses stateful filtering, then ephemeral port 55002 is already open.
