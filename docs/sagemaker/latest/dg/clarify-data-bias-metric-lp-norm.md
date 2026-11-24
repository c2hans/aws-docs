---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-lp-norm.html
---

# L<sub>p</sub>-norm (LP)

**Note**
Amazon SageMaker Clarify is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Clarify, but we do not plan to introduce new features. For more information, see [Clarify availability change](clarify-availability-change.md).

The L<sub>p</sub>-norm (LP) measures the p-norm distance between the facet distributions of the observed labels in a training dataset. This metric is non-negative and so cannot detect reverse bias.

The formula for the L<sub>p</sub>-norm is as follows:

        L<sub>p</sub>(P<sub>a</sub>, P<sub>d</sub>) = ( ∑<sub>y</sub>\|\|P<sub>a</sub> - P<sub>d</sub>\|\|<sup>p</sup>)<sup>1/p</sup>

Where the p-norm distance between the points x and y is defined as follows:

        L<sub>p</sub>(x, y) = (\|x<sub>1</sub>-y<sub>1</sub>\|<sup>p</sup> \+ \|x<sub>2</sub>-y<sub>2</sub>\|<sup>p</sup> \+ … \+\|x<sub>n</sub>-y<sub>n</sub>\|<sup>p</sup>)<sup>1/p</sup>

The 2-norm is the Euclidean norm. Assume you have an outcome distribution with three categories, for example, y<sub>i</sub> = {y<sub>0</sub>, y<sub>1</sub>, y<sub>2</sub>} = {accepted, waitlisted, rejected} in a college admissions multicategory scenario. You take the sum of the squares of the differences between the outcome counts for facets *a* and *d*. The resulting Euclidean distance is calculated as follows:

        L<sub>2</sub>(P<sub>a</sub>, P<sub>d</sub>) = [(n<sub>a</sub><sup>(0)</sup> - n<sub>d</sub><sup>(0)</sup>)<sup>2</sup> \+ (n<sub>a</sub><sup>(1)</sup> - n<sub>d</sub><sup>(1)</sup>)<sup>2</sup> \+ (n<sub>a</sub><sup>(2)</sup> - n<sub>d</sub><sup>(2)</sup>)<sup>2</sup>]<sup>1/2</sup>

Where:
+ n<sub>a</sub><sup>(i)</sup> is number of the ith category outcomes in facet *a*: for example n<sub>a</sub><sup>(0)</sup> is number of facet *a* acceptances.
+ n<sub>d</sub><sup>(i)</sup> is number of the ith category outcomes in facet *d*: for example n<sub>d</sub><sup>(2)</sup> is number of facet *d* rejections.

  The range of LP values for binary, multicategory, and continuous outcomes is [0, √2), where:
  + Values near zero mean the labels are similarly distributed.
  + Positive values mean the label distributions diverge, the more positive the larger the divergence.
