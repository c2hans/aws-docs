---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-banking-modernization-clm/strategy-banking-modernization.html
---

# Banking modernization challenges
<a name="strategy-banking-modernization"></a>

## Changing customer expectations and the rise of neobanks
<a name="customer-expectations-neobanks"></a>

The FS industry is facing a massive change. Customers not only expect a fully digital journey, but also a personalized experience. To meet these customer expectations and compete with neobanks, traditional financial institutions must undergo a massive transformation that requires speed, agility, and innovation. That transformation will require traditional financial institutions to overcome the following near-term challenges:

1. Traditional banks must keep pace with neobanks, which are more agile in nature thanks to the lack of technical and process debt.

1. Traditional financial institutions must develop and provide embedded banking services through banking as a service (BaaS).

1. Traditional financial institutions must develop and enable customizable and flexible customer experiences that integrate machine learning models quickly and cost-effectively.

The key strategic factors to consider for the next few years are to leverage built-in cloud services and to enable time-to-market benefits that result from collaboration with service providers and agile transformation.

## Business problem
<a name="business-problem"></a>

Traditional financial institutions still work with manual or semi-automatic processes. No industry standard is applied for regular banking processes, even though these processes are common to all financial institutions in similar jurisdictions. To overcome these challenges, traditional financial institutions can implement scalable and secure standard processes by using a serverless approach that's built on AWS Cloud services. For example, [Amazon Lex](https://aws.amazon.com/lex/) and [Amazon Rekognition](https://aws.amazon.com/rekognition/) provide trained machine learning models that you can integrate into enhanced customer journeys. Previously, such innovation was hampered by complex integration and expensive development processes, but now these innovations are available directly for customer applications through API calls.

AWS Cloud services not only provide additional innovation and speed of integration, but also leverage the latest security capabilities to ensure data confidentiality and privacy. We want to highlight this modernization approach to banking for the CLM landscape. The client lifecycle is at the heart of the client relationship, which is why it must urgently be modernized and even digitized. As shown in [What the embedded-finance and banking-as-a-service trends mean for financial services](https://www.mckinsey.com/industries/financial-services/our-insights/banking-matters/what-the-embedded-finance-and-banking-as-a-service-trends-mean-for-financial-services) from McKinsey & Company, banks who want to offer BaaS will have to make it work, and "Making it work will require new technologies and capabilities because BaaS is usually distributed to clients via APIs and requires strong risk and compliance management of the embedded finance partner." The *Serverless onboarding *section in this strategy explains how you can make such a strategy work.

## Client lifecycle management use case
<a name="the-client-lifecycle-management-case"></a>

CLM is a set of loosely interdependent and mandatory processes defining the business interaction of a client with its financial institution or insurer. The following figure provides a generalized overview of CLM stages for the banking and insurance industries:

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-banking-modernization-clm/images/guide-img/3dd14f64-3f68-43c4-8bd5-d6738253ef4f/images/b77dee94-ed1e-4ef7-b43d-9bbdd5de75ec.png)

Take into consideration that these processes vary by client segment. For example, commercial client onboarding is different from retail client onboarding. The processes can also vary from industry to industry. Onboarding a banking client is different from onboarding an insurance client. This strategy focuses on the banking retail client experience.

In the diagram above, every box (*Prospecting*, for example) represents a candidate for modernization. You can use a diagram like this to break the use case down into discrete, independent use cases. For example, the *Prospecting* use case can be broken down into constituent use cases. Then, you can map each independent use case to existing capabilities, either from cloud services providers or BaaS providers. This mapping exercise can reveal that document archiving for banking, for instance, could be a service by itself that's provided by an external party. Breaking the client lifecycle management use cases into discrete, independent use cases enables you to design and develop focused services.

This strategy focuses on the example use case of opening a new bank account. For customers, this is often a lengthy, highly-manual, and error-prone process, which results in frustration and dissatisfaction. Today most of onboarding is still happening manually through phone calls or physical touch points. However, research indicates that customers prefer a digital experience. According to [Digital onboarding in finance: a novel model and related cybersecurity risks](https://open-research-europe.ec.europa.eu/articles/1-149) from Open Research Europe, 70 percent of customers prefer to contract products digitally.

## Client onboarding opportunities
<a name="client-onboarding-opportunities"></a>

In the post-COVID crisis age, banking and FS customers must face cumbersome and complex processes. In fact, few customers today can complete the entire process of opening a checking account from a mobile device. The majority of customers must follow a manual onboarding process for opening a bank account that is similar to the following:

1. The customer, or end user, must submit proof of identity, a legal ID, and various other data points. In many cases, these data points include documentation for a physical address, employment proof, and more. Often, the customer must visit a branch office to provide this information, or send it to the bank through standard mail.

1. Before customers can even use their banking accounts, they will receive several paper documents. Then, customers must sign and return the documents to the bank (that is, single contracts for each banking product, such as personal accounts, joint accounts, trading accounts, e-banking, credit cards, or security codes).

1. The bank digitizes all the signed documents and links them to the "work-in-progress" account to make the account operational.

1. Depending on the client segment or the applicant's risk assessment, the bank must regularly repeat this process partially or entirely.

1. If the customer's address, civil status, or any other data considered as a "change of circumstance" is updated, the process is initiated again.

Completion of this process can take up to several days or even weeks, and it often requires intervention from and approval by several bank employees from different departments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
