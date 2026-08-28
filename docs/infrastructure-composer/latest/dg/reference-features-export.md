---
source_url: https://docs.aws.amazon.com/infrastructure-composer/latest/dg/reference-features-export.html
---

# Export an image of Infrastructure Composer's visual canvas
<a name="reference-features-export"></a>

This topic describes the AWS Infrastructure Composer console **export canvas** feature.

For a visual overview of all Infrastructure Composer features, see [AWS Infrastructure Composer console visual overview](reference-visual.md).

## About export canvas
<a name="reference-features-export-about"></a>

The **export canvas** feature exports your application’s canvas as an image to your local machine.
+ Infrastructure Composer removes the visual designer UI elements and exports only your application’s diagram.
+ The default image file format is `png`.
+ The file is exported to your local machine’s default download location.

You can access the **export canvas** feature from the **Menu**.

![Infrastructure Composer's Menu with Export canvas selected.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_ref_13.png)

## Exporting canvas
<a name="reference-features-export-canvas"></a>

When you export your canvas, Infrastructure Composer displays a status message.

If the export is successful, you will see the following message:

![Infrastructure Composer's Menu with Export canvas selected.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_ref_14.png)

If the export was unsuccessful, you will see an error message. If you receive an error, try exporting again.

![Infrastructure Composer's Menu with Export canvas selected.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_ref_15.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Infrastructure Composer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query infrastructure-composer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
