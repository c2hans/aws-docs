---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-reference-architecture-pci-data-security-standard-dss/best-practices.html
---

# AWS Organization Architecture – OU and Account structure
<a name="best-practices"></a>

The AWS Security Reference Architecture (AWS SRA) organizes all AWS accounts within a single AWS Organization, structured across purpose-built Organizational Units (OUs). This multi-account design is foundational to PCI DSS compliance because AWS accounts act as hard security, access, and billing boundaries — by default, no access is permitted between accounts. This native isolation is a powerful primitive for PCI DSS scoping and segmentation that goes beyond traditional network-layer controls.

The AWS SRA defines the following core OUs and accounts:
+ Org Management account — Root of the AWS organization; central governance via AWS Organizations SCPs and AWS Control Tower
+ Security OU – Security Tooling account — Hosts broadly applicable security services (Amazon GuardDuty, AWS Security Hub, AWS Config, Amazon Inspector, Amazon Detective); centralized security monitoring and automated alerting
+ Security OU – Log Archive account — Immutable, centralized ingestion and archival of all logs and backups across all accounts and Regions
+ Infrastructure OU – Network account — Isolates networking services (VPCs, Transit Gateway, AWS Network Firewall, ingress/egress controls) from application workloads; the gateway between workloads and the internet
+ Infrastructure OU – Shared Services account — Hosts services consumed by multiple teams (e.g., AWS IAM Identity Center, Active Directory, messaging services)
+ Workloads OU – Application account(s) — Hosts application workloads; isolated per service rather than per team to improve resilience

## PCI DSS Scoping for an Account or Infrastructure Component
<a name="pci-dss-scoping-for-an-account-or-infrastructure-component.cf8186ed-d49a-5526-a2ed-b8b567ac9cdb"></a>

Under PCI DSS 4.0.1, the scoping process begins by identifying all system components — people, processes, and technologies — that interact with or could impact the security of cardholder data (CHD) or sensitive authentication data (SAD). The PCI Council defines three scoping categories that directly map to how AWS accounts and infrastructure should be classified:

**Category 1** — CDE Systems (In-Scope, Full PCI DSS Requirements Apply) A system component is in the CDE if it stores, processes, or transmits CHD or SAD, or if it resides in the same network segment as systems that do. On AWS, this means any account, VPC, subnet, or service that directly handles PANs, CVVs, expiry dates, or track data. Examples include payment processing Lambda functions, Aurora databases storing encrypted PANs, and API Gateway endpoints receiving card data.

**Category 2** — Connected-To / Security-Impacting Systems (In-Scope, Applicable PCI DSS Requirements Apply) A system component is "connected-to" if it has connectivity to a CDE system and could impact the security of the CDE — even if it never touches CHD directly. On AWS, cloud-native connectivity (cross-account IAM roles, VPC peering, Transit Gateway routes, shared services) can inadvertently pull infrastructure into scope. A system is security-impacting if it provides security services to the CDE (e.g., a centralized logging account, a shared identity provider, a secrets management service). The AWS SRA's Security Tooling account, Log Archive account, and Network account will typically fall into this category and must be assessed accordingly.

**Category 3 **— Out-of-Scope Systems A system component is out of scope only if it is fully isolated from the CDE — no connectivity path exists, and it provides no security services to the CDE. On AWS, achieving true out-of-scope status requires demonstrating that no network path, IAM trust relationship, shared service dependency, or management-plane access connects the component to the CDE. This is where the AWS SRA's account-level hard boundaries are most powerful: an account in a separate, non-peered OU with no cross-account roles and no shared services touching the CDE can be credibly argued as out of scope to a QSA.

The key determinants for scoping any AWS account or infrastructure part is answering the question, "If a bad actor could compromise this account or component, could they use it to access cardholder data or compromise the security of it?" if the answer is yes, the component should be considered in scope. Additional detailed considerations are:
+ Data flow — Does CHD or SAD traverse this component?
+ Network connectivity — Is there a routable path (direct or transitive) to a CDE system?
+ IAM and management-plane access — Can a principal in this account assume roles in, or invoke APIs against, CDE accounts?
+ Security service dependency — Does the CDE rely on this component for logging, secrets, identity, patching, or key management?
+ Shared infrastructure — Is any underlying infrastructure (Transit Gateway, DNS, Active Directory) shared between CDE and non-CDE workloads?

### The AWS SRA Recommendations supporting PCI DSS Requirements
<a name="the-aws-sra-recommendations-supporting-pci-dss-requirements.1204f7fe-04c4-549a-8377-38ee9a5bc1a9"></a>

The AWS SRA's multi-account, multi-OU architecture directly maps to and accelerates compliance with PCI DSS 4.0 requirements across two critical dimensions: segmentation and resource visibility.

### Segmentation
<a name="segmentation.96196265-f94a-52ba-bb82-2523669f3bba"></a>

The PCI Council's Guidance for PCI DSS Scoping and Network Segmentation advises the CDE to be isolated from systems that could impact its security. The AWS SRA supports this through multiple layers:
+ Account-level segmentation — Placing CDE workloads in dedicated AWS accounts within a PCI Workloads OU creates a hard boundary that is not dependent on network configuration alone (Refer to recommended OU and account structure depicted later in this guide under Account and OU structure) . This directly reduces PCI DSS scope by ensuring out-of-scope systems have no connectivity path to CDE accounts by default.
+ SCP-enforced guardrails — AWS Organizations SCPs applied at the OU level prevent CDE accounts from establishing unauthorized cross-account access or enabling unapproved services, supporting Requirement 1.2 (network security control configurations are reviewed and validated).
+ Network-level segmentation — the AWS SRA's Network account centralizes ingress/egress controls using AWS Network Firewall, AWS WAF, and security groups, enforcing east-west (internal) and north-south (external) traffic controls aligned with Requirement 1.3 (restrict inbound and outbound traffic to that which is necessary).
+ VPC design — Dedicated VPCs with private subnets, no direct internet gateway attachment for CDE tiers, and Transit Gateway-mediated routing through the Network account enforces the segmentation boundary at the network layer.

The updated AWS whitepaper [Architecting for PCI DSS Scoping and Segmentation on AWS](https://d1.awsstatic.com/whitepapers/compliance/architecting-pci-dss-segmentation-scoping-aws.pdf) provides actionable network design patterns and reference architectures for OU and account structures specifically designed for PCI DSS 4.0 compliance.

### Resource Visibility
<a name="resource-visibility.e88b9797-0434-5cb1-8f89-9e1e6cda1e8d"></a>

PCI DSS Requirement 12.5.1 requires maintaining an inventory of all in-scope system components, and Requirement 12.5.2 requires that PCI DSS scope is documented and confirmed at least once every 12 months. Requirement 6.3.2 also requires an accurate, up-to-date Software Bill of Materials (SBOM) or software inventory for all bespoke, custom, and third-party software components. The AWS SRA supports continuous, automated resource discovery through:
+ AWS Config (deployed in the Security Tooling account) — [AWS Config](https://aws.amazon.com/config/) Continuously records configuration state of all resources across all accounts and Regions, providing a real-time inventory of in-scope system components.
+ Amazon Inspector SBOMgenerator - The [Amazon Inspector SBOM](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html) Generator (Sbomgen) is a tool that produces an SBOM for archives, container images, directories, local systems, and compiled Go and Rust binaries.
+ AWS Organizations integration — All accounts are visible and manageable from the Org Management account, ensuring no account or resource falls outside the governance perimeter.
+ AWS Systems Manager - [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) provides visibility into AWS computing environment. Inventory can be used to collect metadata from all managed nodes and stored in a central Amazon Simple Storage Service (Amazon S3) bucket. Using built-in tools, the data can be queried to quickly determine which nodes are running the software and configurations required by organization defined software policy.
+ Tags - A [tag](https://docs.aws.amazon.com/solutions/tagging-on-aws/) is a key-value pair applied to a resource to hold metadata about that resource. Users can create and apply Tags to AWS resources using the AWS CLI, API, or the AWS Management Console. Tags can help correctly identify in-scope and out-of-scope resources dynamically without having to manually keep track of every resource in a dynamic environment. It should be noted that tags are not encrypted and should not be used to store sensitive data.

Together, these AWS SRA-recommended services create a continuously validated, automatically documented inventory of the CDE — reducing the manual effort of annual scoping exercises and providing auditors with real-time evidence of compliance posture. Additionally you should also design a strong change management process implemented through Infrastructure as Code (IaC) to ensure you have an accurate inventory of your AWS environment and only authorized changes are introduced.

## Workload Account Structure: CDE and Connected-To Accounts
<a name="workload-account-structure--cde-and-connected-to-accounts.7d50b921-69cd-5613-baf8-3a758eadc80c"></a>

For PCI DSS environment, we need to extend the AWS SRA Workload OU and account structure further, as this is where the CDE is hosted. The AWS SRA's Workloads OU houses application accounts, but for PCI DSS environments, a flat "one Workloads OU" model is not recommended for controlling the scope. The AWS Architecting for PCI DSS Scoping and Segmentation on AWS whitepaper recommends structuring the Workloads OU — and the broader organization — around the three scoping categories above, using dedicated child OUs and accounts to make scope boundaries explicit, enforceable, and auditable.

The recommended account structure maps as follows:

**PCI Workloads OU — CDE Account(s):** These accounts host infrastructure that directly stores, processes, or transmits CHD. Each CDE account should be isolated to a single application or payment flow to minimize scope and simplify scoping. Key characteristics:
+ Dedicated VPC with private subnets only for CDE tiers (no direct internet gateway attachment)
+ All ingress/egress routed through the Network account's inspection VPC via Transit Gateway
+ No shared encryption keys, IAM roles, or service endpoints with non-CDE accounts
+ AWS KMS Customer Managed Keys scoped exclusively to the CDE account
+ SCPs on the PCI Workloads OU deny actions that would expand scope e.g., creating VPC peering to non-PCI accounts, disabling CloudTrail, or attaching internet gateways
+ RCP should also be applied to resources to prevent access from non PCI accounts. As an example, you can apply [RCP](https://github.com/aws-samples/resource-control-policy-examples/blob/main/Establish-intra-organization-boundaries/Deny-access-to-resources-in-an-organizational-unit,except-for-principals-from-the-same-or-specified-organizational-unit.json) to restrict access to specified AWS services for all principals except those in a specific OU path, which belongs to PCI in-scope OU. For other sample RCPs, refer to [resource control policies](https://github.com/aws-samples/resource-control-policy-examples) example on GitHub.

**PCI Workloads OU — Connected-To Account(s)**: These accounts host systems that have connectivity to the CDE but do not directly handle CHD — for example, a tokenization service, a fraud detection engine, or a payment orchestration layer that routes transactions to the CDE. They are fully in scope for applicable PCI DSS requirements and must be treated with the same rigor as CDE accounts for controls like access management (Requirement 7), logging (Requirement 10), and vulnerability management (Requirement 6/11). Key characteristics:
+ Connectivity to CDE accounts is strictly controlled — only specific, documented flows are permitted (e.g., via AWS PrivateLink or tightly scoped Transit Gateway route tables)
+ No broader internet exposure than what is required for their function
+ Inherit the same SCP guardrails as CDE accounts within the PCI Workloads OU

**AWS SRA Infrastructure Accounts — Connected-To / Security-Impacting:** Several AWS SRA accounts outside the Workloads OU should be included into PCI scope as "security-impacting" systems. These are AWS accounts that can impact the security configuration of "CDE Accounts" and/Or "Connected-To-Accounts". A primary example of these are accounts that perform [Delegated administration](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_delegated_admin.html), managing AWS service configuration for the entire AWS organization.

|
|
| AWS SRA Account | Scoping Category | Rationale |
| --- |--- |--- |
| Security Tooling | Connected-To (Security-Impacting) | Hosts GuardDuty, Security Hub, Config that monitor CDE accounts |
| Log Archive | Connected-To (Security-Impacting) | Receives and stores all CDE audit logs; integrity of logs is a PCI DSS Req. 10 control |
| Network | Connected-To (Security-Impacting) | All CDE ingress/egress transits through this account; Network Firewall rules enforce CDE segmentation |
| Shared Services | Evaluate Case-by-Case | In-scope if it provides identity (AD/IAM Identity Center), secrets, AWS CloudFormation StackSet delegated [administrator](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html), or DNS to CDE accounts; out-of-scope if fully isolated |
| Org Management | Connected-To (Security-Impacting) | SCPs and organizational governance directly impact CDE account security posture |

**Non-PCI Workloads OU — Out-of-Scope Accounts:** Workloads with no CHD data flow, no connectivity to PCI accounts, and no shared security services with the CDE can be placed in a separate Non-PCI Workloads OU. SCPs on this OU should explicitly deny any action that would create connectivity to PCI accounts (e.g., creating Transit Gateway attachments to PCI route tables, assuming roles in PCI accounts). This SCP-enforced isolation is what allows a QSA to accept these accounts as out of scope.

The following diagram provides a visual representation of different OU types as described in the AWS SRA and their corresponding PCI DSS scope consideration.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-reference-architecture-pci-data-security-standard-dss/images/guide-img/348f03a4-c34e-48e6-ab09-09381dffd794/images/5a8918da-bc42-44e0-9563-3c3297d4a202.jpeg)

### Segmentation Boundary Enforcement Across the OU Structure
<a name="segmentation-boundary-enforcement-across-the-ou-structure.7f5d3320-b80a-5656-bffb-bf7df760eac9"></a>

The power of the AWS SRA's multi-account model for PCI DSS is that segmentation is enforced at multiple independent layers simultaneously — making it resilient to misconfiguration at any single layer:
+ Account boundary — No default connectivity between accounts; cross-account access requires explicit IAM trust
+ OU-level SCPs — Preventive guardrails that cannot be overridden by account-level administrators
+ Network layer — Transit Gateway route tables and Network Firewall rules in the Network account control all inter-account traffic flows
+ IAM — Resource-based policies and permission boundaries limit cross-account API access
+ Data layer — Account-scoped KMS Customer Managed Keys ensure CDE data cannot be decrypted outside the CDE account. This layered model directly supports the PCI Council's guidance that segmentation must be validated — not just designed — and the AWS whitepaper's recommendation that both network-layer and non-network controls (account boundaries, IAM, SCPs) be documented and presented to QSAs as part of the segmentation evidence package.

**Design Consideration**: On cloud, logical isolation controls provide a strong segmentation boundary enforcement mechanism. One option is to design a strong [Data Perimeter](https://aws.amazon.com/identity/data-perimeters-on-aws/). A data perimeter is a set of permissions guardrails in your AWS environment you use to help ensure that only your trusted identities (PCI In-scope) are accessing trusted resources (PCI In-scope) from expected networks (PCI In-scope). This also helps you prevent your PCI In-scope resources from being accessed by out-of-scope networks/resources.

#### Inventory
<a name="inventory"></a>

PCI DSS Requirement 12.5.1 mandates that an organization maintain an inventory of all in-scope system components, including a description of function/use for each. Requirement 12.5.2 further requires that this inventory be reviewed at least once every 12 months and updated whenever the environment changes. On AWS, the dynamic, API-driven nature of cloud infrastructure — where resources can be provisioned and deprovisioned in seconds — makes a manual inventory approach both impractical and unreliable. The AWS SRA addresses this through a layered, automated inventory architecture built entirely on native AWS services.

##### Layer 1 — Continuous Resource Discovery: AWS Config
<a name="layer-1---continuous-resource-discovery--aws-config.2dd07669-adec-5cf0-b221-9bc23dcd3869"></a>

AWS Config is the foundational service for PCI DSS inventory on AWS. When enabled across all accounts in the organization — which AWS Control Tower enforces automatically upon account enrollment — Config continuously records the configuration state of every supported resource type, generating a [Configuration Item (CI)](https://docs.aws.amazon.com/config/latest/developerguide/config-item-table.html) each time a resource is created, modified, or deleted.

For PCI DSS inventory purposes, Config provides three critical capabilities:
+ Real-time resource tracking — Config detects and records changes to resources right after they occur, maintaining a point-in-time history of every resource's configuration state. This directly supports the "updated whenever the environment changes" requirement of Requirement 12.5.2.
+ Multi-account aggregation — A Config Aggregator deployed in the AWS SRA's [Security Tooling](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) (Audit) account collects configuration data from all member accounts and regions into a single pane of glass. This gives the security team a centralized, organization-wide view of all in-scope resources without requiring account-by-account queries.
+ Advanced Query — Config's [SQL-like query interface](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html) allows teams to run structured queries against the current configuration state of all resources across the organization — for example, querying all EC2 instances, RDS databases, Lambda functions, within specific account of VPC. This is directly usable as evidence for a QSA demonstrating inventory completeness.

You can extend this further by pairing the [Config Aggregator with Amazon Athena ](https://aws.amazon.com/blogs/mt/exploring-aws-config-data-using-amazon-athena-and-amazon-managed-grafana/)for historical querying and [Amazon QuickSight ](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-aws-resource-inventory.html)for interactive compliance dashboards — enabling teams to visualize their in-scope resource inventory, track changes over time, and produce audit-ready reports.

##### Layer 2 — Software and OS-Level Inventory: AWS Systems Manager Inventory, Amazon Inspector
<a name="layer-2---software-and-os-level-inventory--aws-systems-manager-inventory--amazon-inspector.0d0a1199-7699-5c21-8383-db233991ac44"></a>

AWS Config tracks infrastructure-level resources (EC2 instances, S3 buckets, RDS databases, etc.), but PCI DSS Requirement 12.5.1 also requires documenting the function and use of each system component — which demands visibility into what is running inside those resources. AWS Systems Manager (SSM) Inventory fills this gap by collecting metadata from managed nodes at configurable intervals (minimum every 30 minutes).

SSM Inventory collects the following metadata types relevant to PCI DSS:
+ Applications — Names, publishers, and versions of all installed software (critical for Requirement 6.3 software inventory and vulnerability management)
+ Network configuration — IP addresses, MAC addresses, DNS, gateway, and subnet mask per node
+ AWS components — EC2 drivers, SSM agent versions, and other AWS-managed software
+ Services — Running services, start type, and status (supports identification of unnecessary services per Requirement 2.2.4)
+ Windows/Linux updates — Patch status and installed hotfixes (supports Requirement 6.3.3 patching)
+ Tags — Tags assigned to each node, enabling PCI scope classification to be reflected in the software inventory
+ Custom inventory — Organizations can extend SSM Inventory with custom JSON metadata, for example recording the PCI scoping category, data classification, or owning team for each node

SSM Inventory data can be synced to an S3 bucket via [Resource Data Sync](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-resource-data-sync.html) and queried using Amazon Athena, enabling cross-account, cross-region software inventory queries. This is particularly valuable for demonstrating to a QSA that all CDE nodes are running only approved, patched software — a direct evidence artifact for Requirements 2.2 and 6.3.

[Amazon Inspector SBOM Generator](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html) produces SBOM for archives, container images, directories, local systems, and compiled Go and Rust binaries by scanning files that contain information about installed packages. This can be used for Amazon ECR, AWS Lambda and agentless scanning for Amazon EC2. This helps satisfy PCI DSS 4.0 Requirement 6.3.2 mandates that organizations maintain an accurate, up-to-date Software Bill of Materials (SBOM) or software inventory for all bespoke, custom, and third-party software components.

##### Layer 3 — Tagging Strategy as the Inventory Backbone
<a name="layer-3---tagging-strategy-as-the-inventory-backbone.756a6722-9aa4-5762-bebe-c2c4472479ab"></a>

None of the above services can distinguish in-scope from out-of-scope resources without a consistent, enforced resource tagging strategy. Tags are the mechanism by which PCI DSS scoping categories are operationalized in AWS — they allow Config queries, SSM Inventory filters, Inspector coverage reports, and Security Hub findings to be scoped to CDE and Connected-To resources specifically.

[AWS Organizations Tag Policies](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html) enforce consistent tag key naming across all accounts, and AWS Config (e.g., required-tags) can be used to flag any resource that is missing mandatory PCI scope tags — ensuring no resource enters the CDE without being classified.

**Recommended Tagging Schema – PCI DSS Inventory**

|
|
| Tag Key | Example Values | Purpose |
| --- |--- |--- |
| pci-scope | cde, connected-to, out-of-scope | Identifies PCI DSS scoping category per Req. 12.5.1 |
| data-classification | chd, sad, non-pci | Identifies data type handled by the resource |
| environment | prod, staging, dev | Supports scope boundary validation |
| owner | payments-team | Supports accountability and review per Req. 12.5.2 |
| compliance-boundary | pci-cde-prod | Groups resources into named compliance boundaries |

##### Putting It Together — The Inventory Architecture
<a name="putting-it-together---the-inventory-architecture.526fad14-c461-5d7e-b724-f58057d32558"></a>

The three layers combine into following continuous, automated inventory pipeline:
+ AWS Config (with Aggregator) → discovers and tracks all infrastructure-level resources across all accounts in real time
+ SSM Inventory → enriches each managed node with software, service, and configuration metadata
+ Amazon Inspector → enriches each managed node with software bill of material (SBOM)
+ Tag Policies \+ Config Rules → enforce PCI scope classification on every resource at creation time

Together, these services ensure that the PCI DSS inventory is not a point-in-time spreadsheet exercise but a continuously maintained, automatically updated, and audit-ready record — directly aligned with the intent of PCI DSS 4.0.1's scoping and inventory requirements.

The following diagram depicts the different collections layers for inventory, centralization and output layer architecture.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-reference-architecture-pci-data-security-standard-dss/images/guide-img/348f03a4-c34e-48e6-ab09-09381dffd794/images/a74c120c-3909-4595-9a66-5281b54ae0c9.jpeg)

The flow moves left to right across three stages. On the left, the four collection layers feed in parallel — AWS Config Aggregator  discovers all infrastructure resources and change history; SSM Inventory  enriches managed nodes with software and OS metadata; Amazon Inspector  contributes vulnerability findings and SBOM exports; and Tag Policies with Config Rules enforce PCI scope classification across the organization. In the center, all streams converge into the Centralized Inventory Store (S3 \+ Athena), which acts as the single queryable source of truth for the complete PCI DSS asset inventory. On the right, the inventory store feeds two outputs —Security Hub for the live compliance dashboard, and the QSA Evidence Package that directly satisfies Requirements 12.5.1,12.5.2 and 6.3.2.
