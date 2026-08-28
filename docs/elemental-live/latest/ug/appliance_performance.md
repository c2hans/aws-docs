---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/appliance_performance.html
---

# Performance of Elemental Live appliances
<a name="appliance_performance"></a>

This section looks at the factors that affect the performance of an AWS Elemental Live appliance, with particular emphasis on the newest appliances. It provides guidance about how to maximize performance while achieving the preferred balance between density, speed, and quality.
+ **Density** is the number of output encodes or events that you can run on an appliance.

  The density is affected by the following:
  + The capabilities of the appliance.
  + The compute demands of the individual events, especially the demands to achieve the desired video quality in the outputs.
+ **Speed** is the rate at which the workflow content can be processed or transmitted. With live events, there must be enough compute power applied to achieve real-time ingest of the input and real-time encoding of the output.
+ **Quality** refers primarily to the video quality.

This section describes how to obtain the balance that suits your requirements.

**Topics**
+ [Recommended testing procedure](performance-recommended-procedure.md)
+ [Recommendation: Continually upgrade Elemental Live](performance-recommended-upgrade.md)
+ [Assessing performance by measuring](performance-measures.md)
+ [Assessing performance with logging messages](performance-via-logs.md)
+ [Encoding parameters that affect performance](performance-encoding-params.md)
+ [Features that affect performance](performance-features.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
