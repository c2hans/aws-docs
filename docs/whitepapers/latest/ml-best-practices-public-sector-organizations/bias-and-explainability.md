---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/bias-and-explainability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Bias and Explainability
<a name="bias-and-explainability"></a>

 Demonstrating explainability is a significant challenge because complex ML models are hard to understand and even harder to interpret and debug. There is an inherent tension between ML performance (predictive accuracy) and explainability; often the highest performing methods are the least explainable, and the most explainable are less accurate. Hence, public sector organizations need to invest significant time with appropriate tools, techniques, and mechanisms to demonstrate explainability and lack of bias in their ML models, which could be a deterrent to adoption.

 AWS Cloud provides the following capabilities and services to assist public sector organizations in resolving these challenges.

## Amazon SageMaker AI Debugger
<a name="amazon-sagemaker-debugger"></a>

 [Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) provides visibility into the model training process for real-time and offline analysis. In the existing training code for TensorFlow, Keras, Apache MXNet, PyTorch, and XGBoost, the new [SageMaker Debugger](https://aws.amazon.com/sagemaker/debugger) SDK can be used to save the internal model state at periodic intervals in S3. This state is composed of a number of components: The parameters being learned by the model (for example, weights and biases for neural networks), the changes applied to these parameters by the optimizer (gradients), optimization parameters, scalar values such as accuracies and losses, and outputs of each layer of a neural network.

```
SageMaker Debugger provides three built-in tensor collections called feature importance, average_shap, and full_shap, to visualize and analyze captured tensors specifically for model explanation. Feature importance is a technique that explains the features that make up the training data using a score (importance). It indicates how useful or valuable the feature is, relative to other features.

SHAP (SHapley Additive exPlanations) is an open-source technique based on coalitional game theory. It explains an ML prediction by assuming that each feature value of training data instance is a player in a game in which the prediction is the payout. Shapley values indicate how to distribute the payout fairly among the features. The values consider all possible predictions for an instance and use all possible combinations of inputs. Because of this exhaustive approach, SHAP can guarantee consistency and local accuracy. For more information, see the [SHAP website](https://shap.readthedocs.io/en/latest/index.html).
```

 SHAP values can be used for global explanatory methods to understand the model and its feature contributions in aggregate over multiple data points. SHAP values can also be used for local explanations that focus on explaining each individual prediction. See [ML Explainability with Amazon SageMaker AI Debugger](https://aws.amazon.com/blogs/machine-learning/ml-explainability-with-amazon-sagemaker-debugger/) for details.

## Amazon SageMaker AI Clarify
<a name="amazon-sagemaker-clarify"></a>

 Amazon SageMaker AI Clarify is a service that is integrated into SageMaker Studio and detects potential bias during data preparation, model training, and in deployed models, by examining specified attributes. For instance, bias in attributes related to age can be examined in the initial dataset, in the trained as well as the deployed model, and quantified in a detailed report. Clarify provides a range of metrics to measure bias such as Difference in positive proportions in labels (DPL), Difference in positive proportions in predicted labels (DPPL), Accuracy difference (AD), and Counterfactuals – Fliptest (FT). In addition, SageMaker Clarify also enables explainability by including feature importance graphs using SHAP to help explain model predictions. It produces reports and visualizations that can be used to support internal presentations on a model’s predictions. See [New – Amazon SageMaker AI Clarify Detects Bias and Increases the Transparency of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/) for details. Clarify has been designed to work without burdening the inference operations – assessment of a model can be spun off as a separate activity in SageMaker. This capability is very helpful to automate monitoring drift.

## SHAP and LIME (Local Interpretable Model-Agnostic Explanations) libraries:
<a name="shap-and-lime-local-interpretable-model-agnostic-explanations-libraries"></a>

 In case team members are unable to use Amazon SageMaker AI Debugger or Amazon SageMaker AI Clarify for explainability and bias, their libraries can directly be installed on SageMaker Jupyter instances or Studio Notebooks and incorporated into the training code See [Explaining Amazon SageMaker AI Autopilot models with SHAP](https://aws.amazon.com/blogs/machine-learning/explaining-amazon-sagemaker-autopilot-models-with-shap/) for details on using SHAP. LIME provides a model-agnostic approach for setting up explanations; LIME builds sparse linear models around each prediction to explain how the black box model works in that local vicinity. SHAP is a more cost-intensive process as it requires more compute time calculating all the probable combinations and permutations of features for explaining predictions compared to LIME.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
