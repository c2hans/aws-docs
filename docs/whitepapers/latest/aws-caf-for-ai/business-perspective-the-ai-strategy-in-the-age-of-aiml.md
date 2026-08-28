---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/business-perspective-the-ai-strategy-in-the-age-of-aiml.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Business perspective: The AI strategy in the age of AI
<a name="business-perspective-the-ai-strategy-in-the-age-of-aiml"></a>

While the cloud enables organizations to innovate at an accelerated pace, new technological paradigms, such as AI and ML, enable net-new organizational capabilities, products, and services. For decades, those business problems where the decision-making process was complex, the data that informs it was unstructured, or where the environment of the decision was constantly changing, had proven elusive to be solved through the methods of computer science.

The recent advances in ML have changed this and suddenly, problems that require machines to see, or understand language, or learn from past data and predict outcomes can be addressed. The newly and readily available ML capabilities are questioning long standing market hypotheses of established organizations, such as, automotive companies that shy away from driver assistance and automation. This perspective therefore addresses those capabilities that directly enable the business to make the most of these use cases.

|  Foundational Capability  |  Explanation  |
| --- | --- |
|  Strategy Management  |  Unlock new business value through artificial intelligence and machine learning.  |
|  Product Management  |  Manage data-driven and AI infused or enabled products.  |
|  Business Insight  |  The power of AI to answer ambiguous questions or predict from past data. |
|  Portfolio Management  |  Identify and prioritize high-value AI products and initiatives that are feasible. |
|  Innovation Management  |  Question long-standing market hypotheses and innovate your current business. |
|  New: Generative AI  |  Leverage the general-purpose capabilities of large AI models. |
|  Data Monetization  |  This capability is not enriched for AI, [refer to the AWS CAF](https://aws.amazon.com/professional-services/CAF/).  |
|  Strategic Partnership  |  This capability is not enriched for AI, [refer to the AWS CAF](https://aws.amazon.com/professional-services/CAF/).  |
|  Data Science  |  This capability is not enriched for AI, [refer to the AWS CAF](https://aws.amazon.com/professional-services/CAF/).  |

## Strategy management
<a name="strategy-management"></a>

**Unlock new business value through artificial intelligence and machine learning. **

Machine learning enables new value propositions that in turn lead to increased business outcomes, such as reduced business risk, growing revenue, operational efficiency, and improved ESG. Therefore, start by defining a business- and customer-centric north-star for your AI adoption and underpin it with an actionable strategy that moves step by step to adopting AI technology. Make sure that any [adoption strategy](https://aws.amazon.com/blogs/enterprise-strategy/a-guide-to-making-your-ai-vision-a-reality/) is based on tangible (short term and measurable) or at least aspirational (long term and harder to measure) business impact that capitalizes on these new capabilities. Factor in both short-term as well as long-term impact of adopting AI.

 [Work backwards](https://docs.aws.amazon.com/whitepapers/latest/building-cloud-operating-model/step-1.-work-backwards-from-the-customer.html) from existing business and customer problems and the effect that AI can have on them. When moving closer to prioritizing AI opportunities, address how and what data will fuel the systems capability. Consider from the start the self-reinforcing properties of a data flywheel on any ML product or service, where new data leads to an improved system that grows your customer base, increasing the amount of data your business benefits from.

While building such a flywheel, consider if the data you acquire can provide a [defensive moat](https://aws.amazon.com/what-is/data-strategy/?nc1=h_ls) around your value proposition (something that is rare and costly). Given the [broad impact AI technology](https://aws.amazon.com/machine-learning/customers/) already has on the market landscape, consider that your customers are likely to raise their expectations towards your products and services capability in the near future and that AI capabilities are a part of that expectation.

For each opportunity, ask if you need to build, tune, or adopt an existing AI system. For example, if you expect to use the [broad emergent capabilities of foundation models](https://aws.amazon.com/blogs/machine-learning/announcing-new-tools-for-building-with-generative-ai-on-aws/) but lack the capabilities to create them from scratch, focus on customizing them for your specific needs. If your ambition is to create a domain-specific general system to propel your business, invest in the data foundations.

## Product management
<a name="product-management"></a>

**Manage data-driven and AI infused or enabled products. **

 Building and managing AI-based products can be a significant challenge as the development and lifecycle of AI systems differs from traditional software and cloud products. Both the development as well as the operation and continuous creation of results (such as direct predictions) of any AI-based product include potentially costly uncertainties that require specific mitigation strategies.

When building or embedding AI into products, work backwards from your customers' and users' expected value gain, and map measurable business proxies to individual decision points that an AI system can support, enrich, or automate. For each of those, define potential metrics in the ML solution domain (such as how the value gain of detecting fraudulent transactions in the financial sector translates to expected monetary gain and a correlating precision or recall of an ML-enabled transaction classifier) and the [corresponding ML problem](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/machine-learning.html) (such as a classification problem, an intent extraction problem, generative AI and many more). Together, these formulated ML problems and their individual solutions form [the value-gain that ML brings](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost-01.html) to your product.

 Crucially, these ML solutions impose certain data requirements on you and your product, hence you must investigate the [4 V’s of Data](https://aws.amazon.com/blogs/enterprise-strategy/analytics-part-1-why-every-company-has-a-big-data-problem/) for each of them. While you build this knowledge bottom up, make sure to involve business, data, executive, and ML stakeholders in the assessment of your solution. Since ML products fuse data, domain, and technology into one predictive and sometimes prescriptive system, all of them are needed. Pave the path to evolve your AI-based product through a [proper lifecycle management](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/well-architected-machine-learning-lifecycle.html), factor in how users interact with probability based output from AI-systems (such as gracefully fail when the confidence of the system is low) and consider what the impact of your solution is when adopted to make sure you [use AI responsibly.](https://aws.amazon.com/machine-learning/responsible-machine-learning/)

 Condense your understanding of which questions are critical to [properly scope the ML capabilities](https://pages.awscloud.com/EMEA-field-OE-management-AI-ML-powered-products-202111-confirmation) of your product and improve your product management capability for AI. This means, for example, to take an experimental, often time-bound approach to de-risking the ML component and considering from the beginning how learnings from these experiments translate into a production-grade system. Equally it means [designing feedback loops](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mloe-06.html) into the information flow of the system (or explicitly preventing them). Over time, enable the broader organization to build new AI products, based on the output of other ML systems through technologies such as [data mesh](https://aws.amazon.com/blogs/big-data/use-an-event-driven-architecture-to-build-a-data-mesh-on-aws/) (also see [DataZone](https://aws.amazon.com/datazone/)) and [data lake architectures](https://aws.amazon.com/solutions/implementations/data-lake-solution) and by establishing proper knowledge transfer between teams and product groups (implemented such as through [SageMaker AI Model Cards).](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)

## Business insights
<a name="business-insights"></a>

 **The power of AI to answer ambiguous questions or predict from past data.**

 Business intelligence (BI), mostly including descriptive and diagnostic analytics, is frequently where companies begin their journey when preparing to use AI. However, [beyond descriptive and diagnostic analytics](https://aws.amazon.com/what-is/data-analytics/), ML enables predictive and even prescriptive capabilities and together they form the AI journey. It is crucial to acknowledge that the scope of analytical and BI units has been a different one than what is expected organizationally from AI-driven ones.

Today, many companies require subject matter experts (SMEs) to sift through insights and pull out the cause for certain observations in the data (the *why*). However, using AI techniques, BI is starting to augment these SMEs and give them new insights to incorporate into their thought process by [identifying the *why* and the *what if*](https://docs.aws.amazon.com/forecast/latest/dg/what-if.html). With this, data and AI suddenly becomes the driver for predictive decision making.

 When preparing the transition of your BI practice to an AI-enabled one, and to higher level analytics in general, a great way to push the boundaries is using [algorithms](https://aws.amazon.com/what-is/predictive-analytics/) with diagnostic analytics to help you understand [key variables or root causes influencing](https://www.amazon.science/tag/causal-discovery) your problem statement. Make sure that organizational maturity in analytics is not siloed with each subsection of the organization and ponder how you can cross-pollinate your more mature organizations with the less mature to accelerate your AI journey.

In the early stages of transformation, any effective method can be to create a center of excellence for analytics (not necessarily AI) that is closely tied to your [cloud initiatives.](https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/) Such a center of excellence (COE) can provide immediate value through [democratized access to data-driven predictions and analysis](https://aws.amazon.com/quicksight/q/) and propel your larger ambitions. Most importantly, create a rhythm of using AI to inform major business decisions as this will drive the recognition of its value to a true business outcome.

## Portfolio management
<a name="portfolio-management"></a>

 **Identify and prioritize high-value AI products and initiatives that are feasible. **

The challenge of ML initiatives is that short-term results must be shown without sacrificing long-term value. In the worst case, short-term thinking can lead to technical AI proofs of concept (POCs) that never make it beyond that technical stage because they were focused on irrelevant business technicalities. Your first goal when identifying, prioritizing, and running ML projects and products must be to deliver on tangible business results.

Starting somewhere is crucial, and small wins can drive faith in your organization as it helps people connect to where they could use AI in other portions of your business. At the same time, consider what larger customer and business problems you are solving through multiple AI projects and products and combine those into a hierarchical portfolio where the lower layers of that portfolio enable the upper layers. Certain AI capabilities simply can’t be built in one go. Rather, they build upon each other. For example, in the financial industry, before being able to recommend new products to customers, you must be able to categorize what is important today, so classifying transactions precedes next-best-offer actions. Each layer of your portfolio should add additional value to the organization at large.

Next, embed in this portfolio the design of an [AI flywheel](https://pages.awscloud.com/EMEA-Data-Flywheel.html?nc1=f_ls) where the value that your portfolio provides propels business outcomes that, in turn, enable and create additional data from which your portfolio benefits (see Figure 6). This flywheel does not need to be on a single-product level but can reach through your portfolio. As your portfolio evolves and scales, prioritizing what to buy versus what to build becomes crucial. Push back on the *not invented here* syndrome.

Exploring [which use cases](https://aiexplorer.aws.amazon.com/?sc_icampaign=pac-gc-400_AIUseCaseExplorerTool_landingpage_october&sc_ichannel=ha&sc_icontent=awssm-11566_gc&sc_iplace=ribbon&trk=f516a922-57d6-471b-877b-4a4f3385c311~ha_awssm-11566_gc) and [which solutions](https://aws.amazon.com/machine-learning/ai-services/) already exist in the market, and at what maturity level, should not be an afterthought. Also investigate which solutions [require custom modeling](https://aws.amazon.com/ml-solutions-lab/), and raise your AI workforce's efficiency by choosing the right AI products and cloud environment. Realize how complex it is to even just [technically govern your portfolio](https://aws.amazon.com/sagemaker/ml-governance/). To make sure you keep your scarce AI workforce efficient, be decisive and bold, and push back on analysis paralysis.

Finally, as your portfolio grows and more parts of the organization start to use AI, enable efficient collaboration between your business units, teams, and AWS partners that you rely on (see [AWS DataZones](https://aws.amazon.com/datazone/), [AWS Redshift](https://aws.amazon.com/redshift/) and [AWS CleanRoom](https://aws.amazon.com/clean-rooms/)) .

## Innovation management
<a name="innovation-management"></a>

 **Question long-standing market hypothesis and innovate your current business.**

As mentioned in the introduction to this perspective, ML offers new capabilities to businesses that can be and in many cases are disruptive to existing businesses and value chains. The power of this general-purpose technology is seen and felt across sectors and there is virtually no exception to that, as the long-term goal of AI-research is to replicate or at least imitate intelligence. The historically human capability to do knowledge work and process complex information, reason and derive insights, and take actions can [now be tackled by advanced foundation models and generative AI](https://aws.amazon.com/blogs/machine-learning/announcing-new-tools-for-building-with-generative-ai-on-aws/). In your [innovation roadmap and your innovation management practice](https://resources.awscloud.com/ai-and-machine-learning-aws-innovate), bridge to these mid- and long-term goals of AI research through short-term and real-world applicable value propositions.

To do this, start by exploring the evolving customer expectations and needs, both from an internal and external perspective. The business outcomes that the CAF-AI suggests can guide you in identifying these needs and expectations. Consider the value chain of [ML-enabled or infused products](https://aws.amazon.com/events/aws-innovate/machine-learning/resources/#ebooks), and differentiate between innovation for cost reductions (such as process improvements), revenue and profit gains (such as product improvements), or completely new income channels (such as new products and services).

Use and position ML as a unique differentiator to the respective internal and external stakeholders, and customers. Integrate ML to unlock new capabilities, augment existing ones, and reduce effort through automation. Capitalize and double down on domain-specific knowledge that is represented in the data you access. Design a healthy data value chain for your AI system to allow a long-lasting value generation. Don’t get discouraged that some ML-based products only grow better over time, or that your innovation cycles might be longer than what some companies are used to. While you build up single lines of ML-enabled products, pave the way to innovation across the organization by raising data to a first-class citizen of the value-creation process and [creating internal data products for consumption.](https://aws.amazon.com/what-is/data-mesh/)

Additionally, to this top-down approach to innovation-management, get a grassroots movement going through internal AI champions. These champions can be business owners, product managers, technical experts, as well as the C-suite. Constantly keep a balance between audacious goals and the achievable ones. While typical software systems and environments grow their value with an increasing number of users, the value of ML systems is driven largely by the data that makes it more effective. Therefore, managing AI innovation also means bringing your data strategy to life, not just archiving data that describes the past. With this growing high-quality and value data that is governed and accessible across organizational boundaries, you will create gravity for AI ideas and projects.

## New: Generative AI
<a name="new-generative-artificial-intelligence"></a>

 **Use the general-purpose capabilities of large AI models.**

 The overall goal of AI is to create systems that are of general quality and can be applied to many complex problem spaces with little to no additional cost. One particularly powerful stream of this work is generative AI, a type of AI that can create new content and ideas, including conversations, stories, images, videos, and music. Generative AI is powered by very large models that are pre-trained on vast amounts of data and commonly referred to as foundation models (FMs). [The potential of these FMs](https://www.youtube.com/watch?v=dBzCGcwYCJo) lies in their capability to [generalize across domains and tasks](https://aws.amazon.com/bedrock/). Such foundation models will, one way or another, influence your organization and business as they reduce the cost of knowledge work dramatically. When planning to adopt this powerful branch of AI, there are three considerations. Do you require to build such FMs:

1. From scratch and uniquely tailored to your business?

1. Fine-tune a pre-trained model and capitalize on the abilities it has already learned?

1. Use an existing FM from a supplier without further tuning?

[Having the choice between these three is essential](https://aws.amazon.com/blogs/machine-learning/announcing-new-tools-for-building-with-generative-ai-on-aws/) and the correct choice depends on your business case. Very often unlocking the true value of these large models means contextualizing them with your domain specific data (case 2) and applying them to a wide variety of tasks. This is the case because large and pre-trained models already possess emergent capabilities (for example, reasoning) that are costly to produce from scratch (case 1). Therefore, when using foundation models and generative AI, capitalize on a [pre-trained model's ability](https://aws.amazon.com/sagemaker/jumpstart/getting-started/?sagemaker-jumpstart-cards) to adapt and learn from little to no data.

For many businesses, this approach means selecting the right foundation model for their business problems and customizing (for example, through instruction tuning and few-shot learning) and fine-tuning them with domain- or customer-specific data. The effectiveness and differentiating capabilities of generative AI and foundation models, just as with other AI systems, will largely rely on your data strategy and data flywheel. Whichever path you choose, verify that you are comfortable with the data you use, as the data influences how the model will behave in production, and establishing guardrails around generative AI systems is significantly hard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
