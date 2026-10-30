---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/transformation-policy-limits.html
---

# Policy limits
<a name="transformation-policy-limits"></a>

The following table lists the limits for each field in a transformation policy.

| Field | Limit |
| --- | --- |
| Serialized policy size | 10 KB (10,000 characters) |
|  `transformations`  | 100 entries |
|  `outputs`  | 3 entries |
|  `condition.value` array | 50 values |
|  `smartCrop.labels`  | 50 labels, 100 characters each |
|  `smartCrop.priorities`  | 2 entries |
|  `contentModeration.moderationLabels`  | 100 labels, 100 characters each |
|  `quality` output | Default quality plus 20 DPR mapping entries |
|  `autosize` output | 20 widths |

If a create or update request exceeds a limit, the management API rejects it with a `400 Bad Request` and the message `Invalid request`. The limits apply only when a policy is saved. A policy that was stored before version 8.1.3 and exceeds a limit keeps serving images. Before you can save it from the admin UI, or update it through an API request that includes `policyJSON`, bring it within the limits. An update that omits `policyJSON` is not affected.
