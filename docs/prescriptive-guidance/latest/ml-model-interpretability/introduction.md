---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/introduction.html
---

# Machine learning model interpretability with AWS
<a name="introduction"></a>

*Matthew Chasse, Wale Akinfaderin, Michele Donini, and Ben Fenker, Amazon Web Services*

It's easier for end-users to employ machine learning algorithms responsibly when they can understand why a model makes a specific prediction. For model developers, greater insight into how a model makes predictions can aid in feature engineering and selection.  There is no standard definition of what it means to explain a model, except that an explanation should be a prerequisite for standards such as trust, robustness, causality, informativeness, model transferability, and fair and ethical decision-making. There are some common methods for generating interpretations, but they come with different weaknesses and strengths. This is not unexpected: Typically, the heuristic or set of simplifying assumptions that you use to interpret a complex model can simultaneously be a source of inaccuracy for the interpretation.

This guide provides general guidance about model interpretability methods for machine learning practitioners. For brevity, the guide omits many details and implementation specifics, and provides references to help you investigate specific use cases in more depth.

## Targeted business outcomes
<a name="business-outcomes"></a>

In some cases, regulations such as those in the healthcare and finance industries require model interpretability as a desired business outcome.  Model interpretations also provide additional insight that both model developers and users can utilize.  Additional targeted business outcomes for employing model interpretability include the following:
+ Justify important decisions (for example, in healthcare and finance) that affect customer well-being when fairness is critical.
+ Control model inaccuracies and distortions when making business decisions.
+ Improve and expedite model development and feature engineering when model interpretations are used by data scientists.
+ Discover reasons for general model behaviors, and provide new insights about both the data and the model.

These business outcomes map directly to the four reasons for explainability that are identified in [[1](resources.md)].
