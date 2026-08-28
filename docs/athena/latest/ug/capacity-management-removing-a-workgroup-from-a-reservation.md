---
source_url: https://docs.aws.amazon.com/athena/latest/ug/capacity-management-removing-a-workgroup-from-a-reservation.html
---

# Remove a workgroup from a reservation
<a name="capacity-management-removing-a-workgroup-from-a-reservation"></a>

If you no longer require dedicated capacity for a workgroup or want to move a workgroup to its own reservation, you can remove it at any time. Removing a workgroup from a reservation is a straightforward process. After you remove a workgroup from a reservation, queries from the removed workgroup return to using on-demand capacity and are billed based on terabytes (TB) scanned.

**To remove one or more workgroups from a reservation**

1. On the details page for the capacity reservation, select the workgroups that you want to remove.

1. Choose **Remove workgroups**. The **Remove workgroups?** prompt informs you that all currently active queries will finish before the workgroup is removed from the reservation..

1. Choose **Remove**. The details page for your capacity reservation show that the removed workgroups are no longer present.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
