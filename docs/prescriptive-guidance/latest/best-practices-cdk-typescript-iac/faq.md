---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/faq.html
---

# FAQ
<a name="faq"></a>

## What problems can TypeScript solve?
<a name="typescript-problems"></a>

Typically, you can eliminate bugs in your code by writing automated tests, manually verifying that the code works as expected, and then finally having another person validate your code. Validating the connections between every part of your project is time consuming. To speed up the validation process, you can use a type-checked language like TypeScript to automate code validation and provide instant feedback during development.

## Why should I use TypeScript?
<a name="typescript-use"></a>

TypeScript is an open-source language that simplifies JavaScript code, making it easier to read and debug. TypeScript also provides highly productive development tools for JavaScript IDEs and practices, such as static checking. Additionally, TypeScript offers the benefits of ECMAScript 6 (ES6) and can increase your productivity. Finally, TypeScript can help you avoid painful bugs that developers commonly run into when writing JavaScript by type checking the code.

## Should I use the AWS CDK or CloudFormation?
<a name="cdk-cloudformation"></a>

We recommend that you use the AWS Cloud Development Kit (AWS CDK) instead of AWS CloudFormation, if your organization has the development expertise to take advantage of the AWS CDK. This is because the AWS CDK is more flexible than CloudFormation, since you can use a programming language and OOP concepts. Keep in mind that you can use CloudFormation to create AWS resources in an orderly and predictable manner. In CloudFormation, resources are written in text files by using the JSON or YAML format.

## What if the AWS CDK doesn't support a newly launched AWS service?
<a name="unsupported-services"></a>

You can use a [raw override](https://docs.aws.amazon.com/cdk/v2/guide/cfn_layer.html#cfn_layer_raw) or a CloudFormation [custom resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html).

## What are the different programming languages supported by the AWS CDK?
<a name="programming-languages"></a>

The AWS CDK is generally available in JavaScript, TypeScript, Python, Java, C\#, and Go (in Developer Preview).

## How much does the AWS CDK cost?
<a name="cost"></a>

There is no additional charge for the AWS CDK. You pay for AWS resources (such as Amazon EC2 instances or Elastic Load Balancing load balancers) that are created when you use the AWS CDK in the same way as if you created them manually. You only pay for what you use, as you use it. There are no minimum fees and no required upfront commitments.
