---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost04.html
---

# Database optimization
<a name="advcost04"></a>

| ADVCOST04: How are you optimizing user profile storage, access, and replication? |
| --- |
|   |

 User profile databases tend to be large ranging from 100-200 million to 5 billion user profiles and contain a wide range of data about users' online activities and interactions. Storage and Access to this data can increase cost.

**Topics**
+ [ADVCOST04-BP01 Consider lower cost storage for older User Profile data](advcost04-bp01.md)
+ [ADVCOST04-BP02 Consider multi-level caching for user profile data](advcost04-bp02.md)
+ [ADVCOST04-BP03 Store profiles in a single Region and replicate asynchronously](advcost04-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
