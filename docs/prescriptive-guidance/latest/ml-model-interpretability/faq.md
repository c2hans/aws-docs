---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/faq.html
---

# FAQ
<a name="faq"></a>

Q. There are many methods for determining feature importance that are not discussed here. Why are they not mentioned?

A. This guide focuses on what we believe to be the most effective and direct methods for model interpretability. Other methods have advantages in speed and ease of computation, and might be appropriate depending on the model.  The guidance in this article is prescriptive, not proscriptive.

Q. What are the weakness of the recommended methods?

A. SHAP requires attributions that are derived from a weighted average of all feature combinations.  Attributions that are obtained this way can be misleading in estimating feature importance when there are strong interactions among features.  Methods that are based on integrated gradients can be difficult to interpret because of the large number of dimensions that are present in large neural networks.  Models can use features in unexpected ways to achieve a certain level of performance and these can vary with the model, so feature importance is always model dependent.
