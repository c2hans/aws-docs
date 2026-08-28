---
source_url: https://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/the-algorithms.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# The algorithms
<a name="the-algorithms"></a>

 There are three key pillars to building successful ML applications. If not done correctly, in spite of all the state-of-the-art continuous integration/continuous delivery (CI/CD), feature store, feature engineering, and graphics processing unit (GPU)-accelerated DL or automated pipelines, the end-to-end Enterprise AI platform is bound to fail:
+  The quality of the data
+  The minimum level of complexity employed to solve the problem
+  The ability of the solution to be measured and monitored

## Data engineering and data quality
<a name="data-engineering-and-data-quality"></a>

 The talent and skilling industry use case requires over 20 data sources to be ingested from. One of the main challenges is to fix data quality before feeding the raw datasets into your DL models for classification and recommendation. Data quality issues can deeply impact not just the data engineering pipelines, but all the ML pipelines downstream as well. [Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/) helps in analyzing the datasets across all the stages of feature engineering, training and deployment. The [training-serving skew](https://www.qwak.com/post/training-serving-skew-in-machine-learning) is aptly shown by Deequ, by detecting deviation from baseline statistics. Deequ can create schema constraints and statistics for each input feature. Completeness, Correlation, Uniqueness and Compliance Deequ metrics can be tracked in the `MetricsRepository`, and Spark processing alerts can be set on detecting anomalies for immediate actions.

## Hyper-parameter tuning (HPT)
<a name="hyper-parameter-tuning-hpt"></a>

 As hyper-parameters control how the ML algorithm learns the model parameters during training, it’s important to define optimization metrics and create [SageMaker AI Hyper Parameter Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html) jobs to converge on the best combination of hyper-parameters. Based on ML build experience, AWS recommends using [Bayesian hyper-parameter optimization](https://towardsdatascience.com/a-conceptual-explanation-of-bayesian-model-based-hyperparameter-optimization-for-machine-learning-b8172278050f) strategy over manual, random, or grid search, as it usually yields better results using fewer computer resources.

 For the talent and skilling industry use cases defined earlier, the DL models need to classify millions of jobs and skills to predict a good match and user learning sequence. The following details are some of the things that we found useful and were key in our thought leadership for creating AI solutions. We define the objective metric that the HPT job will try to optimize, which is validation accuracy for the talent and skilling use cases. The following is an example code snippet for the metrics definition:

```
objective_metric_name = "validation:accuracy"

metrics_definitions = [
    {"Name": "train:loss", "Regex": "loss: ([0-9\\.]+)"},
    {"Name": "train:accuracy", "Regex": "accuracy: ([0-9\\.]+)"},
    {"Name": "validation:loss", "Regex": "val_loss: ([0-9\\.]+)"},
    {"Name": "validation:accuracy", "Regex": "val_accuracy: ([0-9\\.]+)"},
]
```

 Next, we set the `HyperparameterTuner` with `estimator` and `Hyperparameter` ranges.

 A crucial setting is the early\_stopping\_type, which you set so that SageMaker AI can stop the tuning job when it starts to [overfit](https://en.wikipedia.org/wiki/Overfitting), and can help save cost of the overall tuning job. Inaccurate hyperparameter tuning can not only result in excessive costs, but also an ineffective model even after hours of training.

```
objective_metric_name = "validation:accuracy"

tuner = HyperparameterTuner(
    estimator=estimator,
    objective_type="Maximize",
    objective_metric_name=objective_metric_name,
    hyperparameter_ranges=hyperparameter_ranges,
    metric_definitions=metrics_definitions,
    max_jobs=2,
    max_parallel_jobs=10,
    strategy="Bayesian",
    early_stopping_type="Auto",
)
```

 Combining all of this together, you have the following build and training process taking BERT as an example. Other DL models built with PyTorch, MXNet, or TensorFlow follow the same process. It is essential to get the following three stages (within the box under MACHINE LEARNING ENGINEERING) correct to move on to productionizing the system with large scale model deployments.

![A diagram that shows the complete ML engineering process and fine-tuning deep learning models .](http://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/images/ml-engineering-process.png)

## Model registry
<a name="model-registry"></a>

 It is important to catalog models to explain the model predictions and insights. It is also important that all models promoted to production are cataloged, all model versions managed, metadata such as training metrics are associated with a model, and the approval status of a model is managed. This is especially needed when organizations want to move from ad-hoc one-off proof-of-concepts to embedding AI in their enterprise systems with multiple teams, doing daily DL experiments. This is implemented in the solution using SageMaker AI Model Registry.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
