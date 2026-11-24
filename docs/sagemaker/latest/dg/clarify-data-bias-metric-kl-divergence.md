---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-kl-divergence.html
---

# Kullback-Leibler Divergence (KL)

**Note**
Amazon SageMaker Clarify is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Clarify, but we do not plan to introduce new features. For more information, see [Clarify availability change](clarify-availability-change.md).

The Kullback-Leibler divergence (KL) measures how much the observed label distribution of facet *a*, P<sub>a</sub>(y), diverges from distribution of facet *d*, P<sub>d</sub>(y). It is also known as the relative entropy of P<sub>a</sub>(y) with respect to P<sub>d</sub>(y) and quantifies the amount of information lost when moving from P<sub>a</sub>(y) to P<sub>d</sub>(y).

The formula for the Kullback-Leibler divergence is as follows:

        KL(P<sub>a</sub> \|\| P<sub>d</sub>) = ∑<sub>y</sub>P<sub>a</sub>(y)<sub>\*</sub>log[P<sub>a</sub>(y)/P<sub>d</sub>(y)]

It is the expectation of the logarithmic difference between the probabilities P<sub>a</sub>(y) and P<sub>d</sub>(y), where the expectation is weighted by the probabilities P<sub>a</sub>(y). This is not a true distance between the distributions as it is asymmetric and does not satisfy the triangle inequality. The implementation uses natural logarithms, giving KL in units of nats. Using different logarithmic bases gives proportional results but in different units. For example, using base 2 gives KL in units of bits.

For example, assume that a group of applicants for loans have a 30% approval rate (facet *d*) and that the approval rate for other applicants (facet *a*) is 80%. The Kullback-Leibler formula gives you the label distribution divergence of facet *a* from facet *d* as follows:

        KL = 0.8\*ln(0.8/0.3) \+ 0.2\*ln(0.2/0.7) = 0.53

There are two terms in the formula here because labels are binary in this example. This measure can be applied to multiple labels in addition to binary ones. For example, in a college admissions scenario, assume an applicant may be assigned one of three category labels: y<sub>i</sub> = {y<sub>0</sub>, y<sub>1</sub>, y<sub>2</sub>} = {rejected, waitlisted, accepted}.

Range of values for the KL metric for binary, multicategory, and continuous outcomes is [0, \+∞).
+ Values near zero mean the outcomes are similarly distributed for the different facets.
+ Positive values mean the label distributions diverge, the more positive the larger the divergence.
