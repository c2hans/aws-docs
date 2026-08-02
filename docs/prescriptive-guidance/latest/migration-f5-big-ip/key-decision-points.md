---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/key-decision-points.html
---

# Key decision points
<a name="key-decision-points"></a>

There are many aspects of migration that need to be considered, but before beginning your F5 BIG-IP workload migration, ask yourself the following questions to clarify the migration process.

**Who are the users of your applications?**

Assess if these are internal (not traversing an Elastic IP address) users or external (traversing an Elastic IP address) users. If the users are internal, evaluate whether the application can use DNS to accommodate the failure of an Availability Zone or active deployment. You should also verify if you need to use an alternate design pattern that allows a subnet to span multiple Availability Zones.

**What parts of your applications will migrate to the AWS Cloud?**

Assess whether the entire application is moving or only the presentation tier. You should also consider additional dependencies around security and DNS namespace. Your evaluation needs to determine what would be required from the network topology. Additionally, determine what is required from a service-level agreement (SLA) should an event happen at the Availability Zone, VPC, or AWS Region level.

**Why is the application migrating?**

You might be migrating your application because you are closing data centers or because you want more elasticity. Assess whether the application is migrating to have a per-application architecture, compared to the shared monolithic patterns common in many data centers. It's also worth considering what modernization efforts should be taking place along with the migration.

**Where is the application migrating to?**

Assess if the application needs to move to a single VPC with one Availability Zone or two Availability Zones. Determine the peer or transit VPC topology, along with the need for multi-Region deployments. These will impact the migration pattern design.
