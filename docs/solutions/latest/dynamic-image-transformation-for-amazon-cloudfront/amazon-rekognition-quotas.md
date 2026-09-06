---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/amazon-rekognition-quotas.html
---

# Amazon Rekognition quotas
<a name="amazon-rekognition-quotas"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

Smart cropping and content moderation call Amazon Rekognition, which enforces a per-API, per-account transactions-per-second (TPS) limit. The default limit depends on the Region (for the current per-API defaults across all Regions, see [Amazon Rekognition endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/rekognition.html#limits_rekognition) in the *AWS General Reference*):

| Region | Default TPS (per API) |
| --- | --- |
| US East (N. Virginia), US West (Oregon), Europe (Ireland) | 50 |
| All other supported Regions | 5 |

These limits apply to each detection API separately. A single smart crop request that invokes three detection APIs consumes three TPS against three separate limits. CloudFront caching is the primary way to stay within these limits, because only cache misses reach Amazon Rekognition; at an 80-90% cache hit rate, most edge requests never invoke a detection API.

If you expect sustained smart-crop traffic above these defaults (typically a Medium deployment size or larger), request a Service Quotas increase before you go live. For per-API limits and how to request an increase, see [Amazon Rekognition service quotas](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html) in the *Amazon Rekognition Developer Guide*.
