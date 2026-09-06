---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mlops-checklist/experimentation.html
---

# 2. Experimentation
<a name="experimentation"></a>

Experimentation covers experiment logging, tracking, and metrics. This translates to experiment metadata integration across the platform, in source control, and in development environments. Experimentation also includes being able to optimize model performance and accuracy through debugging.

|  |
| --- |
| 2.1 Integrated development environments | An integrated development environment (IDE) is integrated directly with the cloud. The IDE can interact with and submit commands to the larger system. Ideally, it supports the following:+ Local development<br />+ Version control integration<br />+ Debugging in place, with all logs and artifacts generated going into the version control |
| --- |--- |
| **2.2 Code version control** | To help ensure reproducibility and reusability, all code is committed into the source repository with proper version control. This includes infrastructure code, application code, model code, and even notebooks (if you opt to use them). |
| **2.3 Tracking** | An ML project requires a tool that can track and analyze machine learning experiments. This tool should log all metrics, parameters, and artifacts during a machine learning experiment run, recording all metadata into a central location. The central location will provide the ability to analyze, visualize, and audit all experiments that you run. |
| **2.4 Cross-platform integration** | Historical results for experiments and all their metadata are accessible in other parts of the system. For example, the orchestration pipelines in place can access this data, as can the monitoring tools. |
| **2.5 Debugging: accuracy and system performance** | A comprehensive model debugging framework is in place to examine runs for the following:+ Find bottlenecks<br />+ Alert about anomalies<br />+ Maximize resource utilization<br />+ Aid in analysis of experiments<br />When training is intensive, the ability to maximize throughput is crucial and makes this a necessary tool for cost optimization. |
