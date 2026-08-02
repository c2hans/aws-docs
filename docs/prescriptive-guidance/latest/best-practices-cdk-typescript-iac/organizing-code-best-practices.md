---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/organizing-code-best-practices.html
---

# Organize code for large-scale projects
<a name="organizing-code-best-practices"></a>

## Why code organization is important
<a name="why-code-organization-is-important.1327cc22-ecac-5e53-b78d-9fa2f91f1644"></a>

It's critical for large-scale AWS Cloud Development Kit (AWS CDK) projects to have a high-quality, well-defined structure. As a project gets larger and its number of supported features and constructs grows, code navigation becomes more difficult. This difficulty can impact productivity and slow down developer onboarding.

## How to organize your code for scale
<a name="how-to-organize-your-code-for-scale.d0803b5e-213f-5538-8e56-8bbe55a79383"></a>

To achieve a high level of code flexibility and readability, we recommend that you divide your code into logical pieces based on functionality. This division reflects the fact that most of your constructs are used in different business domains. For example, both your frontend and backend applications could require an AWS Lambda function and consume the same source code. Factories can create objects without exposing the creation logic to the client and use a common interface to refer to newly created objects. You can use a factory as an effective pattern for creating a consistent behavior in your code base. Additionally, a factory can serve as a single source of truth to help you avoid repetitive code and make troubleshooting easier.

To better understand how factories work, consider the example of a car manufacturer. A car manufacturer doesn't need to have the knowledge and infrastructure required for manufacturing tires. Instead, the car manufacturer outsources that expertise to a specialized manufacturer of tires, and then simply orders the tires from that manufacturer as needed. The same principle applies to code. For example, you can create a Lambda factory that is capable of building high-quality Lambda functions, and then call the Lambda factory in your code whenever you need to create a Lambda function. Similarly, you can use this same outsourcing process to decouple your application and build modular components.

## Sample code organization
<a name="sample-code-organization.0e987361-b53c-571e-bb02-bea069dd1691"></a>

The following TypeScript sample project, as shown in the following image, includes a **common** folder where you can keep all your constructs or common functionalities.

![Common folder](http://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/images/guide-img/b7d5d887-7172-4d47-9f1f-1cf7ae181482/images/f62f4ebc-a544-47a2-85cf-6a5cd5b92219.png)

For example, the **compute** folder (residing in the **common** folder) holds all the logic for different compute constructs. New developers can easily add new compute constructs without impacting the other resources. All the other constructs won't need to create new resources internally. Instead, these constructs simply call the common construct factory. You can organize other constructs, such as storage, in the same way.

Configurations contain environment-based data that you must decouple from the **common** folder where you keep the logic. We recommend that you place your common **config** data in a shared folder. We also recommend that you use the **utilities** folder to serve all the helper functions and clean up scripts.
