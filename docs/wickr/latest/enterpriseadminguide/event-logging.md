---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/event-logging.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Event logging
<a name="event-logging"></a>

Event logging changes the default verbosity level for several backend services. It only effects the information in the Admin, Admin-API, Switchboard, and Messaging containers.
+ **Activity:** Shows the least amount of information and is the default.
+ **IP Address:** Shows the IP address of the sending client in addition to the default level.
+ **Messaging:** Shows the most information, which can include:
  + IP address
  + Client ID
  + Device type
  + Recipients
+ **Username ID:** Shows the userID associated with information in all other verbosity settings.

Message contents are never shown regardless of the chosen verbosity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
