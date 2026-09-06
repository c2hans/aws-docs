---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mlops-checklist/training.html
---

# 8. Continuous training
<a name="training"></a>

Continuous training means that the ML system automatically and continuously retrains machine learning models to adapt to changes in the data before it is redeployed. Possible triggers for rebuilding include data changes, model changes, or code changes.

|  |
| --- |
| 8.1 Checks: model input validation | Checks are in place to verify a model's input doesn't deviate from a certain standard. Input validation means running functional testing during model promotion. It also means having immediate verification of input requests, such as using assertions and enumerated types. |
| --- |--- |
| **8.2 Retrain triggering: scheduled jobs** | This is the most basic form of training automation. Model retraining is set on a schedule (for example, every week). In this scenario, automation is likely low, with a manual review and spot check on the results before model promotion. |
| **8.3 Retrain triggering: new training data** | Retraining is initiated by an incoming data threshold. The model can retrain from scratch or run updates incrementally. Given a specified amount of data in place, a training job kicks off. |
| **8.4 Retrain triggering: model performance degradation** | This technique uses monitoring and observability to run model retraining, and it requires a mature level of automation. For example, accuracy lowers from a given range, which acts as a trigger for retraining a model on all or part of the data. |
| **8.5 Retrain triggering: data distribution shift** | Monitoring data distribution shift provides a way set triggers to retrain the model when its underlying data changes. A violation set on [concept shift or data distribution shift](https://aws.amazon.com/blogs/machine-learning/detect-nlp-data-drift-using-custom-amazon-sagemaker-model-monitor/) initiates a model retraining job. |
