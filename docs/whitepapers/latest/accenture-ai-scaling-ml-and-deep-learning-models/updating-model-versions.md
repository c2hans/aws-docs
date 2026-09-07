---
source_url: https://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/updating-model-versions.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Updating model versions
<a name="updating-model-versions"></a>

 Post-deployment of our models, it is important to track business metrics that we are aiming to optimize. The business metrics are usually tied to revenue generation, sales, number of user clicks, purchases, or as in cases found in this whitepaper, on the efficacy of the workforce productivity recommendations or sales forecast shown to C-suite users. In this solution, AWS recommends storing the business metrics in [Amazon DynamoDB.](https://aws.amazon.com/dynamodb/)

 When new versions of the models are available, it is important to see which variant performs better before routing all traffic to the new model. Models tested during the engineering process and the same models running “in the wild” may produce different results, and you don’t want to switch your use base to the new models without first testing them sufficiently with live, unseen, real traffic. Use [Canary testing](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.canary-deployment.en.html), [A/B testing](https://en.wikipedia.org/wiki/A/B_testing), and [Multi-Armed Bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) (MAB) strategies in a champion-challenger framework, to choose the best new model among the various SageMaker AI hosted production variants.

![A diagram that shows deploying production variants and continuous MLOps in production.](https://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/images/production-variants.png)
