---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mlops-checklist/observability-model-management.html
---

# 3. Observability and model management
<a name="observability-model-management"></a>

The observability and model management section of the checklist encompasses model version control and linage tracking across the entire ML system. Model versioning helps to track and control all changes applied to a model so that you can recover a previous version when needed. Lineage tracking provides a view into model inflows and outflows. Another key benefit of lineage tracking is point-in-time recovery (PITR), which automates deployment and system recovery.

|  |
| --- |
| 3.1 Versioned model registry | In general, a model registry supports version control and lineage tracking of model components. A good registry can associate metadata with the versioned model, including the following:+ The data used<br />+ Information about the model<br />+ Evaluation metric results<br />+ Associated model code |
| --- |--- |
| **3.2 Bias, fairness, and explainability** | At a bare minimum, an ML system should have a process whereby a model's predictions are explainable to other parties. Users should be able to check results for bias by each feature. Ideally, measure data bias before inputting the data into the ML model, and record these metrics for model cards and auditing. |
| **3.3 Lineage tracking: data inputs and outputs** | Tracking is in place to follow the flow of data in and out of the system (for example, runs from the data lake to the training pipeline). This tracking acts as a record from which all system processes can be recreated, and it provides an audit trail for analysis. |
| **3.4 Lineage tracking: environment information** | This tracking captures information about the runtime environment setup, such as container images for all model code and the containers' associated dependencies. |
| **3.5 Lineage tracking: model** | This tracking captures information about the model. It includes everything from information on the model's algorithm to parameters and hyperparameters that go into the model. |
| **3.6 Integration with deployment and monitoring** | The system should be linked directly with monitoring and deployment subsystems for PITR. For monitoring, this means testing the model's performance against its training runs to detect model-quality deterioration. For deployment, this supports PITR and the ability to roll back to a previous model version as needed. |
| **3.7 Pipeline parameter configuration** | Technically, pipeline parameter configuration falls under both lineage tracking and experiment tracking because the pipeline configuration must be versioned and associated directly with a model. Pipeline parameter configuration is listed in this section because it's imperative to track all system orchestration configurations and version them. |
| **3.8 Issues are traceable, debuggable, and reproducible.** | An engineer can trace, debug, and reproduce all issues within the system without much effort. This implies that a sufficient level of observability is in place. This check is primarily derived from fulfilling the other items under the Observability and model management section. |
| **3.9 Performance visualization** | The system can capture and gather logs into a time-series database type format and ingest them directly into dashboard. The dashboard provides a holistic view of both model and computer metrics with the ability to drill down and query. |
