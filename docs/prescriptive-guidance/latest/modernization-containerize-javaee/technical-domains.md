---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-containerize-javaee/technical-domains.html
---

# Technical domains
<a name="technical-domains"></a>

This section provides an overview of the main technology domains for containerization. The following diagram shows the architecture of a traditional Java EE application.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-containerize-javaee/images/guide-img/34f6e23c-ad3a-4f13-8f30-05bf7b07cc57/images/e77d30d0-f69a-43fd-af87-8cff09b5430e.png)

The following diagram shows the architecture of a containerized Java EE application.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-containerize-javaee/images/guide-img/34f6e23c-ad3a-4f13-8f30-05bf7b07cc57/images/b290a220-6ed3-4da4-acab-ef672d98ce07.png)

## 1. Session state
<a name="session-state"></a>

In most cases, Java EE applications store the session data associated with user requests, such as cookies for servlets and Enterprise Java Beans (EJB) stateful sessions. We recommend that you avoid storing state information in Java virtual machine (JVM) memory because your container must be kept stateless. For more information on the disposability principle, see [Principles of container-based application design](https://www.redhat.com/cms/managed-files/cl-cloud-native-container-design-whitepaper-f8808kc-201710-v3-en.pdf) in the Red Hat documentation. In Java EE, there are two types of session data: HTTP session data and EJB session data. HTTP and EJB session data can be persisted by the application server. Multiple traditional application servers support memory replication to increase the availability of this session data, such as Infinispan on RedHat JBoss and Data Replication Service on IBM WebSphere Application Server.

The memory replication mechanism assumes that a particular set of servers always exist in the cluster, or a small number of servers join or leave the cluster. This is incompatible with a container environment, so we recommend that you get rid of your memory replication mechanism. In a container environment, the application servers are redeployed when a new version of the container image is built. That is, all replicated memory data is also erased.

## 2. Agents
<a name="agents"></a>

There are multiple agent processes running on a single physical or virtual server that typically perform automation and utility tasks, such as the following:

1. **Monitoring**­ – Traditional Java EE application environments often use dedicated agents for monitoring. These agents are responsible for monitoring server CPU, memory, disk usage, memory usage inside the JVM, log messages, and more. However, it's not possible to directly run monitoring agents in a container environment. You must replace monitoring agents with the monitoring mechanism provided by the container platform, such as Amazon CloudWatch and Amazon CloudWatch Logs.

1. **Jobs (scheduled tasks)** – In traditional Java EE application environments, the job execution environment often resides on the same server as the application server and is responsible for long-running batch processes apart from user requests. For example, the batch process controlled by the job controller accesses the database to retrieve data and create a report. Since these multiple workloads cannot coexist in a container environment, you must build the job and batch execution environment separately from the container environment.

1. **File transfer** – File transfer agents are typically not as common in Java EE application environments, but they sometimes run on the same operating system with the Java application as an independent process to exchange files to or from external applications. For example, data used by other applications is transferred to a file every day and reflected in the database. File transfer agents can't be running aside containers, but must be running on another server that has access to the database and files.

## 3. Application servers
<a name="application-servers"></a>

The most significant challenge in containerization is changing application servers. Traditional Java EE compliant application servers assume a static compute environment, so they might not be suitable for running in a container environment. That is, the physical or virtual servers are assumed as the entity of the compute environment for Java EE applications. For example, proprietary Java EE application servers, such as a traditional IBM WebSphere Application Server (tWAS) and Oracle WebLogic Server, have their own application deployment mechanism.

The situation is different in a container environment. In this environment, containers include an application server and runtime with application build packages (for example, .war and .jar files) and are deployed to container platforms such Amazon ECS or Amazon EKS. We recommend that you use a container platform mechanism to deploy applications to environments. Application servers are frequently deployed with containers, so they must be small in size (less than 500 MB) and fast to start. To meet this requirement, you might need to change the traditional application server and migrate to a more container-friendly application server. This could require a migration from IBM WebSphere Application Server to IBM WebSphere Liberty or JBoss Enterprise Application Platform (EAP) to WildFly.

We recommend that you consider the following impacts that can result from changing an application server:

1. Configuration injection through environment variables (in contrast to traditional Java EE applications that store configurations in a file, such as web.xml)

1. Compatibility with Java EE capabilities

1. JVM versions

## 4. File store
<a name="file-store"></a>

The file store most commonly used for traditional Java EE applications is the local file system. The most common use cases include application log files, application-generated files such as business reports, and user-uploaded content. We recommend that you avoid storing files inside the container because containers are stateless, which means that file stores need to be externalized for containerization.

Consider the following containerization options:

1. [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)**  **–  Amazon EFS is a managed NFS service that's accessible from containers. Amazon EFS is integrated with Amazon ECS and Amazon EKS. If you use Amazon EFS, you don't need to write custom scripts to mount EFS volumes to your containers. The first step for this option is to list all the file system paths in your application that are used to read or write. After you identify the file system path to be persisted, you can map the file system path to an EFS file system path. For more information, see [Tutorial: Using Amazon EFS file systems with Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-efs-volumes.html) in the Amazon ECS documentation. Not all paths are required to be persisted, especially application log files. Most enterprise applications write log files to a local file system. As part of the containerization process, we recommend that you consider changing the logging destination to use Standard Out and Standard Error. This allows you to capture all output to CloudWatch Logs without managing log storage sizing and performance. For more information about logging in Amazon ECS, see [Using the awslogs log driver](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html) in the Amazon ECS documentation.

1. [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)** **– Amazon S3 is less expensive than Amazon EFS and supports a wider bandwidth than Amazon EFS, but Amazon S3 requires a broader application code change than Amazon EFS. This is because Amazon S3 is not a file system.

## 5. Build and deploy process
<a name="build-deploy"></a>

The containerization process involves changing and extending the application delivery process. In traditional environments, the application delivery process primarily involves Java artifacts (for example, .war and .ear files). In a container environment, the container image is the delivery unit. In addition to the process for building existing Java artifacts, you must build a process for building and delivering Docker containers. For more information about the pipeline process, see [Automatically build and deploy a Java application to Amazon EKS using a CI/CD pipeline](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) in the AWS Prescriptive Guidance documentation.

## 6. Database access
<a name="database-access"></a>

Traditional application containerizations are often accompanied by database migration. To reduce migration risk, we recommend following the [migration strategy for relational databases](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-migration/welcome.html) (AWS Prescriptive Guidance). Containerized environments require externalized configuration, including database connection strings. You can use tools such as [Spring Cloud Config](https://github.com/spring-cloud/spring-cloud-config) (GitHub repository) to externalize the Java application configuration in a distributed environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
