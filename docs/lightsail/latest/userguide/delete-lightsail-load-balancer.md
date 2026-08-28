---
source_url: https://docs.aws.amazon.com/lightsail/latest/userguide/delete-lightsail-load-balancer.html
---

# Delete Lightsail load balancers
<a name="delete-lightsail-load-balancer"></a>

You can delete a Lightsail load balancer if you no longer need it. Deleting a load balancer also detaches any Lightsail instances attached to it but doesn't delete the Lightsail instances. If you enabled encrypted (HTTPS) traffic using an SSL/TLS certificate, deleting the load balancer will also permanently delete any SSL/TLS certificates associated with the load balancer.

**Important**
Deleting a Lightsail load balancer and its associated certificate is final and can't be undone.

1. In the left navigation pane, choose **Networking**.

1. Choose the load balancer you want to delete.

1. Choose **Delete**.

1. Choose **Delete load balancer**.

1. Choose **Yes, delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
