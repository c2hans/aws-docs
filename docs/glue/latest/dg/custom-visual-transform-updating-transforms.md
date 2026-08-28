---
source_url: https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-updating-transforms.html
---

# Step 4. Update custom visual transforms as needed
<a name="custom-visual-transform-updating-transforms"></a>

 Once created and used, the transform script can be updated as long as the transform follows the corresponding json definition:
+  The name used when assigning to DynamicFrame much match the json `functionName`.
+  The function arguments must be defined in the json file as described in [Step 1. Create a JSON config file](custom-visual-transform-json-config-file.md).
+  The Amazon S3 path of the Python file cannot change, since the jobs depend directly on it.

**Note**
 If any updates need to be made, ensure the script and the .json file are consistently updated and any visual jobs are correctly saved again with the new transform. If visual jobs are not saved after the updates were made, the updates will not be applied and validated. If the Python script file is renamed or not placed next to the .json file, then you need to specify the full path in the .json file.

**Custom icon**

If you determine the default icon for your **Action** does not visually distinguish it as part of your workflows, you can provide a custom icon, as described in [Getting started with custom visual transforms](custom-visual-transform-getting-started.md). You can update the icon by updating the corresponding SVG hosted in Amazon S3.

For best results, design your image to be viewed at 32x32px following guidelines from the Cloudscape Design System. For more information about Cloudscape guidelines, see [The Cloudscape documentation](https://cloudscape.design/foundation/visual-foundation/iconography/#custom-icons)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
