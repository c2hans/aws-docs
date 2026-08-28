---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/blueprints.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Configure constructs with CDK Blueprints
<a name="blueprints"></a>

Use AWS CDK Blueprints to standardize and distribute L2 construct configurations across your organization. With Blueprints, you can ensure that AWS resources are configured consistently according to your organizational standards and best practices. For example, you can automatically enable encryption for all Amazon S3 buckets, apply specific logging configurations to all AWS Lambda functions, or enforce standard security rules for all security groups.

Blueprints are powered by *property injection*, a mechanism introduced in AWS CDK [v2.196.0](https://github.com/aws/aws-cdk/releases/tag/v2.196.0) that allows you to modify construct properties at instantiation time. A Blueprint is a collection of property injectors, where each property injector specifies optimal configuration for a specific L2 construct. The Blueprint represents the overall best practices for your organization.

Blueprints are not a compliance enforcement mechanism. Developers can still override the defaults if needed. For strict compliance enforcement, consider using AWS CloudFormation Guard, Service Control Policies, or CDK Aspects in addition to Blueprints.

For detailed implementation information, see the [Property Injection RFC](https://github.com/aws/aws-cdk-rfcs/blob/main/text/0693-property-injection.md).

## Key components of Blueprints
<a name="blueprints-key-pieces"></a>

Blueprints are collections of property injectors that apply default properties to constructs when they’re instantiated. A property injector is a component that implements the `IPropertyInjector` interface, which intercepts construct creation and modifies or adds properties before the construct is created.
+  **IPropertyInjector** - An ` [IPropertyInjector](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.IPropertyInjector.html) ` defines a way to inject additional properties that are not specified in the props. It is specific to one L2 construct and operates on that construct’s properties.
+  **PropertyInjectors** - ` [PropertyInjectors](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.PropertyInjectors.html) ` are a collection of injectors attached to the construct tree. Injectors can be attached to any construct, but in practice we expect most of them will be attached to `App`, `Stage` or `Stack`.

## Common use cases for Blueprints
<a name="blueprints-use-cases"></a>

You can use CDK Blueprints to standardize many aspects of your AWS resources. Here are some common use cases:

 **Security standards**
+ Ensure all Amazon S3 buckets have server-side encryption enabled.
+ Configure all security groups to block public access by default.
+ Apply least-privilege AWS Identity and Access Management (IAM) permissions to AWS Lambda functions.
+ Enforce SSL for all network communications.

 **Operational excellence**
+ Configure standardized logging for all AWS Lambda functions.
+ Apply consistent tagging strategies across resources.
+ Set up default monitoring and alerting thresholds.
+ Implement standard retention policies for logs and backups.

 **Cost optimization**
+ Configure appropriate instance sizes based on environment.
+ Apply auto-scaling policies with organizational defaults.
+ Set lifecycle rules for Amazon S3 buckets to transition objects to cheaper storage classes.
+ Configure default provisioned throughput for databases.

 **Compliance requirements**
+ Implement required encryption settings for regulated data.
+ Apply necessary backup policies for data retention requirements.
+ Configure default Amazon VPC settings that meet security requirements.
+ Ensure resources have required tags for cost allocation.

 **Developer productivity**
+ Provide sensible defaults that reduce the need for boilerplate code.
+ Create organization-specific Stack classes with built-in injectors.
+ Share best practices across teams through reusable injectors.
+ Simplify onboarding by encoding organizational knowledge in code.

## Getting started with Blueprints
<a name="blueprints-getting-started"></a>

Here’s a simple example of how to create and use a property injector:

First, create a property injector for Amazon S3 buckets:

```
import { IPropertyInjector, InjectionContext } from 'aws-cdk-lib';
import { Bucket, BucketProps, BlockPublicAccess } from 'aws-cdk-lib/aws-s3';

export class SecureBucketDefaults implements IPropertyInjector {
  public readonly constructUniqueId: string;

  constructor() {
    this.constructUniqueId = Bucket.PROPERTY_INJECTION_ID;
  }

  public inject(originalProps: BucketProps, _context: InjectionContext): BucketProps {
    return {
      // Set security defaults
      blockPublicAccess: BlockPublicAccess.BLOCK_ALL,
      enforceSSL: true,

      // Include original props to allow overrides
      ...originalProps,
    };
  }
}
```

Then, use the injector in your CDK application:

```
import { App, Stack } from 'aws-cdk-lib';
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { SecureBucketDefaults } from './secure-bucket-defaults';

// Attach injectors when creating the App
const app = new App({
  propertyInjectors: [new SecureBucketDefaults()]
});

const stack = new Stack(app, 'MyStack');

// This bucket automatically gets the default properties
const myBucket = new Bucket(stack, 'MyBucket');
```

Alternatively, you can use the `PropertyInjectors.of()` method:

```
import { App, Stack, PropertyInjectors } from 'aws-cdk-lib';
import { SecureBucketDefaults } from './secure-bucket-defaults';

const app = new App();
PropertyInjectors.of(app).add(new SecureBucketDefaults());

const stack = new Stack(app, 'MyStack');
const myBucket = new Bucket(stack, 'MyBucket');
```

## Best practices
<a name="blueprints-best-practices"></a>
+ Place default properties before `…​originalProps` to allow overrides.
+ Place forced properties after `…​originalProps` to prevent overrides.
+ Use a skip flag when creating resources to prevent infinite recursion. For an example, see [What happens when you need to create a accessLogBucket for a Bucket?](https://github.com/aws/aws-cdk-rfcs/blob/main/text/0693-property-injection.md#what-happens-when-you-need-to-create-a-accesslogbucket-for-a-bucket) in the *Property Injection RFC*.
+ Add logging for debugging.
+ Use CDK context to enable/disable injectors for testing.

For more detailed information about property injection, including implementation details, troubleshooting tips, and reference information, see the [Property Injection RFC](https://github.com/aws/aws-cdk-rfcs/blob/main/text/0693-property-injection.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
