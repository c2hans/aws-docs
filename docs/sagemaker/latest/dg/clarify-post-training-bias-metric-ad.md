---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-ad.html
---

# Accuracy Difference (AD)

**Note**
Amazon SageMaker Clarify is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Clarify, but we do not plan to introduce new features. For more information, see [Clarify availability change](clarify-availability-change.md).

Accuracy difference (AD) metric is the difference between the prediction accuracy for different facets. This metric determines whether the classification by the model is more accurate for one facet than the other. AD indicates whether one facet incurs a greater proportion of Type I and Type II errors. But it cannot differentiate between Type I and Type II errors. For example, the model may have equal accuracy for different age demographics, but the errors may be mostly false positives (Type I errors) for one age-based group and mostly false negatives (Type II errors) for the other.

Also, if loan approvals are made with much higher accuracy for a middle-aged demographic (facet *a*) than for another age-based demographic (facet *d*), either a greater proportion of qualified applicants in the second group are denied a loan (FN) or a greater proportion of unqualified applicants from that group get a loan (FP) or both. This can lead to within group unfairness for the second group, even if the proportion of loans granted is nearly the same for both age-based groups, which is indicated by a DPPL value that is close to zero.

The formula for AD metric is the difference between the prediction accuracy for facet *a*, ACC<sub>a</sub>, minus that for facet *d*, ACC<sub>d</sub>:

        AD = ACC<sub>a</sub> - ACC<sub>d</sub>

Where:
+ ACC<sub>a</sub> = (TP<sub>a</sub> \+ TN<sub>a</sub>)/(TP<sub>a</sub> \+ TN<sub>a</sub> \+ FP<sub>a</sub> \+ FN<sub>a</sub>)
  + TP<sub>a</sub> are the true positives predicted for facet *a*
  + TN<sub>a</sub> are the true negatives predicted for facet *a*
  + FP<sub>a</sub> are the false positives predicted for facet *a*
  + FN<sub>a</sub> are the false negatives predicted for facet *a*
+ ACC<sub>d</sub> = (TP<sub>d</sub> \+ TN<sub>d</sub>)/(TP<sub>d</sub> \+ TN<sub>d</sub> \+ FP<sub>d</sub> \+ FN<sub>d</sub>)
  + TP<sub>d</sub> are the true positives predicted for facet *d*
  + TN<sub>d</sub> are the true negatives predicted for facet *d*
  + FP<sub>d</sub> are the false positives predicted for facet *d*
  + FN<sub>d</sub> are the false negatives predicted for facet *d*

For example, suppose a model approves loans to 70 applicants from facet *a* of 100 and rejected the other 30. 10 should not have been offered the loan (FP<sub>a</sub>) and 60 were approved that should have been (TP<sub>a</sub>). 20 of the rejections should have been approved (FN<sub>a</sub>) and 10 were correctly rejected (TN<sub>a</sub>). The accuracy for facet *a* is as follows:

        ACC<sub>a</sub> = (60 \+ 10)/(60 \+ 10 \+ 20 \+ 10) = 0.7

Next, suppose a model approves loans to 50 applicants from facet *d* of 100 and rejected the other 50. 10 should not have been offered the loan (FP<sub>a</sub>) and 40 were approved that should have been (TP<sub>a</sub>). 40 of the rejections should have been approved (FN<sub>a</sub>) and 10 were correctly rejected (TN<sub>a</sub>). The accuracy for facet *a* is determined as follows:

        ACC<sub>d</sub>= (40 \+ 10)/(40 \+ 10 \+ 40 \+ 10) = 0.5

The accuracy difference is thus AD = ACC<sub>a</sub> - ACC<sub>d</sub> = 0.7 - 0.5 = 0.2. This indicates there is a bias against facet *d* as the metric is positive.

The range of values for AD for binary and multicategory facet labels is [-1, \+1].
+ Positive values occur when the prediction accuracy for facet *a* is greater than that for facet *d*. It means that facet *d* suffers more from some combination of false positives (Type I errors) or false negatives (Type II errors). This means there is a potential bias against the disfavored facet *d*.
+ Values near zero occur when the prediction accuracy for facet *a* is similar to that for facet *d*.
+ Negative values occur when the prediction accuracy for facet *d* is greater than that for facet *a* t. It means that facet *a* suffers more from some combination of false positives (Type I errors) or false negatives (Type II errors). This means the is a bias against the favored facet *a*.
