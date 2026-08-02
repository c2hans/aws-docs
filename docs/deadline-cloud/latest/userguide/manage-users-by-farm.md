---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/manage-users-by-farm.html
---

# Understanding access levels
<a name="manage-users-by-farm"></a>

Regardless of your identity source, you assign permissions to users and groups at the farm, queue, and fleet level through the Deadline Cloud console. You can grant access permissions at different levels. Each subsequent level includes the permissions for the previous levels. The following list describes the four access levels from the lowest level to the highest level:
+ **Viewer** – Permission to see resources in the farms, queues, fleets, and jobs they have access to. A viewer can't submit or make changes to jobs.
+ **Contributor** – Same as a viewer, but with permission to submit jobs to a queue or farm.
+ **Manager** – Same as contributor, but with permission to edit jobs in queues they have access to, and grant permissions on resources that they have access to.
+ **Owner** – Same as manager, but can view and create budgets and see usage.

For information about customizing these access levels, see [Monitor role](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security-iam-service-roles.html#monitor-role) in the *Deadline Cloud Developer Guide*.

**Topics**
+ [Access level permissions matrix](access-level-permissions-matrix.md)
+ [Membership inheritance](membership-inheritance.md)
+ [Assign permissions to users and groups](assign-permissions-procedure.md)
