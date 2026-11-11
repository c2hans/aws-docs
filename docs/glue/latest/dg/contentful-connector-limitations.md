---
source_url: https://docs.aws.amazon.com/glue/latest/dg/contentful-connector-limitations.html
---

# Limitations and notes for the Contentful connector
<a name="contentful-connector-limitations"></a>

The following are limitations and notes for the Contentful connector:
+ Contentful is supported as a source only. Writing to Contentful is not supported.
+ Job bookmarks are not supported.
+ The `entries` and `assets` entities return system metadata only, not content `fields`.
