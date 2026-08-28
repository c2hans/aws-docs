---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-avaya-to-connect-lex/targeted-business-outcomes.html
---

# Targeted business outcomes
<a name="targeted-business-outcomes"></a>

Migrating a contact center to the AWS Cloud can provide the following benefits:
+ [AI-based self-service](#ai-based-self-service)
+ [AI-based contact center](#ai-based-contact-center)
+ [AI-based payment collections for contact centers](#ai-based-payment-collection)

## AI-based self-service
<a name="ai-based-self-service"></a>

Artificial intelligence (AI), in the form of conversational platforms utilizing voice bots (specially IVRs), enables callers to self-serve. AI can also help human agents with relevant information in real time and provide recommendations for next actions. Implementing AI capabilities that understand natural language involves *intent detection* by accurately classifying the goal of the customer, routing the call based on that intent, and then providing relevant information to the human agent.

Every organization has objectives and key results (OKRs) that involve either increasing revenue or decreasing costs. AI-based self-service can help you achieve important goals and business outcomes by using bots to generate leads, improve experience, increase fulfillment speed, and generate customer insights. Additionally, self-service can reduce costs, provide intelligent routing, reduce the average handle time of the agent (which reduces telecom costs), and increase first-contact resolution.

## AI-based contact center
<a name="ai-based-contact-center"></a>

In addition to providing self-service, AI can improve the performance of contact centers. It can match customer preferences and provide next actions for agents. Chatbots can help onboard new customers and help predict which customers are likely to sign-up and which are just requesting information.

AI-based contact centers can also help reduce customer churn and improve customer retention. Call transcription can predict which customers will leave the company, based on different behavioral attributes. Call transcription can also prepare an outbound campaign to help retain those customers. For more information, see [Analyze customer churn probability using call transcription and customer profiles with Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/analyze-customer-churn-probability-using-call-transcription-and-customer-profiles-with-amazon-sagemaker/) (AWS blog post).

By using customer segmentation, you can improve customer experience by offering self-service or agent service. For example, if a customer is tech-savvy, offer more self-service options. You can also improve marketing effectiveness by analyzing patterns in the customer data to determine which marketing efforts need improvement.

In certain scenarios, calls might be incorrectly classified and route to the incorrect agent. In this case, the agent must transfer the call. Not only do misrouted calls result in customer frustration, but it also increases costs. By using machine learning (ML) to analyze agent feedback about transferred calls, you can improve the routing models.

## AI-based payment collections for contact centers
<a name="ai-based-payment-collection"></a>

Payment collections is the most important business function because it has a direct effect on company performance. Collecting revenue on time helps a business grow faster by using that revenue to make additional investments. Therefore, higher contact rates are essential to collect customer payments. However, each individual customer has an ideal time to answer calls. AI can help your business predicting the best time to call each customer in order to increase the probability of the customer answering the call.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
