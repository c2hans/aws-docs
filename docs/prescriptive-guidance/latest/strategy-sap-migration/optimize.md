---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/optimize.html
---

# Optimize phase
<a name="optimize"></a>

![https://1a9zxhkqsj.execute-api.us-west-2.amazonaws.com/v1/contents/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/0e96f82b-8a60-4ec3-bd9d-5be57fa6d8ce.png](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/8a472bf2-e6c8-4bbf-bb74-a9ef5c68e8bc.png)

The optimize phase covers continuous process improvements for the infrastructure and ensures that security compliance is met. It focuses on operations that target further infrastructure automation, system fine-tuning, and AWS best practices. In this phase, the project team verifies that the objectives set in the design documents (developed during the mobilize phase) have been achieved, and, if required, adjusts the parameters of the platform for the SAP workloads. If necessary, adjustments are made to maximize performance and business benefits while minimizing risks and costs. The final operations on the platform are set up, reports are generated, and the project closure documentation is signed off.

You can find more about [Automation strategy for SAP operations in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/welcome.html) in our AWS Prescriptive Guidance document. Should you require to optimize costs of your SAP workloads on AWS you can find more details on [Cost optimization strategy for SAP workloads in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-cost-optimization/introduction.html).

|
|
|             Objectives:+ Provide hyper-care support after going live<br />+ Set up detailed operations<br />+ Automate operations<br />+ Review and optimize security setup<br />+ Optimize system performance  |             Actions:+ Automate alerts based on key events and thresholds<br />+ Automate and set up Amazon Machine Image (AMI) and Amazon Elastic Block Store (Amazon EBS) snapshots, SAP automatic scaling, automated database refresh capabilities, and SAP HANA patching<br />+ Review and optimize security setup, including encryption, virtual private cloud (VPC), and central logging<br />+ Optimize cost and performance, including fine-tuning sizing, elasticity, and backups |
| --- |--- |
|             **Inputs:**+ Outputs from the migrate phase<br />+ AWS best practices for operations, related automation mechanisms, and modernization<br />  |             **Outputs:**+ Report of final architecture compliance<br />+ Report on the security of SAP infrastructure on AWS <br />+ Report on cost and performance optimization<br />  |

For more information about this phase, see [Automation strategy for SAP operations in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/welcome.html). For more information about optimizing costs, see [Cost optimization strategy for SAP workloads in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-cost-optimization/introduction.html).

In addition, the following blog posts describe how customers who run SAP on AWS can take advantage of a broad set of additional services to enhance and simplify the operations of running SAP.  Such services are delivered as a part of the optimize phase.
+ [Audit your SAP systems with AWS Config](https://aws.amazon.com/blogs/awsforsap/audit-your-sap-systems-with-aws-config-part-i/) explains how you can validate that your systems are compliant.
+ [Maintain an SAP landscape inventory with AWS Systems Manager and Amazon Athena](https://aws.amazon.com/blogs/awsforsap/maintain-an-sap-landscape-inventory-with-aws-systems-manager-and-amazon-athena/) describes how you can maintain your SAP landscape inventory and operate your infrastructure at an optimum level.
