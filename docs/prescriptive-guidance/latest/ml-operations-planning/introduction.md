---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-operations-planning/introduction.html
---

# Planning for successful MLOps
<a name="introduction"></a>

*Bruno Klein, Amazon Web Services*

Deploying machine learning (ML) solutions in production introduces many challenges that don't arise in standard software development projects. ML solutions are more complex and trickier to get right in the first place. They also exist in usually volatile environments, where the data distribution deviates significantly over time for a variety of expected and unexpected reasons.

These issues are further aggravated by the fact that many ML practitioners don't come from a software engineering background, so they might not be familiar with the best practices of this industry, such as writing testable code, modularizing components, and using version control effectively. These challenges create technical debt, and solutions become more complex and difficult to maintain over time, powered by a compounding effect, for ML teams.

This guide enumerates ML operations (MLOps) best practices that help mitigate these challenges in ML projects and workloads.

Because MLOps is a [cross-cutting concern](https://en.wikipedia.org/wiki/Cross-cutting_concern), these issues affect not only deployment and monitoring processes, but the whole model lifecycle. In this guide, MLOps best practices are organized into four major areas:
+ [Data](data.md)
+ [Training](training.md)
+ [Deployment](deployment.md)
+ [Monitoring](monitoring.md)

## Targeted business outcomes
<a name="business-outcomes"></a>

Deploying ML models in production is a task that requires continuous effort and a dedicated team to maintain these resources throughout their lifetime (in some cases, even years). ML models can unlock considerable value out of business data, but they have high costs. To minimize costs, enterprises should follow good practices in software development and data science. They should be aware of the nuances of ML systems, such as data drift, which makes models perform unexpectedly after a while. By being aware of these concerns, enterprises can meet their business goals safely and with agility in the short term and long term.

There are several kinds of ML models, and the industries they target have varying types of ML tasks and business problems, so you need to consider a different set of concerns for each model and industry. The practices laid out in this guide are not specific to a model or business, but apply to a broad set of models and industries to improve deployment times, generate higher productivity, and build stronger governance and security.

Putting models into production is a multi-disciplinary task that requires data scientists, machine learning engineers, data engineers, and software engineers. When you build your ML team, we recommend that you target these skills and backgrounds.
