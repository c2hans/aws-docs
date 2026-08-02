---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/global.html
---

# Global interpretability
<a name="global"></a>

Understanding how features contribute to a model's output overall provides general insight that is useful for feature selection and model development. To measure the effect of adding a new feature, you typically run cross-validation with and without the feature. However, running a cross-validation for all feature combinations and all model types under consideration is often infeasible due to the computational cost. Other methods for determining feature importance are therefore useful for making quick decisions. Our recommendation for determining global feature attributions is to aggregate the local feature attribution scores recommended in the [previous section](local.md) across all data. We also recommend computing the change in the cross-validation score when a feature is removed, if time and computational constraints allow it. The following example illustrates the aggregation of local attribution scores. It  averages the magnitudes of the SHAP values for the iris classification model (from the [overview](overview.md)) and plots them as a heatmap.  You can see that the sepal measurements don't play a strong role in the model for determining the iris class.

![Heatmap for the iris classification model with SHAP values](http://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/images/guide-img/06158d60-43d0-4890-98e0-af89411cf496/images/24723139-824b-4244-8fd3-b1ee28051302.png)

For a specified model output, the collection of SHAP values across the evaluation instances can be visualized in a beeswarm plot, as illustrated in the following diagram (for a subset of data from the iris dataset [[4](resources.md)]).  Here you can see that the petal\_width attribute has the largest effect on the model output for the class Iris-versicolor, and that a high petal\_width value contributes negatively to the class prediction.  When more than one data point has the same or very similar feature attribution value, the dots are stacked to indicate the larger prevalence at that location.

![Beeswarm plot visualization for the iris classification model with SHAP values](http://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/images/guide-img/06158d60-43d0-4890-98e0-af89411cf496/images/93ee6068-32fe-4017-9a0d-3767a30bb893.png)
