---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/local.html
---

# Local interpretability
<a name="local"></a>

The most popular methods for local interpretability of complex models are based on either Shapley Additive Explanations (SHAP) [[8](resources.md)] or integrated gradients [[11](resources.md)]. Each method has a number of variants that are specific to a model type. To interpret individual model predictions, we recommend the tree SHAP and Kernel SHAP methods.

## For tree ensemble models, use tree SHAP
<a name="tree-shap"></a>

In the case of tree-based models, dynamic programming allows for fast and exact computation of the [Shapley values](https://en.wikipedia.org/wiki/Shapley_value) for each feature, and this is the recommended approach for local interpretations in tree ensemble models. (See [[7](resources.md)], implementation is at [https://github.com/slundberg/shap](https://github.com/slundberg/shap).)

## For neural networks and differentiable models, use integrated gradients and conductance
<a name="ig"></a>

Integrated gradients provide a straightforward way to compute feature attributions in neural networks. Conductance builds on integrated gradients to help you interpret attributions from portions of neural networks such as layers and individual neurons. (See [[3](resources.md),[11](resources.md)], implementation is at [https://captum.ai/](https://captum.ai/).) You cannot use these methods on models without using a gradient; in such cases, you can use Kernel SHAP (discussed in the next section) instead. When the gradient is available, integrated gradient attributions can be computed more quickly than attributions from Kernel SHAP. A challenge to using integrated gradients is choosing the best base point for deriving an interpretation. For example, if the base point for an image model is the image of zero intensity in all the pixels, important regions of an image that are darker might not have attributions that align with human intuition. One approach to address this problem is to use multiple base point attributions and add them together. This is part of the approach taken in the XRAI feature attribution method for images [[5](resources.md)], where the integrated gradient attributions that use a black reference image and a white reference image are added together to produce more consistent attributions.

## For all other cases, use Kernel SHAP
<a name="kernel-shap"></a>

You can use Kernel SHAP to compute feature attributions for any model, but it is an approximation to computing the full Shapley values and remains computationally expensive (see [[8](resources.md)]). The computational resources required for Kernel SHAP grow quickly with the number of features. This requires approximation methods that can reduce the fidelity, repeatability, and robustness of explanations. Amazon Sagemaker Clarify provides convenience methods that deploy prebuilt containers for computing Kernal SHAP values in separate instances. (For an example, see the GitHub repository [Fairness and Explainability with SageMaker Clarify](https://github.com/aws/amazon-sagemaker-examples/blob/35e2faf7d1cc48ccedf0b2ede1da9987a18727a5/sagemaker_processing/fairness_and_explainability/fairness_and_explainability.ipynb).)

For single tree models, the split variables and leaf values provide an immediately explainable model, and the methods discussed previously do not provide additional insight.  Similarly, for linear models, the coefficients provide a clear explanation of model behavior. (SHAP and integrated gradient methods both return contributions that are determined by the coefficients.)

Both SHAP and integrated gradient-based methods have weaknesses.  SHAP requires attributions to be derived from a weighted average of all feature combinations.  Attributions obtained in this way can be misleading when estimating feature importance if there is a strong interaction between features.  Methods that are based on integrated gradients can be difficult to interpret because of the large number of dimensions that are present in large neural networks, and these methods are sensitive to the choice of a base point.  More generally, models can use features in unexpected ways to achieve a certain level of performance and these can vary with the model—feature importance is always model dependent.

## Recommended visualizations
<a name="visualize"></a>

The following chart presents several recommended ways to visualize the local interpretations that were discussed in the previous sections.  For tabular data we advise a simple bar graph that shows the attributions, so they can be easily compared and used to infer how the model is making predictions.

![Visualizing local interpretations by using a bar graph](http://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/images/guide-img/06158d60-43d0-4890-98e0-af89411cf496/images/2044d25c-a1dc-4a2d-a99c-1d29d539ff06.png)

For text data, embedding tokens leads to a large number of scalar inputs.  The methods recommended in the previous sections produce an attribution for each dimension of the embedding and for each output.  In order to distill this information into a visualization, the attributions for a given token can be summed. The following example shows the sum of the attributions for the BERT-based question answering model that was trained on the SQUAD dataset.  In this case, the predicted and true label is the token for the word "france."

![Sum of attributions for a BERT-based question answering model that was trained on the SQUAD dataset, example 1](http://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/images/guide-img/06158d60-43d0-4890-98e0-af89411cf496/images/9e550fd8-4e6a-4e28-8139-c547a35b7800.png)

Otherwise, the vector norm of the token attributions can be assigned as a total attribution value, as shown in the following example.

![Sum of attributions for a BERT-based question answering model that was trained on the SQUAD dataset, example 2](http://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/images/guide-img/06158d60-43d0-4890-98e0-af89411cf496/images/e36ceefa-38cd-4f2a-8f90-2585e89fd9ed.png)

For intermediate layers in deep learning models, similar aggregations can be applied to conductances for visualization, as shown in the following example. This vector norm of the token conductance for transformer layers shows the eventual activation for the end token prediction ("france").

![For intermediate layers in deep learning models, how aggregations can be applied to conductances for visualization](http://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/images/guide-img/06158d60-43d0-4890-98e0-af89411cf496/images/9854a8ec-d66c-417c-ab0b-bc6e5bd1807a.png)

*Concept activation vectors *provide a method for studying deep neural networks in more detail [[6](resources.md)]. This method extracts features from a layer in an already trained network and trains a linear classifier on those features to make inferences about the information in the layer. For example, you might want to determine which layer of a BERT-based language model contains the most information about the parts of speech. In this case, you could train a linear part-of-speech model on each layer output and make a rough estimate that the best performing classifier is associated with the layer that has the most part-of-speech information. Although we do not recommend this as a primary method for interpreting neural networks, it can be an option for more detailed study and aid in the design of network architecture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
