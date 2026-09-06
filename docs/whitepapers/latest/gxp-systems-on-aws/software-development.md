---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/software-development.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Software Development
<a name="software-development"></a>

## Software Development Processes
<a name="software-development-processes"></a>

 The Project and Operation stages of the life cycle approach in GAMP, for instance, are reflected in the AWS information and activities surrounding organizational mechanisms to guide the development and configuration of the information system, including software development lifecycles and software change management. Elements of the organizational mechanisms include policies and standards, the code pathway, deployment, a change management tool, ongoing monitoring, security reviews, emergency changes, management of outsourced and unauthorized development and communication of changes to customers.

 The software development lifecycle activities at AWS include the code development and change management processes at AWS which are centralized across AWS teams developing externally- and internally-facing code with processes applying to both internal and external service teams. Code deployed at AWS is developed and managed in a consistent process, regardless of its ultimate destination. There are several systems utilized in this process, including:
+  A code management system used to assemble a code package as part of development.
+  Internal source code repository.
+  The hosting system in which AWS code pipelines are staged.
+  The tool utilized for automating the testing, approval, deployment, and ongoing monitoring of code.
+  A change management tool which breaks change workflows down into discrete, easy to manage steps and tracks change details.
+  A monitoring service to detect unapproved changes to code or configurations in production systems. Any variances are escalated to the service owner/team.

## Code Pathway
<a name="code-pathway"></a>

 The AWS Code Pathway steps to development and deployment are outlined below. This process is executed regardless of whether the code is net new or if it represents a change to an existing codebase.

1.  Developer writes the code in an approved integrated development environment running on an AWS-managed developer desktop environment. The developer typically does an initial build and integration test prior to the next step.

1.  The developer checks in the code for review to an internal source code repository.

1.  The code goes through a Code Review Verification in which at least one additional person reviews the code and approves it. The list of approvals are stored in an immutable log that is retained within the code review tool.

1.  The code is then built from source code to the appropriate type of deployable code package (which varies from language to language) in an internal build system.

1.  After successful build, including successful passing of all integration tests, the code gets pushed to a test environment.

1.  The code goes through automated integration and verification tests in the pre-production environments and upon successful testing the code is pushed to production.

 AWS may implement open source code within its Services, but any such use of open source code is still subject to the approval, packaging, review, deployment, and monitoring processes described above. Open source software, including binary or machine-executable code and open source licenses, is additionally reviewed and approved prior to implementation. AWS maintains a list of approved open source, as well as open source that is prohibited.

## Deployment and Testing
<a name="deployment-and-testing"></a>

 A pipeline represents the path approved code packages take from initial check-in through a series of automated (and potentially manual) steps to execution in production. The pipeline is where automation, testing, and approvals happen.

 At AWS, the deployment tool is used to create, view, and enforce code pipelines. This tool is utilized to promote the latest approved revision of built code to the production environment.

 A major factor in ensuring safe code deployment is deploying in controlled stages and requiring continuous approvals prior to pushing code to production. As part of the deployment process, pipelines are configured to release to test environments (e.g. “beta,” “gamma,” and others, as defined by the team) prior to pushing the code to the production environment. Automated quality testing (e.g. integration testing, structural testing, behavioral testing) is performed in these environments to ensure code is performing as anticipated. If code is found to deviate from standards, the release is halted and the team is notified of the need to review.

 These development and test environments emulate the production environment and are used to properly assess and prepare for the impact of a change to the production environment. In order to reduce the risks of unauthorized access or change to the production environment, the development, test and production environments are all logically separated.

 The tool additionally enforces phased deployment, if the code is to be deployed across multiple regions. Should a package include deployment for more than one AWS region, the pipeline will enforce deployment on a single-region basis. If the package were to fail integration tests at any region, the pipeline is halted and the team is notified for need to review.

## Configuration and Change Management
<a name="configuration-and-change-management"></a>

 Configuration management is performed during information system design, development, implementation, and operation through the use of the AWS Change Management process.

 Routine, emergency, and configuration changes to existing AWS infrastructure are authorized, logged, tested, approved, and documented in accordance with industry norms for similar systems. Updates to the AWS infrastructure are done to minimize any impact on you and your use of the services.

## Software
<a name="software"></a>

 AWS applies a systematic approach to managing change so that changes to customer-impacting services are thoroughly reviewed, tested, approved, and well-communicated. The AWS change management process is designed to avoid unintended service disruptions and to maintain the integrity of service to you. Changes deployed into production environments are:
+  Prepared: this includes scheduling, determining resources, creating notification lists, scoping dependencies, minimizing concurrent changes as well as a special process for emergent or long running changes.
+  Submitted: this includes utilizing a Change Management Tool to document and request the change, determine potential impact, conduct a code review, create a detailed timeline and activity plan and develop a detailed rollback procedure.
+  Reviewed and Approved: Peer reviews of the technical aspects of a change are required. Changes must be authorized in order to provide appropriate oversight and understanding of business and security impact. The configuration management process includes key organizational personnel that are responsible for reviewing and approving proposed changes to the information system.
+  Tested: Changes being applied are tested to help ensure they will behave as expected and not adversely impact performance.
+  Performed: This includes pre and post change notification, managing timeline, monitoring service health and metrics, and closing out the change

 AWS service teams maintain a current authoritative baseline configuration for systems and devices. Change Management tickets are submitted before changes are deployed (unless it is an emergency change) and include impact analysis, security considerations, description, timeframe and approvals. Changes are pushed into production in a phased deployment starting with lowest impact areas. Deployments are tested on a single system and closely monitored so impacts can be evaluated. Service owners have a number of configurable metrics that measure the health of the service’s upstream dependencies. These metrics are closely monitored with thresholds and alarming in place. Rollback procedures are documented in the Change Management (CM) ticket. AWS service teams retain older versions of AWS baseline packages and configurations necessary to support rollback and previous versions are stored in the repository systems. Integration testing and the validation process is performed before rollbacks are implemented. When possible, changes are scheduled during regular change windows.

 In addition to the preventative controls that are part of the pipeline (e.g. code review verifications, test environments), AWS also uses detective controls configured to alert and notify personnel when a change is detected that may have been made without standard procedure. AWS checks deployments to ensure that they have the appropriate reviews and approvals to be applied before the code is committed to production. Exceptions for reviews and approvals for production lead to automatic ticketing and notification of the service team.

 After code is deployed to the Production environment, AWS performs ongoing monitoring of performance through a variety of monitoring processes. AWS host configuration settings are also monitored as part of vulnerability monitoring to validate compliance with AWS security standards. Audit trails of the changes are maintained.

 Emergency changes to production systems that require deviations from standard change management procedures are associated with an incident and are logged and approved as appropriate. Periodically, AWS performs self-audits of changes to key services to monitor quality, maintain high standards, and facilitate continuous improvement of the change management process. Any exceptions are analyzed to determine the root cause, and appropriate actions are taken to bring the change into compliance or roll back the change if necessary. Actions are then taken to address and remediate the process or people issue.

## Reviews
<a name="reviews"></a>

 AWS performs internal security reviews against Amazon security standards of externally launched products, services, and significant feature additions prior to launch to ensure security risks are identified and mitigated before deployment to a customer environment. AWS security reviews include evaluating the service’s design, threat model, and impact to AWS’ risk profile. A typical security review starts with a service team initiating a review request to the dedicated team and submitting detailed information about the artifacts being reviewed. Based on this information, AWS reviews the design and identifies security considerations; these considerations include, but are not limited to: appropriate use of encryption, analysis of data handling, regulatory considerations, and adherence to secure coding practices. Hardware, firmware and virtualization software also undergo security reviews, including a security review of the hardware design, actual implementation and final hardware samples.

 Code package changes are subject to the following security activities:
+  Full security assessment
+  Threat modeling
+  Security design reviews
+  Secure code reviews (manual and automated methods)
+  Security testing
+  Vulnerability/penetration testing

 Successful completion of the above mentioned activities are pre-requisites for Service launch. Development teams are responsible for the security of the features they develop that meet the security engineering principles. Infrastructure teams incorporate security principles into the configuration of servers and network devices with least privilege enforced throughout. Findings identified by AWS are categorized in terms of risk, and are tracked in an automated workflow tool.

## Product Release
<a name="product-release"></a>

 For all AWS services, information can be found on the associated service website, which describes the key attributes of the Service and product details, as well as pricing information, developer resources (including release notes and developer tools), FAQs, blogs, presentations and additional documentation such as developer guides, API references, and use cases, where relevant ([https://aws.amazon.com/products/](https://aws.amazon.com/products/) ).

## Customer Training
<a name="customer-training"></a>

 AWS has implemented various methods of external communication to support its customer base and the community. Mechanisms are in place to allow the customer support team to be notified of operational issues that impact your experience. A Service Health Dashboard is available and maintained by the customer support team to alert you to any issues that may be of broad impact. The AWS Cloud Security Center ([https://aws.amazon.com/security/](https://aws.amazon.com/security/)) and Healthcare and Life Sciences Center ([https://aws.amazon.com/health/](https://aws.amazon.com/health/)) is available to provide you with security and compliance details and Life Sciences related enablement information about AWS. You can also subscribe to AWS Support offerings that include direct communication with the customer support team and proactive alerts to any customer impacting issues.

 AWS also has a series of training and certification programs ([https://www.aws.training/](https://www.aws.training/)) on a number of cloud-related topics in addition to a series of service and support offerings available through your AWS account team.
