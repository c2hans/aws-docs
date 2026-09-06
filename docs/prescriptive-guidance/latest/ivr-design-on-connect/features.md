---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ivr-design-on-connect/features.html
---

# Connect Customer features for IVR applications
<a name="features"></a>

[Amazon Connect Customer](https://aws.amazon.com/connect/) is an omnichannel cloud contact center that helps companies provide superior customer service at a low cost. Connect Customer provides a seamless experience across voice and chat for customers and agents. This includes a single set of tools for skills-based routing, powerful real-time and historical analytics, easy-to-use, intuitive management tools, and [pay-as-you-go pricing](https://aws.amazon.com/connect/pricing/?p=pm&c=connect&z=2).

This section gives an overview of the Connect Customer features that can help you build an automated self-service experience. For examples of these components, see the [sample architecture](create-architecture.md) described later in this guide.

## Flow designer
<a name="flow-designer.e615faf7-8ec3-536f-95f0-81003ddd3153"></a>

Connect Customer provides a graphical user interface (GUI)‒based, self-service [flow designer](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-contact-flows.html#concepts-visual-editor). This feature includes a drag-and-drop interface that helps you create personalized customer experiences intuitively and make changes on the fly. Flow blocks act as the building blocks of your IVR and routing experience. Each block has a specified function (for example, [Play prompt](https://docs.aws.amazon.com/connect/latest/adminguide/play.html) or[ Get customer input](https://docs.aws.amazon.com/connect/latest/adminguide/get-customer-input.html)), which makes flows visually intuitive.

## Flows
<a name="flows.fb595fd3-f1bb-5099-b8fd-d520ba7676c1"></a>

[Flows ](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html)define the customer experience with your contact center from start to finish. They deliver your IVR options and also route callers to the right agents based on the information they have gathered. You can use flows to interact with other AWS services, such as [AWS Lambda](https://aws.amazon.com/lambda/), to create dynamic and personalized customer experiences. Flows can also integrate with [Amazon Lex](https://aws.amazon.com/lex/) to provide life-like natural language interactions.

## Flow modules
<a name="flow-modules.89fcd796-451b-5273-baa0-8091bb490acc"></a>

[Flow modules](https://docs.aws.amazon.com/connect/latest/adminguide/contact-flow-modules.html) are reusable sections of a flow. You can use these modules to extract repeatable logic across your flows and to perform common functions. For example, you can create a module that implements IVR payments for callers or sends SMS notifications after transactions.

## AWS Lambda functions
<a name="9999999999999999lamlong--functions.2ee206b7-8f62-56e8-81c0-cc6a6c50ac31"></a>

Flows let you interact with backend systems such as order management, CRMs, ticket systems, and databases by using an AWS Lambda flow block. [This integration](https://docs.aws.amazon.com/connect/latest/adminguide/connect-lambda-functions.html) enables self-service interactions on the IVR system with an increased containment rate. You can easily automate common customer use cases such as getting updates on order status or checking credit card balances. You can also use APIs to update customer preferences in your CRM, or create tickets on their behalf.
