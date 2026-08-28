---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/possible-issues-shifting-regions.html
---

# Tips for avoiding issues when shifting agents in your Connect Customer instance across Regions
<a name="possible-issues-shifting-regions"></a>
+ Whenever you update the traffic distribution for agents be sure to also update the traffic distribution for inbound voice contacts. Otherwise, you might end up in a situation where one Region is heavy on agents while the other is heavy on telephony traffic.
+ Before associating users to a traffic distribution group, make sure the same username exists in both the source and replica Connect Customer instances. Otherwise, when you associate a user to a traffic distribution group but the user with the username does not exist in the replica Region, you will get an `InvalidRequestException` error.
+ You must call the [AssociateTrafficDistributionGroupUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateTrafficDistributionGroupUser.html) API to associate agents to a traffic distribution group in the source Region. If you attempt to do this while in the replica Region, you will get a `ResourceNotFoundException` error.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
