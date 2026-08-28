---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/per-frame-metrics-requirements.html
---

# Requirements and processing impact
<a name="per-frame-metrics-requirements"></a>

To use per-frame metric reports, your job settings must include the following:
+ Your output must use one of the following video codecs: H.264, H.265, AV1, MPEG-2, AVC-Intra, or XAVC
+ Include one or more video outputs.
+ For the QVBR metric, your output must use the QVBR rate control mode.

Jobs that generate per-frame metrics take longer to complete than standard encoding jobs. The additional processing time depends on several factors, including:
+ The resolution of your output
+ The complexity of your video content
+ The number of metrics you select

For high-resolution outputs (such as 4K), jobs might take up to twice as long to complete compared to standard encoding.

Some metrics require more computational resources than others. For example, VMAF calculation is more computationally intensive than other metrics. Consider enabling only the metrics you need for your specific analysis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
