---
source_url: https://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/optimization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Optimization
<a name="optimization"></a>

 DL is simple in essence. In the last few years, AWS has achieved astonishing results on machine-perception problems with the help of simple parametric models trained with gradient descent (GD). Extending that, all that is needed at the core is sufficiently large parametric models trained with GD on a large dataset.

 Creating a DL algorithm or identifying the algorithm to use and fine-tune is the first step. The next step for an enterprise is to derive business value out of the algorithm. That can be achieved only when the models are appropriately industrialized, scaled, and continuously improved. Ill-performing models negatively impact a business or organization’s bottom line. In Accenture’s talent and skilling solution, there are over 50 models running in Production, making a large-scale, smooth, operationalization process a necessity.

## Optimization drivers
<a name="optimization-drivers"></a>

 DL has positioned itself as an AI revolution and is here to stay. Some of the benefits of using DL models are:
+  Reusability
+  Scalability

 Optimizing and scaling ML and DL models in production is a crucial set of tasks, and one that must be done with finesse. To maximize the benefits listed previously, a proper implementation approach must be taken.

 Following are details on how it should be implemented for the industry use cases, taking the example of a few of the models. The same approach can be used for scaling many other DL models for new problems.

## Fine-tuning and reuse of models
<a name="fine-tuning-and-reuse-of-models"></a>

 Periodically, businesses get updated training data from market intelligence data sources on new market trends. There is always a need to optimize the hyper-parameters of the TensorFlow BERT classifier layer. For such cases, where the tuning job must be run again with an updated dataset or a new version of the algorithm, warm start with `TRANSFER_LEARNING` as the start type helps reuse the previous HPT job results, but along with new hyperparameters. This speeds up converging on the best model faster.

 This is particularly important in Enterprise AI systems, as multiple teams may want to reuse the models created. Training DL models from scratch requires a lot of GPU, compute, and storage resources. Model reuse across the organization helps in reducing costs. Therefore, a useful technique for model reuse is fine-tuning. Fine-tuning methodology involves unfreezing a few of the top layers of a frozen model base for feature extraction, and then jointly training both the newly added part of the model, which is the fully connected classifier and top layers. With this, a model can be reused for a different problem, and does not have to be re-trained, saving costs for the company.

 In the following sections, you will see how you can implement and scale the model fine-tuning strategies previously discussed, while maintaining a laser focus on the business metrics we need to attain.

 `WarmStartConfig` uses one or more of the previous hyper-parameters tuning job runs called the *parent jobs,* and needs a `WarmStartType`.

```
from sagemaker.tensorflow import TensorFlow

estimator = TensorFlow(
    entry_point="tf_bert_reviews.py",
    source_dir="src",
    role=role,
    instance_count=train_instance_count,
    instance_type=train_instance_type,
    volume_size=train_volume_size,
    py_version="py37",
    framework_version="2.3.1",
    hyperparameters={
        "epochs": epochs,
        "epsilon": epsilon,
        "validation_batch_size": validation_batch_size,
        "test_batch_size": test_batch_size,
        "train_steps_per_epoch": train_steps_per_epoch,
        "validation_steps": validation_steps,
        "test_steps": test_steps,
        "use_xla": use_xla,
        "use_amp": use_amp,
        "max_seq_length": max_seq_length,
        "enable_sagemaker_debugger": enable_sagemaker_debugger,
        "enable_checkpointing": enable_checkpointing,
        "enable_tensorboard": enable_tensorboard,
        "run_validation": run_validation,
        "run_test": run_test,
        "run_sample_predictions": run_sample_predictions,
    },
    input_mode=input_mode,
    metric_definitions=metrics_definitions,
```

 Setting up `HyperparameterTuner` with `WarmStartConfig`, including new hyper-parameter ranges.

```
objective_metric_name = "train:accuracy"
tuner = HyperparameterTuner(
    estimator=estimator,
    objective_type="Maximize",
    objective_metric_name=objective_metric_name,
    hyperparameter_ranges=hyperparameter_ranges,
    metric_definitions=metrics_definitions,
    max_jobs=2,
    max_parallel_jobs=1,
    strategy="Bayesian",
    early_stopping_type="Auto",
    warm_start_config=warm_start_config,
)
```

## Scaling with distributed training
<a name="scaling-with-distributed-training"></a>

 For efficient parallel computing during distributed training, employ both [data parallelism and model parallelism](https://developer.nvidia.com/deep-learning). SageMaker AI supports distributed PyTorch. You can use the [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) library that natively supports the SageMaker AI distributed training framework for both TensorFlow and PyTorch. The SageMaker AI built-in, distributed, all-reduce communication strategy should be used to achieve data parallelism by scaling PyTorch training jobs to multiple instances in a cluster.

## Avoiding common missteps to reduce rework
<a name="avoiding-common-missteps-to-reduce-rework"></a>

 The biggest driving factor in making a successful productionized ML project that has minimal to no amount of rework is a collaborative involvement between the ML team and the business unit.

 Secondly, transforming data science prototype scripts from experimentation phase to modular performant code for production is a deeply involved task, and if not done right, will not produce a stable production system.

 Finally, the ecosystem of ML engineering and MLOps is a culmination of multiple processes and standards from within DevOps, adding in ML-specific tooling and domain-specific elements, thereby building repeatable, resilient, production-capable data science solutions on the cloud. These three tenets alone distinguish a matured AI/ML enterprise from one that has just started in the journey of using ML for deriving business value.

 For industry solutions, as mentioned in the *Workforce analytics use cases* section of this document, following are some optimizations that have proved useful to having an efficient, enterprise-grade, end-to-end, industrialized, ML solution:
+  Remove monolithic prototype scripts
+  Identify difficult-to-test code in large, tightly coupled code bases
+  Introduce effective encapsulation and abstraction techniques

 In a scaled, industrialized, production version, the full end-to-end automated data engineering and ML engineering pipeline is the product built on the data science scripts in the experimentation phase.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
