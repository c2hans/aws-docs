---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-devops-aws-mainframe-modernization/build.html
---

# Build
<a name="build"></a>

During the build phase in a DevOps strategy, you construct the technical infrastructure, and you cultivate a cultural shift toward collaboration, automation, and continuous improvement. This pivotal phase involves the practical orchestration of tools and pipelines. It encompasses the following:
+ Setup of DevOps toolchains
+ Establishment of connections
+ Creation of pipelines that guide code development through application deployment

It includes not only the technical aspect of building software but also the development culture shift toward collaboration, automation, and continuous improvement. By adhering to continuous integration and continuous delivery (CI/CD) principles, the build phase aims to streamline the development and deployment process, improve software quality, and accelerate the deployment of modernized mainframe applications on AWS.

The following diagram represents different stages of a deployment pipeline. Each stage contains required and recommended steps to be implemented in a modernized mainframe workload deployment journey.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-devops-aws-mainframe-modernization/images/guide-img/a8679bf0-2999-4310-8cbd-8d5bbb590170/images/0427988c-c4dd-418b-a6e0-2ecbbcd6ad44.png)

Modernized mainframe workload deployment pipeline stages include the following:
+ **Source stage** – Required steps are configuration, dependency manifests, static assets, infrastructure source, test source, and application source. Recommended step is database source.
+ **Build stage** – Required steps are package artifacts, static application security testing, secrets detection, code quality, unit tests, and build code. Recommended steps are software bill of materials and software composition analysis.
+ **Test (beta) stage** – Required steps are acceptance tests and integration tests. Recommended steps are deploy software, deploy database, and launch environment.
+ **Test (gamma) stage** – Required steps are synthetic test, monitoring and logging, deploy software, and launch environment. Recommended setps are dynamic application security testing (DAST), resilience tests, performance tests, and deploy database.
+ **Prod stage** – Required steps are synthetic tests and progressive deployment. Recommended steps are deploy database and manual approval.

## Continuous integration
<a name="continuous-integration"></a>

Continuous integration (CI) is a software development practice where developers make regular, small alterations to the code and integrate them into a releasable branch of the code repository. The newly integrated code is autonomously built, tested, and validated in a consistent and repeatable manner. CI allows developers to receive feedback swiftly, identify potential issues in the early stages of the development lifecycle, and address them before they escalate in complexity and cost.

Continuous integration can greatly accelerate and streamline the mainframe modernization process on AWS. CI principles apply to the following areas:
+ **Frequent code integration** – In a CI pipeline, code changes are integrated into a shared repository frequently, often multiple times a day. This promotes collaboration and ensures that the entire development team is working with the most up-to-date code base. CI also can help manage code changes and track the history of modifications. Git-based tools such as AWS CodeCommit, GitLab, and GitHub can help in frequent code integration and collaboration. The code from these git repositories can be synchronized back to the mainframe through connectors such as [Git connector for OpenText Changeman ZMF](https://www.microfocus.com/en-us/products/changeman-zmf/overview).
+ **Automated testing** – CI encourages the creation of automated test suites for mainframe applications. This ensures that as code is refactored for the cloud, it remains functional and error-free. Automated tests can include unit tests and integration tests. Mainframe applications can be unit tested by using frameworks such as [ZUnit](https://www.ibm.com/docs/en/developer-for-zos/16.0?topic=samples-zunit-zos-automated-unit-testing-framework).
+ **Early issue detection** – By running automated tests and static code-analysis tools every time code is committed, CI systems quickly detect and flag any issues. This helps development teams to address problems early in the development cycle, reducing the risk of major setbacks during migration. Tools such as SonarQube and Veracode can help with early issue detection and code quality for both Mainframe COBOL and modernized Java code.
+ **Rapid feedback** – CI systems provide rapid feedback to developers about the quality of their code, which can lead to continuous improvement in the modernization process.

## Continuous delivery
<a name="continuous-delivery"></a>

Continuous delivery (CD) takes place after continuous integration (CI). In CD, code changes that pass the build validation are automatically deployed to other environments, including production, with minimal human intervention. CD helps to ensure that new features, fixes, and improvements are deployed in a fast and reliable manner. CD reduces lead times and improves overall efficiency of the deployment process. When you automate the delivery process using CD, the system handles the time-consuming and error-prone process of deploying changes to various environments while teams focus on developing and refining code.

CD facilitates the transition of modernized mainframe applications to AWS by automating the deployment process. CD principles apply to the following areas:
+ **Automated deployments** – To reduce manual intervention and the potential for human errors during the migration process, CD automates the deployment of code changes to target environments. Tools such as AWS CodeDeploy, Jenkins, and IBM Urban CodeDeploy can help with progressive deployment of artifacts to different environments (for example, Dev, Test, Prod).
+ **Continuous deployment** – The difference between continuous delivery and continuous deployment is the presence of a manual approval to update to production. In continuous deployment, production happens automatically without explicit approval.
+ **Rapid feedback loop** – Automated deployments provide quick feedback on whether code changes are ready for deployment. This feedback loop ensures that only thoroughly tested and validated code is deployed.
+ **Frequent release cycles** – By using CD  your organization can release new features, enhancements, and modernized code more frequently. This agility helps businesses to adapt to changing requirements and stay competitive.
+ **Rollback capabilities** – CD pipelines should include rollback mechanisms. If there are issues or unexpected behavior in the AWS environment, teams can use the mechanisms to revert to a previous version of an application.
+ **Infrastructure as code** – CD can be combined with infrastructure as code (IaC) tools such as AWS CloudFormation or HashiCorp Terraform to define and provision infrastructure consistently. Consistent provisioning helps to ensure that the AWS environment matches the required configuration.
