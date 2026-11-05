---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/software-development.html
---

# Software development
<a name="software-development"></a>

## Software development processes
<a name="software-development-processes"></a>

 The Project and Operation stages of the life cycle approach in GAMP, for instance, are reflected in the AWS information and activities surrounding organizational mechanisms to guide the development and configuration of the information system, including software development lifecycles and software change management. Elements of the organizational mechanisms include policies and standards, the code pathway, deployment, a change management tool, ongoing monitoring, security reviews, emergency changes, management of outsourced and unauthorized development and communication of changes to customers.

 The software development lifecycle activities at AWS include the code development and change management processes at AWS which are centralized across AWS teams developing externally facing and internally facing code with processes applying to both internal and external service teams. Code deployed at AWS is developed and managed in a consistent process, regardless of its ultimate destination. There are several systems used in this process, including:
+ A code management system used to assemble a code package as part of development.
+ Internal source code repository.
+ The hosting system in which AWS code pipelines are staged.
+ The tool used for automating the testing, approval, deployment, and ongoing monitoring of code.
+ A change management tool which breaks change workflows down into discrete, easy to manage steps and tracks change details.
+ A monitoring service to detect unapproved changes to code or configurations in production systems. Any variances are escalated to the service owner or team.

## Deployment and testing
<a name="deployment-and-testing"></a>

 A pipeline represents the path approved code packages take from initial check-in through a series of automated (and potentially manual) steps to execution in production. The pipeline is where automation, testing, and approvals happen.

 At AWS, the deployment tool is used to create, view, and enforce code pipelines. This tool is used to promote the latest approved revision of built code to the production environment.

 A major factor in ensuring safe code deployment is deploying in controlled stages and requiring continuous approvals prior to pushing code to production. As part of the deployment process, pipelines are configured to release to test environments (for example, beta, gamma, and others, as defined by the team) prior to pushing the code to the production environment. Automated quality testing (for example, integration testing, black box testing, and white box testing) is performed in these environments to ensure code is performing as anticipated. If code is found to deviate from standards, the release is halted and the team is notified of the need to review.

 These development and test environments emulate the production environment and are used to properly assess and prepare for the impact of a change to the production environment. To reduce the risks of unauthorized access or change to the production environment, the development, test, and production environments are all logically separated.

 The tool additionally enforces phased deployment, if the code is to be deployed across multiple Regions. Should a package include deployment for more than one AWS Region, the pipeline will enforce deployment on a single-Region basis. If the package were to fail integration tests at any Region, the pipeline is halted and the team is notified for need to review. Within each Region, deployments use a rolling deployment strategy that replaces no more than 33% of capacity at once. AWS employs automated monitoring and rollback mechanisms during deployments, including continuous health checks, anomaly detection, and automatic rollback triggers when performance degradation is detected. This automation enables safe, hands-off deployments while maintaining service reliability.

## Configuration and change management
<a name="configuration-and-change-management"></a>

 Configuration management is performed during information system design, development, implementation, and operation through the use of the AWS Change Management process. Routine, emergency, and configuration changes to existing AWS infrastructure are authorized, logged, tested, approved, and documented in accordance with industry norms for similar systems. Updates to the AWS infrastructure are done to minimize any impact on you and your use of the services. This rigorous change management process enables AWS to safely deploy changes multiple times per day across services while maintaining the high standards required for GxP compliance.

## Change management
<a name="software"></a>

 AWS applies a systematic approach to managing change so that changes to customer-impacting services are thoroughly reviewed, tested, approved, and well-communicated. The AWS change management process is designed to avoid unintended service disruptions and to maintain the integrity of service to you.

### Types of changes and customer communication
<a name="types-of-changes"></a>

 AWS categorizes service changes into three primary types based on customer impact:

**Deprecations:** These involve the retirement of existing features, APIs, or services. Customers receive advanced notification (typically more than 12 months) through multiple channels including the AWS Health Dashboard, service-specific notifications, and direct customer outreach. Clear migration paths and documentation are provided to support the transition.

**New features and services:** These represent additions to the AWS platform, including new service releases, significant feature additions, and new API operations. Customers are notified through AWS What's New announcements, service-specific release notes, the AWS Health Dashboard, developer documentation, and blog posts.

**Non-customer impacting changes:** These include internal improvements, infrastructure updates, and backend optimizations that do not affect customer-facing functionality or require customer action. While these changes undergo the same rigorous testing and deployment processes described in this document, they are not communicated to customers. The volume of such changes is substantial and communicating each would result in notification fatigue without providing actionable information. AWS focuses customer communications on changes that require awareness or action, ensuring that notifications remain meaningful and relevant.

 Changes deployed into production environments are:
+ **Prepared:** this includes scheduling, determining resources, creating notification lists, scoping dependencies, minimizing concurrent changes, and a special process for emergent or long-running changes.
+ **Submitted:** this includes using a change management tool to document and request the change, determine potential impact, conduct a code review, create a detailed timeline and activity plan, and develop a detailed rollback procedure.
+ **Reviewed and approved:** Peer reviews of the technical aspects of a change are required. Changes must be authorized in order to provide appropriate oversight and understanding of business and security impact. The configuration management process includes key organizational personnel that are responsible for reviewing and approving proposed changes to the information system.
+ **Tested:** Changes being applied are tested to help ensure they will behave as expected and not adversely impact performance.
+ **Performed:** This includes pre- and post-change notification, managing the timeline, monitoring service health and metrics, and closing out the change.

 AWS service teams maintain a current authoritative baseline configuration for systems and devices. Change management tickets are submitted before changes are deployed (unless it is an emergency change) and include impact analysis, security considerations, description, timeframe and approvals. Changes are pushed into production in a phased deployment starting with lowest impact areas. Deployments are tested on a single system and closely monitored so impacts can be evaluated. Service owners have a number of configurable metrics that measure the health of the service's upstream dependencies. These metrics are closely monitored with thresholds and alarming in place. Rollback procedures are documented in the change management (CM) ticket. AWS service teams retain older versions of AWS baseline packages and configurations necessary to support rollback and previous versions are stored in the repository systems. Integration testing and the validation process is performed before rollbacks are implemented. When possible, changes are scheduled during regular change windows.

 In addition to the preventive controls that are part of the pipeline (for example, code review verifications, test environments), AWS also uses detective controls configured to alert and notify personnel when a change is detected that might have been made without standard procedure. AWS checks deployments to ensure that they have the appropriate reviews and approvals to be applied before the code is committed to production. Exceptions for reviews and approvals for production lead to automatic ticketing and notification of the service team.

 After code is deployed to the production environment, AWS performs ongoing monitoring of performance through a variety of monitoring processes. AWS host configuration settings are also monitored as part of vulnerability monitoring to validate compliance with AWS security standards. Audit trails of the changes are maintained.

 Emergency changes to production systems that require deviations from standard change management procedures are associated with an incident and are logged and approved as appropriate. Periodically, AWS performs self-audits of changes to key services to monitor quality, maintain high standards, and facilitate continuous improvement of the change management process. Any exceptions are analyzed to determine the root cause, and appropriate actions are taken to bring the change into compliance or roll back the change if necessary. Actions are then taken to address and remediate the process or people issue.

## Reviews
<a name="reviews"></a>

 AWS performs internal security reviews against Amazon security standards of externally launched products, services, and significant feature additions prior to launch to ensure security risks are identified and mitigated before deployment to a customer environment. AWS security reviews include evaluating the service's design, threat model, and impact to the risk profile of AWS. A typical security review starts with a service team initiating a review request to the dedicated team and submitting detailed information about the artifacts being reviewed. Based on this information, AWS reviews the design and identifies security considerations; these considerations include but are not limited to: appropriate use of encryption, analysis of data handling, regulatory considerations, and adherence to secure coding practices. Hardware, firmware, and virtualization software also undergo security reviews, including a security review of the hardware design, actual implementation and final hardware samples.

 Code package changes are subject to the following security activities:
+ Full security assessment
+ Threat modeling
+ Security design reviews
+ Secure code reviews (manual and automated methods)
+ Security testing
+ Vulnerability/penetration testing

 Successful completion of the preceding activities is a prerequisite for service launch. Development teams are responsible for the security of the features they develop that meet the security engineering principles. Infrastructure teams incorporate security principles into the configuration of servers and network devices with least privilege enforced throughout. Findings identified by AWS are categorized in terms of risk and are tracked in an automated workflow tool.

## Customer training
<a name="customer-training"></a>

 AWS has implemented various methods of external communication to support its customer base and the community. Mechanisms are in place to allow the customer support team to be notified of operational issues that impact your experience. A [Service Health Dashboard](https://status.aws.amazon.com/) is available and maintained by the customer support team to alert you to any issues that might be of broad impact. The [AWS Cloud Security Center](https://aws.amazon.com/security/) and [Healthcare and Life Sciences Center](https://aws.amazon.com/health/) are available to provide you with security and compliance details and Life Sciences related enablement information about AWS. You can also subscribe to AWS Support offerings that include direct communication with the customer support team and proactive alerts to any customer impacting issues.

 AWS also has a series of [training and certification programs](https://www.aws.training/) on a number of cloud-related topics in addition to a series of service and support offerings available through your AWS account team.
