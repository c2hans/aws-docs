---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/migrate.html
---

# Migrate phase
<a name="migrate"></a>

![https://1a9zxhkqsj.execute-api.us-west-2.amazonaws.com/v1/contents/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/a5d99701-2f4f-41e5-878f-3c0a1fc8c12d.png](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/edbcb404-53d9-4165-89b2-318d883f3e3d.png)

The migrate phase focuses on moving SAP workloads at scale and ensuring that the SAP on AWS infrastructure goes live successfully. To ensure this, the project uses IaC technologies such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to automate SAP provisioning. If you want to use open-source tools,  you can read about the SAP repositories built by AWS Professional Services teams that specialize in SAP migrations, as described in the blog post [Automating SAP installation with open-source tools](https://aws.amazon.com/blogs/awsforsap/automating-sap-installation-with-open-source-tools/).

The project team automates the infrastructure build and provisions the key AWS components in the cloud. You can test the newly provisioned systems and redirect interfaces to new targets while the project team assists in building the AWS infrastructure and resolving SAP-related issues. You can also plan and perform cut-over activities while the project team assists in cutting over to the AWS infrastructure and handling SAP tasks, potential risks, and issues. Your data is migrated by using the tools and methods that were defined in the mobilize phase. For production systems, a mock cut-over is performed, tested, and fine-tuned. Finally, detailed reporting is provided so you can evaluate critical infrastructure, key performance indicators (KPIs) for the project, and milestones. At a macro level, the migrate phase is completed in a number of waves, as described previously in the overview.

|
|
|             Objectives:+ Migrate SAP workloads to AWS<br />+ Deploy automated IaC systems<br />+ Put basic operational procedures in place<br />+ Cut over to SAP on AWS and go live <br />+ Run the SAP on AWS go-live assessment <br />+ Go live with operations  |             Actions:+ Run IaC systems and set up the architecture on AWS<br />+ Set up migration tools<br />+ Automate provisioning of the operating system, file systems, and databases<br />+ Migrate SAP workloads<br />+ Perform testing, defect resolution, and basic performance-tuning<br />+ Automate operational procedures such as backups, automatic scaling, and monitoring<br />+ Cut over and go live |
| --- |--- |
|             **Inputs:**+ Outputs from the mobilize phase<br />+ AWS best practices for migration<br />+ Migration tools<br />  |             **Outputs:**+ Report on enabled AWS services<br />+ Report on running SAP workloads on AWS<br />+ Report on open and resolved defects<br />+ Test reports<br />+ Cutover report |

The following diagram provides a simplified example of the migrate phase (in green) as part of the full migration process. It shows the SAP production systems being migrated in two waves.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/d383f299-152c-4d23-8e93-dc04cea244f1.png)

For more information about this phase, read how the UK energy company Centrica [migrated their multibillion dollar enterprise](https://aws.amazon.com/partners/success/centrica-capgemini/) with the assistance of AWS Professional Services, as part of their digital transformation.

You can also read how [Moderna Therapeutics Delivers used AWS for its SAP workloads](https://aws.amazon.com/solutions/case-studies/moderna-therapeutics/) to deliver mRNA drugs faster and at lower cost. Moderna received help from [AWS Professional Services](https://aws.amazon.com/professional-services/) consultants with life sciences expertise to build a fully validated SAP environment in the AWS Cloud.
