---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost_evaluate_cost_effort_automations_operations.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST11-BP01 Perform automations for operations
<a name="cost_evaluate_cost_effort_automations_operations"></a>

 Evaluate cost of effort for operations on cloud. Quantify reduction in time and effort for admin tasks, deployment and other operations using automation. Evaluate the required time and cost for the effort of operations and automate admin tasks to reduce the human effort where possible.

 **Level of risk exposed if this best practice is not established:** Low

 Automating operations improves consistency and scalability, provides more visibility, reliability, and flexibility, reduces costs, and accelerates innovation by freeing up human resources and improving metrics. It reduces the frequency of manual tasks, improves efficiency, and benefits enterprises by delivering a consistent and reliable experience when deploying, administering, or operating workloads. You can free up infrastructure resources from manual operational tasks and use them for higher value tasks and innovations, thereby improving business outcomes. Enterprises require a proven, tested way to manage their workloads in the cloud. That solution must be secure, fast, and cost effective, with minimum risk and maximum reliability.

 Start by prioritizing your operations based on required effort by looking at overall operations cost in the cloud. For example, how long does it take to deploy new resources in the cloud, make optimization changes to existing ones, or implement necessary configurations? Look at the total cost of human actions by factoring in cost of operations and management. Prioritize automations for admin tasks to reduce the human effort. Review effort should reflect the potential benefit. For example, time spent performing tasks manually as opposed to automatically. Prioritize automating repetitive, high value activities. Activities that pose a higher risk of human error are typically the better place to start automating as the risk often poses an unwanted additional operational cost (like operations team working extra hours).

 Using AWS services, tools, or third-party products, you can choose which AWS automations to implement and customize for your specific requirements. The following table shows some of the core operation functions and capabilities you can achieve with AWS services to automate administration and operation:
+  [AWS Audit Manager](https://aws.amazon.com/audit-manager/): Continually audit your AWS usage to simplify risk and compliance assessment
+  [AWS Backup](https://aws.amazon.com/backup/): Centrally manage and automate data protection.
+  [AWS Config](https://aws.amazon.com/config/): Configure compute resources, assess, audit, and evaluate configurations and resource inventory.
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/): Launch highly available resources with infrastructure as code.
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/): IT change management, compliance, and control.
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/): Schedule events and launch AWS Lambda to take action.
+  [AWS Lambda](https://aws.amazon.com/lambda/): Automate repetitive processes by initiating them with events or by running them on a fixed schedule with Amazon EventBridge.
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/): Start and stop workloads, patch operating systems,a automate configuration, and ongoing management.
+  [AWS Step Functions](https://aws.amazon.com/step-functions/): Schedule jobs and automate workflows.
+  [AWS Service Catalog](https://aws.amazon.com/servicecatalog/): Template consumption and infrastructure as code with compliance and control.

 Consider the time savings that will allow your team to focus on retiring technical debt, innovation, and value-adding features. For example, you might need to lift and shift your on-premises environment into the cloud as rapidly as possible and optimize later. It is worth exploring the savings you could realize by using fully managed services by AWS that remove or reduce license costs such as [Amazon Relational Database Service](https://aws.amazon.com/rds/), [Amazon EMR](https://aws.amazon.com/emr/), [Amazon WorkSpaces](https://aws.amazon.com/workspaces/), and [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/). Managed services remove the operational and administrative burden of maintaining a service, which allows you to focus on innovation. Additionally, because managed services operate at cloud scale, they can offer a lower cost per transaction or service.

 If you would like to adopt automations immediately with using AWS products and service and if don’t have skills in your organization, reach out to [AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/), [AWS Professional Services](https://aws.amazon.com/professional-services/), or [AWS Partners](https://aws.amazon.com/partners/work-with-partners/) to increase adoption of automation and improve your operational excellence in the cloud.

 [AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/) is a service that operates AWS infrastructure on behalf of enterprise customers and partners. It provides a secure and compliant environment that you can deploy your workloads onto. AMS uses enterprise cloud operating models with automation to allow you to meet your organization requirements, move into the cloud faster, and reduce your on-going management costs.

 [AWS Professional Services](https://aws.amazon.com/professional-services/) can also help you achieve your desired business outcomes and automate operations with AWS. AWS Professional Services provides global specialty practices to support your efforts in focused areas of enterprise cloud computing. Specialty practices deliver targeted guidance through best practices, frameworks, tools, and services across solution, technology, and industry subject areas. They help customers to deploy automated, robust, agile IT operations, and governance capabilities optimized for the cloud center.

 **Implementation steps**
+  **Build once and deploy many:** Use infrastructure-as-code such as AWS CloudFormation, AWS SDK, or AWS Command Line Interface (AWS CLI) to deploy once and use many times for same environment or for disaster recovery scenarios. Tag while deploying to track your consumption as defined in other best practices. Use [AWS Launch Wizard](https://aws.amazon.com/launchwizard/) to reduce the time to deploy many popular enterprise workloads. AWS Launch Wizard guides you through the sizing, configuration, and deployment of enterprise workloads following AWS best practices. You can also use the [AWS Service Catalog](https://aws.amazon.com/servicecatalog/), which helps you create and manage infrastructure-as-code approved templates for use on AWS so anyone can discover approved, self-service cloud resources.
+  **Automate operations:** Run routine operations automatically without human intervention. Using AWS services and tools, you can choose which AWS automations to implement and customize for your specific requirements. For example, use [EC2 Image Builder](https://aws.amazon.com/image-builder/) for building, testing, and deployment of virtual machine and container images for use on AWS or on-premises. If your desired action cannot be done with AWS services or you need more complex actions with filtering resources, then automate your operations with using [AWS CLI](https://aws.amazon.com/cli/index.html) or AWS SDK tools. AWS CLI provides the ability to automate the entire process of controlling and managing AWS services via scripts without using the AWS Console. Select your preferred AWS SDKs to interact with AWS services. For other code examples, see [AWS SDK Code examples repository](https://github.com/awsdocs/aws-doc-sdk-examples).

## Resources
<a name="resources"></a>

 **Related documents:**
+ [ Modernizing operations in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/welcome.html)
+ [AWS Services for Automation ](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/aws-services-for-automation.html)
+ [AWS Systems Manager Automation ](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
+ [AWS automations for SAP administration and operations ](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/automations.html)
+ [AWS Managed Services](https://aws.amazon.com/managedservices/index.html)
+ [AWS Professional Services ](https://aws.amazon.com/professional-services/)
+ [ Infrastructure and automation ](https://aws.amazon.com/blogs/infrastructure-and-automation/)

 **Related examples:**
+ [ Reinventing automated operations (Part I) ](https://aws.amazon.com/blogs/mt/reinventing-automated-operations-part-i/)
+ [ Reinventing automated operations (Part II) ](https://aws.amazon.com/blogs/mt/reinventing-automated-operations-part-ii/)
+ [AWS automations for SAP administration and operations ](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/automations.html)
+ [ IT Automations with AWS Lambda](https://aws.amazon.com/lambda/it-automation/)
+ [AWS Code Examples Repository ](https://github.com/awsdocs/aws-doc-sdk-examples)
+ [AWS Samples ](https://github.com/aws-samples)
