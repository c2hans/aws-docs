---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.start-practice-run.html
---

# Starting a practice run zonal shift
<a name="arc-zonal-autoshift.start-practice-run"></a>

The steps in this section explain how to start an on-demand practice run zonal shift on the ARC console. To work with zonal shift and zonal autoshift programmatically, see the [ Zonal Shift and Zonal Autoshift API Reference Guide](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/Welcome.html).

You can start a practice run zonal shift after you configure zonal autoshift and create a practice run configuration.

# To start a practice run zonal shift

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/](https://console.aws.amazon.com/route53recovery/zonalshift/home#/).

1. Under **Zonal autoshift resources**, browse to an individual resource that has zonal autoshift configured.

1. On the **Resource overview** page, choose **Start practice run**.

1. Select an Availability Zone, and then enter a comment for your practice run. The practice run will shift traffic away from the Availability Zone that you selected.

1. Choose **Start**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
