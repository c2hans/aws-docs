---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ivr-design-on-connect/create-architecture.html
---

# Create the foundational architecture
<a name="create-architecture"></a>

After you have defined your organization's goals and outlined the customer contact journey, you can use that information to define a foundational architecture for the IVR system. These data points are critical in creating an IVR architecture that is both modular and scalable. The key principles for building a good foundational framework are:
+ Eliminate static design
+ Identify repeatable processes

## Eliminate static design
<a name="static-design"></a>

A common mistake developers make when they design an IVR system is to introduce static information or hard-coded logic within the flow. This static information includes prompt messages, the value of the next call flow to invoke, or the skill group to route the call to. It could also be the address of API endpoints that are invoked from an IVR or the variables returned, which are then used for branching logic within the IVR system.

Using static values in the IVR system makes it difficult to track and change them in real time, and introduces redundancies in the flow. The best practice is to have a dynamic design wherever possible. Let's look at an example of designing a multi-language IVR system to understand this better.

**Static approach:**

Typically, while designing a multi-language IVR system, developers identify the customer's preferred language, and then create two versions of the same flow. The first version has prompt messages hard-coded in Language A, and the second version might have messages hard-coded in Language B, as the following diagram illustrates.

![Static approach in designing an IVR system](http://docs.aws.amazon.com/prescriptive-guidance/latest/ivr-design-on-connect/images/guide-img/f2589901-9308-49b2-a33a-24321d4bafd8/images/dc980fc6-062f-40d8-899c-c053ef7492bf.png)

 This approach is difficult to scale because developers have to maintain different versions of the same flow. They also have to create a new version of the flow every time they add an new language.

Additionally, any changes they make to business logic in one flow must be replicated manually to the other versions. This makes the IVR design messy and non-modular, and increases the time to market for innovation.

**Dynamic approach:**

The recommended approach to solve this problem is to assign prompt messages to variables instead of using static values in the prompt blocks of the IVR designer. Based on the customer's choice of language, invoke the values of the prompts from an external database and populate the variables to play those messages as shown in the following flowchart. When you use this approach, you can maintain a single IVR flow and easily scale to *n* number of languages. As a developer, you add language prompts to the external database and invoke them (by using an API) based on customer selection in the IVR system or on data returned from a CRM query. This also protects the IVR system from any changes in business logic. When you use this model, make sure that you have a default branch with a minimal set of static messages that can be used in the event of database or query failures.

![Dynamic approach in designing an IVR system](http://docs.aws.amazon.com/prescriptive-guidance/latest/ivr-design-on-connect/images/guide-img/f2589901-9308-49b2-a33a-24321d4bafd8/images/1e8747b0-3f28-48ee-8713-054f9b809f03.png)

## Identifying repeatable processes
<a name="repeatable-processes"></a>

Identifying repeatable patterns in the customer experience can help eliminate redundant components within your IVR system. You can create reusable logic, or modules, for repeated use cases and invoke them as needed in various call flows. For example, if both the sales and support teams need to send a SMS notification within the IVR system, you can create a single, reusable *Send SMS* module that can be used across both lines of business. By using this approach, you can maintain a single flow, and any updates to that module will be reflected across all LOBs in a streamlined way. Some other common examples of repeatable processes are:
+ Assigning language selection to the IVR flow based on customer input.
+ Implementing payment processing in the IVR system.
+ Caller authentication logic.
+ Identifying a customer by using a CRM lookup. By modularizing the customer lookup module in your CRM, you can turn purpose-built connections, which often use proprietary languages, into simple IVR blocks. Anyone who develops customer experiences can then access and use these IVR blocks.
+ Performing emergency message routing.
