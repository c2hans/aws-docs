---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-architecture-considerations.html
---

# Architecture considerations for CDN and MediaTailor integrations
<a name="cdn-architecture-considerations"></a>

Position your content delivery network (CDN) correctly in your architecture to ensure optimal performance and reliability with AWS Elemental MediaTailor. The recommended architecture places the CDN between viewers and MediaTailor, not between MediaTailor and your origin.

For detailed architecture diagrams and workflow explanations, see the following topics.
+ [Ad insertion with CDN](ssai-cdn-workflow.md) for ad insertion architecture diagrams and detailed workflow
+ [Understand CDN architecture](channel-assembly-cdn-architecture.md) for channel assembly architecture diagrams and workflow

Position your CDN correctly in your architecture:

1. Place your CDN between players and MediaTailor (not between MediaTailor and your origin).

   This architecture allows your CDN to cache ad segments and content segments. At the same time, MediaTailor can generate personalized manifests for each viewer.

1. Create separate cache behaviors for different request types:
   + Manifest requests (no caching)
   + Content segments (longer TTL)
   + Ad segments (longer TTL)

1. Configure proper error handling:
   + Set up negative caching (temporarily storing error responses) to avoid overwhelming your origin with repeated requests during service disruptions. Negative caching means the CDN will temporarily store error responses (like 404 or 500 errors) to prevent repeated requests for content that doesn't exist or is temporarily unavailable.
   + Configure appropriate error response codes and retry behavior

1. Implement intermediate caching (origin shield):

   Origin shield is a feature that creates an additional caching layer between CDN edge locations and your origin server. This reduces the number of redundant requests that reach your origin server.
   + Configure an intermediate caching layer between edge locations and your origin
   + Reduce the number of redundant requests to your origin during cache misses
   + Improve cache hit ratios across your CDN infrastructure

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
