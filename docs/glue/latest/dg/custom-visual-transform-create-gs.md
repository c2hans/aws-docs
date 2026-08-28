---
source_url: https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-create-gs.html
---

# Step 5. Use custom visual transforms in AWS Glue Studio
<a name="custom-visual-transform-create-gs"></a>

 To use a custom visual transform in AWS Glue Studio, you upload the config and source files, then select the transform from the **Action** menu. Any parameters that need values or input are available to you in the **Transform** tab.

1.  Upload the two files (Python source file and JSON config file) to the Amazon S3 assets folder where the job scripts are stored. By default, AWS Glue pulls all JSON files from the **/transforms** folder within the same Amazon S3 bucket.

1.  From the **Action** menu, choose the custom visual transform. It is named with the transform `displayName` or name that you specified in the .json config file.

1.  Enter values for any parameters that were configured in the config file.
![The screenshot shows a custom visual transform with parameters for the user to complete in the Transform tab.](http://docs.aws.amazon.com/glue/latest/dg/images/dynamic-transform-parameters.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
