---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/appstream-well-architected-framework/operational-excellence.html
---

# Operational excellence pillar
<a name="operational-excellence"></a>

Operational excellence (OE) represents a dedication to crafting high-quality software solutions that consistently meet and exceed user expectations. The [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/operational-excellence.html) of the AWS Well-Architected Framework encompasses proven strategies for effective team organization, robust workload design, efficient large-scale operations, and seamless adaptation to changing requirements over time. By adhering to these principles, organizations can ensure that their systems remain resilient, performant, and aligned with evolving business needs.

Key focus areas for applying this pillar to your WorkSpaces Applications streaming environment:
+ Monitoring and observability
+ Automation and DevOps
+ Operational procedures and documentation
+ Support and incident management

## Organize teams around business outcomes
<a name="oe-outcomes"></a>

Create a cloud-aligned operating model with strong leadership commitment, where business goals and key performance indicators (KPIs) drive organizational transformation through optimized people, processes, and technology.
+ **Team structure.** Establish dedicated teams that align with application streaming outcomes. For example:
  + Image management team is responsible for application packaging and image optimization.
  + Fleet operations team manages capacity, performance, and scaling.
  + User experience team handles end-user support and satisfaction.
+ **KPIs and metrics.** Define and track business-aligned metrics such as:
  + Application availability rates
  + Time to deploy new applications
  + Cost per application streaming hour
+ **Operating model.** Create clear processes for:
  + Application onboarding and updates
  + Fleet capacity management
  + User access provisioning
  + Incident response and resolution

## Implement observability for actionable insights
<a name="oe-insights"></a>

Implement comprehensive monitoring and observability to track KPIs and workload health. This principle enables data-driven decisions and proactive improvements across performance, reliability, and cost.
+ Implement performance monitoring. Configure [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) to:
  + Ensure sufficient capacity to meet demand. For example, you can use the following metrics:
    + `AvailableCapacity` to monitor available streaming instances
    + `InUseCapacity` to track currently used instances
    + `CapacityUtilization` to monitor the percentage of fleet usage
  + Monitor user experience and performance.
  + Identify and address service issues promptly.
+ Track and analyze WorkSpaces Applications usage reports.
+ Capture and analyze application logs. For more information, see the AWS blog posts [Using Kinesis Agent for Linux to stream application logs in WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-kinesis-agent-for-linux-to-stream-application-logs-in-appstream-2-0/) and [Using Kinesis Agent for Microsoft Windows to store WorkSpaces Applications Windows event logs](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-kinesis-agent-for-microsoft-windows-to-store-appstream-2-0-windows-event-logs/).
+ Monitor WorkSpaces Applications metrics and events through chat notifications. For more information, see the AWS blog post [Monitor and automate AWS end user computing (EUC) with AWS Chatbot](https://aws.amazon.com/blogs/desktop-and-application-streaming/monitor-and-automate-aws-end-user-computingeuc-with-aws-chatbot/).
+ Enable proactive session management through visual cues. For more information, see the AWS blog post [Display session expiration and a countdown timer in Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/display-session-expiration-and-a-countdown-timer-in-amazon-appstream-2-0/).
+ Create visualizations for usage patterns and trends. For more information, see the AWS blog post [Ingest and visualize Amazon WorkSpaces Applications usage reports in Amazon OpenSearch Service](https://aws.amazon.com/blogs/desktop-and-application-streaming/ingest-and-visualize-amazon-appstream-2-0-usage-reports-in-amazon-opensearch-service/).
+ Utilize the EUC toolkit to monitor active sessions, track fleet inventory, and generate session reports (CSV export). For more information, see the AWS blog post [Use the EUC Toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/).

## Safely automate where possible
<a name="oe-automate"></a>

Apply infrastructure as code (IaC) principles to automate all aspects of your workload operations. Use guardrails to help ensure safe and consistent execution while reducing manual intervention.
+ Automate the creation and configuration of WorkSpaces Applications images by using the Image Assistant CLI. For more information, see [Create your Amazon WorkSpaces Applications image programmatically by using the Image Assistant CLI operations](https://docs.aws.amazon.com/appstream2/latest/developerguide/programmatically-create-image.html) in the WorkSpaces Applications documentation.
  + Application installation: Use the Image Assistant CLI to automate the installation of applications during image creation.
  + Image creation: Programmatically create WorkSpaces Applications images by using the Image Assistant CLI commands.
  + Configuration management: Automate the configuration of default application settings and launch parameters.
+ Automate the customization of WorkSpaces Applications images. For more information, see the AWS blog post [Automatically create customized WorkSpaces Applications Windows images](https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-create-customized-appstream-2-0-windows-images/).
+ Apply IaC to deploy the infrastructure and application components for WorkSpaces Applications. For more information, see the AWS blog post [Automation of infrastructure and application deployment for Amazon WorkSpaces Applications with Terraform](https://aws.amazon.com/blogs/desktop-and-application-streaming/automation-of-infrastructure-and-application-deployment-for-amazon-appstream-2-0-with-terraform/).
+ Implement automated processes for fleet management, including:
  + Fleet scaling based on demand. Configure automatic scaling policies to adjust fleet capacity automatically based on utilization metrics. For more information, see the AWS blog post [Use AWS Lambda to adjust scaling steps and thresholds for Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/use-aws-lambda-to-adjust-scaling-steps-and-thresholds-for-amazon-appstream-2-0/).
  + Base image updates. Benefit from automatic updates to the WorkSpaces Applications base image that's provided by AWS.
  + Capacity optimization. Set up automated scaling thresholds to optimize resource usage based on demand patterns.
+ Configure guardrails to automate safety controls:
  + Maximum fleet size limits. Set upper bounds on fleet capacity to prevent over-provisioning.
  + Scaling policy configuration. Implement step scaling or target tracking scaling policies with appropriate thresholds.
  + Service quotas. Use AWS service quotas as built-in limits to prevent excessive resource allocation.
  + Scale-in protection. Configure scale-in protection to prevent the removal of active instances during scaling events.
+ Perform testing and validation, including image builder, fleet, and integration testing.
  + Image builder testing:
    + Test applications directly in the image builder interface.
    + Verify application launch and functionality.
    + Test user settings and configurations.
    + Validate application compatibility.
  + Fleet testing:
    + Test streaming sessions from different client devices.
    + Verify user entitlements and access.
    + Validate application performance.
    + Test user experience for elements and operations such as the clipboard, file transfer, and printing.
  + Integration testing:
    + Test Active Directory or SAML 2.0-based authentication.
    + Test home folders and persistent storage.
    + Test application entitlements.
    + Test USB device redirection (if configured).
+ Use the WorkSpaces Applications applications manager to automate application packaging and deployment. For more information, see the AWS blog post [Streamline application onboarding with applications manager for Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/streamline-application-onboarding-with-applications-manager-for-amazon-appstream-2-0/).
+ Automate the deployment of new application versions by using continuous integration and continuous delivery (CI/CD) pipelines. For more information, see the AWS blog post [Screening Eagle: Optimize CI/CD and end user experience in ](https://aws.amazon.com/blogs/desktop-and-application-streaming/screening-eagle-optimize-ci-cd-and-end-user-experience-in-amazon-appstream-2-0/)Amazon WorkSpaces Applications.

## Make frequent, small, reversible changes
<a name="oe-changes"></a>

Build loosely coupled, scalable workloads that enable frequent, small-scale automated deployments with minimal risk and easy rollback capabilities.
+ For image updates, use versioned image creation and incremental updates.
  + Versioned image creation:
    + Create new images for each set of changes by using an image builder.
    + Maintain multiple image versions to support rollback scenarios.
    + Use [AWS tagging strategies](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) to track image versions and attributes.
  + Incremental updates:
    + Make small, incremental changes to applications or configurations.
    + Test updates thoroughly in the image builder before you create a new image.
    + Document all the changes that you made in each new image version.
+ For control fleet updates:
  + Create new fleets with updated images for testing.
  + Modify existing fleet attributes without disrupting active sessions.
+ Establish change management procedures for documentation, testing protocols, approval workflows, and monitoring processes.
  + Documentation:
    + Maintain detailed change logs for all image and fleet updates.
    + Document testing procedures and results for each change.
    + Use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to track and audit configuration changes.
  + Testing protocols:
    + Establish a comprehensive testing process for all changes.
    + Include application functionality, performance, and user experience tests.
    + Conduct testing in the image builder before you create new images.
    + Perform additional testing on non-production fleets before full deployment.
  + Approval workflows:
    + Implement an approval process for changes to production environments.
    + Define criteria for changes that require approval versus standard updates.
    + Establish roles and responsibilities for change approval.
  + Monitoring and validation:
    + Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to monitor fleet and application performance after changes.
    + Set up alerts for key metrics to quickly identify issues after updates.
    + Conduct post-implementation reviews to validate change success and gather learnings.

## Refine operations procedures frequently
<a name="oe-ops"></a>

Continuously improve operational procedures through regular reviews, updates, and team engagement to keep all stakeholders informed and aligned with best practices.
+ **Documentation management.** Maintain current, version-controlled documentation of WorkSpaces Applications procedures in a central location to ensure operational consistency and knowledge sharing across teams.
  + Required documentation: Maintain up-to-date documentation for critical WorkSpaces Applications operations for image creation and management, fleet operations, and troubleshooting.
  + Operational reviews: Monitor and review key operational aspects, including performance metrics and incident management.
+ **Continuous improvement.** Systematically enhance WorkSpaces Applications operations by incorporating AWS service updates, operational metrics, and learned best practices into standard procedures.
  + Service updates: Monitor WorkSpaces Applications release notes for new features, service improvements, security updates, and Regional availability.
  + Best practices: Review and incorporate AWS Well-Architected Framework updates, WorkSpaces Applications best practices, AWS reference architectures, and AWS security recommendations.
  + Knowledge management: Maintain and update standard operating procedures, runbooks, troubleshooting guides, and user support documentation.

## Anticipate failure
<a name="oe-failure"></a>

Conduct failure scenario testing regularly to understand risks, validate response procedures, and improve team readiness for handling real incidents.
+ **Failure testing.** Regularly simulate and test for failures such as fleet capacity exhaustion, application launch failures, and network connectivity issues.
  + Fleet capacity exhaustion:
    + Monitor and test fleet scaling behavior when approaching capacity limits.
    + Configure CloudWatch alarms for `CapacityUtilization` and `AvailableCapacity` metrics.
    + Implement procedures for handling capacity constraints during peak usage.
  + Application launch failures:
    + Test application launch behavior on streaming instances.
    + Validate application access and performance across different fleet configurations.
  + Network connectivity issues:
    + Test streaming session performance across different network conditions.
    + Monitor `StreamingSessionLatency` for connection quality issues.
    + Ensure proper configuration of VPC settings and security groups.
+ **Recovery procedures.** Develop and test procedures for:
  + Fleet failover between AWS Availability Zones. In addition, document procedures for scaling fleet capacity, managing fleet updates, and responding to instance health issues.
  + User data management:
    + Configure and test [application settings persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-settings-persistence.html) and storage solutions for home folders in Amazon Simple Storage Service (Amazon S3) for Windows fleets and shared file systems in Amazon Elastic File System (Amazon EFS) for Linux fleets.
    + Validate data synchronization between sessions.
  + Service continuity. Maintain procedures for creating new fleet instances, managing image updates, and handling session disconnections.
+ **Risk management.** Identify and mitigate:
  + Capacity constraints by setting appropriate fleet minimum capacity, configuring automatic scaling policies based on demand patterns, and monitoring fleet utilization trends by using CloudWatch metrics such as `CapacityUtilization`, `InUseCapacity`, and `AvailableCapacity`.
  + Performance bottlenecks by tracking key metrics such as `StreamingSessionLatency` and configuring the appropriate CloudWatch alarms.

## Learn from all operational events and metrics
<a name="oe-learn"></a>

Foster a culture of continuous improvement by sharing lessons learned from operational events and failures across the organization. Emphasize their impact on business outcomes.
+ **Event analysis.** Document and analyze service interruptions, performance degradation, user complaints, and capacity issues.
+ **Metrics review.** Analyze usage patterns, performance trends, cost metrics, and user satisfaction data on a regular basis.
+ **Knowledge sharing.** Establish processes for team learning sessions, best practice documentation, cross-team knowledge transfer, and incident retrospectives.

## Use managed services
<a name="oe-managed"></a>

Minimize operational overhead by using AWS managed services and building standardized procedures around them. Integrate with the following AWS managed services:
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) for automation
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for monitoring
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) for access control
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for user storage for Windows fleets
+ [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) for user storage for Linux fleets
+ [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) for user authentication
