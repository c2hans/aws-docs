---
source_url: https://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/feature-engineering.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Feature engineering
<a name="feature-engineering"></a>

 Many DL and ML models are used for the workforce productivity solution; however, text classification and sentence prediction are inherently the main classifiers you need. Given the superior performance of neural language models, and because it enables machines to understand qualitative information, it fits the need of building neural network-based DL models for assessing peoples’ skills proficiency, and for recommending new career pathways.

 [Bidirectional Encoder Representations from Transformers](https://en.wikipedia.org/wiki/BERT_(language_model)) (BERT) is the first Natural Language Processing (NLP) technique to rely solely on a self-attention mechanism, which is made possible by the bidirectional transformers at the center of BERT's design. This is significant because a word may change meaning as a sentence develops. Each word added augments the overall meaning of the sentence, and the context may completely alter the meaning of a specific word.

## The feature store
<a name="the-feature-store"></a>

 One of the key needs for the industry use cases listed in this whitepaper is to provide C-suite and organizations with a roadmap to accelerate, scale, and sustain digital adoption. To enable individual talent mobility using AI, it is necessary to collect data points at the individual level. Making AI models understand people’s strengths, interests, and other personal criteria result in providing better career recommendations that benefit the workforce and organizations alike. One of the first steps in the journey of creating a productionized, stable AI/ML platform is to focus on a centralized feature store.

 After [Amazon SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) applies the transformations defined in the [SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/), the normalized features are stored in an offline feature store so the features can be shared and reused consistently across the organization among collaborating data scientists. This means SageMaker AI Processing and Data Wrangler can be used to generate features, and then store them in a feature store. This standardization is often key to creating a normalized, reusable set of features that can be created, shared, and managed as input into training ML models. You can use this feature consistency across the [maturity spectrum](https://www.accenture.com/_acnmedia/Thought-Leadership-Assets/PDF-5/Accenture-Art-of-AI-Maturity-Report.pdf), whether you are a startup or an advanced organization with an ML center of excellence.

 The [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) is accessible across the organization for different teams to collaborate, promoting reuse, reducing overall cost, and avoiding silos with duplicate work efforts. The following query is a sample of the central Feature Store created with BERT embeddings. A [SageMaker AI Feature Group](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-create-feature-group.html) and a Feature Store are created. Multiple downstream teams can retrieve and use features from this central store instead of redoing feature engineering repeatedly, adding to the organization’s operational costs and non-standardization issues.

![A screenshot of the Feature Store with BERT embeddings ready for reuse across the organization .](http://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/images/feature-store.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
