---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-byoi-launch.html
---

# Launch a custom SageMaker image in RStudio
<a name="rstudio-byoi-launch"></a>

You can use your custom image when launching an RStudio applicaton from the console. After you create your custom SageMaker image and attach it to your domain, the image appears in the image selector dialog box of the RStudio Launcher. To launch a new RStudio app, follow the steps in [Launch RSessions from the RStudio Launcher](rstudio-launcher.md) and select your custom image as shown in the following image.

![Screenshot of the RStudio launcher with image dropdown.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/rstudio-launcher-custom.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
