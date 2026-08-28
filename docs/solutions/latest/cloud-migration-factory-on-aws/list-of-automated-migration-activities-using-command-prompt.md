---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-command-prompt.html
---

# List of automated migration activities using command prompt
<a name="list-of-automated-migration-activities-using-command-prompt"></a>

**Note**
We recommend running automation from the Cloud Migration Factory on AWS console. You can use the following steps to run automation scripts. Make sure that you download the automation scripts from the GitHub repo and configure the automation server with steps in [Run Automations from Command prompt](run-automations-from-command-prompt.md), and following the instructions to configure permissions in [Configure AWS permissions for the migration automation server](configure-migration-automation-server.md#configure-aws-permissions-for-the-migration-automation-server).

The Cloud Migration Factory on AWS solution deploys automated migration activities that you can leverage for your migration projects. You can follow the migration activities listed below and customize them based on your business needs.

Before starting any of the activities, verify that you are logged on to your migration automation server as a domain user with local administrator permission on the in-scope source servers.

**Important**
You must log in as an administrator user to complete the activities listed in this section.

Use the following procedures in the same order to conduct a complete test run of the solution using the sample automation script and activities.

## Check prerequisites
<a name="prerequisites-3"></a>

Connect with the in-scope source servers to verify the necessary prerequisites such as TCP 1500, TCP 443, root volume free space, .Net framework version, and other parameters. These prerequisites are required for replication.

Before you can conduct the prerequisite check, you must install the first agent manually on one source server, so this will create a replication server in EC2, we will be connecting to this server for port 1500 testing. After installation, AWS Application Migration Service (AWS MGN) creates the replication server in Amazon Elastic Compute Cloud (Amazon EC2). You will need to verify the TCP port 1500 from the source server to the replication server in this activity. For information about installing the AWS MGN agent on your source servers, refer to [Installation instructions](https://docs.aws.amazon.com/mgn/latest/ug/agent-installation-instructions.html) in the *Application Migration Service User Guide*.

Use the following procedure while signed in to the migration automation server to check for the prerequisites.

1. Signed in as an administrator, open a command prompt (`CMD.exe`).

1. Navigate to the `c:\migrations\scripts\script_mgn_0-Prerequisites-checks` folder and run the following Python command:

```
python 0-Prerequisites-checks.py --Waveid <wave-id> --ReplicationServerIP <rep-server-ip>
```

Replace {{<wave-id>}} and {{<rep-server-ip>}} with the appropriate values:
+ The `Waveid` is a unique integer value to identify your migration waves.
+ The `ReplicationServerIP` value identifies the replication server IP address. Change this value to the Amazon EC2 IP address. To locate this address, sign in to the AWS Management Console, search for **Replication**, select one of the replication servers, and copy the private IP address. If the replication occurs over the public internet, use the public IP address instead.

  1. The script automatically retrieves a server list for the specified wave.

The script then checks the prerequisites for Windows servers and returns a state of either `pass` or `fail` for each check.

**Note**
You might get a security warning like the following when the PowerShell script is not trusted. Run the following command in PowerShell to resolve the issue:

```
Unblock-File C:\migrations\scripts\script_mgn_0-Prerequisites-checks\0-Prerequisites-Windows.ps1
```

Next, the script checks the Linux servers.

Once the checks are completed, the script will return a final result for each server.

 **Script final result**

![script final result](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/script-final-result.png)

If the server failed one or more prerequisites checks, you can identify the faulty server by either reviewing the detailed error message provided at the completion of the check or by scrolling through the log details.

The script will also update the solution’s **Migration Status** in the Migration Factory web interface as shown in the following screenshot of an example project.

## Install the replication agents
<a name="install-the-replication-agents-1"></a>

**Note**
Before you install the agent, make sure that [AWS MGN is initialized in each target account](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize.html).

Use the following procedure to automatically install the Replication agents in the in-scope source servers.

1. In the migration automation server, signed is as an administrator, open a command prompt (`CMD.exe`).

1. Navigate to the `c:\migrations\scripts\script_mgn_1-AgentInstall` folder and run the following Python command:

```
python 1-AgentInstall.py --Waveid <wave-id>
```

Replace <*wave-id*> with the appropriate Wave ID value to install the Replication agent on all servers in the identified wave. The script will install the agent on all source servers in the same wave one by one.

**Note**
To reinstall the agent, you can add `--force` argument.

1. The script generates a list identifying the source servers included for the specified wave. In addition, servers that are identified in multiple accounts and for different OS versions may also be provided.

If there are Linux machines included in this wave, you must enter your Linux sudo sign-in credentials to sign in to those source servers.

The installation starts on the Windows, then proceeds to the Linux for each AWS account.

 **Install replication agents**

![install replication agents](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/install-replication-agents.png)

**Note**
You might get a security warning like the following when the PowerShell script is not trusted. Run the following command in PowerShell to resolve the issue:

```
Unblock-File C:\migrations\scripts\script_mgn_1-AgentInstall\1-Install-Windows.ps1
```

Results are displayed after the script finishes installing the replication agents. Review the results for error messages to identify servers that failed to install the agents. You will need to manually install the agents on the failed servers. If manual installation does not succeed, go to the [AWS support center](https://console.aws.amazon.com/support/home) and log a support case.

 **Agent install result**

![install agent result](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/install-agent-result.png)

The script also provides the migration status in the Migration Factory web interface as shown in the following screenshot of an example project.

## Push the post-launch scripts
<a name="push-the-post-launch-scripts-1"></a>

AWS Application Migration Service supports post-launch scripts to help you automate OS-level activities such as the install/uninstall of software after launching target instances. This activity pushes the post-launch scripts to Windows and/or Linux machines, depending on the servers identified for migration.

Use the following procedure from the migration automation server to push the post-launch scripts to Windows machines.

1. Logged in as an administrator, open a command prompt (`CMD.exe`).

1. Navigate to the `c:\migrations\scripts\script_mgn_1-FileCopy` folder and run the following Python command:

```
python 1-FileCopy.py --Waveid <wave-id> --WindowsSource <file-path> --LinuxSource <file-path>
```

Replace {{<wave-id>}} with the appropriate Wave ID value and {{<file-path>}} with the full file path for Source, where the script is located. For example, `c:\migrations\scripts\script_mgn_1-FileCopy`. This command copies all files from the source folder to the destination folder.

**Note**
At least one of these two arguments must be provided: WindowsSource, LinuxSource. If you provide WindowsSource path, this script will only push files to Windows servers in this wave, same as LinuxSource, which only pushes files to the Linux Servers in this wave. Provide both will push files to both Windows and Linux servers.

1. The script generates a list identifying the source servers included for the specified wave. In addition, servers that are identified in multiple accounts and for different OS versions may also be provided.

If there are Linux machines included in this wave, you must enter your Linux sudo sign-in credentials to sign in to those source servers.

1. The script copies the files to the destination folder. If the destination folder does not exist, the solution creates a directory and notifies you of this action.

## Verify the replication status
<a name="verify-the-replication-status-1"></a>

This activity verifies the replication status for the in-scope source servers automatically. The script repeats every five minutes until the status of all source servers in the given wave changes to a *Healthy* status.

Use the following procedure from the migration automation server to verify the replication status.

1. Signed in as an administrator, open a command prompt (`CMD.exe`).

1. Navigate to the `\migrations\scripts\script_mgn_2-Verify-replication` folder and run the following Python command:

```
python 2-Verify-replication.py --Waveid <wave-id>
```

Replace {{<wave-id>}} with the appropriate Wave ID value to verify the replication status. The script verifies the replication details for the all servers in the specific wave and updates the **replication status** attribute for the source server identified in the solution.

1. The script generates a list identifying the servers included for the specified wave.

The expected status for the in-scope source servers that is ready to launch is **Healthy**. If you receive a different status for a server, then it is not ready for launch yet.

The following screenshot of an example wave shows that all servers in the current wave have finished replication and are ready for testing or cutover.

 **Agent install result**

![replication status](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/replication-status.png)

Optionally, you can verify status in the **Migration Factory** web interface.

## Verify the target instance status
<a name="verify-the-target-instance-status-1"></a>

This activity verifies the status of the target instance by checking the boot up process for all in-scope source servers in the same wave. It may take up to 30 minutes for the target instances to boot up. You can check the status manually by logging into the Amazon EC2 console, searching for the source server name, and checking the status. You will receive a health check message stating *2/2 checks passed*, which indicates that the instance is healthy from an infrastructure perspective.

However, for a large-scale migration, it’s time-consuming to check the status of each instance, so you can run this automated script to verify the *2/2 checks passed* status for all source servers in a given wave.

Use the following procedure from the migration automation server to verify the status of the target instance.

1. Signed in as an administrator, open a command prompt (`CMD.exe`).

1. Navigate to the `c:\migrations\scripts\script_mgn_3-Verify-instance-status` folder and run the following Python command:

```
python 3-Verify-instance-status.py --Waveid <wave-id>
```

Replace {{<wave-id>}} with the appropriate Wave ID value to verify instance status. This script verifies the instance boot up process for all source servers in this wave.

1. The script returns a listing of the server list and Instance IDs for the specified wave.

1. The script will then return a list of target instance IDs.
**Note**
If you get an error message that the target instance Id does not exist, the launch job might still be running. Wait a few minutes before continuing.

1. You will receive instance status checks that indicates whether your target instances passed the 2/2 health checks.

**Note**
If your target instances fail the 2/2 health checks the first time, it may be due to the boot up process taking longer to complete. We recommend running the health checks a second time about an hour after the first health check. This ensures that the boot up process completes. If the health checks fail this second time, go to the [AWS support center](https://console.aws.amazon.com/support/home) to log a support case.

## Shut down the in-scope source servers
<a name="shut-down-the-in-scope-source-servers-1"></a>

This activity shuts down the in-scope source servers involved with the migration. After you verify the source servers' replication status, you are ready to shut down the source servers to stop transactions from the client applications to the servers. You can shut down the source servers in the cutover window. Shutting down the source servers manually could take five minutes per server, and, for large waves, it could take a few hours in total. Instead, you can run this automation script to shut down all your servers in the given wave.

Use the following procedure from the migration automation server to shut down all the source servers involved with the migration.

1. Signed in as an administrator, open a command prompt (`CMD.exe`).

1. Navigate to the `c:\migrations\scripts\script_mgn_3-Shutdown-all-servers` folder and run the following Python command:

   ```
   Python 3-Shutdown-all-servers.py -Waveid <wave-id>
   ```

1. Replace {{<wave-id>}} with the appropriate Wave ID value to shut down the source servers.

1. The script returns a listing of the server list and Instance IDs for the specified wave.

1. The script first shuts down Windows servers in the specified wave. After the Windows servers are shut down, the script proceeds to the Linux environment and prompts for the login credentials. After successful login, the script shuts down the Linux servers.

## Retrieve the target instance IP
<a name="retrieve-the-target-instance-ip"></a>

This activity retrieves the target instance IP. If the DNS update is a manual process in your environment, you would need to get the new IP addresses for all the target instances. However, you can use the automation script to export the new IP addresses for all the instances in the given wave to a CSV file.

Use the following procedure from the migration automation server to retrieve the target instance Ips.

1. Signed in as an administrator, open a command prompt (`CMD.exe`).

1. Navigate to the `c:\migrations\scripts\script_mgn_4-Get-instance-IP` folder and run the following Python command:

```
Python 4-Get-instance-IP.py --Waveid <wave-id>
```

Replace {{<wave-id>}} with the appropriate Wave ID value to get the new IP addresses for the target instances.

1. The script returns a server list and the target instance ID information.

1. The script will then return the target server IP.

The script exports the server name and IP addresses information to a CSV file ({{<wave-id>}}-{{<project-name>}}-Ips.csv) and places it in the same directory as your migration script (`c:\migrations\scripts\script_mgn_4-Get-instance-IP`).

The CSV file provides **instance\_name** and **instance\_Ips** details. If the instance contains more than one NIC or IP, they will all be listed and separated by commas.

## Verify the target server connections
<a name="verify-the-target-server-connections"></a>

This activity verifies the connections for the target server. After you update the DNS records, you can connect to the target instances with the host name. In this activity, you check to determine if you can log in to the operating system by using Remote Desktop Protocol (RDP) or through Secure Shell (SSH) access. You can manually log in to each server individually, but it is more efficient to test the server connection by using the automation script.

Use the following procedure from the migration automation server to verify the connections for the target server.

1. Logged in as an administrator, open a command prompt (`CMD.exe`).

1. Navigate to the `c:\migrations\scripts\script_mgn_4-Verify-server-connection` folder and run the following Python command:

```
Python 4-Verify-server-connection.py --Waveid <wave-id>
```

Replace {{<wave-id>}} with the appropriate Wave ID value to get the new IP addresses for the target instances.

**Note**
This script uses the default RDP port 3389 and SSH port 22. If needed, you can add the following arguments to reset to the default ports: --RDPPort {{<rdp-port>}} --SSHPort {{<ssh-port>}}.

1. The script returns a server list.

1. The script returns the test results for both RDP and SSH access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
