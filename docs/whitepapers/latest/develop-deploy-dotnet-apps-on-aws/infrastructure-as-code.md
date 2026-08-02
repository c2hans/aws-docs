---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/infrastructure-as-code.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Infrastructure as Code
<a name="infrastructure-as-code"></a>

Modern deployment patterns require that applications, and the services and infrastructure and those applications depend on, can be provisioned and deployed reliably and consistently.

Given the complexity of deploying modern applications and infrastructure, doing so in a repeatable manner requires the deployment to be automated, and the practice and processes of automating infrastructure deployment are commonly known as Infrastructure as Code.

## AWS CloudFormation
<a name="aws-cloudformation"></a>

 [AWS CloudFormation](https://aws.amazon.com/cloudformation/) provides a declarative language that allows you to describe and provision all the infrastructure resources in your AWS Cloud environment.

Using a simple text file called an [AWS CloudFormation template](https://aws.amazon.com/cloudformation/resources/templates/), you can model resources across all [Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) and accounts, with the file serving as the single source of truth for your cloud environment. By keeping CloudFormation templates along with your application code in the same code repository, you can ensure code changes are bundled together with infrastructure changes, ensuring integrity and enabling reliable deployment.

Templates can be written using [JavaScript Object Notation](https://www.json.org/json-en.html) (JSON) or [YAML](https://yaml.org/). There are many predeveloped templates you can use as starting point, or you can create your templates from scratch.

You can use a variety of methods to deploy templates and provision resources, including the AWS Management Console, AWS Command Line Interface (AWS CLI), and PowerShell or the AWS SDK for .NET. You can also use the [AWS Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/) to create and develop CloudFormation templates, with assistance of [Intellisense](https://www.intellisenseinc.com/), and also directly deploy them into AWS from within the IDE.

A deployed version of a CloudFormation template is called a [CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html). You can instantiate one or multiple stacks based on each CloudFormation template, and delete deployed stacks and all resources associated with them. AWS CloudFormation is a powerful way to quickly deploy, duplicate, provision or deprovision resources of your applications.

CloudFormation stacks are always deployed in a single AWS Account and Region, but you can use [CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy your templates across multiple AWS Accounts and Regions.

## AWS Cloud Development Kit (AWS CDK)
<a name="aws-cloud-development-kit"></a>

Although CloudFormation provides a flexible mechanism to define cloud infrastructure as code, its use of declarative syntax is not well suited in all situations.

For infrastructure requiring a high number of interrelated services, or that is best defined using iteration, the resulting CloudFormation template can easily grow to hundreds or thousands of lines, which raises its own complications.

The [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/) (AWS CDK) enables you to define cloud resources in various programming languages, including TypeScript, JavaScript, Python, C\#, and Java. Developers use one of the supported languages to write code that defines reusable cloud components known as Constructs, which can then be composed into Stacks and Apps.

After you’ve defined an AWS CDK App, you can use the AWS CDK toolkit to synthesize a CloudFormation template, and then to deploy the defined resources to AWS.

Although using the AWS CDK adds an additional level of complexity to your Infrastructure as Code, by using an imperative language it allows you to work with high-level abstractions, rich logic, and enables the sharing of infrastructure definitions as reusable libraries of components.
