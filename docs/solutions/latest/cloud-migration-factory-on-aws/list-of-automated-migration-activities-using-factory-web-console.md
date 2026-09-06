---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html
---

# List of automated migration activities using Migration Factory web console
<a name="list-of-automated-migration-activities-using-factory-web-console"></a>

The Cloud Migration Factory on AWS solution deploys automated migration activities that you can leverage for your migration projects. You can follow the migration activities listed below and customize them based on your business needs.

Before starting any of the activities, make sure that you read [User Guide - Run Automation from console](run-automation-from-console.md) to understand how this works. Also, you must [Build an Automation server](configure-migration-automation-server.md) and [create Windows and Linux users](credentials-management.md) to run automation from the console.

Use the following procedures in the same order to conduct a complete test run of the solution using the sample automation script and activities.

## Check prerequisites
<a name="prerequisites-2"></a>

Connect with the in-scope source servers to verify the necessary prerequisites such as TCP 1500, TCP 443, root volume free space, .Net framework version, and other parameters. These prerequisites are required for replication.

Before you can conduct the prerequisites check, you must install the first manually on one source server, so this will create a replication server in EC2. We will connect to this server for port 1500 testing. After installation, AWS Application Migration Service (AWS MGN) creates the replication server in Amazon Elastic Compute Cloud (Amazon EC2). You must verify the TCP port 1500 from the source server to the replication server in this activity. For information about installing the AWS MGN agent on your source servers, refer to [Installation instructions](https://docs.aws.amazon.com/mgn/latest/ug/agent-installation-instructions.html) in the *AWS Application Migration Service User Guide*.

Use the following procedure while signed in to the migration factory web console.

1. On the Migration Factory console, select **Jobs** on the left-hand side menu, and select **Actions**, and then **Run Automation** on the right-hand side.

1. Enter **Job Name**, select **0-Check MGN Prerequisites** script and your automation server to run the script. If automation server does not exist, make sure that you complete [Build a migration automation server](configure-migration-automation-server.md).

1. Select **Linux Secrets** and/or **Windows Secrets** depends on what OSs you have for this wave. Enter MGN replication server IP, choose the wave you want to run automation on and choose **Submit Automation Job.**

1. You will be redirected to the **Jobs** list page. The job status should be RUNNING. Choose **Refresh** to see the status. It should change to Complete after a few minutes.

1. The script will also update the solution’s **migration status** in the Migration Factory web interface as shown in the following screenshot of an example project.

 **Migration status**

![migration status](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/migration-status.png)

## Install the replication agents
<a name="install-the-replication-agents"></a>

**Note**
Before you install the agent, make sure that [AWS MGN is initialized in each target account](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize.html) and region.

Use the following procedure to automatically install the Replication agents in the in-scope source servers.

1. On the Migration Factory console, select **Jobs** on the left-hand side menu, and select **Actions**, and then **Run Automation** on the right-hand side.

1. Enter **Job Name**, select **1-Install MGN Agents** script and your automation server to run the script. If automation server does not exist, make sure that you complete [Build a migration automation server](configure-migration-automation-server.md).

1. Select **Linux Secrets** and/or **Windows Secrets** depends on what OSs you have for this wave. Choose the wave you want to run automation, and choose **Submit Automation Job**.

1. You will be redirected to the **Jobs** list page. The job status should be running. Choose **Refresh** to see the status. It should change to **Complete** after a few minutes.

1. The script also provides the migration status in the Migration Factory web interface as shown in the following example screenshot.

    **Migration status**
![migration status success](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/migration-status-success.png)

## Push the post-launch scripts
<a name="push-the-post-launch-scripts"></a>

AWS Application Migration Service (MGN) supports post-launch scripts to help you automate OS-level activities, such as installing/uninstalling the software after launching target instances. This activity pushes the post-launch scripts to Windows and/or Linux machines, depending on the servers identified for migration.

**Note**
Before you push the post-launch scripts, you must copy the files to a folder on the migration automation server.

Use the following procedure to push the post-launch scripts to Windows machines.

1. On the Migration Factory console, select **Jobs** on the left-hand side menu, and select **Actions**, and then **Run Automation** on the right-hand side.

1. Enter Job Name, select **1-Copy Post Launch Scripts** script and your automation server to run the script. If automation server does not exist, make sure that you complete [Build a migration automation server](configure-migration-automation-server.md).

1. Select **Linux Secrets** and/or **Windows Secrets** depends on what OSs you have for this wave. Provide a **Linux source location** and/or **Windows source location**.

1. Choose the wave you want to run automaton and choose **Submit Automation Job**.

1. You will be redirected to the **Jobs** list page, the job status should be running, and you can choose **Refresh** to see the status. It should change to **Complete** after a few minutes.

## Verify the replication status
<a name="verify-the-replication-status"></a>

This activity verifies the replication status for the in-scope source servers automatically. The script repeats every five minutes until the status of all source servers in the given wave changes to a *Healthy* status.

Use the following procedure to verify the replication status.

1. On the Migration Factory console, select **Jobs** on the left-hand side menu, and select **Actions**, and then **Run Automation** on the right-hand side.

1. Enter Job Name, select **2-Verify Replication Status** script and your automation server to run the script. If automation server does not exist, make sure that you complete [Build a migration automation server](configure-migration-automation-server.md).

1. Choose the wave you want to run automaton and choose **Submit Automation Job**.

1. You will be redirected to the **Jobs** list page, the job status should be running, and you can click **refresh** button to see the status. It should change to **Complete** after a few minutes.

 **Data replication status**

![data replication status](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/data-replication-status.png)

**Note**
Replication can take a while. You might not see the status update from the factory console for a few minutes. Optionally, you can also check the status in MGN service.

## Validate launch template
<a name="validate-launch-template-1"></a>

This activity validates the server metadata in the migration factory and makes sure it works with EC2 template and no typos. It will validate both test and cutover metadata.

Use the following procedure to validate EC2 launch template.

1. Navigate to the Migration Factory console, and select **Wave** in the menu pane.

1. Select the target wave, and choose **Actions**. Select **Rehost**, and then select **MGN**.

1. Select **Validate Launch Template \*for the \*Action**, then select All\* applications.\*

1. Choose **Submit** to initiate the validation.

After some time, the validation will return a successful result.

**Note**
If validation is not successful, you will receive a specific error message:
The errors may be due to invalid data in the server attribute such as an invalid **subnet\_IDs**, **securitygroup\_IDs**, or **instanceType**.
You can switch to the Pipeline page from the Migration Factory web interface and select the problematic server to fix the errors.

## Launch instances for testing
<a name="launch-instances-for-testing"></a>

This activity launches all target machines for a given wave in AWS Application Migration Service (MGN) in test mode.

Use the following procedure to launch test instances.

1. On the Migration Factory console, select **Wave** on the navigation menu.

1. Select target wave, and choose **Actions**. Select **Rehost**, and then select **MGN**.

1. Select **Launch Test Instances** Action, select **All applications.**

1. Choose **Submit** to launch test instances.

1. After some time, the validation will return a successful result.

 **Wave action success**

![wave action success](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/wave-action-success.png)

**Note**
This action will also update the migration status for the server launched.

## Verify the target instance status
<a name="verify-the-target-instance-status"></a>

This activity verifies the status of the target instance by checking the boot up process for all in-scope source servers in the same wave. It may take up to 30 minutes for the target instances to boot up. You can check the status manually by logging into the Amazon EC2 console, searching for the source server name, and checking the status. You will receive a health check message stating *2/2 checks passed*, which indicates that the instance is healthy from an infrastructure perspective.

However, for a large-scale migration, it’s time consuming to check the status of each instance, so you can run this automated script to verify the *2/2 checks passed* status for all source servers in a given wave.

Use the following procedure to verify the status of the target instance.

1. Navigate to the Migration Factory console, and select **Jobs** on the left-hand side menu.

1. Select **Actions**, then **Run Automation** on the right-hand side.

1. Enter **Job Name**, select **3-Verify Instance Status** script and your automation server to run the script. If automation server does not exist, ensure that you complete [Build a migration automation server](configure-migration-automation-server.md).

1. Choose the wave you want to run automaton, and choose **Submit Automation Job**.

1. You will be redirected to the **Jobs** list page, the job status should be running, and you can choose **Refresh** to see the status. It should change to **Complete** after a few minutes.

 **AWS Migration Management dashboard showing server list with migration status for 5 servers.**

![migration 2by2 status](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/migration-2by2-status.png)

**Note**
Instance boot up can take a while and you might not see the status update from the factory console for a few minutes. Migration factory also receives a status update from the script. Refresh the screen if necessary.

**Note**
If your target instances fail the 2/2 health checks the first time, it may be due to the boot up process taking longer to complete. We recommend running the health checks a second time about an hour after the first health check. This ensures that the boot up process completes. If the health checks fail this second time, go to the [AWS support center](https://console.aws.amazon.com/support/home) to log a support case.

## Mark as ready for cutover
<a name="mark-as-ready-for-cutover"></a>

Once testing is finished, this activity changes the status of the source server to mark as ready for cutover, so that user is able to launch a cutover instance.

Use the following procedure to validate EC2 launch template.

1. On the Migration Factory console, and select **Wave** on the left-hand side.

1. Select target wave, and click **Actions** button. Select **Rehost**, and then select **MGN**.

1. Select **Mark as Ready for Cutover** Action, select **All applications.**

1. Choose **Submit** to launch live instances.

After some time, the validation will return a successful result.

 **Wave action ready for cutover**

![wave action ready cutover](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/wave-action-ready-cutover.png)

## Shut down the in-scope source servers
<a name="shut-down-the-in-scope-source-servers"></a>

This activity shuts down the in-scope source servers involved with the migration. After you verify the source servers' replication status, you are ready to shut down the source servers to stop transactions from the client applications to the servers. You can shut down the source servers in the cutover window. Shutting down the source servers manually could take five minutes per server, and, for large waves, it could take a few hours in total. Instead, you can run this automation script to shut down all your servers in the given wave.

Use the following procedure to shut down all the source servers involved with the migration.

1. On the Migration Factory console, select **Jobs** on the left-hand side menu, and select **Actions**, and then **Run Automation** on the right-hand side.

1. Enter Job Name, select **3-Shutdown All Servers** script and your automation server to run the script. If automation server does not exist, make sure that you complete [Build a migration automation server](configure-migration-automation-server.md).

1. Select **Linux Secrets** and/or **Windows Secrets** depends on what OSs you have for this wave.

1. Choose the wave you want to run automaton and choose **Submit Automation Job**.

1. You will be redirected to the **Jobs** list page, the job status should be running, and you can click **refresh** button to see the status. It should change to **Complete** after a few minutes.

## Launch instances for Cutover
<a name="launch-instances-for-cutover"></a>

This activity launches all target machines for a given wave in AWS Application Migration Service (MGN) in Cutover mode.

Use the following procedure to launch test instances.

1. On the Migration Factory console, and select **Wave** on the left-hand side.

1. Select target wave, and choose **Actions**. Select **Rehost**, and then select **MGN**.

1. Select **Launch Cutover Instances** Action, select **All applications.**

1. Choose **Submit** to launch test instances.

After some time, the validation will return a successful result.

**Note**
This action will also update the migration status for the server launched.
