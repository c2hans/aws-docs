---
source_url: https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-regions.html
---

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Regions and quotas for Amazon Q Developer in chat applications
<a name="chatbot-regions"></a>

Although most AWS Regions are active by default for your AWS account, certain Regions are activated only when you manually select them. This document refers to those Regions as *opt-in Regions*. In contrast, Regions that are active by default, as soon as your AWS account is created, are referred to as *commercial Regions*, or simply, *Regions*.

## Supported Regions for Amazon Q Developer in chat applications
<a name="region-info"></a>

Supported Regions include:
+ US East (Ohio)
+ US East (N. Virginia)
+ US West (N. California)
+ US West (Oregon)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Paris)
+ Europe (Stockholm)
+ South America (São Paulo)

You can combine Amazon SNS topics from multiple Regions in a single Amazon Q Developer in chat applications configuration.

### Opt-in Regions
<a name="opt-in-Regions"></a>

Opt-in Regions aren't enabled by default. You must manually enable these Regions to use them with Amazon Q Developer in chat applications. For more information about AWS Regions, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html). The following opt-in Regions are supported:
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Jakarta)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Melbourne)
+ Asia Pacific (Thailand)
+ Canada West (Calgary)
+ Europe (Milan)
+ Europe (Spain)
+ Europe (Zurich)
+ Israel (Tel Aviv)
+ Middle East (Bahrain)
+ Middle East (UAE)
+ Mexico (Central)

## Endpoints and quotas for Amazon Q Developer in chat applications
<a name="chatbot-quotas"></a>

Amazon Q Developer in chat applications currently supports service endpoints, however there are no adjustable quotas. For more information about Amazon Q Developer in chat applications endpoints and quotas, see [Amazon Q Developer in chat applications endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/chatbot.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
