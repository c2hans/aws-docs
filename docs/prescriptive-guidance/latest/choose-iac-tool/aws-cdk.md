---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/aws-cdk.html
---

# AWS CDK
<a name="aws-cdk"></a>

The [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is an open source software development framework that lets you define your cloud application resources by using familiar programming languages. The AWS CDK supports JavaScript, TypeScript, Python, Java, C\#, and Go. The AWS CDK provisions your resources in a safe, repeatable manner through AWS CloudFormation. When you synthesize your AWS CDK code, the result is a CloudFormation template. The AWS CDK provides high-level abstractions that simplify the process of defining AWS resources.

The AWS CDK uses the concept of [constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html). A *construct *is a component within your application that represents one or more CloudFormation resources and their configuration, such as an Amazon Simple Storage Service (Amazon S3) bucket. Constructs can be composed and customized to create more complex infrastructure. For more information, see [Construct levels](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html#constructs_lib_levels) in the AWS CDK documentation. The AWS CDK generates CloudFormation templates based on the code written by developers. This eliminates the need for manual CloudFormation template creation. Many organizations customize, share, and reuse constructs within a community, just like any other software library. Sharing constructs helps developers code faster and incorporate best practices by default.

AWS CDK [aspects](https://docs.aws.amazon.com/cdk/v2/guide/aspects.html) can help organizations apply standards to all constructs within a given scope. The aspect could modify the constructs, such as by adding tags. Or it could verify something about the state of the constructs.

The AWS CDK allows developers to use their existing programming skills and knowledge to define cloud infrastructure. By using familiar programming languages, developers can apply their expertise to describe AWS resources, making it easier to transition from application development to infrastructure provisioning. Also the AWS CDK can expedite the creation of AWS infrastructure. This accelerates the development lifecycle compared to manually writing CloudFormation templates.

**Advantages of using the AWS CDK:**
+ The AWS CDK supports well-known programming languages.
+ General-purpose languages allow for the use of logical constructs, such as for-loops, objects, strong types, and other programming techniques. This helps developers declare infrastructure in a concise and error-free manner. This approach also makes it possible to use an integrated development environment (IDE) and related tooling to help manage the complexity around declaring a large number of resources.
+ AWS CDK constructs are shareable and help you meet your governance and compliance requirements.
+ The AWS CDK constructs can decrease time and effort for development. For more information, see the [Construct Library API Reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html).
+ The AWS CDK is based on CloudFormation. If you are familiar with CloudFormation and its concepts, then AWS CDK concepts are easier to understand.
+ The AWS CDK helps you perform [unit tests and snapshot tests](https://docs.aws.amazon.com/cdk/v2/guide/testing.html).
+ If a feature is not supported natively in the AWS CDK, you can use a [Level 1 construct](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html#constructs_lib_levels_one) and [raw overrides](https://docs.aws.amazon.com/cdk/v2/guide/cfn_layer.html#cfn_layer_raw). Alternatively, you can use a [CloudFormation custom resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) that calls the API directly.
+ You can clean up resources efficiently by deleting CloudFormation stacks.

**Disadvantages of using the AWS CDK:**
+ The AWS CDK requires a [bootstrapped environment](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) in each AWS account. Bootstrapping is a one-time action that you must perform for every environment that you deploy resources into.
+ The AWS CDK can be used to deploy IaC only in the AWS Cloud.
