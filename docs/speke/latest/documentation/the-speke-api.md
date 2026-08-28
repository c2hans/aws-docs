---
source_url: https://docs.aws.amazon.com/speke/latest/documentation/the-speke-api.html
---

# SPEKE API v1
<a name="the-speke-api"></a>

This is the REST API for Secure Packager and Encoder Key Exchange (SPEKE) v1. Use this specification to provide DRM copyright protection for customers who use encryption. To be SPEKE-compliant, your DRM key provider must expose the REST API described in this specification. The encryptor makes API calls to your key provider.

**Note**
The code examples in this specification are for illustration purposes only. You can’t run the examples because they aren’t part of a complete SPEKE implementation.

SPEKE uses the DASH Industry Forum Content Protection Information Exchange Format (DASH-IF-CPIX) data structure definition for key exchange, with some restrictions. DASH-IF-CPIX defines a schema to provide an extensible, multi-DRM exchange from the DRM platform to the encryptor. This enables content encryption for all adaptive bitrate packaging formats at the time of content compression and packaging. Adaptive bitrate packaging formats include HLS, DASH, and MSS.

For detailed information about the exchange format, see the DASH Industry Forum CPIX specification at https://dashif.org/docs/DASH-IF-CPIX-v2-0.pdf.

**Topics**
+ [SPEKE API v1 - Customizations and constraints to the DASH-IF specification](speke-constraints.md)
+ [SPEKE API v1 - Standard payload components](standard-payload-components.md)
+ [SPEKE API v1 - Live workflow method call examples](live-workflow-methods.md)
+ [SPEKE API v1 - VOD workflow method call examples](vod-workflow-methods.md)
+ [SPEKE API v1 - Content key encryption](content-key-encryption.md)
+ [SPEKE API v1 - Heartbeat](heartbeat.md)
+ [SPEKE API v1 - Overriding the key identifier](kid-override.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Packager and Encoder Key Exchange API Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query speke` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
