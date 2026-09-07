---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/overview.html
---

# Overview
<a name="overview"></a>

There is no universally accepted definition for what an interpretable model is, or what information is adequate as an interpretation of a model. This guide focuses on the commonly used notion of *feature importance*, where an importance score for each input feature is used to interpret how it affects model outputs. This method provides insight but also requires caution.  Feature importance scores can be misleading and should be analyzed carefully, including validation with subject matter experts if possible. Specifically, we advise you not to trust feature importance scores without verification, because misinterpretations can lead to poor business decisions.

In the following illustration, the measured features of an iris are passed into a model that predicts the species of the plant, and associated feature importances (SHAP attributions) for this prediction are displayed. In this case, the petal length, petal width, and sepal length all contribute positively to the classification of *Iris virginica,* but sepal width has a negative contribution. (This information is based on the iris dataset from [[4](resources.md)].)

![Predicting an iris by using measured features and SHAP attributions](https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/images/guide-img/06158d60-43d0-4890-98e0-af89411cf496/images/3ccb4920-613c-4956-9bd0-dbb0015b8d1f.png)

Feature importance scores can be *global, *indicating that the score is valid for the model across all inputs, or *local, *indicating that the score applies to a single model output.   Local feature importance scores are often scaled and summed to produce the model output value, and thus termed *attributions*. Simple models are considered more interpretable, because the effects of the input features on model output are more easily understood. For example, in a linear regression model, the magnitudes of the coefficients provide a global feature importance score, and for a given prediction, a local feature attribution is the product of its coefficient and the feature value. In the absence of a direct local feature importance score for a prediction, you can compute an importance score from a set of baseline input features to understand how a feature contributes relative to the baseline.
