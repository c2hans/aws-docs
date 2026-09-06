---
source_url: https://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/monitoring-for-performance-and-bias.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Monitoring for performance and bias
<a name="monitoring-for-performance-and-bias"></a>

![A diagram that shows bias detection with SageMaker AI Clarify and nearly continuous monitoring with SageMaker AI Model Monitor .](http://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/images/bias-detection.png)

DL models can be heavily impacted by data bias. Model and data bias detection and rectification should be constant underlying themes in an Enterprise AI system. You can use [SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/) extensively to perform evaluation for detecting data bias, during featuring engineering for evaluating feature importance, for assessing model bias during training/hyper-parameter tuning and finally with [SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/) to take actions on live models.

 An important need is to generate reports throughout all these stages to maintain transparency of the process. Using SageMaker AI Data Wrangler along with SageMaker AI Clarify, you can generate reports that explain the features that are considered important, the choices made by the model, and the reasoning behind the predictions.

 Data drift, covariate, label drifts, and concept shift mandate nearly continuous monitoring and updates to models. Nearly continuous monitoring of model insights, measuring them, and testing their production effectiveness are critical steps to achieve a successful Enterprise AI. Baseline metrics first need to be calculated during model training and thresholds should be set for Kullback–Leibler (KL), Kolmogorov-Smirnov (KS), and Linear Programming (LP) Key Performance Indicators (KPIs).

 SageMaker AI Model Monitor detects drift on live model output which can be integrated with SageMaker AI Clarify for various detections and takes corrective actions, such as re-training models, introducing new production variants, and retiring older non-performing models.

 Because our focus is always on the end-state, the models and all supporting infrastructure and data feeds that are employed to solve a problem need to have a measurable characteristic tied to business outcomes.

## Post-training bias metrics
<a name="post-training-bias-metrics"></a>

 The [following metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-post-training-bias.html) are helpful for detecting and explaining our model predictions:
+  Proportions in Predicted Labels (DPPL)
+  Disparate Impact (DI)
+  Difference in Conditional Acceptance (DCAcc)
+  Difference in Conditional Rejection (DCR)

 For all post-training data and model bias metrics, you can use SageMaker AI Clarify. Taking the trained model, you choose the feature to analyze for bias and determine the conditional rejection (DCR) and other metrics listed previously. Because SageMaker AI Clarify supports [SHAP](https://shap.readthedocs.io/en/latest/index.html), you can determine the contribution of each feature to the model prediction. This helps in performing feature attribution and generating the model explainability report with SageMaker AI Clarify. This provides you with all the information you need for detecting drifts in feature attribution and model explainability on live model endpoints – a key business goal in ensuring you have responsible AI baked in into all your solutions.

## Monitoring performance
<a name="monitoring-performance"></a>

### Data quality monitoring
<a name="data-quality-monitoring"></a>

 Earlier, this whitepaper described a process of creating data-quality baseline using Deequ, which helps detect drift in the statistical characteristics of input data being sent to the live model. If this step is not accurately performed in the ML and DL pipelines, the rest of the components downstream are deeply impacted, resulting in incorrect or sub-optimal results.

## Dealing with drifts
<a name="dealing-with-drifts"></a>

 Models are bound to drift; it is only a matter of time. It can be gradual or rapid, based on the circumstances. There are various types of drifts to deal with once your models are in production.
+  **Feature drift, Label drift and Concept drift**, which can be handled by either revisiting feature engineering, model re-training, or training on new data.
+  **Prediction drift and Feedback drift**, which require more involved approach of new versions of the models as otherwise it may impact the business objectives.

 Regardless of the types and causes of drifts, it is vital to monitor model metrics associated with training for passive retraining, and the model attribution data for active retraining. Monitoring these shifts in model efficacy can help with early intervention (Model Monitor), explainable analytics reports (SageMaker AI Clarify), and the ability to resolve the issue in a way that will not cause disruption to the project.
