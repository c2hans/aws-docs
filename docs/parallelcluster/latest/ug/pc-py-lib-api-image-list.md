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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
