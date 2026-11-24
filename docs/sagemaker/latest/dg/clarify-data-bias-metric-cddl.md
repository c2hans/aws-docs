---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-cddl.html
---

# Conditional Demographic Disparity (CDD)

**Note**
Amazon SageMaker Clarify is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Clarify, but we do not plan to introduce new features. For more information, see [Clarify availability change](clarify-availability-change.md).

The demographic disparity metric (DD) determines whether a facet has a larger proportion of the rejected outcomes in the dataset than of the accepted outcomes. In the binary case where there are two facets, men and women for example, that constitute the dataset, the disfavored one is labelled facet *d* and the favored one is labelled facet *a*. For example, in the case of college admissions, if women applicants comprised 46% of the rejected applicants and comprised only 32% of the accepted applicants, we say that there is *demographic disparity* because the rate at which women were rejected exceeds the rate at which they are accepted. Women applicants are labelled facet *d* in this case. If men applicants comprised 54% of the rejected applicants and 68% of the accepted applicants, then there is not a demographic disparity for this facet as the rate of rejection is less that the rate of acceptance. Men applicants are labelled facet *a* in this case.

The formula for the demographic disparity for the less favored facet *d* is as follows:

        DD<sub>d</sub> = n<sub>d</sub><sup>(0)</sup>/n<sup>(0)</sup> - n<sub>d</sub><sup>(1)</sup>/n<sup>(1)</sup> = P<sub>d</sub><sup>R</sup>(y<sup>0</sup>) - P<sub>d</sub><sup>A</sup>(y<sup>1</sup>)

Where:
+ n<sup>(0)</sup> = n<sub>a</sub><sup>(0) </sup>\+ n<sub>d</sub><sup>(0)</sup> is the total number of rejected outcomes in the dataset for the favored facet *a* and disadvantaged facet *d*.
+ n<sup>(1)</sup> = n<sub>a</sub><sup>(1) </sup>\+ n<sub>d</sub><sup>(1)</sup> is the total number of accepted outcomes in the dataset for the favored facet *a* and disadvantaged facet *d*.
+ P<sub>d</sub><sup>R</sup>(y<sup>0</sup>) is the proportion of rejected outcomes (with value 0) in facet *d*.
+ P<sub>d</sub><sup>A</sup>(y<sup>1</sup>) is the proportion of accepted outcomes (value 1) in facet *d*.

For the college admission example, the demographic disparity for women is DD<sub>d</sub> = 0.46 - 0.32 = 0.14. For men DD<sub>a</sub> = 0.54 - 0.68 = - 0.14.

A conditional demographic disparity (CDD) metric that conditions DD on attributes that define a strata of subgroups on the dataset is needed to rule out Simpson's paradox. The regrouping can provide insights into the cause of apparent demographic disparities for less favored facets. The classic case arose in the case of Berkeley admissions where men were accepted at a higher rate overall than women. The statistics for this case were used in the example calculations of DD. However, when departmental subgroups were examined, women were shown to have higher admission rates than men when conditioned by department. The explanation was that women had applied to departments with lower acceptance rates than men had. Examining the subgrouped acceptance rates revealed that women were actually accepted at a higher rate than men for the departments with lower acceptance rates.

The CDD metric gives a single measure for all of the disparities found in the subgroups defined by an attribute of a dataset by averaging them. It is defined as the weighted average of demographic disparities (DD<sub>i</sub>) for each of the subgroups, with each subgroup disparity weighted in proportion to the number of observations in contains. The formula for the conditional demographic disparity is as follows:

        CDD = (1/n)<sub>\*</sub>∑<sub>i</sub>n<sub>i</sub> <sub>\*</sub>DD<sub>i</sub>

Where:
+ ∑<sub>i</sub>n<sub>i</sub> = n is the total number of observations and n<sub>i</sub>is the number of observations for each subgroup.
+ DD<sub>i</sub> = n<sub>i</sub><sup>(0)</sup>/n<sup>(0)</sup> - n<sub>i</sub><sup>(1)</sup>/n<sup>(1)</sup> = P<sub>i</sub><sup>R</sup>(y<sup>0</sup>) - P<sub>i</sub><sup>A</sup>(y<sup>1</sup>) is the demographic disparity for the ith subgroup.

The demographic disparity for a subgroup (DD<sub>i</sub>) are the difference between the proportion of rejected outcomes and the proportion of accepted outcomes for each subgroup.

The range of DD values for binary outcomes for the full dataset DD<sub>d</sub> or for its conditionalized subgroups DD<sub>i</sub> is [-1, \+1].
+ \+1: when there no rejections in facet *a* or subgroup and no acceptances in facet *d* or subgroup
+ Positive values indicate there is a demographic disparity as facet *d* or subgroup has a greater proportion of the rejected outcomes in the dataset than of the accepted outcomes. The higher the value the less favored the facet and the greater the disparity.
+ Negative values indicate there is not a demographic disparity as facet *d* or subgroup has a larger proportion of the accepted outcomes in the dataset than of the rejected outcomes. The lower the value the more favored the facet.
+ -1: when there are no rejections in facet *d* or subgroup and no acceptances in facet *a* or subgroup

If you don't condition on anything then CDD is zero if and only if DPL is zero.

This metric is useful for exploring the concepts of direct and indirect discrimination and of objective justification in EU and UK non-discrimination law and jurisprudence. For additional information, see [Why Fairness Cannot Be Automated](https://arxiv.org/abs/2005.05906). This paper also contains the relevant data and analysis of the Berkeley admissions case that shows how conditionalizing on departmental admission rate subgroups illustrates Simpson's paradox.
