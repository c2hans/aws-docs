---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mlops-checklist/data-management.html
---

# 1. Data-centric management
<a name="data-management"></a>

Data management is the practice of ensuring that data used in training, testing, and inference is properly managed, secured, and validated. When building models at scale, data is the primary commodity that enables high model performance.

|  |
| --- |
| 1.1 Data repository | A data repository requires the ability to track data and see its point of origination. When new data is added or removed, the data repository records those changes in point-in-time recovery. The data repository should take into account how label data is tracked and processed, and how intermediate data artifacts are tracked. |
| --- |--- |
| **1.2 Diverse data source integration** | Depending on the application, training your model might require data from many sources. Designing and maintaining a manifest that informs ML practitioners of the available data sources and how they tie together is critical to building models. |
| **1.3 Data schema validation** | To feed models data, it's important that the training data be homogeneous. Transformations or other exploratory analysis might be required for data that is stored in data lake solutions such as Amazon Simple Storage Service (Amazon S3) or in document data stores. |
| **1.4 Data versioning and lineage** | When training models that might be used in production, you must be able to reproduce results and have a reliable way to perform [ablation studies](https://arxiv.org/abs/1901.08644) to better understand the overall model performance. Tracking the state of the training data is critical to this reproducibility. Tools such as [Data Version Control (DVC)](https://github.com/iterative/dvc) can assist with this. |
| **1.5 Labeling workflow** | In cases where labeled data is not available at the project start, creating labeled data is often a necessary step. Tools such as Amazon SageMaker Ground Truth require input data to be appropriately structured, and they require a defined and tested labeling job. A workforce of either internal or external labelers must be used. Data should then be validated, using either redundant labeling or machine learning approaches to identify outliers or errors in the training dataset. |
| **1.6 Online and offline feature storage** | The ML system has a [Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.htmlc) or a centralized store for features and associated metadata so that it's possible to reuse features, or model inputs. You can create an online or an offline store. Use an online store for low-latency, real-time inference use cases. Use an offline store for training and batch inference.  |
