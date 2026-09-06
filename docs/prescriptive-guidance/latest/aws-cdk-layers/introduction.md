---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-cdk-layers/introduction.html
---

# The AWS CDK layer guide
<a name="introduction"></a>

*Steven Guggenheimer, Amazon Web Services*

One of the main concepts behind the AWS Cloud Development Kit (AWS CDK) is a lot like the concept behind staying warm on a cold day. That concept is called *layering*. On a cold day you put on a shirt, a jacket, and sometimes an even bigger jacket depending on how cold it is. Then if you go inside and the heater is blazing, you can take off one or both jacket layers so you're not too hot. The AWS CDK uses layering to provide different levels of abstraction for using cloud components. Layering  ensures that you never have to write too much code or have too little access to resource properties when you deploy your infrastructure as code (IAC) stacks.

If you don't use the AWS CDK, you have to write your [AWS CloudFormation](https://aws.amazon.com/pm/cloudformation/)templates by hand; that is, you're leveraging only a single layer that forces you to write far more code than is usually necessary. On the other hand, if the AWS CDK were to abstract away everything in CloudFormation that you *usually* don't need to write out, you wouldn't be able to handle any edge cases.

To address this issue, the AWS CDK splits resource provisioning into three separate and distinct layers:
+ **Layer 1** – *The CloudFormation layer*: The most basic layer where the CloudFormation resource and the AWS CDK resource are nearly identical.
+ **Layer 2** – *The curated layer*: The layer where CloudFormation resources are abstracted into programmatic classes that streamline much of the boilerplate CloudFormation syntax under the hood. This layer makes up most of the AWS CDK itself.
+ **Layer 3** – *The pattern layer*: The most abstracted layer where you can use the building blocks provided by layers 1 and 2 to customize the code for your specific use case.

Each item from each layer is an instance of a special AWS CDK class called a `Construct`. According to [AWS documentation](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html), constructs are "the basic building blocks of AWS CDK apps. A construct represents a 'cloud component' and encapsulates everything AWS CloudFormation needs to create the component." The constructs within these layers are known as *L1*, *L2, *and *L3 constructs* depending on which layer they belong to. In this guide we'll take a tour through each AWS CDK layer to find out what they're used for and why they matter.

This guide is intended for technical managers, leads, and developers who are interested in digging deeper into the core concepts that make the AWS CDK work. The AWS CDK is a popular tool, but it's very common for teams to miss out on a large portion of what it has to offer. When you begin to understand the concepts described in this guide, you can unlock a whole new world of possibilities and optimize your teams' resource provisioning processes.
