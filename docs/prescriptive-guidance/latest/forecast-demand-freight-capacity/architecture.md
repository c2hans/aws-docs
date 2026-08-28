---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-freight-capacity/architecture.html
---

# Architecture for forecasting freight demand
<a name="architecture"></a>

The following image shows the workflow of the solution, including data ingestion, data preparation, model building, and final output and monitoring.

![Architecture diagram of a ML model for forecasting freight demand](http://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-freight-capacity/images/guide-img/4600072e-6d1e-414c-b39d-f89e1eed9438/images/27bc898f-2a60-451b-881d-b4dff3a1873c.png)

The solution architecture includes the following main components:

1. **Data ingestion** –** **You store both organic data and external data in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

1. **Data preparation** – [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) cleans up the data and prepares it for ML model training. For more information, see [Prepare data](https://docs.aws.amazon.com/sagemaker/latest/dg/data-prep.html) in the SageMaker AI documentation.

1. **Model building: Input feature forecast** – SageMaker AI uses [Prophet](https://facebook.github.io/prophet/) to generate a time series forecast for each input feature. You examine the forecast results. If needed, you provide user inputs to overwrite the feature's forecast.

1. **Model building: Target variable forecast** –** **SageMaker AI creates a regression model for inference by using the modified input features.

1. **Model output and monitoring** – The regression model outputs the forecast results to Amazon S3. You can visualize the forecast in [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html). Analysts can monitor the forecast results and evaluate accuracy by comparing the forecast with actual demand volume.

The entire processing pipeline from data ingestion to final model output can be orchestrated to run automatically. For example, you can set it up to automatically run monthly for a monthly demand forecast. If you need forecasts for more than one product, you can run the pipeline in parallel for multiple products. For more information, see [Implement MLOps](https://docs.aws.amazon.com/sagemaker/latest/dg/mlops.html) in the SageMaker AI documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
