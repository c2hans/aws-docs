---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to MCS:

 **module**

A CloudFormation deployment launched by Service Catalog through the MCS web console or API. Service Catalog provisions the module stack, and CloudFormation takes care of provisioning and configuring the necessary AWS resources for you.

 **enable module**

Enabling means activating a module such that its resources are included in the MCS content production studio. In other words, deploying the CloudFormation stack that represents the module.

 **register module**

Registering makes an external module known to MCS and available for an MCS administrator to enable. Registering does not enable the module.

 **AWS developed MCS modules**

The set of modules developed by AWS that are included with MCS and available when MCS is deployed. When you deploy MCS, all of these modules are available without an explicit registration step. Additionally, these modules cannot be deregistered.

 **Third-Party Modules**

Similar to AWS Partner storage modules, the MCS admin user must explicitly register third-party modules with MCS to make them available to users.

**Note**
Modular Cloud Studio on AWS allows you to deploy and manage a scalable, secure, and global content production infrastructure in the cloud. This includes custom modules, developed by AWS Partners or other third parties, that you can choose to use ("Third-Party Modules"). AWS does not own or otherwise have any control over Third-Party Modules.
Your use of the Third-Party Modules is governed by any terms provided to you by the Third-Party Module providers when you acquired your license to use them (for example, their terms of service, license agreement, acceptable use policy, and privacy policy). You are responsible for ensuring that your use of the Third-Party Modules comply with any terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.
You are also responsible for making your own independent assessment of the Third-Party Modules that you use. AWS does not make any representations, warranties, or guarantees regarding the Third-Party Modules, which are "Third-Party Content" under your agreement with AWS. Modular Cloud Studio on AWS is offered to you as "AWS Content" under your agreement with AWS.

 **AWS Partner storage modules**

A curated list of storage modules from AWS ISVs that are treated similar to Third-Party Modules or custom modules. MCS displays the AWS Partner storage modules, letting users know that these modules exist and can be registered with MCS.

**Note**
AWS Partner storage modules are easily discoverable. However, to make them available to users, the MCS admin user must review and register these modules with MCS.

 **hub Region**

The Region from which you launch the solution.

 **spoke Region**

Region from which you launch a module, different from the hub Region. You can optionally use spoke Regions to increase availability and reliability for geographically diverse teams.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html).
