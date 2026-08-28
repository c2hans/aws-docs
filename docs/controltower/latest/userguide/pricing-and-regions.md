---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/pricing-and-regions.html
---

# Step 2a. Review and select your AWS Regions
<a name="pricing-and-regions"></a>

Be sure you've correctly designated the AWS Region that you select for your home Region. After you've deployed AWS Control Tower, you can't change the home Region.

In this section of the setup process, you can add any additional AWS Regions that you require. You can add more Regions at a later time, if needed, and you can remove Regions from governance.

**To select additional AWS Regions to govern**

1. The panel shows you the current Region selections. Open the dropdown menu to see a list of additional Regions available for governance.

1. Check the box next to each Region to bring into governance by AWS Control Tower. Your home Region selection is not editable.

**To deny access to certain Regions**

To deny access to AWS resources and workloads in certain AWS Regions, select **Enabled** in the section for the Region deny control. By default, the setting for this control is **Not enabled**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
