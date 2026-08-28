---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/testing-prerequisites.html
---

# Testing prerequisites and setup for CDN and MediaTailor integrations
<a name="testing-prerequisites"></a>

AWS Elemental MediaTailor content delivery network (CDN) integration testing requires proper preparation and resource allocation. Before beginning systematic testing, ensure you have the necessary resources and tools in place.

**Required resources:**
+ Test CDN distribution configured to mirror production settings
+ Test MediaTailor configuration with known content and ad sources
+ Test content with predictable characteristics (duration, format, ad break markers)
+ Test ad decision server or mock ADS responses
+ Multiple test devices and player types

**Testing tools:**
+ `curl` for HTTP request testing
+ `ffprobe` for HLS manifest validation
+ `mp4box` for DASH manifest validation
+ Browser developer tools for network analysis
+ Video players for end-to-end testing

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
