---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/data-prep.html
---

# Recommendations for choosing the right data preparation tool in SageMaker AI
<a name="data-prep"></a>

Data preparation in machine learning refers to the process of collecting, preprocessing, and organizing raw data to make it suitable for analysis and modeling. This step ensures that the data is in a format from which machine learning algorithms can effectively learn. Data preparation tasks may include handling missing values, removing outliers, scaling features, encoding categorical variables, assessing potential biases and taking steps to mitigate them, splitting data into training and testing sets, labeling, and other necessary transformations to optimize the quality and usability of the data for subsequent machine learning tasks.

## Choose a feature
<a name="data-prep-choose"></a>

There are 3 primary use cases for *data preparation* with Amazon SageMaker AI. Choose the [use case](#data-prep-choose-use-cases) that aligns with your requirements, and then refer to the corresponding [recommended feature](#data-prep-choose-recommended).

### Use cases
<a name="data-prep-choose-use-cases"></a>

The following are the primary uses cases when performing data preparation for Machine Learning.
+ **Use case 1**: For those who prefer a visual interface, SageMaker AI provides ways to explore, prepare, and engineer features for model training through a point-and-click environment.
+ **Use case 2**: For users comfortable with coding who want more flexibility and control over data preparation, SageMaker AI integrates tools into its coding environments for exploration, transformations, and feature engineering.
+ **Use case 3**: For users focused on scalable data preparation, SageMaker AI offers serverless capabilities that leverage the Hadoop/Spark ecosystem for distributed processing of big data.

### Recommended features
<a name="data-prep-choose-recommended"></a>

The following table outlines the key considerations and tradeoffs for the SageMaker AI features related to each data preparation use case for machine learning. To get started, identify the use case that aligns to your requirements and navigate to its recommended SageMaker AI feature.

| Descriptor | Use case 1 | Use case 2 | Use case 3 |
| --- | --- | --- | --- |
| SageMaker AI feature | [Data Wrangler](canvas-data-prep.md) within Amazon SageMaker Canvas | [Data preparation with SQL in Studio](sagemaker-sql-extension.md) | [Prepare data using EMR Serverless](studio-notebooks-emr-serverless.md) applications in Studio |
| Description | SageMaker Canvas is a visual low-code environment for building, training, and deploying machine learning models in SageMaker AI. Its integrated Data Wrangler tool allows users to combine, transform, and clean datasets through point-and-click interactions. | The SQL extension in Studio allows users to connect to Amazon Redshift, Snowflake, Athena, and Amazon S3 to author ad-hoc SQL queries, and preview results in JupyterLab notebooks. The output of these queries can be manipulated using Python and Pandas for additional processing, visualization, and transformation into formats usable for machine learning model development. | The integration between EMR Serverless and Amazon SageMaker Studio provides a scalable serverless environment for large-scale data preparation for machine learning using open-source frameworks such as Apache Spark and Apache Hive. Users can directly access EMR Serverless applications and data from their Studio notebooks to perform their data preparation tasks at scale. |
| Optimized for | Using a visual interface in which you can: [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/data-prep.html)Optimized for tabular data tasks such as handling missing values, encoding categorical variables, and applying data transformations. | For users whose data resides in Amazon Redshift, Snowflake, Athena, or [Amazon S3](studio-sqlexplorer-athena-s3-quickstart.md) and want to combine exploratory SQL and Python for data analysis and preparation without the need to learn Spark. | For users who prefer a serverless experience with automatic resource provisioning and termination for scaling short-running or intermittent interactive workloads revolving around Apache Spark, while taking advantage of SageMaker AI's machine learning capabilities. |
| Considerations |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/data-prep.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/data-prep.html)  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/data-prep.html)  |
| Recommended environment | [Getting started with using SageMaker Canvas](canvas-getting-started.md) | [Launch Studio](studio-updated-launch.md#studio-updated-launch-prereq) | [Launch Studio](studio-updated-launch.md#studio-updated-launch-prereq) |

### Additional options
<a name="data-prep-choose-additional"></a>

 SageMaker AI offers the following additional options for preparing your data for use in machine learning models.
+ [Data preparation using Amazon EMR](studio-notebooks-emr-cluster.md): For long-running, computationally intensive, large-scale data processing tasks, consider using Amazon EMR clusters from SageMaker Studio. Amazon EMR clusters are designed to handle massive parallelization and can scale to hundreds or thousands of nodes, making them well-suited for big data workloads that require frameworks like Apache Spark, Hadoop, Hive, and Presto. The integration of Amazon EMR with SageMaker Studio allows you to leverage the scalability and performance of Amazon EMR, while keeping your full ML experimentation, model training and deployment, centralized and managed within the SageMaker Studio environment.
+ [Prepare data using glue interactive sessions](studio-notebooks-glue.md): You can use the Apache Spark-based serverless engine from AWS Glue interactive sessions to aggregate, transform, and prepare data from multiple sources in SageMaker Studio.
+ [Identify bias in training data]() using Amazon SageMaker Clarify processing jobs: SageMaker Clarify analyzes your data and detect potential biases across multiple facets. For example, you can use Clarify API in Studio to detect if your training data contains imbalanced representations or labeling biases between groups such as gender, race, or age. Clarify can help you identify these biases before training a model to avoid propagating biases into the model's predictions.
+ [Create, store, and share features](): Amazon SageMaker Feature Store optimizes the discovery and reuse of curated features for machine learning. It provides a centralized repository to store feature data that can be searched and retrieved for model training. Storing features in a standardized format enables reuse across ML projects. The Feature Store manages the full lifecycle of features including lineage tracking, statistics, and audit trails for scalable and governed machine learning feature engineering.
+ [Label data with a human-in-the-loop](data-label.md): You can use SageMaker Ground Truth to manage the data labeling workflows of your training datasets.
+ [Use SageMaker Processing API](processing-job.md): After performing exploratory data analysis and creating your data transformations steps, you can productionize your transformation code using [SageMaker AI Processing jobs](processing-job.md) and automate your preparation workflow using [SageMaker Model Building Pipelines](pipelines.md).
