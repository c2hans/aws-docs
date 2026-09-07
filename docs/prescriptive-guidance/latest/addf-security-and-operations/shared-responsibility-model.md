---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/shared-responsibility-model.html
---

# Shared responsibility model
<a name="shared-responsibility-model"></a>

The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) that applies to AWS services also applies to Autonomous Driving Data Framework (ADDF). The following entities share the responsibility to secure ADDF as set out in the following diagram:
+ **AWS** – The cloud infrastructure provider offering AWS services.
+ **ADDF core team** – The ADDF core team is the entity that publishes ADDF releases in the [ADDF repository](https://github.com/awslabs/autonomous-driving-data-framework) (GitHub).
+ **ADDF user** – ADDF users include, but aren't limited to:
  + **ADDF developer** – Anyone that changes, customizes, or creates new ADDF module code.
  + **ADDF operator** – Anyone that sets up and operates an ADDF instance.
  + **ADAS developer** – The end-user or consumer of the resources deployed by ADDF. For example, an ADAS developer can query a visualization frontend that was created as part of the ADDF deployment.

The following diagram summarizes the shared responsibility between AWS, the ADDF core team, and the ADDF user.

![The responsibilities of each entity in the shared responsibility model.](https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/images/guide-img/b7c99a03-2a36-4dc2-9b13-9b2a1cbf7eb9/images/b864d84d-5301-4571-bbb2-c3bab5ae5664.png)

## AWS responsibility
<a name="aws-responsibility"></a>

AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud; as defined in the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.

## ADDF core team responsibility
<a name="addf-core-team-responsibility"></a>

The ADDF core team provides a framework that is secure in itself, on a best-effort basis, according to [Apache License 2.0](https://github.com/awslabs/autonomous-driving-data-framework/blob/main/LICENSE) (GitHub). The ADDF core team is responsible for the following:
+ Periodic security reviews of releases
+ Baseline security features
+ Security-hardened default modules (This excludes any modules in the `/modules/demo-only/` folder. Those modules are only for proof-of-concept purposes and don't receive security hardening.)
+ Security-hardened deployment and orchestration framework

These security responsibilities extend only to the framework, as provided in the GitHub repository, without any modifications or customization. This includes all ADDF modules, except ADDF modules in the `modules/demo-only/` folder. ADDF modules in this folder aren't security hardened and shouldn't be deployed in production environments or in any environment with sensitive or protected data. These modules are included to showcase system capabilities, and you can use them as the base for creating your own customized, security-hardened modules.

**Note**
ADDF as a framework is delivered on an as-is basis. It doesn't come with any liability and warranty, as stated in the [Apache License 2.0](https://github.com/awslabs/autonomous-driving-data-framework/blob/main/LICENSE) (GitHub). You should conduct your own security assessment of ADDF and verify it's compliant with your organization's specific security requirements.

## ADDF user responsibility
<a name="addf-user-responsibility"></a>

ADDF and its modules are secure only if ADDF is set up, customized, and operated in a secure manner. The ADDF user is fully responsible for the security of the following:
+ General AWS account responsibilities:
  + Security controls and checks (directive, detective, preventive, and responsive)
  + Multi-account architecture
  + Networking design
  + Identity and access management
+ ADDF-specific responsibilities:
  + ADDF setup
  + ADDF customization
  + ADDF module development
  + ADDF operations
  + ADDF updates

### General AWS account responsibilities
<a name="general-aws-account-responsibilities.ae2b1f42-49a4-54b9-a543-4c27d69cc5f1"></a>

Before you deploy any ADDF-related resources into AWS accounts, your AWS accounts should be configured according to the best practices in the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/). This includes directive, detective, preventive, and responsive security controls. You should have detailed mitigation processes in place, in case of any security violations or incidents. Your organization's policy should include requirements for centrally managing identity and access and networking. Commonly, these requirements and services are handled by a dedicated landing zone team.

### ADDF-specific responsibilities
<a name="addf-specific-responsibilities.5e422882-0c59-536b-b874-d2346f7d177d"></a>

#### Secure ADDF setup
<a name="secure-addf-setup.6d530390-a1f7-5ae4-a64a-ec95ca20f19f"></a>

An ADDF user's responsibility starts with the secure setup of ADDF according to the ADDF documentation. We highly recommend that you follow the instructions in the [ADDF Deployment Guide](https://github.com/awslabs/autonomous-driving-data-framework/blob/main/docs/deployment_guide.md) (GitHub). For more information about securely setting up ADDF, see [Defining your ADDF architecture](defining-your-addf-architecture.md) and [Initial setup](initial-setup.md).

#### Secure ADDF customization
<a name="secure-addf-customization.8120b4ab-1608-537b-91b5-ecbf3dd84054"></a>

In case of any customization of ADDF core functionality, such as CodeSeeder, SeedFarmer, and ADDF core modules, the ADDF user assumes full responsibility for those changes. For more information, see [Customizing the ADDF deployment framework code](customizing-the-addf-deployment-framework-code.md).

#### Secure ADDF module development
<a name="secure-addf-module-development.10082700-490f-5291-be17-172893433409"></a>

The ADDF user is fully responsible for any custom module that is deployed using ADDF. Furthermore, the ADDF user is responsible for any code changes to ADDF-supplied modules. For more information, see [Writing custom modules in ADDF](writing-custom-modules-in-addf.md).

#### Secure ADDF updates and operations
<a name="secure-addf-updates-and-operations.7cf0e2eb-2ded-583d-878d-0107b58f1513"></a>

As the framework evolves, ADDF receives feature and security updates. It is the ADDF user's responsibility to regularly check for updates published to the GitHub repository and to operate ADDF securely over the long-term. For more information, see [Reoccurring ADDF deployments](reoccurring-addf-deployments.md), [Reoccurring security audits](reoccurring-security-audits.md), [ADDF updates](addf-updates.md), and [Decommissioning](decommissioning.md).
