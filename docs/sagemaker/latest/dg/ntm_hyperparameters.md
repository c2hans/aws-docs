---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/ntm_hyperparameters.html
---

# NTM Hyperparameters
<a name="ntm_hyperparameters"></a>

The following table lists the hyperparameters that you can set for the Amazon SageMaker AI Neural Topic Model (NTM) algorithm.

| Parameter Name | Description |
| --- | --- |
| `feature_dim` | The vocabulary size of the dataset.<br />**Required**<br />Valid values: Positive integer (min: 1, max: 1,000,000) |
| num\_topics | The number of required topics.<br />**Required**<br />Valid values: Positive integer (min: 2, max: 1000) |
| batch\_norm | Whether to use batch normalization during training.<br />**Optional**<br />Valid values: *true* or *false*<br />Default value: *false* |
| clip\_gradient | The maximum magnitude for each gradient component.<br />**Optional**<br />Valid values: Float (min: 1e-3)<br />Default value: Infinity |
| encoder\_layers | The number of layers in the encoder and the output size of each layer. When set to *auto*, the algorithm uses two layers of sizes 3 x `num_topics` and 2 x `num_topics` respectively. <br />**Optional**<br />Valid values: Comma-separated list of positive integers or *auto*<br />Default value: *auto* |
| encoder\_layers\_activation | The activation function to use in the encoder layers.<br />**Optional**<br />Valid values: [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/ntm_hyperparameters.html)<br />Default value: `sigmoid` |
| epochs | The maximum number of passes over the training data.<br />**Optional**<br />Valid values: Positive integer (min: 1)<br />Default value: 50 |
| learning\_rate | The learning rate for the optimizer.<br />**Optional**<br />Valid values: Float (min: 1e-6, max: 1.0)<br />Default value: 0.001 |
| mini\_batch\_size | The number of examples in each mini batch.<br />**Optional**<br />Valid values: Positive integer (min: 1, max: 10000)<br />Default value: 256 |
| num\_patience\_epochs | The number of successive epochs over which early stopping criterion is evaluated. Early stopping is triggered when the change in the loss function drops below the specified `tolerance` within the last `num_patience_epochs` number of epochs. To disable early stopping, set `num_patience_epochs` to a value larger than `epochs`.<br />**Optional**<br />Valid values: Positive integer (min: 1)<br />Default value: 3 |
| optimizer | The optimizer to use for training.<br />**Optional**<br />Valid values:[See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/ntm_hyperparameters.html)<br />Default value: `adadelta` |
| rescale\_gradient | The rescale factor for gradient.<br />**Optional**<br />Valid values: float (min: 1e-3, max: 1.0)<br />Default value: 1.0 |
| sub\_sample | The fraction of the training data to sample for training per epoch.<br />**Optional**<br />Valid values: Float (min: 0.0, max: 1.0)<br />Default value: 1.0 |
| tolerance | The maximum relative change in the loss function. Early stopping is triggered when change in the loss function drops below this value within the last `num_patience_epochs` number of epochs.<br />**Optional**<br />Valid values: Float (min: 1e-6, max: 0.1)<br />Default value: 0.001 |
| weight\_decay |  The weight decay coefficient. Adds L2 regularization.<br />**Optional**<br />Valid values: Float (min: 0.0, max: 1.0)<br />Default value: 0.0 |
