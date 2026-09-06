---
source_url: https://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/development-phase.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Development phase
<a name="development-phase"></a>

 Regardless of team size, software type being developed, or project duration, development tools are mandatory to rationalize the process, coordinate efforts, and centralize production. Like any IT system, development tools require proper administration and maintenance. Operating such tools on AWS not only relieves your development team from low-level system maintenance tasks such as network configuration, hardware setup, and so on, but also facilitates the completion of more complex tasks. The following sections describe how to operate the main components of development tools on AWS.

## Source code repository
<a name="source-code-repository"></a>

 The source code repository is a key tool for development teams. As such, it needs to be available, and the data it contains (source files under version control) needs to be durably stored, with proper backup policies. Ensuring these two characteristics— availability and durability—requires resources, expertise, and time investment that typically aren’t a core competency of a software development team.

 Building a source code repository on AWS involves creating an [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) repository. AWS CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories. It eliminates the need for you to operate your own source control system, and there is no hardware to provision and scale or software to install, configure, and operate.

 You can use CodeCommit to store anything from code to binaries, and it supports the standard functionality of GitHub, allowing it to work seamlessly with your existing GitHub-based tools. Your team can also use CodeCommit’s online code tools to browse, edit, and collaborate on projects.

 CodeCommit enables you to store any number of files, and there are no repository size limits. In a few simple steps, you can find information about a repository and clone it to your computer, creating a local repository where you can make changes and then push them to the CodeCommit repository. You can work from the command line on your local machines or use a GUI-based editor.

## Project management tools
<a name="project-management-tools"></a>

 In addition to the source code repository, teams often use additional tools such as issue tracking, project tracking, code quality analysis, collaboration, content sharing, and so on. Most of the time, those tools are provided as web applications. Like any other classic web application, they require a server to run, and frequently a relational database. The web components can be installed on [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2), with the database using [Amazon Relational Database Service](https://docs.aws.amazon.com/rds/index.html) (Amazon RDS) for data storage.

 Within minutes, you can create Amazon EC2 instances, which are virtual machines over which you have complete control. A variety of different operating systems and distributions are available as [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMIs). An AMI is a template that contains a software configuration (operating system, application server, and applications) that you can run on Amazon EC2. After you’ve properly installed and configured the project management tool, AWS recommends you create an AMI from this setup so you can quickly recreate that instance without having to reinstall and reconfigure the software.

 Project management tools have the same needs as source code repositories: they need to be available, and data has to be durably stored. While you can mitigate the loss of code analysis reports by recreating them against the desired repository version, losing project or issue tracking information might have more serious consequences. You can address the availability of the project management web application service by using AMIs to create replacement Amazon EC2 instances in case of failure.

 You can store the application’s data separately from the host system to simplify maintenance or migration operations. [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) provides off-instance storage volumes that persist independently from the life of an instance. After you create a volume, you can attach it to a running Amazon EC2 instance. As such, an Amazon EBS volume is provisioned and attached to the instance to store the data of the version control repository.

 You achieve durability by taking point-in-time snapshots of the EBS volume containing the repository data. EBS snapshots are stored in [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3), a highly durable and scalable data store. Objects in Amazon S3 are redundantly stored on multiple devices across multiple facilities in an [AWS Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html). You can automate the creation and management of snapshots using [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html).

 These snapshots can be used as the starting point for new Amazon EBS volumes, and can protect your data for long-term durability. In case of a failure, you can recreate the application data volume from the snapshots, and recreate the application instance from an AMI.

 To facilitate proper durability and restoration, [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) offers an easy way to set up, operate, and scale a relational database in AWS. It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, freeing the project team from this responsibility. [Amazon RDS Database instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.html) (DB instances) can be provisioned in a matter of minutes.

 Optionally, Amazon RDS will ensure that the relational database software stays up to date with the latest patches. The automated backup feature of Amazon RDS enables point-in-time recovery for DB instances, allowing restoration of a DB instance to any point in time within the backup retention period.

 An Elastic IP address provides a static endpoint to an Amazon EC2 instance, and can be used in combination with DNS (for example, behind a DNS [CNAME](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#CNAMEFormat)). This helps teams to access their hosted services, such as the project management tool, in a consistent way, even if infrastructure is changed underneath; for example, when scaling up or down, or when a replacement instance is provisioned.

![A diagram depicting An elastic IP address that provides a static endpoint to an Amazon EC2 instance .](http://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/images/elastic-ip-address.png)

**Note**
 : For even quicker and easier deployment, many project management tools are available from the [AWS Marketplace](https://aws.amazon.com/marketplace/b/2649274011/) or as [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html).

 As your development team grows or adds more tools to the project management instance, you might require extra capacity for both the web application instance and the DB instance. In AWS, scaling instances vertically is an easy and straightforward operation. You simply stop the EC2 instance, change the instance type, and start the instance.

 Alternatively, you can create a new web application server from the AMI on a more powerful Amazon EC2 instance type, and replace the previous server. You can use horizontal scaling by using [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/), adding more instances to the system by using [AWS Auto Scaling](https://aws.amazon.com/autoscaling/). In this case, as you have more than one node, you can use Elastic Load Balancing to distribute the load across all application nodes. Amazon RDS DB instances can scale compute and memory resources with a few clicks on the [AWS Management Console](https://aws.amazon.com/console/).

![A diagram showing Elastic Load Balancing being used to distribute the load across all application nodes.](http://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/images/elastic-load-balancing.png)

 When you want to quickly set up a software development project on AWS and don’t want to configure custom project management tools on EC2, you can use AWS CodeStar. AWS CodeStar comes with a unified project dashboard and integration with [Atlassian JIRA](https://www.atlassian.com/software/jira) software, a third-party issue tracking and project management tool. With the AWS CodeStar project dashboard, you can easily track your entire software development process, from a backlog work item to production code deployment.

## On-demand development environments
<a name="on-demand-development-environments"></a>

 Developers primarily use their local laptops or desktops to run their development environments. This is typically where the integrated development environment (IDE) is installed, where unit tests are run, where source code is checked in, and so on.

 However, there are a few cases where on-demand development environments hosted in AWS are helpful.

 [AWS Cloud9](https://aws.amazon.com/cloud9/) is a cloud-based IDE that enables you to write, run, and debug your code with just a browser. It includes a code editor, debugger, and terminal. AWS Cloud9 comes prepackaged with essential tools for popular programming languages, including JavaScript, Python, PHP, Ruby, Go, C\+\+, and more, so you don’t need to install files or configure your development machine to start new projects. Because your AWS Cloud9 IDE is cloud-based, you can work on your projects from your office, home, or anywhere using an internet-connected machine. With AWS Cloud9, you can quickly share your development environment with your team, enabling you to pair program and track each other's inputs in real time.

 Some development projects may use specialized sets of tools that would be cumbersome or resource-intensive to install and maintain these on local machines, especially if the tools are used infrequently. For such cases, you can prepare and configure development environments with required tools (development tools, source control, unit test suites, IDEs, and so on), and then bundle them as AMIs.

 You can easily start the right environment and have it up and running in minimal time and with minimal effort. When you no longer need the environment, you can shut it down to free up resources. This can also be helpful if you need to switch context in the middle of having code checked out and work in progress. Instead of managing branches or dealing with partial check-ins, you can spin up a new temporary environment.

 On AWS, you have access to a [variety of different instance types](https://aws.amazon.com/ec2/instance-types), some with very specific hardware configurations. If you are developing specifically for a given configuration, it may be helpful to have a development environment on the same platform where the system is going to run. [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) enables you to provision virtual, cloud-based Microsoft Windows or Amazon Linux desktops for your users to run IDEs using your favorite applications such as Visual Studio, IntelliJ, Eclipse, AWS CLI, AWS SDK tools, Visual Studio Code, Eclipse, Atom, and many more.

 The concept of hosted desktops is not limited to development environments; it can apply to other roles or functions as well. For more complex working environments, [AWS CloudFormation](https://aws.amazon.com/cloudformation/) makes it easy to set up collections of AWS resources. This topic is discussed further in the *Testing* section of this document. In many cases, such environments are set up within the [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), which enables you to extend your on-premises private network to the cloud. You can then provision the development environments as if they were on the local network, but instead they are running in AWS. This can be helpful if such environments require any on-premises resources such as Lightweight Directory Access Protocol (LDAP).

 The following diagram shows a deployment where development environments are running on Amazon EC2 instances within an Amazon VPC. Those instances are remotely accessed from an enterprise network, through a secure VPN connection.

![A diagram depicting development environments running on Amazon EC2 instances within an Amazon VPC .](http://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/images/dev-environments.png)

### Stopping vs. ending Amazon EC2 instances
<a name="stopping-vs.-ending-amazon-ec2-instances"></a>

 Whenever development environments are not used; for example, during the hours when you are not working, or when a specific project is on hold, you can easily shut them down to save resources and cost. There are two possibilities:
+  **Stopping** the instances, which is roughly equivalent to hibernating the operating system
+  **Ending** the instances, which is roughly equivalent to discarding the operating system

 When you stop an instance (possible for Amazon EBS−backed AMIs), the compute resources are released and no further hourly charges for the instance apply. The Amazon EBS volume stores the state, and next time you start the instance, it will have the working data as it did before you stopped it.

**Note**
 : any data stored on ephemeral drives will not be available after a stop/start sequence.

 When you end an instance, the root device and any other devices attached during the instance launch are automatically deleted (unless the DeleteOnTermination flag of a volume is set to “false”), meaning that data may be lost if there is no backup or snapshot available for the deleted volumes. An ended instance doesn’t exist anymore and must be recreated from an AMI if needed. You would typically end the instance of a development environment if all work has been completed and/or the specific environment will not be used anymore.

 If you use [AWS Cloud9](https://aws.amazon.com/cloud9/) IDE, the EC2 instance that AWS Cloud9 connects to by default stops 30 minutes after you close the IDE, and restarts automatically when you open the IDE. As a result, you typically only incur EC2 instance charges for when you are actively working.

 If you chose to run your development environments on EC2 instances, you can use [AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/) to automatically stop your instances during weekends or non- working schedules. This can help reduce the instance utilization and overall spend.

## Integrating with AWS APIs and IDE enhancements
<a name="integrating-with-aws-apis-and-ide-enhancements"></a>

 With AWS, you can now code against and control IT infrastructure, either if the target platform of your project is AWS, or if the project is about orchestrating resources in AWS. For such cases, you can use the various AWS SDKs to easily integrate their applications with AWS APIs, taking the complexity out of coding directly against a web service interface and dealing with details around authentication, retries, error handling, and so on. The AWS SDK tools are available for multiple languages: [C\+\+](https://aws.amazon.com/sdk-for-cpp/), [Go](https://aws.amazon.com/sdk-for-go/), [JavaScript](https://aws.amazon.com/sdk-for-browser/), [Node.js](https://aws.amazon.com/sdk-for-node-js/), [Python](https://aws.amazon.com/sdk-for-python/), [Java](https://aws.amazon.com/sdk-for-java/), [.Net](https://aws.amazon.com/sdk-for-net/), [PHP](https://aws.amazon.com/sdk-for-php/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), and for [mobile platforms](https://aws.amazon.com/mobile) Android and iOS.

 AWS also offers IDE tools that make it easier for you to interact with AWS from within your IDEs, such as:
+  [AWS Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/)
+  [AWS Toolkit for VS Code](https://aws.amazon.com/visualstudiocode/)
+  [AWS Toolkit for Eclipse](https://aws.amazon.com/eclipse/)
+  [AWS Toolkit for IntelliJ IDEA](https://aws.amazon.com/intellij/)
+  [AWS Toolkit for PyCharm](https://aws.amazon.com/pycharm/)
+  [AWS Toolkit for Azure DevOps](https://aws.amazon.com/vsts/)
+  [AWS Toolkit for Rider](https://aws.amazon.com/rider/)
+  [AWS Toolkit for WebStorm](https://aws.amazon.com/webstorm/)

 For developing and building Serverless applications, AWS offers the [Serverless Application Model](https://aws.amazon.com/serverless/sam/) (AWS SAM) open-source framework, which can be used with the AWS toolkits mentioned previously.
