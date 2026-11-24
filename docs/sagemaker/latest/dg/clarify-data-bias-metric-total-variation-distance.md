---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-total-variation-distance.html
---

# Total Variation Distance (TVD)

**Note**
Amazon SageMaker Clarify is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Clarify, but we do not plan to introduce new features. For more information, see [Clarify availability change](clarify-availability-change.md).

The total variation distance data bias metric (TVD) is half the L<sub>1</sub>-norm. The TVD is the largest possible difference between the probability distributions for label outcomes of facets *a* and *d*. The L<sub>1</sub>-norm is the Hamming distance, a metric used compare two binary data strings by determining the minimum number of substitutions required to change one string into another. If the strings were to be copies of each other, it determines the number of errors that occurred when copying. In the bias detection context, TVD quantifies how many outcomes in facet *a* would have to be changed to match the outcomes in facet *d*.

The formula for the Total variation distance is as follows:

        TVD = ½<sub>\*</sub>L<sub>1</sub>(P<sub>a</sub>, P<sub>d</sub>)

For example, assume you have an outcome distribution with three categories, y<sub>i</sub> = {y<sub>0</sub>, y<sub>1</sub>, y<sub>2</sub>} = {accepted, waitlisted, rejected}, in a college admissions multicategory scenario. You take the differences between the counts of facets *a* and *d* for each outcome to calculate TVD. The result is as follows:

        L<sub>1</sub>(P<sub>a</sub>, P<sub>d</sub>) = \|n<sub>a</sub><sup>(0)</sup> - n<sub>d</sub><sup>(0)</sup>\| \+ \|n<sub>a</sub><sup>(1)</sup> - n<sub>d</sub><sup>(1)</sup>\| \+ \|n<sub>a</sub><sup>(2)</sup> - n<sub>d</sub><sup>(2)</sup>\|

Where:
+ n<sub>a</sub><sup>(i)</sup> is number of the ith category outcomes in facet *a*: for example n<sub>a</sub><sup>(0)</sup> is number of facet *a* acceptances.
+ n<sub>d</sub><sup>(i)</sup> is number of the ith category outcomes in facet d: for example n<sub>d</sub><sup>(2)</sup> is number of facet *d* rejections.

  The range of TVD values for binary, multicategory, and continuous outcomes is [0, 1), where:
  + Values near zero mean the labels are similarly distributed.
  + Positive values mean the label distributions diverge, the more positive the larger the divergence.
