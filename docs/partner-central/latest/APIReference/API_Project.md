---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Project.html
---

# Project
<a name="API_Project"></a>

An object that contains the `Opportunity`'s project details.

## Contents
<a name="API_Project_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdditionalComments **   <a name="AWSPartnerCentral-Type-Project-AdditionalComments"></a>
Captures additional comments or information for the `Opportunity` that weren't captured in other fields.
Type: String
Pattern: `(?s).{1,255}`
Required: No

 ** ApnPrograms **   <a name="AWSPartnerCentral-Type-Project-ApnPrograms"></a>
Specifies the Amazon Partner Network (APN) program that influenced the `Opportunity`. APN programs refer to specific partner programs or initiatives that can impact the `Opportunity`.
Valid values: `APN Immersion Days | APN Solution Space | ATO (Authority to Operate) | AWS Marketplace Campaign | IS Immersion Day SFID Program | ISV Workload Migration | Migration Acceleration Program | P3 | Partner Launch Initiative | Partner Opportunity Acceleration Funded | The Next Smart | VMware Cloud on AWS | Well-Architected | Windows | Workspaces/AppStream Accelerator Program | WWPS NDPP`
Type: Array of strings
Required: No

 ** AwsPartition **   <a name="AWSPartnerCentral-Type-Project-AwsPartition"></a>
AWS partition where the opportunity will be deployed. Possible values: `aws-eusc` for AWS European Sovereign Cloud, `null` for all other partitions.
Type: String
Valid Values: `aws-eusc`
Required: No

 ** CompetitorName **   <a name="AWSPartnerCentral-Type-Project-CompetitorName"></a>
Name of the `Opportunity`'s competitor (if any). Use `Other` to submit a value not in the picklist.
Type: String
Valid Values: `Oracle Cloud | On-Prem | Co-location | Akamai | AliCloud | Google Cloud Platform | IBM Softlayer | Microsoft Azure | Other- Cost Optimization | No Competition | *Other`
Required: No

 ** CustomerBusinessProblem **   <a name="AWSPartnerCentral-Type-Project-CustomerBusinessProblem"></a>
Describes the problem the end customer has, and how the partner is helping. Utilize this field to provide a concise narrative that outlines the customer's business challenge or issue. Elaborate on how the partner's solution or offerings align to resolve the customer's business problem. Include relevant information about the partner's value proposition, unique selling points, and expertise to tackle the issue. Offer insights on how the proposed solution meets the customer's needs and provides value. Use concise language and precise descriptions to convey the context and significance of the `Opportunity`. The content in this field helps AWS understand the nature of the `Opportunity` and the strategic fit of the partner's solution.
Type: String
Pattern: `(?s).{20,2000}`
Required: No

 ** CustomerUseCase **   <a name="AWSPartnerCentral-Type-Project-CustomerUseCase"></a>
Specifies the proposed solution focus or type of workload for the Opportunity. This field captures the primary use case or objective of the proposed solution, and provides context and clarity to the addressed workload.
Valid values: `AI Machine Learning and Analytics | Archiving | Big Data: Data Warehouse/Data Integration/ETL/Data Lake/BI | Blockchain | Business Applications: Mainframe Modernization | Business Applications & Contact Center | Business Applications & SAP Production | Centralized Operations Management | Cloud Management Tools | Cloud Management Tools & DevOps with Continuous Integration & Continuous Delivery (CICD) | Configuration, Compliance & Auditing | Connected Services | Containers & Serverless | Content Delivery & Edge Services | Database | Edge Computing/End User Computing | Energy | Enterprise Governance & Controls | Enterprise Resource Planning | Financial Services | Healthcare and Life Sciences | High Performance Computing | Hybrid Application Platform | Industrial Software | IOT | Manufacturing, Supply Chain and Operations | Media & High performance computing (HPC) | Migration/Database Migration | Monitoring, logging and performance | Monitoring & Observability | Networking | Outpost | SAP | Security & Compliance | Storage & Backup | Training | VMC | VMWare | Web development & DevOps`
Type: String
Required: No

 ** DeliveryModels **   <a name="AWSPartnerCentral-Type-Project-DeliveryModels"></a>
Specifies the deployment or consumption model for your solution or service in the `Opportunity`'s context. You can select multiple options.
Options' descriptions from the `Delivery Model` field are:
+ SaaS or PaaS: Your AWS based solution deployed as SaaS or PaaS in your AWS environment.
+ BYOL or AMI: Your AWS based solution deployed as BYOL or AMI in the end customer's AWS environment.
+ Managed Services: The end customer's AWS business management (For example: Consulting, design, implementation, billing support, cost optimization, technical support).
+ Professional Services: Offerings to help enterprise end customers achieve specific business outcomes for enterprise cloud adoption (For example: Advisory or transformation planning).
+ Resell: AWS accounts and billing management for your customers.
+ Other: Delivery model not described above.
Type: Array of strings
Valid Values: `SaaS or PaaS | BYOL or AMI | Managed Services | Professional Services | Resell | Other`
Required: No

 ** ExpectedContractDuration **   <a name="AWSPartnerCentral-Type-Project-ExpectedContractDuration"></a>
Optional. The expected duration of the contract associated with this opportunity. Partners use this value alongside expected customer spend to convert Total Contract Value (TCV) into Monthly Recurring Revenue (MRR).
Type: [ExpectedContractDuration](API_ExpectedContractDuration.md) object
Required: No

 ** ExpectedCustomerSpend **   <a name="AWSPartnerCentral-Type-Project-ExpectedCustomerSpend"></a>
Represents the estimated amount that the customer is expected to spend on AWS services related to the opportunity. This helps in evaluating the potential financial value of the opportunity for AWS.
Type: Array of [ExpectedCustomerSpend](API_ExpectedCustomerSpend.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** OtherCompetitorNames **   <a name="AWSPartnerCentral-Type-Project-OtherCompetitorNames"></a>
Only allowed when `CompetitorNames` has `Other` selected.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** OtherSolutionDescription **   <a name="AWSPartnerCentral-Type-Project-OtherSolutionDescription"></a>
Specifies the offered solution for the customer's business problem when the ` RelatedEntityIdentifiers.Solutions` field value is `Other`.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** RelatedOpportunityIdentifier **   <a name="AWSPartnerCentral-Type-Project-RelatedOpportunityIdentifier"></a>
Specifies the current opportunity's parent opportunity identifier.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** SalesActivities **   <a name="AWSPartnerCentral-Type-Project-SalesActivities"></a>
Specifies the `Opportunity`'s sales activities conducted with the end customer. These activities help drive AWS assignment priority.
Valid values:
+ Initialized discussions with customer: Initial conversations with the customer to understand their needs and introduce your solution.
+ Customer has shown interest in solution: After initial discussions, the customer is interested in your solution.
+ Conducted POC/demo: You conducted a proof of concept (POC) or demonstration of the solution for the customer.
+ In evaluation/planning stage: The customer is evaluating the solution and planning potential implementation.
+ Agreed on solution to Business Problem: Both parties agree on how the solution addresses the customer's business problem.
+ Completed Action Plan: A detailed action plan is complete and outlines the steps for implementation.
+ Finalized Deployment Need: Both parties agree with and finalized the deployment needs.
+ SOW Signed: Both parties signed a statement of work (SOW), and formalize the agreement and detail the project scope and deliverables.
Type: Array of strings
Valid Values: `Initialized discussions with customer | Customer has shown interest in solution | Conducted POC / Demo | In evaluation / planning stage | Agreed on solution to Business Problem | Completed Action Plan | Finalized Deployment Need | SOW Signed`
Required: No

 ** Title **   <a name="AWSPartnerCentral-Type-Project-Title"></a>
Specifies the `Opportunity`'s title or name.
Type: String
Pattern: `(?s).{0,255}`
Required: No

## See Also
<a name="API_Project_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Project)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Project)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Project)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
