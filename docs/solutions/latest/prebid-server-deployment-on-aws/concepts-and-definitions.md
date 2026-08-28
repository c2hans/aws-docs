---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution:

 **custom headers**

Amazon CloudFront can be configured to add custom headers, which enable you to send and gather information from your origin that you don’t get with typical viewer requests.

 **header bidding**

Header bidding is a process that enables publishers to capture bids for ad units from demand sources that might otherwise have been missed. By implementing header bidding, a publisher can gather bids from multiple sources that will then compete directly with bids from the ad server

 **Prebid Server**

Prebid Server is an open source solution for server-to-server header bidding.

 **wrapper**

A wrapper is a type of Software Development Kit (SDK) for advertising. A wrapper provides browser code to consolidate multiple header bidding partners into a unified framework. It simplifies the management of ad placements and real-time bidding across different ad networks, optimizing ad revenues by allowing simultaneous bids on inventory.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
