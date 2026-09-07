---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-data/align-stories-goals.html
---

# Aligning stories with business goals
<a name="align-stories-goals"></a>

After you perform business and technical assessments, we recommend that you create a diagram that includes a set of stories for each level of data usage maturity. This visualization makes it easy to align your data usage with your company's business goals. For example, a near real-time fraud detection business outcome requires a near real-time actions capability story.

The stories are technical capabilities, data sharing mechanisms, people, and processes that are required to achieve the business goals. You write the business outcomes on the right side of the diagram based on your business discovery interviews, and fill the status of each story based on technical assessments. You can then select the stories your company should work on, and create a roadmap.

The following diagram shows whether each story is required, based on business outcomes. It also shows the current status of each story based on information that you collected in technical assessments. The diagram is usually followed by a report that explains each status in detail.

![Visualizing enablement stories for each data maturity phase](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-data/images/guide-img/7eadad47-3e6a-4775-bcac-a88d1e364e51/images/f0c32d5f-2250-414f-8469-292279813457.png)

You work back from the right side (*Business outcomes*) to the left side to enable the stories. For example, to enable a story in the third stage (*Insights and reports*), you have to enable its dependencies in the second stage (*Data lake*) and first stage (*Data foundation*).

Based on the assessment and the requirements for business outcomes, each story is classified as green, yellow, red, or gray.
+ Green means that the story is in place and can scale to deliver the business outcomes. For example, in the diagram, the CDC ingestion story in the first (*Data foundation*) stage is green, which means that the company has the tools and process to accomplish the story for the data source they have. The *Better customer experience* business outcome requires ingesting relevant customer data and enriching it with other data inside the company, to better understand the customer and provide personalization.
+ Yellow means that the capability or process exists, but it is not fully functional or will not support the scale that the business outcome requires. For example, in the diagram, the *Centralized data catalog* story in the second (*Data lake*) stage is yellow. This indicates that the company has a central data catalog, but the catalog isn't fully populated with the metadata required by the other stages, or it's used by only a few business areas. This classification impacts the data sharing capabilities in the next (*Insights and reports*) stage.
+ Gray means that the story isn't required.
+ Red means that the story is required by business outcomes but hasn't been implemented. For example, in the diagram, the *Data sharing* story in the *Insights and reports* stage is red. Creating a comprehensive machine learning model for customer recommendations requires grouping datasets, which requires data sharing capabilities. However, this story hasn't been implemented. In this example, data sharing also requires capabilities in the *Data lake *stage to be fully functional, at least for the datasets that are part of the models, but you can see that data stewardship hasn't been implemented.

The story *Data privacy, protection, and compliance* (in the *Data lake* stage) is always required, and it becomes more relevant as data privacy regulations are pushed by new data protection requirements. For example, the [General Data Protection Regulation (GDPR)](https://gdpr.eu/what-is-gdpr/) started in the US with the [Virginia Consumer Data Protection Act (CDPA)](https://law.lis.virginia.gov/vacodefull/title59.1/chapter53/) and the [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa), and is already in place for some Latin American countries such as [Lei Geral de Proteção a Dados Pessoais (LGPD)](https://www.serpro.gov.br/privacidade-protecao-dados) in Brazil, [Mexican data protection](https://www.dataguidance.com/notes/mexico-data-protection-overview) in Mexico, Data Protection in Colombia, [Law 29733](https://www.leyes.congreso.gob.pe/Documentos/Leyes/29733.pdf) in Peru, and [Argentina Personal Data Protection](https://servicios.infoleg.gob.ar/infolegInternet/anexos/320000-324999/323901/norma.htm) laws.
