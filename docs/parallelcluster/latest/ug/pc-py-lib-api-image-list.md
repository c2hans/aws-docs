---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pc-py-lib-api-image-list.html
---

# `list_images`
<a name="pc-py-lib-api-image-list"></a>

```
list_images(image_status, region, next_token)
```

Retrieve the list of existing images.Parameters:

**`image_status` (required)**
Filters by image status.
Valid values: `AVAILABLE` \| `PENDING` \| `FAILED`

**`region`**
Lists images built in a given AWS Region.

**`next_token`**
The token for the next set of results.
