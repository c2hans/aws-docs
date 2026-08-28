---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/drm-content-key-rotation.html
---

# Understanding key rotation behavior
<a name="drm-content-key-rotation"></a>

When you enable key rotation on live content from HLS, CMAF, and DASH endpoints, AWS Elemental MediaPackage retrieves content keys before the live content begins. As the content progresses, MediaPackage retrieves new keys at the interval that you set on the endpoint, as described in [Package encryption fields](endpoints-hls-encryption.md).

If MediaPackage is unable to retrieve the content key, it takes the following actions:
+ If MediaPackage successfully retrieved a content key for this endpoint before, it uses the last key that it fetched. This ensures that endpoints that worked previously continue to work.
+ If MediaPackage has *not* successfully retrieved a content key for this endpoint before, MediaPackage responds to the playback request with error 404.

In all cases, when MediaPackage can't fetch a content key, it generates a CloudWatch event, as described in [Key provider notification events](cloudwatch-events-example.md#key-provider-state-events).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
