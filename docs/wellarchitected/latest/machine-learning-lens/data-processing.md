---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/data-processing.html
---

# Data processing
<a name="data-processing"></a>

 In ML workloads, the data (inputs and corresponding desired output) serves important functions including:
+  Defining the goal of the system: the output representation and the relationship of each output to each input, by means of the input and output pairs.
+  Training the algorithm that associates inputs to outputs.
+  Measuring the performance of the model against changes in data distribution or data drift.
+  Building a baseline dataset to capture data drift.

 As shown in Figure 6, data processing consists of data collection and data preparation. Data preparation includes data preprocessing and feature engineering. It mainly uses data wrangling for interactive data analysis and data visualization for exploratory data analysis (EDA). EDA focuses on understanding data, sanity checks, and validation of data quality.

 It is important to note that the same sequence of data processing steps that is applied to the training data needs to also be applied to the inference requests.

![Figure showing data processing components](http://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/images/data-processing-components.png)

**Topics**
+ [Data collection](data-collection.md)
+ [Data preparation](data-preparation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
