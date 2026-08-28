---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/refactor.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Preserve deployed resources when refactoring CDK code
<a name="refactor"></a>

**Important**
CDK refactoring is in preview release and is subject to change.

With AWS Cloud Development Kit (AWS CDK) refactoring, you can refactor your CDK code, such as renaming constructs, moving resources between stacks, and reorganizing your application, while preserving your deployed resources instead of replacing them. This feature helps you maintain good software engineering best practices without resulting in unintentional resource replacements.

## What is CDK refactoring with resource preservation?
<a name="refactor-intro"></a>

When you deploy a CDK application, AWS CloudFormation identifies resources by their logical IDs. The AWS CDK generates these logical IDs based on the construct ID and its path in the construct tree. If you change a construct’s ID or move it to a different location in your code, AWS CloudFormation typically interprets this as a request to create a new resource and delete the old one. For stateful resources such as databases, storage buckets, or queues, this replacement can cause service interruptions or data loss.

**Tip**
You can proactively prevent logical ID changes when you extract resources into higher-level constructs. By using `Default` as the construct ID for the primary resource in a wrapper construct, the logical ID remains unchanged. For more information, see [Logical ID path component heuristics](identifiers.md#identifiers-logical-id-heuristics).

CDK refactoring addresses this challenge by:
+ Detecting when resources have been moved or renamed in your code.
+ Using AWS CloudFormation’s refactoring capabilities to preserve the underlying physical resources.
+ Updating logical IDs without replacing the actual resources.
+ Maintaining references between resources across your stacks.

You can perform CDK refactoring using either the CDK CLI `cdk refactor` command or the CDK Toolkit Library’s `refactor` action. This guide primarily discusses the CLI approach, but the underlying principles apply to both methods. For information on using the Toolkit Library, see [Perform programmatic actions using the CDK Toolkit Library](toolkit-library.md).

**Important**
Refactoring operations must be performed alone, separately from other actions, such as adding new resources, deleting resources, or modifying resource properties.
If you need to add, delete, or modify resources as well as refactor, you should first deploy those changes separately, and then use refactoring to reorganize your resources.

## Benefits of CDK refactoring
<a name="refactor-benefits"></a>

CDK refactoring offers the following benefits for AWS CDK developers:
+  **Improve code organization** – Rename constructs and reorganize your CDK application’s structure without resource replacement.
+  **Create reusable components** – Extract duplicated code into reusable L3 constructs while preserving deployed resources.
+  **Enhance architectural separation** – Move resources between stacks to better isolate different parts of your application.
+  **Prevent accidental resource replacement** – Avoid unintended resource recreation when renaming constructs.
+  **Mitigate third-party library changes** – Protect your application from logical ID changes in construct libraries you depend on.
+  **Apply software engineering best practices** – Refactor your code without compromising your deployed infrastructure.

## How the CDK CLI `cdk refactor` command works
<a name="refactor-how"></a>

**Important**
You must provide the `--unstable=refactor` option with all commands that use this feature.

First, you deploy your initial CDK application to establish baseline resources in your AWS account. After refactoring your CDK code, such as renaming constructs or moving resources between stacks, use the `cdk refactor` command to begin the process of refactoring your deployed resources.

When you run the refactor command, the CDK CLI detects your local changes by comparing your current code with the deployed state. It verifies that your CDK application contains exactly the same set of resources as the deployed state, differing only in their locations in the construct tree. The CDK CLI then generates a refactor plan that maps the old resource locations to their new locations. The CDK CLI shows you the proposed changes and, after your confirmation, uses AWS CloudFormation’s refactoring API to update the logical IDs of resources without replacing them.

Behind the scenes, the CDK CLI determines which resources have been moved by comparing their properties and dependencies, identifying resources that are functionally equivalent but have different paths in the construct tree. If it detects any resource additions, deletions, or modifications, the refactoring operation will be rejected with an error message.

## Example of preserving resources when refactoring CDK code
<a name="refactor-example"></a>

In this example, we preserve deployed resources while refactoring our CDK code using the CDK CLI `cdk refactor` command.

Our example CDK application consists of a single stack containing an S3 bucket, a CloudFront distribution, and a Lambda function. The construct tree is structured as follows:

```
App
└─ MyStack
   ├─ Bucket
   ├─ Distribution
   └─ Function
```

The following is an example of our application code:

```
const app = new cdk.App();
const myStack = new cdk.Stack(app, 'MyStack');

const bucket = new s3.Bucket(myStack, 'Bucket');
const distribution = new cloudfront.Distribution(myStack, 'Distribution', {
  defaultBehavior: { origin: new origins.S3Origin(bucket) }
});
const function = new lambda.Function(myStack, 'Function', {
  // function properties
});

// Synthesize the app
app.synth();
```

Now, imagine you want to refactor this code to:

1. Rename the bucket from `Bucket` to the more descriptive `WebsiteOrigin`.

1. Move the bucket and distribution to a new `WebStack` stack.

After refactoring, the construct tree would look like this:

```
App
├─ WebStack
│  ├─ WebsiteOrigin
│  └─ Distribution
└─ MyStack
   └─ Function
```

And the refactored code would be:

```
// Refactored structure
const app = new cdk.App();

// New WebStack with the bucket and distribution
const webStack = new cdk.Stack(app, 'WebStack');
const bucket = new s3.Bucket(webStack, 'WebsiteOrigin');
const distribution = new cloudfront.Distribution(webStack, 'Distribution', {
  defaultBehavior: { origin: new origins.S3Origin(bucket) }
});

// Original MyStack with just the function
const myStack = new cdk.Stack(app, 'MyStack');
const function = new lambda.Function(myStack, 'Function', {
  // function properties
});

// Synthesize the app
app.synth();
```

Without CDK refactoring, these changes would cause AWS CloudFormation to create new resources and delete the old ones, because the logical IDs would change:
+  `MyStack/Bucket/Resource` would become `WebStack/WebsiteOrigin/Resource`.
+  `MyStack/Distribution/Resource` would become `WebStack/Distribution/Resource`.

With CDK refactoring, the CDK CLI detects these path changes and uses AWS CloudFormation’s refactoring capabilities to preserve the underlying resources. When you run `cdk refactor`, the CLI shows you the changes it will make:

```
$ cdk refactor

The following resources were moved or renamed:

┌───────────────────────────────┬───────────────────────────────┬───────────────────────────────────┐
│ Resource Type                 │ Old Construct Path            │ New Construct Path                │
├───────────────────────────────┼───────────────────────────────┼───────────────────────────────────┤
│ AWS::S3::Bucket               │ MyStack/Bucket/Resource       │ WebStack/WebsiteOrigin/Resource   │
├───────────────────────────────┼───────────────────────────────┼───────────────────────────────────┤
│ AWS::CloudFront::Distribution │ MyStack/Distribution/Resource │ WebStack/Distribution/Resource    │
└───────────────────────────────┴───────────────────────────────┴───────────────────────────────────┘

Do you wish refactor these resources (y/n)?
```

When you confirm by entering `y`, the CDK CLI shows the progress of the refactoring operation:

```
Refactoring...
✅  Stack refactor complete
```

After confirming, the CDK CLI runs the refactoring operation, preserving both resources while updating their logical IDs to match your new code structure.

The same mapping is also shown in the output of the `cdk diff` command, organized by stack:

```
Stack MyStack
Resources
[-] AWS::S3::Bucket Bucket Bucket1234567 destroy (OR move to WebStack.WebsiteOrigin1234567 via refactoring)
[-] AWS::CloudFront::Distribution Distribution Distribution1234567 destroy (OR move to WebStack.Distribution1234567)
...

Stack WebStack
Resources
[+] AWS::S3::Bucket WebsiteOrigin WebsiteOrigin1234567 (OR move from MyStack.Bucket1234567)
[+] AWS::CloudFront::Distribution Distribution Distribution1234567 (OR move from MyStack.Distribution1234567)
...
```

## Get started with CDK refactoring
<a name="_get_started_with_cdk_refactoring"></a>

To get started with refactoring, complete these prerequisites:

 **Bootstrap your environment with the latest template**
The CDK refactoring feature requires new permissions in the bootstrap stack. To ensure you have the necessary permissions, bootstrap your environment with the latest template:

```
cdk bootstrap
```
For more information on bootstrapping, see [Bootstrapping environments for AWS CDK](bootstrapping-env.md).

 **Install the latest CDK CLI version**
CDK refactoring requires a recent version of the CDK CLI. To ensure you have the latest version:

```
npm install -g aws-cdk
```
For detailed installation instructions, see [Getting started with the AWS CDK](getting-started.md).

## Use override files to resolve ambiguities in refactoring
<a name="override-file"></a>

The CDK CLI automatically computes all resource mappings based on comparing your code to the deployed resources. In most cases, this automatic detection works well, but there are situations where the CLI might encounter ambiguities it can’t resolve on its own. To provide guidance to the CDK CLI, use an override file.

 **Create an override file to resolve ambiguities**
An override file is a JSON file that provides mappings when the CDK CLI is unable to determine a refactoring resolution for resources. The file contains resource mappings organized by environment:

```
{
    "environments": [
        {
            "account": "123456789012",
            "region": "us-east-2",
            "resources": {
                "StackA.OldName": "StackB.NewName",
                "StackC.Foo": "StackC.Bar"
            }
        }
    ]
}
```
In this file:
+ The `environments` array contains one or more environment entries with account and region.
+ Within each environment, the `resources` object contains the mappings.
+ Keys represent the current locations in the format `<stack name>.<logical ID>`.
+ Values represent the new locations in the same format.
To use an override file with the CDK CLI:

```
cdk refactor --override-file=overrides.json
```

## Refactoring stacks across multiple environments
<a name="refactor-environments"></a>

A CDK application can contain multiple stacks that deploy to different environments (AWS accounts and Regions). When preserving resources during refactoring in such applications, the CDK CLI handles environments in a specific way:
+ The CLI groups stacks by environment and performs refactoring separately in each environment.
+ You can move resources between stacks during refactoring, but all stacks involved in the move must be in the same environment.
+ Attempting to move resources across environments will result in an error.

This behavior ensures that resources remain within their original AWS account and Region, which is necessary because CloudFormation resources cannot be physically moved across account or Region boundaries.

For example, if your CDK application defines stacks for both development and production environments, the refactoring operation will be performed independently in each environment. Resources can be moved between stacks within the development environment or within the production environment, but not from development to production or vice versa.

## Handling resources designed to be replaced
<a name="refactor-replaceable-resources"></a>

Some CDK constructs rely on CloudFormation’s resource replacement behavior as part of their design. For example, API Gateway’s `Deployment` and Lambda’s `Version` constructs are designed to create new resources when their properties change.

When refactoring, do not include any changes that should result in resource replacements. Otherwise, the CDK CLI may detect and preserve these resources. This means that resources that are designed to be replaced must be handled separately from refactoring operations.

To properly manage resources designed to be replaced:

1. First, deploy your application to replace these resources as needed.

1. Then, perform your refactoring operations separately to reorganize your code.

This two-step approach ensures that resources designed to be replaced are properly handled, while still allowing you to benefit from CDK refactoring for other resources.

## General considerations and limitations
<a name="refactor-considerations"></a>

When preserving resources during CDK refactoring, keep these considerations in mind:
+  **Environment constraints**: Resources can only be moved between stacks in the same environment. Cross-environment moves are not supported.
+  **Ambiguity**: If you have multiple identical resources that are renamed simultaneously, the CDK CLI may not be able to determine the correct mapping automatically. In these cases, you’ll need to provide an explicit mapping using an override file.
+  **Bootstrap requirements**: To preserve resources during refactoring, you need to update your bootstrap stack with the latest version that includes the necessary permissions.
+  **Certain constructs excluded**: Some constructs like API Gateway’s `Deployment` and Lambda’s `Version` rely on resource replacement and are automatically excluded from refactoring.

## Refactoring with CI/CD pipelines
<a name="refactor-pipelines"></a>

To use the refactoring feature in CI/CD pipelines, you need to be able to run the CDK CLI as part of your pipeline. The following are some important considerations for integrating refactoring into your CI/CD workflow.

 **Prerequisites for using refactoring in CI/CD**
You must be able to use the CDK CLI in your CI/CD environment to benefit from this feature.

 **Integrating refactoring into your pipeline workflow**
If you are using the CLI for deployment in your CI/CD pipeline, your script typically looks like:

```
...
cdk deploy <stack filter>
...
```
If you want to include refactoring as part of the workflow, the following is a basic example:

```
...
cdk refactor <stack filter>
cdk deploy <stack filter>
...
```
You can also have refactoring as a separate step in your pipeline.

 **Handling refactor failures**
Be aware that `cdk refactor` will fail if your code includes actual resource modifications alongside refactoring. Since you’re calling refactor automatically in your pipeline, you need to handle potential failures:

```
# Allow refactoring to fail but continue the pipeline
cdk refactor <stack filter> || true
cdk deploy <stack filter>
```
Alternatively, you might want to ensure that no deployment happens until you’ve run a successful refactor:

```
# Only deploy if refactoring succeeds
cdk refactor <stack filter> && cdk deploy <stack filter>
```

 **Best practices for CI/CD environments**
To use refactoring effectively in CI/CD pipelines:
+  **Separate refactoring from other changes**: Remember that refactoring operations must be separate from resource additions, deletions, or modifications. In your pipeline, consider having dedicated commits and deployments for refactoring.
+  **Use override files appropriately**: Understand that override files are used by the CDK CLI only as a fallback to resolve ambiguity cases.
+  **No need for `--force` in pipelines**: In non-interactive environments like CI/CD pipelines, the CDK refactor command automatically proceeds without prompting for confirmation. The `--force` option is only needed in interactive environments.

## Related resources
<a name="refactor-resources"></a>

For information on options and arguments for the CDK CLI `cdk refactor` command, see ` cdk refactor `.

To get started with the CDK Toolkit Library’s `refactor` action, see [Perform programmatic actions using the CDK Toolkit Library](toolkit-library.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
