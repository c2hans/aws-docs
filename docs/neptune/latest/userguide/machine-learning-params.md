---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-params.html
---

# Fields to set in the params object when exporting training data
<a name="machine-learning-params"></a>

The `params` object in an export request can contain various fields, as described in the [`params` documentation](export-params-fields.md). The following ones are most relevant for exporting machine-learning training data:
+ **`endpoint`**   –   Use `endpoint` to specify an endpoint of a Neptune instance in your DB cluster that the export process can query to extract data.
+ **`profile`**   –   The `profile` field in the `params` object must be set to **`neptune-ml`**.

  This causes the export process to format the exported data appropriately for Neptune ML model training, in a CSV format for property-graph data or as N-Triples for RDF data. It also causes a `training-data-configuration.json` file to be created and written to the same Amazon S3 location as the exported training data.
+ **`cloneCluster`**   –   If set to `true`, the export process clones your DB cluster, exports from the clone, and then deletes the clone when it is finished.
+ **`useIamAuth`**   –   If your DB cluster has [IAM authentication](iam-auth-enable.md) enabled, you must include this field set to `true`.

The export process also provides several ways to filter the data you export (see [these examples](export-filtering-examples.md)).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
