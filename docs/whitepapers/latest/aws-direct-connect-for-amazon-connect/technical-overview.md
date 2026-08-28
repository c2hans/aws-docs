---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/technical-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Technical overview
<a name="technical-overview"></a>

 This whitepaper outlines the ease with which Amazon Connect users of the agent Contact Control Panel (CCP or Agent UI) can ensure that data flows across new or existing Direct Connect services, and that customers realize the benefits of doing so. It also provides the context of using the Amazon Connect CCP, and ensures that the signaling, messaging, and voice payload flows over the AWS Direct Connect service to the Amazon Connect public IP addresses.

 There are five simple steps to configure Direct Connect for operation with Amazon Connect:

1.  Connect—Establish a connection in an AWS Direct Connect location.

1.  Set up a Direct Connect Public Virtual Interface.

1.  Select the Border Gateway Protocol (BGP) community tags—Regional, continental, or global.

1.  Set up and advertise an 802.1q virtual local area network (VLAN).

1.  Route CCP traffic to advertised Amazon Connect addresses.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
