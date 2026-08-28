---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/set-up-queue-based-routing.html
---

# Set up queue-based, or skills-based, routing in Connect Customer
<a name="set-up-queue-based-routing"></a>

Here's an overview of the steps to set up queue-based routing:

1. [Create the queues](create-queue.md), for example, one for each skill you want to use for routing.

1. [Create the routing profiles](routing-profiles.md):
   + Specify the channels supported by this routing profile.
   + Specify the queues: the channel, priority, and delay.

1. [Configure agent settings](configure-agents.md) to assign the routing profiles to them.

When you [create your flows](create-contact-flow.md), you'll add the queues to them. If a contact chooses to speak to an agent in Spanish, for example, they will be routed to the Spanish Reservations queue.

For information about how routing works, and queue-based routing, see these topics:
+ [How routing works with multiple channels](about-routing.md#routing-profile-channels-works)
+ [Queue-based routing to route customers to a specific contact center agent](concepts-queue-based-routing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
