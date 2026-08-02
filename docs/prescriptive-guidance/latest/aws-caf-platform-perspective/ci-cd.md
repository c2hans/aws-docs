---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/ci-cd.html
---

# Continuous integration and continuous delivery
<a name="ci-cd"></a>

**Evolve and improve applications and services faster than organizations that use traditional software development and infrastructure management processes.**

Adopting [DevOps](https://aws.amazon.com/devops/) practices with [continuous integration](https://aws.amazon.com/devops/continuous-integration/) and [continuous delivery](https://aws.amazon.com/devops/continuous-delivery/) (CI/CD) promotes a streamlined, automated, and efficient process for building, testing, and deploying applications. CI/CD enables rapid delivery of software, reduces the risk of deployment errors, and ensures that applications are always up to date with the latest features and bug fixes. The main objective is to evolve and improve applications and services at a faster pace by evolving from the use of traditional software development and infrastructure management processes.

## Start
<a name="ci-cd-start"></a>

### Adopt software component management
<a name="adopt-software-component-management.e399d467-0148-52ce-b6ca-c6cad2a508d5"></a>

Software component management is the practice of managing all the individual components used to build software, including libraries, frameworks, source code repositories, modules, artifacts, and third-party dependencies. We recommend that you use a version control system such as Git or Apache Subversion to manage source code, enable collaboration, and maintain a history of code changes. You can monitor changes and events in the repository to automate the process, create pipelines, manage your code, and integrate your workflows with additional services as needed.

### Create CI/CD pipelines
<a name="create-ci-cd-pipelines.1348faba-e689-5125-85cc-bc48adf2bace"></a>

CI/CD pipelines are sets of automated instructions that are initiated by changes committed to the version control system. They typically include instructions for building the application, running automated tests, and deploying code to a specific environment. You can set up an automated CI/CD pipeline by using tools such as [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html), Jenkins, GitLab, or CircleCI. You can also set them up directly in version control systems that support pipeline generation.

Start with a minimum viable pipeline for continuous integration, and then transition to a [continuous delivery](https://aws.amazon.com/builders-library/going-faster-with-continuous-delivery/?did=ba_card&trk=ba_card) pipeline that includes more actions and stages. Treat your continuous delivery configuration as code. You can use multiple, distinct pipelines for each branch and team, so think about which configuration variables you need to set up and how to best support the teams that will use the pipelines.

Consider deployment windows―which days and times you want to deploy your code. Consider your system's low-demand hours, so if you have to roll back, it will have the least impact on your customers. Other best practices include avoiding deployments on Fridays and implementing a code freeze during high peak dates or before holidays. Consider defining rules about deploying code when the author of the commit isn't available (for example, on vacation). Keep in mind that deployments fail and you might need to rely on external help. Evaluate different [deployment methods](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.html) such as in-place, rolling, immutable, and blue/green deployments. Consider using fully managed services for continuous delivery workflows in order to increase availability and security while minimizing complexity and management.

### Deploy automated testing
<a name="deploy-automated-testing.12a48045-f45e-5431-a261-556a150bc5c4"></a>

Modern practices recommend *shifting left* (moving testing closer to the developer and to the [IDE](https://aws.amazon.com/what-is/ide/), and earlier in the lifecycle) to detect and remediate problems before they are committed to a repository and initiate a pipeline. This practice involves quick feedback loops with the developer, because errors are detected while the developer is coding. Shifting left is associated with lower costs, because testing doesn't require running pipelines, which can result in asynchronous feedback and higher operational expenses.

Automated testing catches errors early in the development process, and includes unit tests, integration tests, and functional tests. We recommend that you encourage [developers to use tools](https://aws.amazon.com/products/developer-tools/) to create unit tests as early as possible and to run them before pushing the code to the central repository. Additionally, make sure that your automated processes include [static code analysis](https://aws.amazon.com/blogs/devops/automating-detection-of-security-vulnerabilities-and-bugs-in-ci-cd-pipelines-using-amazon-codeguru-reviewer-cli/), performance benchmarking, and security application testing.

### Create documentation
<a name="create-documentation.89866517-dc8b-5f8e-92a4-e79ecb920243"></a>

In addition to implementing a CI/CD pipeline to streamline development workflows, you should maintain clear and comprehensive documentation to ensure the pipeline's ongoing effectiveness, maintainability, and scalability. Documentation is a vital aspect of CI/CD pipelines, because it provides development teams with a clear understanding of the pipeline's design, components, and processes. When you create documentation, start with a pipeline overview, explain the architecture and design tradeoffs, describe the tools and technologies that are being used, specify the initial configuration and settings, outline the security measures and access control, and include troubleshooting and maintenance information.

### Use infrastructure as code
<a name="use-infrastructure-as-code.adcf0e7e-af1e-53c4-97d6-b12f5f3f43db"></a>

Use tools such as Terraform, Ansible, or [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to manage infrastructure and to ensure consistent and reproducible environments. Treat your infrastructure as code, make sure you track changes in the infrastructure, and avoid making changes directly in the console. Define all infrastructure―including database provisioning―as code and deploy these changes by using pipelines. Consider running database integration as code in pipelines with a small subset of sanitized production data. When possible, make the changes and track those changes in the code.

As with software code, follow these best practices for your infrastructure code:
+ Use version control.
+ Make use of bug tracking and ticketing systems.
+ Have peers review changes before applying them.
+ Establish infrastructure code patterns and designs.
+ Test infrastructure changes.

### Keep and track standard metrics
<a name="keep-and-track-standard-metrics.dce84599-ffaf-5d78-8d1e-06148b98b1ac"></a>

To maintain a high level of performance, develop and track against key metrics to understand the health and business impact of your pipelines, including:
+ **Build frequency.** The number of builds offers insights into your team's productivity and the complexity of changes.
+ **Deployment frequency.** Regular deployments indicate a healthy, agile development process.
+ **Lead time for changes.** Measuring the average time for changes to reach production can help you identify bottlenecks in your deployment process.
+ **Mean time through pipeline.** The average time from the initial pipeline stage to each subsequent stage can help optimize your workflow.
+ **Production change volume.** Keeping track of the number of changes reaching production can provide insights into the stability of your production environment.
+ **Build time.** The average build time can indicate potential issues in the codebase or infrastructure.

## Advance
<a name="ci-cd-advance"></a>

### Use configuration management
<a name="use-configuration-management.0e2da601-efd2-5971-80ff-40ae8f5c5727"></a>

Configuration management tools play a critical role in automating the deployment, configuration, and management of software and infrastructure. They provide a systematic approach to handling changes and maintaining the desired state of infrastructure, software, and configurations across various environments. These tools enable developers to define the desired state of a system by using declarative or imperative languages. The configuration management tool then automates the process of applying these configurations to the target systems, ensuring consistency and repeatability.

Use configuration management tools to automate the deployment, configuration, and management of software and infrastructure.  [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) is a secure and scalable configuration management service that automates the process of keeping your managed nodes and other AWS resources in a state that you define.

### Integrate monitoring and logging
<a name="integrate-monitoring-and-logging.675b23c2-eb7f-5535-bde1-5781198e463d"></a>

Integrating monitoring and logging solutions into CD pipelines offers numerous benefits for development teams and for the overall software development process. These solutions can provide real-time insights into application performance, enable faster identification and resolution of issues, and promote continuous improvement to help ensure that applications remain reliable, performant, and scalable throughout their lifecycle. Investing in monitoring and logging solutions is a key aspect of maintaining a robust and efficient CD pipeline, and ultimately contributes to the successful delivery of high-quality software.

### Create cadence for merging
<a name="create-cadence-for-merging.0886078b-9d3b-5fa3-aad2-144daeeb32dc"></a>

Commit or merge code changes to the mainline (trunk or main) branch at least once every day or, ideally, multiple times a day after each task. This cadence leads to multiple daily pipeline invocations. A pull-based branching workflow model aligns with this approach. Use [feature flags](https://aws.amazon.com/blogs/mt/using-aws-appconfig-feature-flags/), [dark launching](https://martinfowler.com/bliki/DarkLaunching.html), and similar techniques to customize the features your customers use.

### Capture post-deployment behavior
<a name="capture-post-deployment-behavior.6ea5d6fe-17a8-5f9d-b5e6-c266532ad482"></a>

After a deployment, capture production behavior by using automated synthetic tests and synchronize results with the continuous delivery pipeline to ensure that corrective actions occur promptly. The top priority for developers should be to fix errors discovered in pipelines as soon as possible, commit code changes to the source code repository, and verify error resolution in the pipeline.

Best post-deployment practices include observing the most important key performance indicators (KPIs) and validating that there are no errors in the production environment. Automate error handling and evaluating post-deployment KPIs to quantify the impact of your release. Automatically generate speed, security, and stability metrics that developers can use to make improvements. For more information, see the solution [DevOps Monitoring Dashboard](https://aws.amazon.com/solutions/implementations/aws-devops-monitoring-dashboard/) on AWS.

## Excel
<a name="ci-cd-excel"></a>

Adopt cutting-edge practices and technologies for optimal performance. Continually refining your CI/CD processes helps you improve software quality, reduce time to market, and increase agility. New techniques and tools continuously emerge, which makes it essential for your organization to stay informed and adapt to maintain a competitive edge.

To remain adaptive, consider the following:
+ Define everything as code, including your application, configuration, infrastructure, data, AWS accounts and organizations, deployment pipelines, networking, and security and compliance controls.
+ Create corresponding [deployment pipelines](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture) for compute images, shared services, and applications.
+ Consider a GitOps model in which pull-based requests initiate a workflow to deploy changes by comparing the existing infrastructure state to the desired state, as described in the code.
+ Consider using CD pipelines to deploy machine learning (ML), data, Internet of Things (IoT), and other workloads.
+ Digitally sign all build artifacts and store them in a secure repository.
+ Track software provenance by automatically generating a software bill of materials that creates a record of all versioned and digitally signed artifacts that are deployed to customers.
+ After you eliminate all manual activity in a software delivery process, remove manual review boards.

For applications and services that have automated their entire software delivery process, consider continuous deployment in which teams deploy changes that pass all checks in a pipeline to customers in production. For a visualization, see the first diagram in [What is Continuous Delivery?](https://aws.amazon.com/devops/continuous-delivery/) on the AWS website.

### Integrate AI/ML technologies
<a name="integrate-ai-ml-technologies.94b3bdd4-b464-5a3c-a673-82d35a417430"></a>

The integration of artificial intelligence (AI) and machine learning (ML) technologies into CI/CD pipelines offers several benefits, including the following:
+ Automated test generation
+ Intelligent test prioritization
+ Predictive analytics for issue detection
+ Anomaly detection and root cause analysis
+ Code review and quality assurance
+ Deployment optimization

For more information, see [Add intelligence to your developer operations](https://aws.amazon.com/machine-learning/ml-use-cases/ai-for-devops/) on the AWS website.

### Adopt chaos engineering practices
<a name="adopt-chaos-engineering-practices.8dd4207d-c4d9-5cf0-9bd8-9b17c84d5c74"></a>

Chaos engineering involves intentionally injecting failures into systems to test their ability to withstand and recover from unexpected events. By identifying weaknesses and addressing them proactively, organizations can improve their overall system reliability and minimize the impact of potential issues.

Adopt chaos engineering practices to test the resilience of your systems by using tools such as Gremlin, Chaos Monkey, or Litmus. Run controlled experiments regularly to identify vulnerabilities, validate fault tolerance, and ensure that your application handles unexpected failures gracefully. This proactive approach helps improve system reliability and contributes to a more robust CI/CD pipeline.

### Optimize performance
<a name="optimize-performance.ef9b5373-3181-5ff5-bfc0-fa73654cb3dd"></a>

Optimize your application's performance continuously by using profiling tools, real-time monitoring, and feedback loops. Apply techniques such as the following to ensure that your applications can handle increased traffic and demand:
+ Code optimization
+ Profiling
+ Real-time monitoring
+ Feedback loops
+ Caching
+ Load balancing
+ Scalability and performance testing

### Implement advanced observability
<a name="implement-advanced-observability.1a2a43b9-75c5-5ea1-8c99-77c34dd0db39"></a>

Elevating your cloud infrastructure's observability goes beyond the basics of collecting, aggregating, and analyzing metrics, logs, and traces. When observability is enhanced with tools such as [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html), it evolves into a strategic practice that fuels continuous delivery and innovation.

In a robust CI/CD pipeline, advanced observability enables you to uncover insights, not just about your applications and infrastructure but also about your entire system's performance and health, including the pipeline itself. These insights help you:
+ Rapidly identify, understand, and address potential issues to improve application stability and reduce downtime
+ Streamline your CI/CD processes to create faster and more reliable deliveries
+ Gain deeper insights into the impact of code changes and deployments to drive informed decision-making
+ Optimize resource utilization to improve operational efficiency and cost-effectiveness

To elevate observability:
+ Embed observability into every layer of your applications and infrastructure to create a comprehensive view of your systems' performance, behavior, and health.
+ Centralize data collection, storage, and analysis with tools such as Amazon CloudWatch to unify your observability data for easy access and interpretation.
+ Use AWS X-Ray for distributed tracing to understand how your applications and their underlying services are performing.
+ Establish feedback loops for continuous improvement, and use your observability data to drive iterative enhancements to your systems.

Adopting advanced observability isn't just about maintaining your systems—it's a strategic move toward achieving operational excellence and driving continuous innovation in your organization.

### Implement GitOps practices
<a name="implement-gitops-practices.eb4fdebb-e4de-5a72-8334-b5ae5dca336e"></a>

Implement GitOps practices to manage infrastructure and application configurations by using a Git repository as a single source of truth. This approach simplifies change management, enhances traceability, and ensures consistency across environments.
