---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/risk-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Risk management
<a name="risk-management"></a>

** Use cloud to lower your risk profile. **

 Any transformation journey includes many different types of risks, including security, compliance, environmental, resiliency, and business. An organization either rejects, accepts and manages, or transfers the risks. The risk management lifecycle is cyclically completed through assessments to identify risks, treatments through the implementation of risk mitigation strategies, and management through continuous monitoring. Efforts and resources to perform risk assessments, treatments, and management can be significantly reduced by moving workloads to the cloud, enabling the business to innovate faster and operate more efficiently.

## Start
<a name="start-2"></a>

 Develop or identify an industry leading risk management framework. Identify and create an inventory of the high value assets, including but not limited to people, process, technology and data. Organizations must identify, categorize, assess, and quantify:
+  Operational [risks](https://pages.awscloud.com/rs/112-TZM-766/images/GEN_windows-on-aws-risk-mitigation-idc-mini-report_Sep-2019.pdf) related to infrastructure availability, reliability, performance, and security
+  Business risks related to reputation, business continuity, and the ability to quickly respond to changing market conditions
+  Compliance risks for companies obligated to comply with laws, regulations, or rules associated with the industries in which they participate, such as [National Institute of Standards and Technology](https://aws.amazon.com/compliance/nist/) (NIST) 800-53, [Payment Card Industry Data Security Standard](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/) (PCI DSS), [Health Insurance Portability and Accountability Act](https://aws.amazon.com/compliance/hipaa-compliance/) of 1996 (HIPAA), and others

 Develop the risk profile, determine organizational risk appetite based on each identified event’s impact to the business and acceptable probability of occurrence. Clearly understand the attributes that are contributing to an elevated risk profile. Determine areas that are ripe to reduce risk. Build an initial backlog of stories and a roadmap for lowering your risk profile on the cloud.

 Consider using cloud to reduce risks relating to infrastructure operations and failure. Eliminate the need for large upfront infrastructure expenditures and reduce the risk of purchasing assets that may be no longer needed. Depending on the needs of your users, mitigate procurement schedule risks by using cloud to instantly provision and deprovision resources.

## Advance
<a name="advance-2"></a>

 Maintain a strong risk posture in the cloud, without having to define, build, and maintain hundreds of controls. Remove the burden of defining, enforcing, and evidencing the configurations and controls required to ensure the confidentiality, integrity, and availability of high value assets. Organizations should consider continuous risk assessments to understand and prioritize AWS services in an agile manner. Consider a [shift left](https://devopedia.org/shift-left) approach in the secure development to identify and manage risks at early as possible.

 Implement AWS services required for [risk management and compliance](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/governance.html) including:
+  [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)
+  [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
+  [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)
+  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
+  [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
+  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM)
+  [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
+  [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
+  [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
+  [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html)
+  [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html), and more.

 Continuously monitor, inventory and tag the business’s AWS high value assets to the right categories. Include third party risks in the risk management approach.

## Excel
<a name="excel-2"></a>

 Automate and orchestrate to provide means for the risk management processes to enforce controls consistently by using [policy as code](https://aws.amazon.com/blogs/mt/policy-as-code-for-securing-aws-and-third-party-resource-types/) (PaC) programmatically and at scale. This requires organizations to adopt a [Zero Trust](https://aws.amazon.com/security/zero-trust/) approach with least privilege and risk-based access controls through automation of use cases and design patterns using DevSecOps.

 Automating processes and workflows minimizes defects due to human error by embedding automated controls and tests into the [DevSecOps pipelines](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/). These also avoid bottlenecks and deliver capabilities faster by automating the tasks and approval gates that do not require human intervention. However, for risk automation process to be successful, it is critical to involve the right stakeholders such as business, risks, security, governance and operations teams in the initial, as well as routine, pipeline-related activities.

 Consider implementing AWS Control Tower, [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), [Terraform](https://aws.amazon.com/blogs/apn/using-terraform-to-manage-aws-programmable-infrastructures/), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) functions to perform automated, event-driven actions that automate the security operations. AWS Security Hub CSPM, AWS CloudTrail, AWS CloudWatch, [Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/detective-investigation-about.html), Amazon GuardDuty, Amazon Inspector, and AWS Config provide continuous protection from real-time threats and misconfigurations, ultimately ensuring that risk appetite remains within the acceptable range for the organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
