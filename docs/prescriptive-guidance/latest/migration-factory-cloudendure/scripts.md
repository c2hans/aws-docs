---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/scripts.html
---

# Cloud Migration Factory automation scripts
<a name="scripts"></a>

The following diagram shows the automation scripts included in Cloud Migration Factory. These scripts cover most of the automation tasks for rehost migration using AWS Transform MGN (AWS MGN). Automation scripts can be connected to the source machines or to AWS APIs, as shown in the following diagram.

![The Cloud Migration Factory automation and orchestration scripts](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/images/guide-img/3ff8a3b6-fa4d-412f-ba5f-3d8aad3942a7/images/e800d01c-0a47-4086-a57c-be15068bedac.png)

Cloud Migration Factory includes scripts for the following phases and tasks:
+ Build phase:
  + Checking prerequisites for the migration
  + Installing replication agents for multiple servers
  + Pushing the post-launch script
+ Validate phase:
  + Monitoring replication
  + Creating the local administrator account
  + Performing a dry run
+ Test phase:
  + Testing the Amazon Elastic Compute Cloud (Amazon EC2) instance launch
  + Performing 2/2 (system status and instance status) health checks on instances
  + Terminating test instances
+ Cutover phase:
  + Shutting down servers at the source location
  + Orchestrating the cutover process
  + Verifying that all application servers are up and running

These automation scripts help you save significant time and effort in your large-scale migration tasks. For example:
+ Automating replication agent installation for 100 or more servers. Installing the replication agent on one server takes about 5 minutes. However, if you have 100 servers running Microsoft Windows and Linux for 10 different AWS accounts, there can be 20 different ways to install the agent on the source machine, and this process could take over 500 minutes. The automation script reduces the agent installation time from 500 minutes to less than 5 minutes of operator time, and it works for both Windows and Linux operating systems and any target AWS account.
+ Orchestrating the cutover process. This process involves checking the replication status, checking the server status, updating the Amazon EC2 launch templates, launching servers in cutover mode, verifying job status, cleaning up the server, and many other tasks. It is a long process even for one server, and it could be a nightmare if you have hundreds of servers in a single cutover. The Cloud Migration Factory solution automates and orchestrates the entire process for you.

These tasks and the Cloud Migration Factory scripts that automate them are described in more detail in the following sections.
