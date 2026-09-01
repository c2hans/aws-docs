---
source_url: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-con.html
---

# Connect Customer in AWS GovCloud (US)
<a name="govcloud-con"></a>

Amazon Connect is an easy to use omnichannel cloud contact center that helps you provide superior customer service at a lower cost. It provides a seamless experience across voice and chat for your customers and agents. This includes one set of tools for skills-based routing, powerful real-time and historical analytics, and intuitive management tools – all with pay-as-you-go pricing, which means Amazon Connect simplifies contact center operations, improves agent efficiency, and lowers costs. You can set up a contact center in minutes that can scale to support millions of customers from the office or as a virtual contact center.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West)

## How Connect Customer differs
<a name="govcloud-con-diffs"></a>

The following differences apply to Connect Customer:
+ Amazon Connect instances in AWS GovCloud (US) use the domain **\*.govcloud.connect.aws**
+ It supports only the [latest Contact Control Panel](https://docs.aws.amazon.com/connect/latest/adminguide/upgrade-to-latest-ccp.html) (CCP) for both voice and chat contacts for agents. The earlier CCP is not available.
+ It supports only the latest contact search experience, as described in [What’s new in contact search](https://docs.aws.amazon.com/connect/latest/adminguide/contact-search.html#new-contact-search-experience).
+ Amazon Connect in AWS GovCloud (US) is in a separate partition from all commercial Regions. Therefore it does not support cross-partition integration with other AWS services – such as Amazon Lex, Amazon Lambda, Amazon Kinesis, Amazon S3, Amazon CloudWatch, amongst others – that are available in commercial Regions.
+ The following Amazon Connect features are not available.
  + Amazon Connect Customer Profiles
  + Amazon Q in Connect
  + Amazon Connect Voice ID
  + Amazon Connect Live Media Streaming
  + Amazon Connect Chat integration with Apple Business Chat
  + Amazon Connect email channel
  + Amazon Connect Cases
  + Amazon Connect Outbound Campaigns
  + Granular access controls for real-time metrics
  + Amazon Connect Contact Lens GenAI features and the [ListRealTimeContactAnalysisSegments](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-contact-lens_ListRealtimeContactAnalysisSegments.html) API

## Documentation
<a name="govcloud-con-docs"></a>
+  [Connect Customer documentation](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html)

## Export-controlled content
<a name="con"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Amazon Connect instance and resource configuration metadata is not permitted to contain export-controlled data. This metadata includes all configuration data (for example, name, alias, description, tags) that you enter when creating and maintaining your Amazon Connect instance and resources within an instance, such as users, queues, routing profiles, contact flows, or scheduled report names.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS GovCloud (US). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query govcloud-us` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
