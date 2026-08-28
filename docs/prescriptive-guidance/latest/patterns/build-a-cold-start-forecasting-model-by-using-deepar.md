---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-cold-start-forecasting-model-by-using-deepar.html
---

# Build a cold start forecasting model by using DeepAR for time series in Amazon SageMaker AI Studio Lab
<a name="build-a-cold-start-forecasting-model-by-using-deepar"></a>

*Ivan Cui and Eyal Shacham, Amazon Web Services*

## Summary
<a name="build-a-cold-start-forecasting-model-by-using-deepar-summary"></a>

Whether you’re allocating resources more efficiently for web traffic, forecasting patient demand for staffing needs, or anticipating sales of a company’s products, forecasting is an essential tool. Cold start forecasting builds forecasts for a time series that has little historical data, such as a new product that just entered the retail market. This pattern uses the Amazon SageMaker AI DeepAR forecasting algorithm to train a cold start forecasting model and demonstrates how to perform forecasting on cold start items.

[DeepAR](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar.html) is a supervised learning algorithm for forecasting scalar (one-dimensional) time series using recurrent neural networks (RNN). DeepAR takes the approach of training a single model jointly over all of the time series of related products’ time series.

Traditional time series forecasting methods such as autoregressive integrated moving average (ARIMA) or exponential smoothing (ETS) rely heavily on historical time series of each individual product. Therefore, those methods aren’t effective for cold start forecasting. When your dataset contains hundreds of related time series, DeepAR outperforms the standard ARIMA and ETS methods. You can also use the trained model to generate forecasts for new time series that are similar to the time series that it has been trained on.

## Prerequisites and limitations
<a name="build-a-cold-start-forecasting-model-by-using-deepar-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An Amazon SageMaker AI [domain.](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html)
+ An [Amazon SageMaker AI Studio Lab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab.html) or Jupiter lab application.
+ An Amazon Simple Storage Service (Amazon S3) bucket with read and write permissions.
+ Knowledge of programming in Python.
+ Knowledge of using a Jupyter notebook.

**Limitations**
+ Invoking the forecast model without any historical data points will return an error. Invoking the model with minimal historical data points will return inaccurate predictions with high confidence. This pattern suggests an approach to resolving these known limitations of cold start forecasting.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ Python version 3.10 or later.
+ The pattern’s notebook was tested in Amazon SageMaker AI Studio on an ml.t3.medium instance with the Python 3 (Data Science) kernel.

## Architecture
<a name="build-a-cold-start-forecasting-model-by-using-deepar-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Workflow to build a cold start forecasting model using SageMaker and Amazon S3.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/98d021d3-96d2-40a9-b0ce-717934652173/images/d97d66a0-8eef-4d30-ac5f-4c6c79cf6c9f.png)

The workflow performs the following tasks:

1. Input files of training and testing data are synthesized and then uploaded to an Amazon S3 bucket. This data includes multiple time series with categorical and dynamic features, along with target values (to be predicted). The Jupyter notebook visualizes the data to better understand the requirements of the training data and the expected predicted values.

1. A hyperparameters tuner job is created to train the model and find the best model based on predefined metrics.

1. The input files are downloaded from the Amazon S3 bucket to each instance of the hyperparameters tuning jobs.

1. After the tuner job selects the best model based on the tuner’s predefined threshold, the model is deployed as a SageMaker AI endpoint.

1. The deployed model is then ready to be invoked where its predictions are validated against the test data.

The notebook demonstrates how well the model predicts the target values when an adequate number of historical data points are available. However, when we invoke the model with fewer historical data points (which represent a cold product), the model’s predictions do not match the original testing data even within the model’s confidence levels. In the pattern, a new model is built for cold products where its initial context length (predicted points) is defined as the amount of available historical points, and a new model is trained iteratively as new data points are acquired. The notebook shows that the model will have accurate predictions as long as the amount of historical data points is close to its context length.

## Tools
<a name="build-a-cold-start-forecasting-model-by-using-deepar-tools"></a>

**AWS services**
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/?id=docs_gateway) is a managed machine learning (ML) service that helps you build and train ML models and then deploy them into a production-ready hosted environment.
+ [Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html) is a web-based, integrated development environment (IDE) for ML that lets you build, train, debug, deploy, and monitor your ML models.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [DeepAR-ColdProduct-Pattern](https://github.com/aws-samples/DeepAR-ColdProduct-Pattern) repository.

## Best practices
<a name="build-a-cold-start-forecasting-model-by-using-deepar-best-practices"></a>
+ Train your model in a virtual environment, and always use version control for the highest reproducibility effort.
+ Include as many high-quality categorical features as you can to get the highest predictive model.
+ Make sure that the metadata contains similar categorical items in order for the model to infer cold start products predictions adequately.
+ Run a hyperparameter tuning job to get the highest predictive model.
+ In this pattern, the model you build has a context length of 24 hours, which means that it will predict the next 24 hours. If you try to predict the next 24 hours when you have less than 24 hours of data historically, the model’s prediction accuracy degrades linearly based on the amount of historical data points. To mitigate this issue, create a new model for each set of historical data points until this number reaches the desired prediction (context) length. For example, start with a context length model of 2 hours, then increase the model progressively to 4 hours, 8 hours, 16 hours, and 24 hours.

## Epics
<a name="build-a-cold-start-forecasting-model-by-using-deepar-epics"></a>

### Start your SageMaker AI Studio Classic application
<a name="start-your-sm-studio-classic-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start your notebook environment. | 1. Sign in to the AWS Management Console, and open the SageMaker AI Studio home page. Then choose **Open Studio**.<br />2. In the left navigation pane, choose the **Studio Classic** icon in **Applications**. Then, choose the **Open** button on the **Application** list.For more information, see [Launch Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html) in the SageMaker AI documentation. | Data scientist |

### Create and activate the notebook
<a name="create-and-activate-the-notebook"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up your virtual environment for model training. | To set up your virtual environment for model training, do the following:1. Download the `deepar_synthetic.ipynb` notebook from this pattern’s GitHub [repository](https://github.com/aws-samples/DeepAR-ColdProduct-Pattern) to your local machine.<br />2. In Amazon SageMaker AI Studio Classic, choose the **Upload Files** icon from the **Studio Classic** menu bar and select the downloaded notebook.<br />3. Choose the notebook in the **File Browser** in the left navigation pane. Follow the prompts to set up a notebook environment. Select the Data Science 3.0 Image and Python 3 Kernel.<br />For more information, see [Upload Files to SageMaker AI Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-files.html) in the SageMaker AI documentation. | Data scientist |
| Create and validate a forecasting model. | + Follow the instructions in the notebook to create the training and testing data, train the model, and then invoke the model.<br />+ Observe how accurate the model’s predictions are when it’s provided with adequate historical data points. | Data scientist |

## Related resources
<a name="build-a-cold-start-forecasting-model-by-using-deepar-resources"></a>
+ [DeepAR Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar_hyperparameters.html)
+ [Forecasting demand for new product introductions by using AWS machine learning services](https://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-new-product/introduction.html)
+ [Launch Amazon SageMaker AI Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html)
+ [Use the SageMaker AI DeepAR forecasting algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
