---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/recommended-ous-and-accounts.html
---

# Recommended OUs and accounts
<a name="recommended-ous-and-accounts"></a>

 This section provides details on the recommended OUs and, when applicable, a set of recommended AWS accounts.

![Diagram showing recommended OUs](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/recommended-ous.png)

 Depending on your requirements, you might not need to establish all the recommended OUs. As you adopt AWS and learn more about your needs, you can expand the overall set of OUs. Refer to the Patterns for organizing your AWS accounts for examples of how you might begin to organize your AWS accounts.

 While the provided OU recommendations are geared towards common use cases, it is your organization's responsibility to define a customized OU structure that aligns with your distinct requirements relevant to isolation and automation.

 The recommended OUs consist of:

## Foundational organizational units (OUs)
<a name="foundational-organizational-units-ous-x"></a>

 Foundational OUs are used to group AWS accounts that support the management, governance, and common infrastructure of your AWS environment.
+ **Security OU:** Groups AWS accounts that apply security policies, governance and compliance controls across the organization.
+ **Infrastructure OU:** Groups AWS accounts that host and manage core infrastructure and networking services and resources that are shared across the organization.

## Application OUs
<a name="application-ous-x"></a>

 Application OUs are used to group AWS accounts for production and nonproduction workload environments.
+  **Workloads OU:** Groups AWS accounts that host the organization's business-specific workloads, including both production and non-production environments.

## Experimental OUs
<a name="experimental-ous-x"></a>

 Experimental OUs are used to group accounts for research and development environments.
+  **Sandbox OU:** Groups AWS accounts used for experimentation, testing and development activities, typically with limited access to production resources.

## Procedural OUs
<a name="procedural-ous-x"></a>

 Procedural OUs are used to group accounts for process driven activities on AWS Accounts.
+ **Exceptions OU:** Groups AWS accounts that host workloads requiring specific configurations or policies that deviate from the organization's standard governance model.
+ **Transitional OU:** Temporary OU for housing AWS accounts during migration or restructuring processes, ensuring controlled management and gradual integration into the organization's standard governance structure.
+ **Suspended OU:** Groups AWS accounts that have been temporarily suspended or deactivated due to security concerns, policy violations or other administrative reasons.
+ **Policy Staging OU:** Hosts AWS accounts that are used to test and validate new or modified organizational policies before applying them to production environments.

## Advanced OUs
<a name="advanced-ous-x"></a>

 Advanced OUs are used to group accounts for specific advanced use-cases.
+ **Individual Business Users OU:** Groups AWS accounts associated with individual employees or business units, ensuring appropriate access controls and compliance with organizational policies.
+ **Deployments OU:** Groups accounts that host services and resources used to orchestrate the deployment of applications, services and infrastructure across multiple AWS accounts within an organization.
+ **Business Continuity OU:** Houses resources and accounts specifically designed for disaster recovery, backup and ensuring continuous operations of critical business functions across the organization.
