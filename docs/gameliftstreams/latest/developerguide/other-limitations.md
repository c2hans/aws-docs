---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/other-limitations.html
---

# Other Amazon GameLift Streams limitations
<a name="other-limitations"></a>

This page lists other limitations to be aware of as you create your streaming solution. Unless noted otherwise, these limits are fixed within the service for all customers.

| Name | Limitation | Description |
| --- | --- | --- |
| Active stream URLs per account | 20 | The maximum number of stream URLs in ACTIVE status per AWS account. |
| Active stream URLs per stream group | 5 | The maximum number of stream URLs in ACTIVE status per stream group. |
| Applications in a stream group | 100 | The maximum number of Amazon GameLift Streams applications that can be associated to a stream group. |
| GPUs in a stream group | 2500 | The maximum number of GPUs in a stream group across all Regions and remote locations. |
| Single file size (GiB) | 80 GiB | The maximum size (in GiB) of a single file in an application. Note that a gibibyte (GiB) equals 1024\*1024\*1024 bytes. |
| Stream group associations per application | 100 | The maximum number of stream groups that an Amazon GameLift Streams application can be associated to. |
| Stream URL expiration (minutes) | 1,440 | The maximum value (in minutes) for UrlExpiresAfterMinutes on CreateStreamUrl, equal to 24 hours. |
| Usage limit per stream URL | 50 | The maximum value for UsageLimit on CreateStreamUrl. The default is 1. |
| VPC transit configurations | 5 | The maximum number of VPC transit configurations per AWS account per Region. |

Stream URL limits are default service limits and are not managed through AWS Service Quotas. To request a higher limit, contact AWS Support.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
