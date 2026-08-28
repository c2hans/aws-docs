---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-jensen-shannon-divergence.html
---

# Jensen-Shannon Divergence (JS)
<a name="clarify-data-bias-metric-jensen-shannon-divergence"></a>

**Note**
Amazon SageMaker Clarify is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Clarify, but we do not plan to introduce new features. For more information, see [Clarify availability change](clarify-availability-change.md).

The Jensen-Shannon divergence (JS) measures how much the label distributions of different facets diverge from each other entropically. It is based on the Kullback-Leibler divergence, but it is symmetric.

The formula for the Jensen-Shannon divergence is as follows:

        JS = ½\*[KL(Pa \|\| P) \+ KL(Pd \|\| P)]

Where P = ½( Pa \+ Pd ), the average label distribution across facets *a* and *d*.

The range of JS values for binary, multicategory, continuous outcomes is [0, ln(2)).
+ Values near zero mean the labels are similarly distributed.
+ Positive values mean the label distributions diverge, the more positive the larger the divergence.

This metric indicates whether there is a big divergence in one of the labels across facets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
