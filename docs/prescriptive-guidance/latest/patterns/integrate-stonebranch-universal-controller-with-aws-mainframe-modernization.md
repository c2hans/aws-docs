---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-stonebranch-universal-controller-with-aws-mainframe-modernization.html
---

# Integrate Stonebranch Universal Controller with AWS Mainframe Modernization
<a name="integrate-stonebranch-universal-controller-with-aws-mainframe-modernization"></a>

*Vaidy Sankaran and Pablo Alonso Prieto, Amazon Web Services*

*Robert Lemieux and Huseyin Gomleksizoglu, Stonebranch*

## Summary
<a name="integrate-stonebranch-universal-controller-with-aws-mainframe-modernization-summary"></a>

Note: AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

This pattern explains how to integrate [Stonebranch Universal Automation Center (UAC) workload orchestration](https://www.stonebranch.com/stonebranch-platform/universal-automation-center) with [Amazon Web Services (AWS) Mainframe Modernization service](https://aws.amazon.com/mainframe-modernization/). AWS Mainframe Modernization service migrates and modernizes mainframe applications to the AWS Cloud. It offers two patterns: [AWS Mainframe Modernization Replatform](https://aws.amazon.com/mainframe-modernization/patterns/replatform/) with Micro Focus Enterprise technology and [AWS Mainframe Modernization Automated Refactor](https://aws.amazon.com/mainframe-modernization/patterns/refactor/?mainframe-blogs.sort-by=item.additionalFields.createdDate&mainframe-blogs.sort-order=desc) with AWS Blu Age.

Stonebranch UAC is a real-time IT automation and orchestration platform. UAC is designed to automate and orchestrate jobs, activities, and workflows across hybrid IT systems, from on-premises to AWS. Enterprise clients using mainframe systems are transitioning to cloud-centric modernized infrastructures and applications. Stonebranch’s tools and professional services facilitate the migration of existing schedulers and automation capabilities to the AWS Cloud.

When you migrate or modernize your mainframe programs to the AWS Cloud using AWS Mainframe Modernization service, you can use this integration to automate batch scheduling, increase agility, improve maintenance, and decrease costs.

This pattern provides instructions for integrating [Stonebranch scheduler](https://www.stonebranch.com/) with mainframe applications migrated to the AWS Mainframe Modernization service Micro Focus Enterprise runtime. This pattern is for solutions architects, developers, consultants, migration specialists, and others working in migrations, modernizations, operations, or DevOps.

**Targeted outcome**

This pattern focuses on providing the following target outcomes:
+ The ability to schedule, automate, and run mainframe batch jobs running in AWS Mainframe Modernization service (Microfocus runtime) from Stonebranch Universal Controller.
+ Monitor the application’s batch processes from the Stonebranch Universal Controller.
+ Start/Restart/Rerun/Stop batch processes automatically or manually from the Stonebranch Universal Controller.
+ Retrieve the results of the AWS Mainframe Modernization batch processes.
+ Capture the [AWS CloudWatch](https://aws.amazon.com/cloudwatch/) logs of the batch jobs in Stonebranch Universal Controller.

## Prerequisites and limitations
<a name="integrate-stonebranch-universal-controller-with-aws-mainframe-modernization-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A Micro Focus [Bankdemo](https://d1vi4vxke6c2hu.cloudfront.net/demo/bankdemo_runtime.zip) application with job control language (JCL) files, and a batch process deployed in a AWS Mainframe Modernization service (Micro Focus runtime) environment
+ Basic knowledge of how to build and deploy a mainframe application that runs on Micro Focus [Enterprise Server](https://www.microfocus.com/media/data-sheet/enterprise_server_ds.pdf)
+ Basic knowledge of Stonebranch Universal Controller
+ Stonebranch trial license (contact [Stonebranch](https://www.stonebranch.com/))
+ Windows or Linux Amazon Elastic Compute Cloud (Amazon EC2) instances (for example, xlarge) with a minimum of four cores, 8 GB memory, and 2 GB disk space
+ Apache Tomcat version 8.5.x or 9.0.x
+ Oracle Java Runtime Environment (JRE) or OpenJDK version 8 or 11
+ [Amazon Aurora MySQL–Compatible Edition](https://aws.amazon.com/rds/aurora/)
+ [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket for export repository
+ [Amazon Elastic File System (Amaon EFS)](https://aws.amazon.com/efs/) for agent Stonebranch Universal Message Service (OMS) connections for high availability (HA)
+ Stonebranch Universal Controller 7.2 Universal Agent 7.2 Installation Files
+ AWS Mainframe Modernization [task scheduling template](https://github.com/aws-samples/aws-mainframe-modernization-stonebranch-integration/releases) (latest released version of the .zip file)

**Limitations**
+ The product and solution has been tested and compatibility validated only with OpenJDK 8 and 11.
+ The [aws-mainframe-modernization-stonebranch-integration](https://github.com/aws-samples/aws-mainframe-modernization-stonebranch-integration/releases) task scheduling template will work only with AWS Mainframe Modernization service.
+ This task scheduling template will work on only a Unix, Linux, or Windows edition of Stonebranch agents.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="integrate-stonebranch-universal-controller-with-aws-mainframe-modernization-architecture"></a>

**Target state architecture**

The following diagram shows the example AWS environment that is required for this pilot.

![Stonebranch UAC interacting with AWS Mainframe Modernization environment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01c6f9fa-87e6-459a-b694-5e03dd7f7952/images/4a7bea37-0a5b-4663-902b-9b051e92f0cb.png)

1. Stonebranch Universal Automation Center (UAC) includes two main components: Universal Controller and Universal Agents. Stonebranch OMS is used as a message bus between the controller and individual agents.

1. Stonebranch UAC Database is used by Universal Controller. The database can be MySQL, Microsoft SQL Server, Oracle, or Aurora MySQL–Compatible.

1. AWS Mainframe Modernization service – Micro Focus runtime environment with the [BankDemo application deployed](https://aws.amazon.com/blogs/aws/modernize-your-mainframe-applications-deploy-them-in-the-cloud/). The BankDemo application files will be stored in an S3 bucket. This bucket also contains the mainframe JCL files.

1. Stonebranch UAC can run the following functions for the batch run:

   1. Start a batch job using the JCL file name that exists in the S3 bucket linked to the AWS mainframe modernization service.

   1. Get the status of the batch job run.

   1. Wait until the batch job run is completed.

   1. Fetch logs of the batch job run.

   1. Rerun the failed batch jobs.

   1. Cancel the batch job while the job is running.

1. Stonebranch UAC can run the following functions for the application:

   1. Start Application

   1. Get Status of the Application

   1. Wait until the Application is started or stopped

   1. Stop Application

   1. Fetch Logs of Application operation

**Stonebranch jobs conversion**

The following diagram represents Stonebranch’s job conversion process during the modernization journey. It describes how the job schedules and tasks definitions are converted into a compatible format that can run AWS Mainframe Modernization batch tasks.

![Process from the mainframe to conversion to job scheduler on Amazon EC2 with JCL files in Amazon S3.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01c6f9fa-87e6-459a-b694-5e03dd7f7952/images/4d2ed890-f143-455e-8180-4d967b71c494.png)

1. For the conversion process, the job definitions are exported from the existing mainframe system.

1. JCL files can be uploaded to the S3 bucket for the Mainframe Modernization application so that these JCL files can be deployed by the AWS Mainframe Modernization service.

1. The conversion tool converts the exported job definitions to UAC tasks.

1. After all the task definitions and job schedules are created, these objects will be imported to the Universal Controller. The converted tasks then run the processes in the AWS Mainframe Modernization service instead of running them on the mainframe.

**Stonebranch UAC architecture**

The following architecture diagram represents an active-active-passive model of high availability (HA) Universal Controller. Stonebranch UAC is deployed in multiple Availability Zones to provide high availability and support disaster recovery (DR).

![Multi-AZ environment with DR and controllers, Amazon EFS, Aurora, and an S3 bucket for backups.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01c6f9fa-87e6-459a-b694-5e03dd7f7952/images/3f94b855-c146-4fcb-902c-5d343438a558.png)

*Universal Controller*

Two Linux servers are provisioned as Universal Controllers. Both connect to the same database endpoint. Each server houses a Universal Controller application and OMS. The most recent version of Universal Controller is used at the time it is provisioned.

The Universal Controllers are deployed in the Tomcat webapp as the document ROOT and are served on port 80. This deployment eases the configuration of the frontend load balancer.

HTTP over TLS or HTTPS is enabled using the Stonebranch wildcard certificate (for example, `https://customer.stonebranch.cloud`). This secures communication between the browser and the application.

*OMS*

A Universal Agent and OMS (Opswise Message Service) reside on each Universal Controller server. All deployed Universal Agents from the customer end are set up to connect to both OMS services. OMS acts as a common messaging service between the Universal Agents and the Universal Controller.

Amazon EFS mounts a spool directory on each server. OMS uses this shared spool directory to keep the connection and task information from controllers and agents. OMS works in a high-availability mode. If the active OMS goes down, the passive OMS has access to all the data, and it resumes active operations automatically. Universal Agents detect this change and automatically connect to the new active OMS.

*Database*

Amazon Relational Database Service (Amazon RDS) houses the UAC database, with Amazon Aurora MySQL–Compatible as its engine. Amazon RDS is helps in managing and offering scheduled backups at regular intervals. Both Universal Controller instances connect to the same database endpoint.

*Load balancer*

An Application Load Balancer is set-up for each instance. The load balancer directs traffic to the active controller at any given moment. Your instance domain names point to the respective load balancer endpoints.

*URLs*

Each of your instances has a URL, as shown in the following example.

|
|
| Environment | Instance |
| --- |--- |
| **Production** | `customer.stonebranch.cloud` |
| **Development (non-production)** | `customerdev.stonebranch.cloud` |
| **Testing (non-production)** | `customertest.stonebranch.cloud` |

**Note**
  Non-production instance names can be set based on your needs.

*High availability*

High availability (HA) is the ability of a system to operate continuously without failure for a designated period of time. Such failures include, but are not limited to, storage, server communication response delays caused by CPU or memory issues, and networking connectivity.

To meet HA requirements:
+ All EC2 instances, databases, and other configurations are mirrored across two separate Availability Zones within the same AWS Region.
+ The controller is provisioned through an Amazon Machine Image (AMI) on two Linux servers in the two Availability Zones. For example, if you are provisioned in the Europe eu-west-1 Region, you have a Universal Controller in Availability Zone eu-west-1a and Availability Zone eu-west-1c.
+ No jobs are allowed to run directly on the application servers and no data is allowed to be stored on these servers.
+ The Application Load Balancer runs health checks on each Universal Controller to identify the active one and direct traffic to it. In the event that one server incurs issues, the load balancer automatically promotes the passive Universal Controller to an active state. The load balancer then identifies the new active Universal Controller instance from the health checks and starts directing traffic. The failover happens within four minutes with no job loss, and the frontend URL remains the same.
+ The Aurora MySQL–Compatible database service stores Universal Controller data. For production environments, a database cluster is built with two database instances in two different Availability Zones within a single AWS Region. Both Universal Controllers use a Java Database Connectivity (JDBC) interface that points to a single database cluster endpoint. In the event that one database instance incurs issues, the database cluster endpoint dynamically points to the healthy instance. No manual intervention is required.

*Backup and purge*

Stonebranch Universal Controller is set to back up and purge old data following the schedule shown in the table.

|
|
| Type | Schedule |
| --- |--- |
| **Activity** | 7 days |
| **Audit** | 90 days |
| **History** | 60 days |

Backup data older than the dates shown is exported to .xml format and stored in the file system. After the backup process is complete, older data is purged from the database and archived in an S3 bucket for up to one year for production instances.

You can adjust this schedule in your Universal Controller interface. However, increasing these time-frames might cause a longer downtime during maintenance.

## Tools
<a name="integrate-stonebranch-universal-controller-with-aws-mainframe-modernization-tools"></a>

**AWS services**
+ [AWS Mainframe Modernization](https://docs.aws.amazon.com/m2/latest/userguide/what-is-m2.html) is an AWS cloud-native platform that helps you modernize your mainframe applications to AWS managed runtime environments. It provides tools and resources to help you plan and implement migration and modernization.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block-level storage volumes for use with Amazon EC2 instances.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud. This pattern uses Amazon Aurora MySQL–Compatible Edition.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon EC2 instances, containers, and IP addresses in one or more Availability Zones. This pattern uses an Application Load Balancer.

**Stonebranch**
+ [Universal Automation Center (UAC)](https://stonebranchdocs.atlassian.net/wiki/spaces/SD/pages/239239169/Universal+Automation+Center) is a system of enterprise workload automation products. This pattern uses the following UAC components:
  + [Universal Controller](https://www.stonebranch.com/documentation-universal-controller), a Java web application running in a Tomcat web container, is the enterprise job scheduler and workload automation broker solution of Universal Automation Center. The Controller presents a user interface for creating, monitoring, and configuring Controller information; handles the scheduling logic; processes all messages to and from Universal Agents; and synchronizes much of the high availability operation of Universal Automation Center.
  + [Universal Agent](https://www.stonebranch.com/documentation-universal-agent) is a vendor-independent scheduling agent that collaborates with existing job scheduler on all major computing platforms, both legacy and distributed. All schedulers that run on z/Series, i/Series, Unix, Linux, or Windows are supported.
+ [Universal Agent](https://www.stonebranch.com/documentation-universal-agent) is a vendor-independent scheduling agent that collaborates with existing job scheduler on all major computing platforms, both legacy and distributed. All schedulers that run on z/Series, i/Series, Unix, Linux, or Windows are supported.
+ [Stonebranch aws-mainframe-modernization-stonebranch-integration AWS Mainframe Modernization Universal Extension](https://github.com/aws-samples/aws-mainframe-modernization-stonebranch-integration/releases) is the integration template to run, monitor and rerun batch jobs in AWS Mainframe Modernization platform.

**Code**

The code for this pattern is available in the [aws-mainframe-modernization-stonebranch-integration](https://github.com/aws-samples/aws-mainframe-modernization-stonebranch-integration/releases/) GitHub repository.

## Epics
<a name="integrate-stonebranch-universal-controller-with-aws-mainframe-modernization-epics"></a>

### Install Universal Controller and Universal Agent on Amazon EC2
<a name="install-universal-controller-and-universal-agent-on-amazon-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the installation files. | Download the installation from Stonebranch servers. To get the installation files, contact with Stonebranch. | Cloud architect |
| Launch the EC2 instance. | You will need about 3 GB of extra space for the Universal Controller and Universal Agent installations. So provide at least 30 GB of disk space for the instance.<br />Add port 8080 to the security group so that it’s accessible. | Cloud architect |
| Check prerequisites. | Before the installation, do the following:1. Install Java as described in [Downloading Java Runtime Environment](https://www.stonebranch.com/documentation-java-runtime).<pre>$ sudo yum -y update<br />$ sudo yum install java-11-amazon-corretto</pre><br />Be sure to use one of the supported JAVA versions. The previous command should install java-11. Check the Java version and be sure you are using version 11 before continuing.<br />2. As described in [Installing Apache Tomcat](https://www.stonebranch.com/documentation-apache-tomcat), run the following commands.<pre>$ sudo yum install tomcat tomcat-admin-webapps<br />$ sudo systemctl enable tomcat<br />$ sudo systemctl start tomcat</pre><br />3. Create an Amazon Aurora database as described in [Creating and connecting to an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.Aurora.html). Use Amazon Aurora MySQL-Compatible Edition.<br />Choose a Master username and Master password. Keep the default values for the rest of the settings. | Cloud administrator, Linux administrator |
| Install Universal Controller. | 1. Upload the `universal-controller-7.2.0.0.tar`** **installation file to the EC2 instance.<br />2. Unarchive the installation files to a `temp` folder.<pre>$ tar -xvf universal-controller-7.2.0.0.tar</pre><br />3. Give the installation script run permission.<pre>$ chmod a+x install-controller.sh</pre><br />4. Install the controller. This example uses the following command to install Universal Controller under `/usr/share/tomca`t. Use the Amazon Aurora database that you created in the previous steps.<pre>$ sudo ./install-controller.sh --tomcat-dir /usr/share/tomcat/ --controller-file universal-controller-7.2.0.0-build.145.war --dbuser admin --dbpass "****" --dbname uc --rdbms mysql --dburl jdbc:mysql://database-2-instance-1.cih63miincgy.us-east-1.rds.amazonaws.com:3306/</pre><br />The last line of the output of the script should be "Installation complete."<br />5. Navigate to the following URL in the EC2 instance.<pre>http://<public_ip>:8080/uc</pre><br />6. On the login screen, enter **ops.admin** in the **Username** section, and keep the **Password** field empty.<br />7. Set a new password for the `ops.admin` user. | Cloud architect, Linux administrator |
| Install Universal Agent. | 1. Upload the `sb-7.2.0.1-linux-3.10-x86_64.tar.Z` installation file to the EC2 instance.<br />2. Log in to the EC2 instance.<br />3. Unarchive the Universal Agent installation package.<pre>$ zcat sb-7.2.0.1-linux-3.10-x86_64.tar.Z | tar xvf –</pre><br />4. Run the following command.<pre>$ sudo ./unvinst --oms_servers 7878@localhost --oms_autostart yes --python yes</pre><br />5. Create a PAM file.<pre>$ cp /etc/pam.d/login /etc/pam.d/ucmd</pre><br />6. Enable Autostart for Universal Agent.<pre>$ /sbin/restorecon -v /etc/rc.d/init.d/ubrokerd</pre> | Cloud administrator, Linux administrator |
| Add OMS to Universal Controller. | 1. Log in to Universal Controller with the `ops.admin` user.<br />2. Choose the **Services** menu at the top left corner of the screen, and then choose the **OMS Servers** menu in the **System**<br />3. In the OMS Server Address field, type `localhost`, and then save.<br />4. You will see the status of the OMS server as **Connected** and the **Session Status** as **Operational**. | Universal Controller administrator |

### Import AWS Mainframe Modernization Universal Extension and create a task
<a name="import-aws-mainframe-modernization-universal-extension-and-create-a-task"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Import Integration Template. | For this step, you need the [AWS Mainframe Modernization Universal Extension](https://github.com/aws-samples/aws-mainframe-modernization-stonebranch-integration/releases). Ensure the latest released version of the .zip file is downloaded.1. Log in to the Universal Controller with the `ops.admin` user.<br />2. Navigate to **Services**, **Import Integration Template**.<br />3. Select the Integration Template .zip file (`aws_mainframe_modernization_stonebranch_extension.zip`), and choose **Import**.<br />After the Integration Template is imported, you will see **AWS Mainframe Modernization Tasks** under **Available Services**. | Universal Controller administrator |
| Enable resolvable credentials. | 1. Navigate to **Services**, **AWS Mainframe Modernization Tasks**.<br />2. On the right panel, fill in the required fields:**Name**: New Mainframe Modernization Task**Agent**: Select the only agent (AGNT0001).<br />Under **AWS Mainframe Modernization Details**:**Action**: List Environments**AWS Credentials**: If you have an AWS Identity and Access Management (IAM) role added to the EC2 instance, you can keep this field empty. If you will use `AWSAccessKeyID` and `AWSSecretKey`, choose the icon **()** next to the field.<br />In the **Credential Details** window that opens, enter the following information and then save.**Name**: AWS Mainframe Modernization Credentials**Runtime User**: Write the AWS access key ID in this field.**Runtime Password**: Write the AWS secret key in this field.**End Point**:** **Be sure that the endpoint has the correct AWS Region. The default is `https://m2.us-east-1.amazonaws.com`.**Region**: Enter the Region of the AWS Mainframe Modernization service. The default is `us-east-1`.<br />3. Keep the default values in the rest of the fields, and save the task. | Universal Controller administrator |
| Launch the task. | 1. At the top of the right panel, choose **Launch Task**.<br />2. In the **Confirm** window, choose **Launch**. After that, the Universal Controller Console will display a message similar to the following message.<br />*2022-08-24 10:11:49 AM*<br />*Successfully launched the Universal task "New Mainframe Modernization Task" with task instance sys\_id 1661291493634146313NC8E38DB8OZJY.*<br />3. Navigate to the **Instances** If you don’t see the **Instances** tab, choose the right arrow to scroll right.<br />4. Open the context (right-click) menu for the task instance in the list, choose **Retrieve Output**, and then choose **Submit** in the **Retrieve Output**<br />5. In the **Retrieve Output** window, you will see the list of environments in STDOUT. | Universal Controller administrator |

### Test starting a batch job
<a name="test-starting-a-batch-job"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a task for the batch job. | 1. Navigate to **Services**, **AWS Mainframe Modernization Tasks**.<br />2. On the right panel, fill in the required fields:**Name**: New Mainframe Modernization Task**Agent**: Select the only agent (AGNT0001).<br />Under **AWS Mainframe Modernization Details**:**Action**: Start Batch (or Start Batch and Wait to run the batch job and wait until the task completes in AWS)**AWS Credentials**: If you have an IAM role added to the EC2 instance, you can keep this field empty. If you will use `AWSAccessKeyID` and `AWSSecretKey`, choose the icon **()** next to the field.**End Point**:** **Be sure that the endpoint has the correct AWS Region. The default is [https://m2.us-east-1.amazonaws.com](https://m2.us-east-1.amazonaws.com).**Region**: Enter the Region of the AWS Mainframe Modernization service. The default is `us-east-1`.**Application**: Choose the icon next to the field **()**, and choose **Submit** in the **Refresh Application Choices**. This will connect to the AWS Mainframe Modernization service and return the list of applications. Now you can select the application from the dropdown list. Select the application you want to run the batch job.**JCL File Name**: `RUNHELLO.jcl`**Wait for Success or Failure**:** **If this option is selected, the task will wait until the status of the batch job is success or failure.**Polling Interval**: This is the amount of time between each polling.**Fetch Execution Logs**: If selected, logs will be fetched automatically when the batch job has completed.**Log Format**: This is the format of the logs to be printed out. It can be Text or JSON format.<br />3. Keep the default values in the rest of the fields, and save the task. | Universal Controller administrator |
| Launch the task. | 1. At the top of the right panel, choose **Launch Task**.<br />2. In the **Confirm** window, choose **Launch**. After that, the Universal Controller Console will display a message similar to the following message.<br />*2022-08-24 11:11:59 AM*<br />*Successfully launched the Universal task "Mainframe Modernization Start Batch" with task instance sys\_id <sys id>.*<br />3. Navigate to the **Instances** If you don’t see the **Instances** tab, choose the right arrow to scroll right.<br />4. Open the context (right-click) menu for the task instance in the list, choose **Retrieve Output**, and then choose **Submit** in the **Retrieve Output**<br />5. In the **Retrieve Output** window, you will see the list of environments in STDOUT. | Universal Controller administrator |

### Create a workflow for multiple tasks
<a name="create-a-workflow-for-multiple-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Copy the tasks. | 1. Open the context (right click) menu for the task that you want to create copies of, and choose **Copy**.<br />2. In the **Copy AWS Mainframe Modernization Task** window enter the following new name for the new task: Mainframe Modernization Start Batch - *RUNAWS2.*<br />3. Copy the task again, using the following name: Mainframe Modernization Start Batch - *RUNAWS3.*<br />4. Copy with the task again, using the following name: Mainframe Modernization Start Batch - *RUNAWS4.*<br />5. Copy the task a final time, using the following name: Mainframe Modernization Start Batch - *FOOBAR.* | Universal Controller administrator |
| Update tasks. | 1. Open (double-click) the Mainframe Modernization Start Batch - RUNAWS2 task, change the **JCL File Name** field to `RUNAWS2.jcl`, and save.<br />2. Open (double-click) the Mainframe Modernization Start Batch - RUNAWS3 task, change the **JCL File Name** field to `RUNAWS3.jcl`*, *and save.<br />3. Open (double-click) the Mainframe Modernization Start Batch - RUNAWS4 task, change the **JCL File Name** field to `RUNAWS4.jcl`*,* and save.<br />4. Open (double-click) the Mainframe Modernization Start Batch - FOOBAR task, change the **JCL File Name** field to `MISSING.jcl`*,* and save. **This task will fail because the JCL File Name value is incorrect.** | Universal Controller administrator |
| Create a workflow. | 1. Navigate to **Services**, **Workflows**.<br />2. On the right panel, enter **Mainframe Modernization Workflow** in the **Name** field, and save.<br />3. In the right panel, choose **Edit Workflow**.<br />4. On the **Workflow Editor Tab**, the** Add Task** button **(\+)**.<br />5. In the **Task Find** window, choose **Search** to see all the tasks in the Universal Controller.<br />6. Click the icon next to Mainframe Modernization Start Batch Task, and drag the icon into an empty place in the **Workflow Editor**.<br />7. Repeat the same action for the other Mainframe Modernization tasks and place them as shown in the *Additional information* section.<br />8. Choose the **Connect** button **()**, and connect the tasks together. To connect a task with another, click in the middle of a task, and drag it to the target task.<br />9. Connect the tasks as shown in the *Additional information* section, and save the workflow.<br />10. Right-click an empty place in the Workflow Editor, choose **Launch Workflow**, and then choose **OK**. | Universal Controller administrator |
| Check the status of the workflow. | 1. On the left menu, choose the **Activity**<br />2. In the middle of the window, choose **Start**.<br />You will see the list of task instances in the list.<br />3. Open (double-click) Mainframe Modernization Workflow in the list, or open the context (right-click) menu and choose **Workflow Task Commands**, **View Workflow**.<br />You will see the tasks as shown in the Additional information section. The second task was expected to fail because you used a missing JCL file. | Univeral Controller administrator |

### Troubleshoot failed batch jobs and rerun
<a name="troubleshoot-failed-batch-jobs-and-rerun"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Fix the failed task and rerun. | 1. Open (double-click) the failed task to see the error for the task.<br />2. You have two options for fixing the failed task.Fix the JCL file name, and set it to `FOOBAR.jcl`.Add the correct JCL file name to the **JCL File Name (Temp)**. This field will overwrite the **JCL File Name** field.<br />For this pilot, choose the second option, and save the task instance.<br />3. In the **Workflow Monitor**, open the context (right-click) menu for the failed task, and choose **Commands**, **Re-run**.<br />4. After that, all the tasks will complete successfully. | Universal Controller administrator |

### Create Start Application and Stop Application tasks
<a name="create-start-application-and-stop-application-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Start Application action. | 1. Navigate to **Services**, **AWS Mainframe Modernization Tasks**.<br />2. On the right panel, fill in the required fields.**Name**: Mainframe Modernization Start Application**Agent**: Select the only agent (AGNT0001)<br />Under **AWS Mainframe Modernization Details**:**Action**:** **Start Application**AWS Credentials**: If you have an IAM role added to the EC2 instance, you can keep this field empty. If you will use `AWSAccessKeyID` and `AWSSecretKey`, select the credential that you created before.**End Point**:** **Be sure that the endpoint has the correct Region. The default is `https://m2.us-east-1.amazonaws.com`.**Region**: Enter the Region of the AWS Mainframe Modernization service. The default is `us-east-1`.**Application**: Choose the icon next to the field **()**, and choose **Submit** in the **Refresh Application Choices**. This will connect to the AWS Mainframe Modernization service and return the list of applications. Now you can select the application from the dropdown list. Select the application you want to run the batch job.**Wait for Success or Failure**:** **If this option is selected, the task will wait until the status of the batch job is success or failure.**Polling Interval**: This is the amount of time between each polling.**Fetch Execution Logs**: If selected, logs will be fetched automatically when the batch job has completed.**Log Format:** This is the format of the logs to be printed out. It can be Text or JSON format.<br />3. Keep the default values in the rest of the fields, and save the task.<br />4. Now copy this task and create a task for Stop Application. Change the name to **Mainframe Moderinization Stop Application**, and change the action to **Stop Application**. | Universal Controller administrator |

### Create a Cancel Batch Execution task
<a name="create-a-cancel-batch-execution-task"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Cancel Batch action. | 1. Navigate to **Services**, **AWS Mainframe Modernization Tasks**.<br />2. On the right panel, fill in the required fields.**Name**: Mainframe Modernization Cancel Batch Execution**Agent**: Select the only agent (AGNT0001)<br />Under **AWS Mainframe Modernization Details**:**Action**:** **Cancel Batch Execution**AWS Credentials**: If you have an IAM role added to the EC2 instance, you can keep this field empty. If you will use `AWSAccessKeyID` and `AWSSecretKey`, select the credential that you created before.**End Point**:** **Be sure that the endpoint has the correct Region. The default is `https://m2.us-east-1.amazonaws.com`.**Region**: Enter the Region of the AWS Mainframe Modernization service. The default is `us-east-1`.**Application**: Choose the icon next to the field **()**, and choose **Submit** in the **Refresh Application Choices**. This will connect to the AWS Mainframe Modernization service and return the list of applications. Now you can select the application from the dropdown list. Select the application you want to run the batch job.**Wait for Success or Failure**:** **If this option is selected, the task will wait until the status of the batch job is success or failure.**Polling Interval**: This is the amount of time between each polling.**Fetch Execution Logs**: If selected, logs will be fetched automatically when the batch job has completed.**Log Format**: This is the format of the logs to be printed out. It can be Text or JSON format.<br />3. Keep the default values in the rest of the fields, and save the task. |  |

## Related resources
<a name="integrate-stonebranch-universal-controller-with-aws-mainframe-modernization-resources"></a>
+ [Universal Controller](https://stonebranchdocs.atlassian.net/wiki/spaces/UC77/overview)
+ [Universal Agent](https://stonebranchdocs.atlassian.net/wiki/spaces/UA77/overview)
+ [LDAP Settings](https://stonebranchdocs.atlassian.net/wiki/spaces/UC77/pages/794552355/LDAP+Settings)
+ [SAML Single Sign-On](https://stonebranchdocs.atlassian.net/wiki/spaces/UC77/pages/794553130/SAML+Single+Sign-On)
+ [Xpress Conversion Tool](https://www.stonebranch.com/resources/xpress-conversion-windows)

## Additional information
<a name="integrate-stonebranch-universal-controller-with-aws-mainframe-modernization-additional"></a>

**Icons in the Workflow Editor**

![RUNHELLO task at the top, FOOBAR in the middle, and the remaining tasks at the third level.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01c6f9fa-87e6-459a-b694-5e03dd7f7952/images/837430ee-3159-4fe2-8e17-65168294ef1e.png)

**All tasks connected**

![RUNHELLO connects to FOOBAR, which connects to the three remaining tasks.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01c6f9fa-87e6-459a-b694-5e03dd7f7952/images/fe483348-9a6f-450b-87e6-ceae6b2bdaad.png)

**Workflow status**

![FOOBAR task fails and the remaining three tasks are waiting.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01c6f9fa-87e6-459a-b694-5e03dd7f7952/images/5ea4e239-fbbe-4fa4-9ffa-b7a9443b7975.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
