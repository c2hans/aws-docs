---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_ops_model_def_resource_owners.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS02-BP01 Resources have identified owners
<a name="ops_ops_model_def_resource_owners"></a>

 Understand who has ownership of each application, workload, platform, and infrastructure component, what business value is provided by that component, and why that ownership exists. Understanding the business value of these individual components and how they support business outcomes informs the processes and procedures applied against them.

 **Benefits of establishing this best practice:** Understanding ownership identifies whom can approve improvements, implement those improvements, or both.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Resources have identified owners: Define what ownership means for the resource use cases in your environment. Specify and record owners for resources including at a minimum name, contact information, organization, and team. Store resource ownership information with resources using metadata such as tags or resource groups. Use AWS Organizations to structure accounts and implement policies to ensure ownership and contact information are captured.
  +  Define forms of ownership and how they are assigned: Ownership may have multiple definitions in your organization with different uses cases. You may wish to define a workload owner as the individual who owns the risk and liability for the operation of a workload, and whom ultimately has authority to make decisions about the workload. You may wish to define ownership in terms of financial or administrative responsibility where ownership rolls up to a parent organization. A developer may be the owner of their development environment and be responsible for incidents that its operation causes. Their product lead may own responsibility for the financial costs associated to the operation of their development environments.
  +  Define who owns an organization, account, collection of resources, or individual components: Define and record ownership in an appropriately accessible location organized to support discovery. Update definitions and ownership details as they change.
  +  Capture ownership in the metadata for the resources: Capture resource ownership using metadata such as tags or resource groups, specifying ownership and contact information. Use AWS Organizations to structure accounts and ensure ownership and contact information are captured.
