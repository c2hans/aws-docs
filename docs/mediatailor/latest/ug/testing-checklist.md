---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/testing-checklist.html
---

# Pre-deployment testing checklist for CDN and MediaTailor integrations
<a name="testing-checklist"></a>

AWS Elemental MediaTailor content delivery network (CDN) integration must pass comprehensive testing before production deployment. Use this checklist before deploying configuration changes to production.

**Basic functionality:**
+ ☐ Manifest requests return HTTP 200 responses
+ ☐ Content segments load correctly
+ ☐ Ad segments load correctly
+ ☐ Ad breaks appear at expected times
+ ☐ Playback transitions smoothly between content and ads

**Configuration validation:**
+ ☐ Query parameters are forwarded correctly
+ ☐ Required headers are forwarded correctly
+ ☐ Manifest caching is disabled (TTL = 0)
+ ☐ Segment caching is configured appropriately
+ ☐ CORS headers are configured for web players

**Cross-platform testing:**
+ ☐ Tested on mobile devices
+ ☐ Tested on desktop browsers
+ ☐ Tested with different player types
+ ☐ Tested both HLS and DASH formats

**Performance validation:**
+ ☐ AWS Support ticket created for load testing approval
+ ☐ Response times meet performance targets
+ ☐ Cache hit ratios are acceptable
+ ☐ Error rates are within acceptable limits
+ ☐ Monitoring and alerting are configured

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
