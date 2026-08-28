---
source_url: https://docs.aws.amazon.com/athena/latest/ug/capacity-management-adding-workgroups-to-a-reservation.html
---

# Add workgroups to a reservation
<a name="capacity-management-adding-workgroups-to-a-reservation"></a>

After you create a capacity reservation, you can add up to 20 workgroups to the reservation. Adding a workgroup to a reservation tells Athena which queries should execute on your reserved capacity. Queries from workgroups that are not associated with a reservation continue to run using the default per terabyte (TB) scanned pricing model.

When a reservation has two or more workgroups, queries from those workgroups can use the reservation's capacity. You can add and remove workgroups at any time. When you add or remove workgroups, queries that are running are not interrupted.

When your reservation is in a pending state, queries from workgroups that you have added continue to run using the default per terabyte (TB) scanned pricing model until the reservation becomes active.

**To add one or more workgroups to your capacity reservation**

1. On the details page for the capacity reservation, choose **Add workgroups**.

1. On the **Add workgroups** page, select the workgroups that you want to add, and then choose **Add workgroups**. You cannot assign a workgroup to more than one reservation.

   The details page for your capacity reservation lists the workgroups that you added. Queries that run in those workgroups will use the capacity that you reserved when the reservation is active.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
