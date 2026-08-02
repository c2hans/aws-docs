---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/platform-eng.html
---

# Platform engineering
<a name="platform-eng"></a>

**Build a secure, compliant multi-account cloud environment with packaged, reusable cloud products.**

To support innovation by enabling development teams, the platform needs to adapt at a rapid pace to keep up with the demands of the business. (See the [AWS CAF Business perspective](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-business-perspective/aws-caf-business-perspective.html).) It must do so while being flexible enough to adapt to product management demands, rigid enough to adhere to security constraints, and fast enough to enable operations needs.  This process requires the building of a compliant multi-account cloud environment with enhanced security features, and packaged, reusable cloud products.

An effective cloud environment allows your teams to easily provision new accounts while ensuring that those accounts conform to organizational policies. A curated set of cloud products enable you to codify best practices, help you with governance, and help increase the speed and consistency of your cloud deployments. Deploy your best practice blueprints, and detective and preventative [guardrails](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-lens/controlsandguardrails.html). [Integrate](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-lens/networkconnectivity.html) your cloud environment with your existing landscape to enable desired hybrid cloud use cases.

Automate the account provisioning workflow and use [multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) to support your security and governance goals. Set up connectivity between your on-premises and cloud environments as well as between different cloud accounts. Implement [federation](https://aws.amazon.com/single-sign-on/) between your existing identity provider (IdP) and your cloud environment so that users can authenticate by using their existing login credentials. Centralize logging, establish cross-account security audits, create inbound and outbound DNS resolvers, and get dashboard visibility into your accounts and guardrails.

Evaluate and certify cloud services for consumption in alignment with corporate standards and configuration management. Package and continuously improve enterprise standards as self-service deployable products and consumable services. Leverage [infrastructure as code (IaC)](https://aws.amazon.com/cloudformation/) to define configurations in a declarative way. Create enablement teams to evangelize the platform to developers and business users and allow them to build integrations that accelerate adoption across your organization.

Completing the tasks discussed in the following sections requires you to build [capabilities](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/capabilities.html) and teams to evolve your organizations toward modern platform engineering. For technical details, see the [Establishing your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html) whitepaper.

## Start
<a name="platform-eng-start"></a>

### Build a landing zone and deploy guardrails
<a name="build-a-landing-zone-and-deploy-guardrails.f98cb1c4-bb84-5a42-b2dc-074cf2872c57"></a>

As you start your journey to mature platform engineering, you must first deploy your [landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html) with detective and preventative guardrails as defined in the platform architecture capability. Guardrails ensure that organizational standards aren't violated as application owners consume cloud resources. With this mechanism, you automate the account provisioning workflow to use [multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) that support your [security](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html) and [governance](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/governance-perspective.html) goals.

### Establish authentication
<a name="establish-authentication.a76efff6-4a62-5b36-8455-1fe291e14ae4"></a>

Implement [identity management and access control](https://aws.amazon.com/solutions/guidance/identity-management-and-access-control-on-aws) across all environments, systems, workloads, and processes in accordance with standards dictated in the [AWS CAF Security perspective](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html). For workforce identities, restrict the use of [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) users and instead rely on an identity provider that enables you to manage identities in a centralized place. This makes it easier to manage access across multiple applications and services, because you are creating, managing, and revoking access from a single location. Use existing processes to manage the creation, update, and removal of access to include your AWS environments.

### Deploy network
<a name="deploy-network.e852c040-4026-5cf8-976c-6d7fb893d85b"></a>

In accordance with your *platform architecture* designs, create a [centralized network account](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/infrastructure-ou-and-accounts.html#network-account) to control inbound and outbound traffic to and from your environment. We recommend that you design your networks for rapidly provisioned connectivity between your on-premises network and your AWS environments, to and from the internet, and across your AWS environments. Centralizing your network management enables you to deploy network controls to isolate networks and connectivity across your environment by using preventive and reactive controls.

### Collect, aggregate, and protect event and log data
<a name="collect--aggregate--and-protect-event-and-log-data.2ede802e-b753-5900-aa12-80481771e733"></a>

Use [Amazon CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html). It provides a unified interface to search, visualize, and analyze metrics, logs, and traces across your linked accounts, and eliminates account boundaries.

If your organization has specific compliance requirements for centralized log control and security, consider setting up a dedicated [log archive account](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/security-ou-and-accounts.html#log-archive-account). This offers a centralized, encrypted repository specifically for log data. Enhance the security of this archive by regularly rotating encryption keys.

Implement robust policies for protecting sensitive log data, using [masking techniques](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) as necessary. Use log aggregation for compliance, security, and audit logs, and ensure the use of strict guardrails and identity constructs to prevent unauthorized changes to log configurations.

### Establish controls
<a name="establish-controls.525c10cb-a971-5755-b339-19a61a30d7c6"></a>

In accordance with the definitions from the [AWS CAF Security perspective](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html), deploy foundational [security capabilities](https://aws.amazon.com/architecture/cloud-foundations/security-capabilities/) that meet your business requirements. Deploy additional [preventative](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/preventative-controls.html) and [detective controls](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/detective-controls.html), and provision those programmatically and consistently across all your accounts where required. Integrate detective controls into operational tooling as defined by the platform architecture capability so that non-compliant resources can be reviewed by operational mechanisms.

### Implement cloud financial management
<a name="implement-cloud-financial-management.ff1dc3a6-8fd0-55be-bd7c-eb36b0095225"></a>

In accordance with the [AWS CAF Governance perspective](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/governance-perspective.html), implement cost allocation tags, and AWS Cost Categories that align your organization's tagging strategy with financial accountability for cloud consumption. AWS Cost Categories let you charge or show cloud charges back to internal cost centers by using tools such as [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and billing data published in [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html).

## Advance
<a name="platform-eng-advance"></a>

### Build infrastructure automation
<a name="build-infrastructure-automation.c455306d-186d-5a83-96f9-ceeff9bcb799"></a>

Before you proceed, evaluate and certify cloud services for consumption in alignment with your *platform architecture*. Then, package and continuously improve enterprise standards as deployable products and consumable services, and use infrastructure as code (IaC) to define configurations in a declarative way. Infrastructure automation mimics software development cycles by allowing access to specific services in each account with role-based access control (RBAC) or attribute-based access control (ABAC). Deploy a method to rapidly provision new accounts and align them with your service and incident management capabilities by using APIs, or develop self-service capabilities. Automate network integration and IP allocation as accounts are created to ensure compliance and network security. Integrate new accounts with your IT service management  (ITSM) solution by using native connectors that are conﬁgured to operate with AWS. Update your playbooks and runbooks as appropriate.

### Provide centralized observability services
<a name="provide-centralized-observability-services.4286fc4d-a95c-51aa-aacd-40c17fb9428d"></a>

To achieve effective [cloud observability](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/observability.html), your platform should support real-time search and analysis of both local and centralized log data. As your operations scale, your platform's ability to index, visualize, and interpret log, metrics, and traces is key to turning raw data into actionable insights.

By correlating logs, metrics, and traces, you can extract actionable conclusions and develop targeted, informed responses. Establish rules that allow proactive responses to security events or patterns that are identified in your logs, metrics, or traces. As your AWS solutions expand, ensure that your monitoring strategy scales in tandem to maintain and enhance your observability capabilities.

### Implement systems management and AMI governance
<a name="implement-systems-management-and-ami-governance.aee40cee-ed90-5b6a-9d7e-d8ce3e824717"></a>

Organizations that use Amazon Elastic Compute Cloud (Amazon EC2) instances extensively require operational tooling to manage instances at scale. Software asset management, endpoint detection and response, inventory management, vulnerability management, and access management are foundational capabilities for many organizations.  These capabilities are often delivered through software agents that are installed on instances. Develop a capability to package agents and other custom configurations into Amazon Machine Images (AMIs), and make these AMIs available to consumers of the cloud platform. Use preventative and detective controls that govern the use of these AMIs. AMIs should contain tooling that enables management of long-running EC2 instances at scale, particularly for mutable Amazon EC2 workloads that don't consume new AMIs on a regular basis. You can use [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) at scale to automate agent upgrades, collect system inventory, access EC2 instances remotely, and patch operating system vulnerabilities.

### Manage credential use
<a name="manage-credential-use.bac76e15-b3dc-5ebc-9452-0bd397056647"></a>

In accordance with the [AWS CAF Security perspective, ](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html)implement roles and temporary credentials. Use tooling to manage remote access to instances or on-premises systems by using a pre-installed agent without storing secrets. Reduce reliance on long-term credentials, and scan for hardcoded credentials in your IaC templates. If you can't use temporary credentials, use programmatic tools such as application tokens and database passwords to automate credential rotation and management. Codify users, groups, and roles by using principles of least privilege with IaC, and prevent the manual creation of identity accounts by using guardrails.

### Establish security tooling
<a name="establish-security-tooling.cb84f26e-3645-522f-94a8-4e9ce31d3fba"></a>

Security monitoring tools should support granular security monitoring across infrastructure, applications, and workloads and provide aggregated views for pattern analysis. As with all other security management tools, you should extend your extended detection and response (XDR) tools to provide functions to assess, detect, respond to, and remediate the security of your applications, resources, and environments on AWS in accordance with requirements defined in the [AWS CAF Security perspective](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html).

## Excel
<a name="platform-eng-excel"></a>

### Source and distribute identity constructs with automation
<a name="source-and-distribute-identity-constructs-with-automation.29e90156-f162-5088-a645-4e745de0cc8b"></a>

Codify and version identity constructs such as roles, policies, and templates with IaC tools. Use policy  validation tools to check for security warnings, errors, general warnings, suggested changes to your IAM policies, and other findings. Where appropriate, deploy and remove identity constructs that provide temporary access to the environment in an automated manner, and prohibit deployment by individuals who are using the console.

### Add detection and alerts for anomalous patterns across environments
<a name="add-detection-and-alerts-for-anomalous-patterns-across-environments.d8496871-93cd-5bcc-bf9b-c2123c215b8c"></a>

Proactively assess environments for known vulnerabilities and add detection for unusual event and activity patterns. Review findings and make recommendations to platform architecture teams for changes that drive further efficiency and innovation.

### Analyze and model for threats
<a name="analyze-and-model-for-threats.a07ff2e6-1c63-59a2-8d31-27a16b028d3e"></a>

Implement continuous monitoring and measurement against industry and security benchmarks in accordance with the requirements from the [AWS CAF Security perspective](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html). When you implement your instrumentation approach, determine which types of event data and information will best inform your security management functions. This monitoring encompasses several attack vectors, including service usage. Your security foundations should include a comprehensive capability for secure logging and analytics across your multi-account environments that includes the ability to correlate events from multiple sources. Prevent changes to this conﬁguration with speciﬁc controls and guardrails.

### Continuously collect, review, and reﬁne permissions
<a name="continuously-collect--review--and-re-ne-permissions.b5c0ea20-c6d1-5574-9194-78000f9f7281"></a>

Record changes to identity roles and permissions and implement alerts when detective guardrails detect deviations from your expected conﬁguration state. Use aggregated and pattern identiﬁcation tools to review your centralized collection of events and reﬁne permissions as required.

### Select, measure, and continuously improve your platform metrics
<a name="select--measure--and-continuously-improve-your-platform-metrics.acd84f98-c6cb-53f6-96af-91692a304051"></a>

To enable successful platform operations, establish and routinely review comprehensive metrics. Ensure that they align with organizational goals and stakeholder needs. Track both platform performance and improvement metrics, and combine operational parameters such as patch, backup, and compliance by using team enablement and tool adoption indicators.

Use [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) for efficient metric management. This service streamlines data aggregation and visualization to enable informed decisions and targeted enhancements. Use these metrics as indicators of success and drivers of change to foster an environment of continuous improvement.
