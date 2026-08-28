---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ivr-design-on-connect/example.html
---

# Example use case
<a name="example"></a>

Now, let's examine a use case that illustrates how to apply these principles and derive a modular foundational architecture. Example Corp, a fictitious global company, is the focal point of our example.

Example Corp wants to migrate to a cloud-based contact center to reduce data center maintenance, to focus on innovation, and to cut costs. A key priority for them is self-service, with the aim of enhancing customer experience as part of the migration. Example Corp is a global organization that manages multiple toll-free numbers (TFNs) and direct inward dial numbers (DIDs) based on countries (United States, Canada, Italy, Netherlands, and so on) and lines of business (sales, support, new products, and so on). This means that they need to support multiple languages (such as US English, Canadian French, and Italian). Example Corp also wants to provide personalized, customized experiences to their callers based on the number dialed or the originating country, which could result in changing the menu options or offering different prompt messages in the IVR system. Additionally, each country has a dedicated set of skills (based on language, line of business, and so on) that must be assigned to agents for call routing. In total, the company supports 25 countries and 12 languages. They also plan to offer payment processing and the ability to purchase products and add-ons without speaking to an agent. As a best practice, Example Corp will maintain development, staging, and production environments for their contact center.

This section demonstrates how the [IVR design principles](design-principles.md) we discussed earlier in this guide can be applied to the Example Corp use case. We walk through the process of identifying organizational goals, building a customer contact journey, and creating an architectural framework to meet the company's requirements by using AWS services.

## Identifying the organization's goals
<a name="example-goals"></a>

For Example Corp, the primary organizational goals include the following:
+ **Cost savings:** Migrate to a cloud-based contact center to reduce maintenance costs and enhance innovation.
+ **Personalized self-service:** Provide a personal, customized experience for customers based on their originating number or country, including language options.
+ **Improved IVR containment rate: **Streamline payment processing within the IVR system to enable customers to purchase products and add-ons without agent intervention.
+ **Improved change management/innovation center:** Maintain separate environments (development, staging, and production) for the IVR system, for effective change management and experimentation.
+ **Improved first call resolution: **Implement effective routing strategies based on language, country, and customer intent.

## Mapping the customer contact journey
<a name="example-map"></a>

To create a customer contact journey for Example Corp, we need to consider the following aspects:
+ **Call origination**: Identify the country and line of business associated with the incoming call to provide a tailored experience.
+ **Language selection: **Offer an appropriate language menu based on the caller's originating country, profile, and the languages supported by Example Corp.
+ **Customer authentication**: Authenticate the caller by using their account details, voice biometrics, or another secure method.
+ **Personalization**: Collect and use customer data to personalize the IVR experience, such as greeting the caller by name or providing customized menu options based on their account history.
+ **Self-service options**: Offer self-service options to address common customer inquiries, such as balance inquiries, order status updates, or password resets.
+ **Payment processing**: Integrate a secure payment gateway so that customers can make purchases within the IVR system.
+ **Backend integrations**: Consider the backend API integrations to implement self-service processes, such as personalized greetings, order updates, and payments. Check availability and readiness of these APIs.
+ **Security and compliance**: Determine the information that requires further encryption, masking, or disablement of logs (for example, card information and customer PII).
+ **Repeatable processes**: Identify processes such as payment and caller authentication that will be repeated across most countries and lines of business.

## Creating the foundational architecture
<a name="example-architecture"></a>

To create a modular and dynamic architectural framework for the Example Corp IVR system, consider eliminating static content and modularizing repeatable processes.

**Eliminating static content**
+ Consider using variables to invoke prompts dynamically based on the toll-free numbers (TFNs) assigned to each country. For example, if TFN1 belongs to Canada, you can invoke the appropriate prompt from the external database to provide the customer with English and Canadian French as language options. Based on the customer's selection, you can then invoke the English (or Canadian French) prompts from the external database and play them throughout the IVR call flow. This approach uses a single IVR flow and eliminates redundancies across all TFNs.
+ Consider storing the agent queues and skills that the caller needs to be routed to, the next IVR tree the call needs to traverse through, and the values of API endpoints such as URLs and Amazon Resource Names (ARNs) in an external database. You can also invoke these based on the TFN assigned to a country or line of business.
+ To streamline the experience further, you can also store the deployment environment details in the external database. For example, if TFN2 is mapped to a development environment, you can invoke the relevant language prompts, API endpoints, agent queues and skills that are relevant for that environment only. If TFN3 is mapped to a staging environment, you can invoke call details assigned to staging, and so on. This approach streamlines call flow maintenance and development significantly. Developers can have a single call flow to maintain, and they can alter the experience easily based on key parameters such as the TFN assigned to a country, the line of business, or the environment.

**Identifying repeatable processes**

For Example Corp, some of the repeatable processes identified across countries and lines of business are caller language selection and payment processing. You can build these processes as modules so they are easy to centralize, maintain, and invoke across all call flows.

The following diagram shows a sample architecture based on the IVR design methodology discussed in this guide. This architecture uses Amazon Connect Customer flows and modules with these additional AWS services:
+ Amazon DynamoDB tables store ARNs, dynamic attributes, and prompts.
+ AWS Lambda functions retrieve information from the DynamoDB tables.
+ Amazon Polly converts the text prompts to speech.
+ Amazon Simple Storage Service (Amazon S3) stores [Connect Customer contact records](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html).

![Example IVR architecture with AWS services](http://docs.aws.amazon.com/prescriptive-guidance/latest/ivr-design-on-connect/images/guide-img/f2589901-9308-49b2-a33a-24321d4bafd8/images/841627c9-0f07-4802-b5a8-52833cd8327e.png)

The IVR system implements the following steps:

1. A customer calls the company's country-specific DID or TFN.

1. The call enters an Connect Customer initialization flow (initFlow).

1. The initialization flow calls three Lambda functions that retrieve data from three DynamoDB tables:
   + The first function retrieves [Connect Customer instance ARNs](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) based on the environment the call was made to (such as production, staging, or development).
   + A second function retrieves dynamic attributes such as country, language, and support queue based on the dialed number.
   + A third function gets IVR prompt messages based on the customer's language selection.

1. The Connect Customer language module (langModule) sets an Amazon Polly voice based on the language selected.

1. The call then traverses to the next contact flow (mainFlow) that plays dynamic prompts such as a welcome message or call center options, which were retrieved from the third DynamoDB table.

1. A Lambda function calls a DynamoDB API to invoke sub-contact flows, modules, and queues.

1. The call might be routed to a support center agent based on the customer's selection in the IVR system. The agent's screen is dynamically populated with the data that was captured, such as the customer's country, identity, and reason for the call.

1. The customer contact data is also stored in an Amazon S3 bucket as part of Connect Customer contact records, and can be used to generate custom reports by using Amazon Quick.

For information about how this design was used in a real-world scenario, see the re:Invent 2020 presentation [How Best Western built a modular and dynamic contact center using Connect Customer](https://youtu.be/qnIXMh203vc).  For sample code, see the [Dynamic Contact Center project](https://github.com/amazon-connect/amazon-connect-snippets/tree/master/projects/DynamicContactCenter) in GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
