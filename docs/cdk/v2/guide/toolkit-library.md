---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/toolkit-library.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Perform programmatic actions using the CDK Toolkit Library
<a name="toolkit-library"></a>

## Understanding the CDK Toolkit Library
<a name="toolkit-library-intro"></a>

The CDK Toolkit Library enables you to perform CDK actions programmatically through code instead of using CLI commands. You can use this library to create custom tools, build specialized CLI applications, and integrate CDK capabilities into your development workflows.

 **Manage your infrastructure lifecycle with programmatic control**
The CDK Toolkit Library provides programmatic interfaces for the following CDK actions:
+  **Synthesis** - Generate AWS CloudFormation templates and deployment artifacts.
+  **Deployment** - Provision or update infrastructure using CloudFormation templates.
+  **Refactor** - Preserve deployed resources when refactoring CDK code, such as renaming constructs or moving them between stacks.
+  **List** - View information about stacks and their dependencies.
+  **Watch** - Monitor CDK apps for local changes.
+  **Rollback** - Return stacks to their last stable state.
+  **Destroy** - Remove CDK stacks and associated resources.

 **Enhance and customize your infrastructure management**
+  **Control through code** - Integrate infrastructure management directly into your applications and build responsive deployment pipelines.
+  **Manage cloud assemblies** - Create, inspect, and transform your infrastructure definitions before deployment.
+  **Customize deployments** - Configure parameters, rollback behavior, and monitoring to match your requirements.
+  **Preserve resources during refactoring** - Automatically detect and preserve resources when you refactor CDK code.
+  **Handle errors precisely** - Implement structured error handling with detailed diagnostic information.
+  **Tailor communications** - Configure custom progress indicators and logging through `IoHost` implementations.
+  **Connect with AWS ** - Configure profiles, Regions, and authentication flows programmatically.

## Choosing when to use the CDK Toolkit Library
<a name="toolkit-library-intro-when"></a>

The CDK Toolkit Library is particularly valuable when you need to:
+ Automate infrastructure deployments as part of CI/CD pipelines.
+ Build custom deployment tools tailored to your organization’s needs.
+ Integrate CDK actions into existing applications or platforms.
+ Create specialized deployment workflows with custom validation or approval steps.
+ Implement advanced infrastructure management patterns across multiple environments.
+ Automate refactoring operations to preserve resources when you refactor CDK code.

## Using the CDK Toolkit Library
<a name="toolkit-library-intro-example"></a>

The following example shows how to create and deploy a simple S3 bucket using the CDK Toolkit Library:

```
// Import required packages
import { Toolkit } from '@aws-cdk/toolkit-lib';
import { App, Stack } from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';

// Create and configure the CDK Toolkit
const toolkit = new Toolkit();

// Create a cloud assembly source with an inline app
const cloudAssemblySource = await toolkit.fromAssemblyBuilder(async () => {
   const app = new App();
   const stack = new Stack(app, 'SimpleStorageStack');

   // Create an S3 bucket in the stack
   new s3.Bucket(stack, 'MyFirstBucket', {
      versioned: true
   });

   return app.synth();
});

// Deploy the stack
await toolkit.deploy(cloudAssemblySource);
```

 **What you can do next**
+  **Automate deployments** - Trigger deployments programmatically and add pre/post deployment steps.
+  **Integrate with systems** - Connect with CI/CD workflows, custom tools, and monitoring solutions.
+  **Control deployment details** - Configure fine-grained options for stack selection and multi-environment deployments.
+  **Enhance reliability** - Implement production-ready error handling and deployment progress tracking.
+  **Automate refactoring** - Detect and preserve resources when you refactor CDK code.

## Next steps
<a name="toolkit-library-intro-next"></a>

To begin using the CDK Toolkit Library, see [Get started with the CDK Toolkit Library](toolkit-library-gs.md).

## Learn more
<a name="toolkit-library-intro-learn"></a>

To learn more about the CDK Toolkit Library, see the following:
+  [ReadMe](https://www.npmjs.com/package/@aws-cdk/toolkit-lib) in the *@aws-cdk/toolkit-lib* `npm` package.
+  [AWS CDK Toolkit Library API Reference](https://docs.aws.amazon.com/cdk/api/toolkit-lib/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
