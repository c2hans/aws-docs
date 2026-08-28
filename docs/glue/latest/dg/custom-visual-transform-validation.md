---
source_url: https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-validation.html
---

# Step 3. Validate and troubleshoot custom visual transforms in AWS Glue Studio
<a name="custom-visual-transform-validation"></a>

 AWS Glue Studio validates the JSON config file before custom visual transforms are loaded into AWS Glue Studio. Validation includes:
+  Presence of required fields
+  JSON format validation
+  Incorrect or invalid parameters
+  Presence of both the .py and .json files in the same Amazon S3 path
+  Matching filenames for the .py and .json

 If validation succeeds, the transform is listed in the list of available **Actions** in the visual editor. If a custom icon has been provided, it should be visible beside the **Action**.

 If validation fails, AWS Glue Studio does not load the custom visual transform.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
