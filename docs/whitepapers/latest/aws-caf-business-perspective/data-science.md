---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-business-perspective/data-science.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data science
<a name="data-science"></a>

** Use experimentation, advanced analytics, and ML to solve complex business problems. **

 The use of artificial intelligence (AI) and ML are rapidly expanding within many industries and sectors, with [56% of organizations](https://www.mckinsey.com/business-functions/mckinsey-analytics/our-insights/global-survey-the-state-of-ai-in-2021) reporting in a 2021 McKinsey Global Survey that they have at least one use case functioning in their organization. Those organizations are using AI/ML on a broad range of objectives like enhancing products with AI for better customer experiences, creating new revenue streams through new product launches, reducing costs by identifying process optimizations, and many more.

## Start
<a name="start-6"></a>

 AI/ML technologies enable innovation by converting data at hand into tangible information that can be used to make or improve decisions.
+  Begin by [defining business problems that can be solved with AI/ML](https://aws.amazon.com/machine-learning/ml-use-cases/), and have a clear idea of the business value to be gained.
+  Establish an observable and quantiﬁable performance metric for the project.
+  [Formulate the ML question](https://aws.amazon.com/blogs/apn/building-the-business-case-for-machine-learning-in-the-real-world/) in terms of inputs, desired outputs, and the performance metric to be optimized.
+  [Evaluate whether ML is the right approach](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html). Some business problems don’t need ML and simple business rules can do a much better job. For other business problems, there might not be sufficient data to apply ML as a solution.
+  With the relevant stakeholders, brainstorm which value drivers could be improved through the use of automation or model prediction. This could be through the reduction of manual processing of data or through the consistency/improvement that an automated process would bring.
+  Find the key decision points along the process and collect an inventory of data that could be used to inform those decisions.
+  Frame the decisions and the data into the AI/ML context. Conduct a proof-of-concept study with offline data to test whether the problem can be modeled and if the required business value can be achieved. If the results are not satisfactory, reframe the problem, collect more data, or move on.
+  Workshop to see how the stakeholders will use the modeling results in their process. Maybe choose an owner from the business who will collect user requirements and give feedback.
+  Create an approach for collecting, cleansing and joining the data that comes from different data sources. Creating reliability within this [data pipeline](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/) will allow you to begin to experiment with different proof of concept approaches with minimal investment to better understand what insights your organization values and highlight areas for future focus.
+  Once you’ve identified a successful approach, build a Minimum Lovable Product (MLP) to validate the return on investment (ROI) in a real-world business scenario. The MLP can then be augmented and enhanced to create your first productionized AI/ML solution.
+  Collect feedback from the stakeholders and improve the solution. If the results are acceptable, create an approach for collecting, cleansing and joining the data that comes from different data sources.

## Advance
<a name="advance-6"></a>
+  Enable the broader organization to think in the AL/ML context. Framing an AI/ML problem is simply another competency just like mathematics or programming. Anyone from the organization can lead an initiative, but it is essential that the leader has a firm understanding of the business drivers and can formulate how the solution will be used. Data scientists and engineers can be consulted to create an initial scope and estimations.
+  Define value from a business point of view and work out the value of key metrics in financial terms; there are many value-based management approaches that can be applied. This way any improvement or automation can have a business value and a return on investment attached.
+  Once you’ve identified opportunities where data can drive value for your customers and organization, begin creating mechanisms to allow you to deliver insights programmatically throughout your organization.
+  Create the right environment for this invention of ML value to happen. Paramount to this is making data accessible within the organization in a standard way. Allow people to be able to access data relevant to their roles and get them to explore how they can automate their analysis and reporting.
+  Define your organization’s approach to [data warehousing](https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/data-warehousing-on-aws.html) to provide access to data to everyone who needs it. Utilize [data pipelines](https://aws.amazon.com/datapipeline/) and [data catalogs](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) to support the building, training, and testing of your ML models. Use [continuous integration and continuous delivery (CI/CD)](https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/) practices to improve operational resilience and reproducibility of your [ML workflows](https://aws.amazon.com/blogs/opensource/using-kedro-pipelines-to-train-amazon-sagemaker-models/).
+  Enable other groups to use the insights created by sharing information through dashboards and data visualizations. At the same time, iterate frequently while you measure the effectiveness and the route to business value. Learning from your experiments will form the basis for future approaches tailored to your organization.
+  Instrument your model and pipelines to [monitor their performance](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html), ensuring that they are behaving in production as expected. Continuous monitoring will reveal whether model outputs are matching what you expect, or whether they are drifting.
+  Build an approach to adjust or retrain your models proactively, this may require data scientists to interpret results and review changes in response data changes and retraining.
+  To help mitigate risk, delegate low confidence predictions for human review.
+  Set up a review process to evaluate how implemented projects are working. Sometimes things do not go as planned; perhaps the projects do not realize the saving, or user interaction is low. Always get feedback and use the findings to update and improve the model pipeline.

## Excel
<a name="excel-6"></a>

 As the number of ML projects grows, the need for an effective [governance strategy](https://aws.amazon.com/blogs/machine-learning/intelligent-governance-of-document-processing-pipelines-for-regulated-industries/) for data and automation becomes more pressing. This responsibility cuts across your organization, from the central infrastructure and IT teams, DevOps, data engineering, ML Ops, data stewards, and business stakeholders. Governance provides a common operational model with well-defined guardrails to allow scaling ML beyond specialists.
+  Use [multi-account patterns](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/) to organize, standardize, and expedite the provisioning of secured, governed ML environments to provide teams with flexibility in their tooling choices. Flexibility enables teams to use production data to train high-quality ML models to move fast to meet business objectives.
+  Set up a centralized, curated, and secured [repository](https://aws.amazon.com/lake-formation/) that stores all your data, both in its original form and prepared for analysis.
+  Grant fine-grained access to datasets, and audit access over time across a wide range of analytics and ML tools and services.
+  Secure access to your sensitive data using granular controls at the column, row, and cell-levels. Let your users access a centralized data catalog that describes available datasets and their appropriate usage. They can then use these datasets with their choice of analytics and ML services.
+  Set up methods to trace ML [model lineage](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html) from data preparation, model development, and training iterations, and how to audit who did what at any given point in time, across [different accounts](https://aws.amazon.com/about-aws/whats-new/2021/12/amazon-sagemaker-cross-account-lineage-tracking-query/). This includes the ability to reproduce the ML model based on model lineage and the stored artifacts.
+  Enable methods that help [explain and interpret](https://aws.amazon.com/sagemaker/clarify/) the trained model and obtain feature importance. Empower all teams and individual decision makers to create ML systems at scale. [Business users or data analysts](https://aws.amazon.com/blogs/aws/announcing-amazon-sagemaker-canvas-a-visual-no-code-machine-learning-capability-for-business-analysts/) can build prediction systems based on the data they analyze and process every day, without having to learn about hundreds of algorithms, training parameters, and evaluation metrics, and deployment details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
