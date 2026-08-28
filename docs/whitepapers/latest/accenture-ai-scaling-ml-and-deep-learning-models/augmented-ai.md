---
source_url: https://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/augmented-ai.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Augmented AI
<a name="augmented-ai"></a>

 While you have multiple continually running automated ML pipelines that save the final batch predictions and insights in a curated zone, it is essential to insert human supervision and guidance in the automated AI/ML workflows. Humans can provide the necessary critical quality assurances before pushing sensitive models into production to help the models learn better. Use [Amazon Augmented AI](https://aws.amazon.com/augmented-ai/) (A2I) along with [SageMaker AI Ground Truth](https://aws.amazon.com/sagemaker/data-labeling/) to bring together ML and humans, to provide automation while continuously improving your models.

 With [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), A2I, Ground Truth, [Amazon CloudFront](https://aws.amazon.com/cloudfront/), and [Amazon Cognito](https://aws.amazon.com/cognito/), you have a fully functional web application validation system that lets your functional domain experts and technical leads validate samples of model predictions, which in turn helps quickly optimize and fine-tune your predictive models.

## Human-in-the-loop workflows
<a name="human-in-the-loop-workflows"></a>

 In the workforce productivity use cases, one important business requirement is an unbiased, efficient, and effective model for assessing a person’s current skills based on CV, professional profile, so on. While you can use custom entity recognition and customize BERT layers (not just the classifier top layers) for roles, skills, titles, and so on, it is essential to integrate human oversight in the entire workflow involving many models in the pipeline (custom models, [Amazon Textract](https://aws.amazon.com/textract/), [Amazon Comprehend](https://aws.amazon.com/comprehend/), fine-tuned BERT) and decision-making process, so that your models learn better.

 It is important to know how to make this workflow function well, as it will impact the business outcomes if an appropriate automated workflow is not put in place to fix low-confidence predictions and improve the models. For example, in the industry use case, there has been a regular need to parse a document with a person’s work history and professional skills, which can be in virtually any format and predicting skill proficiency scores.

 Using Amazon Textract (which offers AI powered extraction of text and structured data from documents) and a series of models in an inference pipeline, AWS was able to provide the recommended insights. This also allowed AWS to integrate human judgement into the workflow wherever needed with A2I, to help the models learn better and improve over time.

 A front-end web application integrated with augmented AI instills confidence in the predictions and recommendations being made by the models. This is especially important in creating and maintaining a matured, productionized, enterprise AI system such as the ones in our use case. The Ground Truth labels that were acquired using A2I and human-in-the-loop workflow are actively used with SageMaker AI Model Monitor to continuously evaluate concept drift. For all other drifts in model bias, feature importance, and explainability, use Model Monitor to compare against the baseline provided to each SageMaker AI deployed endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
