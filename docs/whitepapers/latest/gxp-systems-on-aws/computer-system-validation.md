---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/computer-system-validation.html
---

# Computer systems assurance
<a name="computer-system-validation"></a>

Computer Software Assurance (CSA) in GxP environments are guidelines referring to a modern, risk-based approach to software validation. These guidelines are designed to ensure product quality, patient safety, and data integrity across all stages of the product lifecycle. Historically, the industry has relied on Computer System Validation (CSV) as a compliance framework, particularly in accordance with the U.S. Food and Drug Administration (FDA) requirements outlined in 21 CFR Part 11 for electronic records and signatures and 21 CFR Part 820 for quality system regulations in medical device manufacturing. However, the FDA's guidance on Computer Software Assurance for Production and Quality System Software, published in September 2025, marks a significant shift toward a more flexible and risk-based approach to software validation.

The FDA's guidance proposes CSA as a modernized alternative to traditional CSV, focusing on risk-based assurance rather than exhaustive documentation. This shift reflects the FDA's intent to streamline validation processes without compromising regulatory compliance or patient safety. The guidance emphasizes that manufacturers should focus on ensuring that software functions as intended, particularly when used within production or quality systems as defined under 21 CFR 820.70(i). This regulation mandates that manufacturers validate software for its intended use when it is part of the production or quality system, highlighting the importance of functionality in maintaining compliance.

A core principle of CSA, as outlined in the FDA guidance, is to shift effort from documentation to critical thinking, reasoned decisions, and testing that assure quality, not only paper trails.

Assurance activities should be proportional to the risk associated with the software's failure. This requires manufacturers to assess the software's intended use and the potential consequences if it fails. If a failure could directly affect patient safety, product quality, or data integrity, it demands more rigorous assurance activities. For example, software used to control critical production parameters—such as temperature, pressure, or humidity—poses a high risk, because failure could compromise product safety. Such systems, under 21 CFR Part 820.70, must undergo comprehensive validation. Conversely, administrative software, like scheduling tools or email systems, falls outside the scope of 21 CFR 820.70(i) and typically requires minimal validation, as their failure would not directly impact product quality or patient safety.

In this section we will apply some critical thinking to find alternate ways of achieving some of our control objectives but in a much more efficient way, using current cloud engineering good practices.

## Installation verification
<a name="installation-verification"></a>

Traditionally, this meant creating an installation qualification protocol and having various system administrators execute their parts, sign, date, and so on. This worked well to demonstrate control over a manual installation process. However, good engineering practices now automate this whole procedure.

This verification and documentation demonstrate a system is installed according to a pre-approved specification. Verification is achieved through testing that shows that the installation and configuration of software and hardware is correct.

First, let's consider the pre-approved specification. It is an AWS best practice to define the required infrastructure through the use of an infrastructure as code (IaC) template or code. This template describes the required resources and their configuration. The configuration might change slightly between environments (QA, UAT, PRE-PROD, and PROD) and Regions, but the core IaC template does not. This flexibility is achieved through template parameters. This template is then used by CloudFormation to provision the resources.

These templates are controlled in a similar way as source code. By storing them in a source code repository it enables us to version the template and keep a complete history of its evolution over time.

Another key part of that phrase is pre-approved. There are many ways that a customer can handle the approval. For example, a Jira workflow or a pull request approval in their source code repository. Whatever the method it will be vetted and approved by the customers Quality IT or Compliance team. The net result is a specific version of the template in the source code repository being recorded as approved.

So, you now have a pre-approved specification describing the resources you want deployed. An automated pipeline is then triggered to deploy the resources. You then need to look at the next requirement, which is to demonstrate the installation was correct. This can be done at various points in the pipeline.

Testing application code during development is a common practice. If using AWS CDK you can perform [local testing](https://docs.aws.amazon.com/cdk/v2/guide/testing-locally.html) during the development cycle of your infrastructure code.

[CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html) is a feature that helps ensure that your CloudFormation resources, stacks, and change sets comply with your organization's security, operational, and cost optimization best practices. CloudFormation Hooks can also ensure this same level of compliance for your [AWS Cloud Control API](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html) resources. With CloudFormation Hooks, you can provide code that proactively inspects the configuration of your AWS resources before provisioning. If non-compliant resources are found, CloudFormation either fails the operation and prevents the resources from being provisioned or emits a warning and allows the provisioning operation to continue.

CloudFormation is the service that provisions your resources. Its sole purpose is to help you model and provision AWS infrastructure as code (IaC). It allows you to manage, provision, and update related AWS and third-party resources in an orderly and predictable fashion. If there is no error during provisioning, then confidence is high the resources were provisioned as expected. If there is an error, then manual intervention is required but we have improved process efficiency and positioned manual review by exception only.

Post-deployment, automated tests can be included in the pipeline to test provisioned resources. These tests can generate evidence that the resources are configured correctly and functioning as expected. In addition, it is a best practice to use [AWS Config Rules](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRule.html) which evaluate the configuration settings of your provisioned AWS resources. AWS Config rules continuously evaluate your AWS resource configurations for compliance with desired settings helping ensure resource configurations remain compliant. A rule can run when AWS Config detects a configuration change to an AWS resource or at a periodic frequency that you choose.

With all these checks at various points in the automated pipeline, and all the evidence they generate, it could be argued that traditional manual testing and verification reporting is no longer needed. Should a report still be needed to adhere to SOPs, it can be generated from the data generated by the automation.

## Inspection readiness through IT records
<a name="inspection-readiness"></a>

Under the CSA framework the focus shifts from documentation toward collecting only the evidence necessary to demonstrate that the software is fit for its intended use. The FDA encourages using electronic records, audit trails, and system logs to capture objective evidence efficiently.

Development tools generate extensive compliance documentation during the engineering process. Version control systems maintain complete histories of every code change with developer attribution and timestamps. Continuous integration pipelines capture test results in machine-readable formats that provide better evidence than manual screenshots. Deployment automation documents every change from development to production with full traceability. These tools create richer compliance documentation by preserving the actual evolution of software rather than collecting signatures on point-in-time snapshots.

The basic premise is to have access to all the data generated by our IT tooling. Rather than generating separate documents as evidence, use the IT records from the tooling. This data can be gathered into a data lake or joined virtually. The main requirement being that nobody should be able to change the data—that it is immutable—because it forms the basis of your regulatory evidence. This data effectively enables you to create a digital twin of your software development lifecycle (SDLC). After this data is available it can be queried to answer quality related questions or demonstrate control effectiveness. For example, data from requirements management and test management tooling can be combined to create a traceability matrix showing requirements have been tested and those tests are passing. The data can answer inspection questions like what features were included in a specific release or demonstrate that server patching is happening and that all servers are on the latest release.

Along with answering questions, dashboards can be created to show the current compliance status at all times, helping move from a static point-in-time view of compliance to a continuous compliance stance. It also helps show operational healthiness, for example, team velocity or end-to-end productivity.

The next logical progression is that this data foundation enables agentic AI quality management. For example, if a defect is detected or reported it can trigger an agentic workflow to determine the root cause and suggest remediation steps. It could even execute those remediation steps.

## Good technical documentation
<a name="good-technical-documentation"></a>

Documentation remains a crucial aspect of GxP compliance. The documentation should include the intended use of the software, risk assessment results, assurance activities performed, and any issues discovered during testing, along with their resolutions.

During a typical development cycle there is a risk that documentation gets out of sync with reality. One mechanism that has proven effective to combat this, for technical documentation usually maintained by the technical team, is the use of markup stored in the code repository alongside the code (application code, infrastructure as code, LZA template, and so on.). As the code is updated, the markup is also updated, and this is confirmed during code review or approval. As the code is built and deployed, the documentation is also deployed to a wiki. This technique has the advantage that documentation is stored in the same place as the code, updated at the same time, and maintained using the same development tools as the code, reducing the risk of documentation getting out of sync with reality.

Development tools generate extensive compliance evidence during the engineering process. Version control systems maintain complete histories of every code change with developer attribution and timestamps. Continuous integration pipelines capture test results in machine-readable formats that provide better evidence than manual screenshots. Deployment automation documents every change from development to production with full traceability. These tools create richer compliance evidence by preserving the actual evolution of software rather than collecting signatures on point-in-time snapshots.

## Validation during cloud migration
<a name="validation-during-cloud-migration"></a>

One important point that might be covered in a cloud strategy is the overarching approach to computer system validation (CSV) during migration. If you are embarking on a migration effort, part of the analysis of the application portfolio will be to identify archetypes, or groups of applications with similar architectures. A single runbook can be developed and then repeated for each of the applications in the group, speeding up migration.

At this point, if the applications are GxP relevant, the CSV or migration strategy can also be defined for the archetype and repeated for each application.

For further information about the migration of GxP workloads to the AWS cloud, see [this series of blog posts](https://aws.amazon.com/blogs/migration-and-modernization/gxp-considerations-for-large-scale-migrations-part-1/).
