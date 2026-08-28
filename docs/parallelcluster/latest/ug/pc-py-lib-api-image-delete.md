---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pc-py-lib-api-image-delete.html
---

# `delete_image`
<a name="pc-py-lib-api-image-delete"></a>

```
delete_image(image_id, region, force)
```

Delete an image in a given Region.Parameters:

**`image_id` (required)**
The image ID.

**`region`**
The image AWS Region.

**`force`**
If set to `True`, AWS ParallelCluster forces deletion if instances are using the AMI or if the AMI is shared. The default is `False`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
