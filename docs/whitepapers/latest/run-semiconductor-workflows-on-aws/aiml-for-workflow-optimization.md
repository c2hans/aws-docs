---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/aiml-for-workflow-optimization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AI/ML for workflow optimization
<a name="aiml-for-workflow-optimization"></a>

 Using AWS artificial intelligence/machine learning (AI/ML) services, you can easily train models and do real-time inference in the cloud or on-premises. In the semiconductor industry, an example is optimizing job queues and license usage. The following figure shows a simple workflow for optimization using AI/ML.

![This image shows the AI/ML workflow for job optimization.](http://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-ai-ml-workflow.png)

**AI/ML for workflow optimization **

 This example uses multiple data sources for model training. For example, from the login server, you can collect when users are active, what data (file system level) they are using, and any other relevant user activities. When the user submits a job to the scheduler server, you can scan the submit script and collect job and runtime configurations. These configurations include system resources requested (compute, memory, and so on), file system usage, expected job runtime, which tools will be used, and so on. You also have data coming in from the license server(s), so you know exactly which licenses were used for which job and for how long. With this data, you can build a model that predicts if the license will be fully utilized. As the model is trained over time (or historical data is used), inference is performed to alter the job runtimes to only the time needed to complete the job, thereby reducing or eliminating unused license time. This inference further results in cost savings and license optimization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
