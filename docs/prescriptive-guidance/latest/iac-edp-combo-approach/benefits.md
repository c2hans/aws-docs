---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iac-edp-combo-approach/benefits.html
---

# Benefits
<a name="benefits"></a>

This section covers some of the main benefits of using IaC and EDP to solve common problems with managing or provisioning IT infrastructure resources.

## IaC benefits
<a name="iac-benefits"></a>

The key benefit of an IaC approach is that it can help you represent and preserve the state of IT infrastructure resources by using version control. This approach can solve multiple problems, but the two most important problems include the following:
+ **Ability to revert back to a previous configuration or state if a resource fails without worrying about the resource's values** – Typically, resources and their configurations are backed up and restored without IaC, but IaC can use a version control system to help you revert back (or roll back) to one or more versions of a backup in the backup timeline. You can also tag deployments so that versions that are unsuccessful due to configuration values could be marked and eventually discarded.
+ **An accurate representation of a resource's state **– If a resource is successfully created or updated or a rollback is completed, then the template file will have the resource properties matching the actual resource. This means that you can scan and query the repository so that you can understand the state of the resource. Additionally, an IaC approach doesn't require developers to have environment permissions (for example, in a production environment). Finally, you can better ensure a tight security posture for your organization if you have an accurate representation of a resource's state.

## EDP benefits
<a name="edp-benefits"></a>

The key benefit of EDP is that it can help you plan for and solve issues that arise from specified future events without the need for an engineer (that is, human effort). Instead, you can use event-driven code to respond to potential issues. EDP also offers the following additional benefits:
+ **Reduced deployment time** – An EDP approach reduces the time it takes to make deployment changes because code is invoked immediately after the event.
+ **Scalable resources **– You can use an EDP approach to scale resources that must be modified, which could take much longer to modify manually.
