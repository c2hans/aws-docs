---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-containerize-javaee/migration-approach.html
---

# Migration approach
<a name="migration-approach"></a>

This section describes an approach for containerizing traditional Java EE applications in the AWS Cloud. For more general migration guidelines, see [Mobilize your organization to accelerate large-scale migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/welcome.html) in the AWS Prescriptive Guidance documentation.

## Start the discovery and planning process
<a name="planning"></a>

Java EE application migration requires deep application discovery. As part of the discovery and planning process, we recommend that you identify the following in your Java EE application:
+ Number of CPUs
+ Memory and disk requirements
+ Java EE, the Java Development Kit (JDK), and application server versions (such as Oracle WebLogic Server 10)

## Understand clustering options for high availability and scalability
<a name="clustering-options"></a>

More and more traditional Java EE applications are running on vendor-specific clustering systems that improve application availability and scalability. In a containerized approach, clustering is performed by container orchestration platforms such as Amazon ECS and Amazon EKS. We recommend that you understand the difference between clustering done by container orchestration platforms and clustering done by your current application platforms.

## Assess the compatibility of vendor-specific packages
<a name="vendor-specific-packages"></a>

Application server vendors can offer their own Java EE packages. To ensure compatibility with containerized environments, check if your application uses any Java EE packages from application server vendors.

## Select a target container platform
<a name="target-platform"></a>

Choosing the right container platform for Java EE depends on your business needs. Popular choices include container-friendly, open-source (and sometimes light-weight) Java EE platforms that are distributed on Docker Hub, including GlassFish Server, WildFly, and Open Liberty. We recommend that you consider a container platform that offers production-level technical support and licensing.

## Prepare for automated testing
<a name="automated-testing"></a>

Migrating Java EE applications to a new application server requires code or configuration changes other than business logic. Without an automated test and build process for your current application, you can't verify that your code and configuration changes won't break existing business logic. We recommend that you establish an automated build and test pipeline in the first phase of the project, which includes modernizing manual test processes and unmaintained application build settings (such as build.xml in Apache Ant) with mainstream build tools such as [Maven](https://maven.apache.org/) (Apache Maven documentation) or [Gradle](https://gradle.org/) (Gradle documentation). For more information, see [Automatically build and deploy a Java application to Amazon EKS using a CI/CD pipeline](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) in the AWS Prescriptive Guidance documentation.
