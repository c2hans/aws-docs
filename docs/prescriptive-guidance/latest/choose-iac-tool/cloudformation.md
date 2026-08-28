---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/cloudformation.html
---

# CloudFormation
<a name="cloudformation"></a>

[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) is an AWS service that uses template files to automate the provisioning of AWS resources. You create a template that describes all of the AWS resources that you want to deploy, and CloudFormation provisions and configures those resources for you.

CloudFormation templates are written by using JSON or YAML. A CloudFormation *stack* is the implementation of the resources defined in your template. You can manage your CloudFormation stacks through the AWS Management Console, programmatically through the CloudFormation SDK, or through the AWS Command Line Interface (AWS CLI). For more information about how CloudFormation works, see [AWS CloudFormation concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) and [How does AWS CloudFormation work](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html) in the CloudFormation documentation.

**Advantages of using CloudFormation:**
+ CloudFormation [change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#cfn-concepts-change-sets) allow you to preview changes to a running stack before you deploy those changes. *Change sets* summarize the proposed changes to the running resources in an existing stack. This can help you identify conflicts or unintended consequences before deployment. For example, if you change the name of an Amazon Relational Database Service (Amazon RDS) database instance, CloudFormation will create a new database and delete the old one. You would lose the data in the old database unless you've already backed it up. If you generate a change set, you see that your change will cause your database to be replaced, and you will be able to plan accordingly before you update your stack.
+ If an error occurs during the deployment of a change set, CloudFormation rolls back automatically to the last known working state.
+ You can use CloudFormation [stack sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy resources across multiple AWS accounts and AWS Regions.
+ There is no additional charge for using CloudFormation with resource providers in the following namespaces: AWS::\*, Alexa::\*, and Custom::\*. In these cases, you pay only for the AWS resources that you provision, as if you had provisioned them manually.
+ CloudFormation manages state for you. This means that CloudFormation makes underlying service calls to AWS to provision and configure your resources as defined in your CloudFormation templates.
+ CloudFormation provides tools to detect and remediate configuration drift. For more information, see [Detecting unmanaged configuration changes to stacks and resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) in the CloudFormation documentation.
+ You can use CloudFormation to create [custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html). You can write custom provisioning logic in templates that CloudFormation runs anytime you create, update, or delete stacks.
+ CloudFormation supports the modeling, provisioning, and managing of third-party application resources with [CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html).
+ CloudFormation supports [importing existing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html) into CloudFormation management.

**Disadvantages of using CloudFormation:**
+ If you are not familiar with JSON or YAML syntax, it may take some getting used to. JSON was not designed to be human readable, and it does not allow you to make inline comments. YAML allows you to make comments and is easier to read. However, its syntax is based on tabs and spaces, so it can be easy to make indentation mistakes.
+ CloudFormation does not support multi-cloud deployments.
+ You must use a higher-level implementation, such as the AWS Cloud Development Kit (AWS CDK), to create reusable constructs and other modularized code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
