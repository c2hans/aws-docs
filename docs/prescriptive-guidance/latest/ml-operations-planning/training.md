---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-operations-planning/training.html
---

# Training
<a name="training"></a>

MLOps is concerned with the operationalization of the ML lifecycle. Therefore, it must facilitate the work of data scientists and data engineers toward creating pragmatic models that achieve business needs and work well in the long term, without incurring technical debt.

Follow the best practices in this section to help address model training challenges.

## Create a baseline model
<a name="create-a-baseline-model"></a>

When practitioners face a business problem with an ML solution, typically their first inclination is to use the state-of-the-art algorithm. This practice is risky, because it's likely that the state-of-the-art algorithm hasn't been time-tested. Moreover, the state-of-the-art algorithm is often more complex and not well understood, so it might result in only marginal improvements over simpler, alternative models. A better practice is to create a baseline model that is relatively quick to validate and deploy, and can earn the trust of the project stakeholders.

When you create a baseline, we recommend that you evaluate its metric performance whenever possible. Compare the baseline model's performance with other automated or manual systems to guarantee its success and to make sure that the model implementation or project can be delivered in the medium and long term.

The baseline model should be further validated with ML engineers to confirm that the model can deliver the non-functional requirements that have been established for the project, such as inference time, how often the data is expected to shift distribution, if the model can be easily retrained in these cases, and how it will be deployed, which will affect the cost of the solution. Get multi-disciplinary viewpoints on these questions to increase the chance that you're developing a successful and long-running model.

Data scientists might be inclined to add as many features as possible to a baseline model. Although this increases the capability of a model to predict the desired outcome, some of these features might generate only incremental metric improvements. Many features, especially those that are highly correlated, might be redundant. Adding too many features increases costs, because it requires more compute resources and tuning. Too many features also affects day-to-day operations for the model, because data drift becomes more likely or happens faster.

Consider a model in which two input features are highly correlated, but only one feature has causality. For example, a model that predicts whether a loan will default might have input features such as customer age and income, which might be highly correlated, but only income should be used to give or deny a loan.  A model that was trained on these two features might be relying on the feature that doesn't have causality, such as age, to generate the prediction output. If, after going to production, the model receives inference requests for customers older or younger than the average age included in the training set, it might start to perform poorly.

Furthermore, each individual feature could potentially experience distribution shift while in production and cause the model to behave unexpectedly. For these reasons, the more features a model has, the more fragile it is with respect to drift and staleness.

Data scientists should use correlation measures and [Shapley values](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-shapley-values.html) to gauge which features add sufficient value to the prediction and should be kept. Having such complex models increases the chance of a feedback loop, in which the model changes the environment that it was modeled for. An example is a recommendation system in which consumer behavior might change because of a model's recommendations. Feedback loops that act across models are less common. For example, consider a recommendation system that recommends movies, and another system that recommends books. If both models target the same set of consumers, they would affect each other.

For each model that you develop, consider which factors might contribute to these dynamics, so you know which metrics to monitor in production.

## Use a data-centric approach and error analysis
<a name="use-a-data-centric-approach-and-error-analysis"></a>

If you use a simple model, your ML team can focus on improving the data itself, and taking a data-centric approach instead of a model-centric approach. If your project uses unstructured data, such as images, text, audio, and other formats that can be assessed by humans (compared with structured data, which might be more difficult to map to a label efficiently), a good practice to get better model performance is to perform error analysis.

Error analysis involves evaluating a model on a validation set and checking for the most common errors. This helps identify potential groups of similar data samples that the model might be having difficulties getting right. To perform error analysis, you can list inferences that had higher prediction errors, or rank errors in which a sample from one class was predicted as being from another class, for example.

## Architect your model for fast iteration
<a name="architect-your-model-for-fast-iteration"></a>

When data scientists follow best practices, they can experiment with a new algorithm or mix and match different features easily and quickly during proof of concept or even retraining. This experimentation contributes to success in production. A good practice is to build upon the baseline model, employing slightly more complex algorithms and adding new features iteratively while monitoring performance on the training and validation set to compare actual behavior with expected behavior. This training framework can provide an optimal balance in prediction power and help keep models as simple as possible with a smaller technical debt footprint.

For fast iteration, data scientists must swap different model implementations in order to determine the best model to use for particular data. If you have a large team, a short deadline, and other project management-related logistics, fast iteration can be difficult without a method in place.

In software engineering, the [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle) is a mechanism for architecting interactions among software components. This principle states that you should be able to replace one implementation of an interface with another implementation without breaking the client application or the implementation. When you write training code for your ML system, you can employ this principle to establish boundaries and encapsulate the code, so you can replace the algorithm easily, and try out new algorithms more effectively.

For example, in the following code, you can add new experiments by just adding a new class implementation.

```
from abc import ABC, abstractmethod

from pandas import DataFrame

class ExperimentRunner(object):

    def __init__(self, *experiments):
        self.experiments = experiments

    def run(self, df: DataFrame) -> None:
        for experiment in self.experiments:
            result = experiment.run(df)
            print(f'Experiment "{experiment.name}" gave result {result}')

class Experiment(ABC):

    @abstractmethod
    def run(self, df: DataFrame) -> float:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

class Experiment1(Experiment):

    def run(self, df: DataFrame) -> float:
        print('performing experiment 1')
        return 0

    def name(self) -> str:
        return 'experiment 1'

class Experiment2(Experiment):

    def run(self, df: DataFrame) -> float:
        print('performing experiment 2')
        return 0

    def name(self) -> str:
        return 'experiment 2'

class Experiment3(Experiment):

    def run(self, df: DataFrame) -> float:
        print('performing experiment 3')
        return 0

    def name(self) -> str:
        return 'experiment 3'

if __name__ == '__main__':
    runner = ExperimentRunner(*[
        Experiment1(),
        Experiment2(),
        Experiment3()
    ])
    df = ...
    runner.run(df)
```

## Track your ML experiments
<a name="track-your-ml-experiments"></a>

When you work with a large number of experiments, it's important to gauge whether the improvements you observe are a product of implemented changes or chance. You can use [Amazon SageMaker Experiments](https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/) to easily create experiments and associate metadata with them for tracking, comparison, and evaluation.

Reducing the randomness of the model build process is useful for debugging, troubleshooting, and improving governance, because you can predict the output model inference with more certainty, given the same code and data.

It is often not possible to make a training code fully reproducible, because of random weight initialization, parallel compute synchronicity, inner GPU complexities, and similar non-deterministic factors. However, properly setting random seeds, to make sure that each training run starts from the same point and behaves similarly, significantly improves outcome predictability.

## Troubleshoot training jobs
<a name="troubleshoot-training-jobs"></a>

In some cases, it might be difficult for data scientists to fit even a very simple baseline model. In this case, they might decide that they need an algorithm that can better fit complex functions. A good test is to use the baseline of a very small part of the dataset (for example, around 10 samples) to make sure that the algorithm overfits on this sample. This helps rule out data or code issues.

Another helpful tool for debugging complex scenarios is [Amazon SageMaker Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html), which can capture issues related to algorithmic correctness and infrastructure, such as optimal compute usage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
