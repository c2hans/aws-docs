---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/constructs-best-practices.html
---

# Create or extend constructs
<a name="constructs-best-practices"></a>

## What a construct is
<a name="what-a-construct-is.96f2869f-3d86-5c01-a71c-dc5f17a6def7"></a>

A construct is the basic building block of an AWS CDK application. A construct can represent a single AWS resource, such as an Amazon Simple Storage Service (Amazon S3) bucket, or it can be a higher-level abstraction consisting of multiple AWS related resources. The components of a construct can include a worker queue with its associated compute capacity, or a scheduled job with monitoring resources and a dashboard. The AWS CDK includes a collection of constructs called the AWS Construct Library. The library contains constructs for every AWS service. You can use the [Construct Hub](https://constructs.dev/search?q=&cdk=aws-cdk&cdkver=2&sort=downloadsDesc&offset=0) to discover additional constructs from AWS, third parties, and the open-source AWS CDK community.

## What the different types of constructs are
<a name="what-the-different-types-of-constructs-are.70b8f853-60c3-506d-a5ae-06f8a7e0ce7c"></a>

There are three different types of constructs for the AWS CDK:
+ **L1 constructs** – Layer 1, or L1, constructs are exactly the resources defined by AWS CloudFormation—no more, no less. You must provide the resources required for configuration yourself. These L1 constructs are very basic and must be manually configured. L1 constructs have a `Cfn`** **prefix and correspond directly to CloudFormation specifications. New AWS services are supported in the AWS CDK as soon as CloudFormation has support for these services. [CfnBucket](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-s3.CfnBucket.html) is a good example of an L1 construct. This class represents an S3 bucket where you must explicitly configure all the properties. We recommend that you only use an L1 construct if you can't find the L2 or L3 construct for it.
+ **L2 constructs** – Layer 2, or L2, constructs have common boilerplate code and glue logic. These constructs come with convenient defaults and reduce the amount of knowledge you need to know about them. L2 constructs use intent-based APIs to construct your resources and typically encapsulate their corresponding L1 modules. A good example of an L2 construct is [Bucket](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html). This class creates an S3 bucket with default properties and methods such as [bucket.addLifeCycleRule()](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-s3.Bucket.html#add-wbr-lifecycle-wbr-rulerule), which adds a lifecycle rule to the bucket.
+ **L3 constructs** – A layer 3, or L3, construct is called a *pattern*. L3 constructs are designed to help you complete common tasks in AWS, often involving multiple kinds of resources. These are even more specific and opinionated than L2 constructs and serve a specific use case. For example, the [aws-ecs-patterns.ApplicationLoadBalancedFargateService ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs_patterns.ApplicationLoadBalancedFargateService.html)construct represents an architecture that includes an AWS Fargate container cluster that uses an Application Load Balancer. Another example is the [aws-apigateway.LambdaRestApi](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.LambdaRestApi.html) construct. This construct represents an Amazon API Gateway API that's backed by a Lambda function.

As construct levels get higher, more assumptions are made as to how these constructs are going to be used. This allows you to provide interfaces with more effective defaults for highly specific use cases.

## How to create your own construct
<a name="how-to-create-your-own-construct.ca4f6cd7-0d46-5622-a408-e99e55b1d570"></a>

To define your own construct, you must follow a specific approach. This is because all constructs extend the `Construct` class. The `Construct` class is the building block of the construct tree. Constructs are implemented in classes that extend the `Construct` base class. All constructs take three parameters when they are initialized:
+ **Scope** – A construct's parent or owner, either a stack or another construct, which determines its place in the construct tree. You usually must pass `this` (or `self` in Python), which represents the current object, for the scope.
+ **id** – An identifier that must be unique within this scope. The identifier serves as a namespace for everything that's defined within the current construct and is used to allocate unique identities, such as resource names and CloudFormation logical IDs.
+ **Props** – A set of properties that define the construct's initial configuration.

The following example shows how to define a construct.

```
import { Construct } from 'constructs';

export interface CustomProps {
  // List all the properties
  Name: string;
}
export class MyConstruct extends Construct {
  constructor(scope: Construct, id: string, props: CustomProps) {
    super(scope, id);

    // TODO
  }
}
```

## Create or extend an L2 construct
<a name="create-or-extend-an-l2-construct.5a333c2f-1b31-5fe4-a5a3-69bda6a5fb80"></a>

An L2 construct represents a "cloud component" and encapsulates everything that CloudFormation must have to create the component. An L2 construct can contain one or more AWS resources, and you're free to customize the construct yourself. The advantage of creating or extending an L2 construct is that you can reuse the components in CloudFormation stacks without redefining the code. You can simply import the construct as a class.

When there's an "is a" relationship to an existing construct you can extend an existing construct to add additional default features. It's a best practice to reuse the properties of the existing L2 construct. You can overwrite properties by modifying the properties directly in the constructor.

The following example shows how to align with best practices and extend an existing L2 construct called `s3.Bucket`. The extension establishes default properties, such as `versioned`, `publicReadAccess`, `blockPublicAccess`, to make sure that all the objects (in this example, S3 buckets) created from this new construct will always have these default values set.

```
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';
export class MySecureBucket extends s3.Bucket {
  constructor(scope: Construct, id: string, props?: s3.BucketProps) {

    super(scope, id, {
      ...props,
      versioned: true,
      publicReadAccess: false,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL
    });
  }
}
```

## Create an L3 construct
<a name="create-an-l3-construct.f654c10a-2258-5370-a81b-1b72b3c147fc"></a>

Composition is the better choice when there's a "has a" relationship with an existing construct composition. Composition means that you build your own construct on top of other existing constructs. You can create your own pattern to encapsulate all the resources and their default values inside a single higher-level L3 construct that can be shared. The benefit of creating your own L3 constructs (patterns) is that you can reuse the components in stacks without redefining the code. You can simply import the construct as a class. These patterns are designed to help consumers provision multiple resources based on common patterns with a limited amount of knowledge in a concise manner.

The following code example creates an AWS CDK construct called `ExampleConstruct`. You can use this construct as a template to define your cloud components.

```
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';

export interface ExampleConstructProps {
  //insert properties you wish to expose
}

export class ExampleConstruct extends Construct {
  constructor(scope: Construct, id: string, props: ExampleConstructProps) {
    super(scope, id);
    //Insert the AWS components you wish to integrate
  }
}
```

The following example shows how to import the newly created construct in your AWS CDK application or stack.

```
import { ExampleConstruct } from './lib/construct-name';
```

The following example shows how you can instantiate an instance of the construct that you extended from the base class.

```
import { ExampleConstruct } from './lib/construct-name';

new ExampleConstruct(this, 'newConstruct', {
  //insert props which you exposed in the interface `ExampleConstructProps`
});
```

For more information, see [AWS CDK Workshop](https://cdkworkshop.com/) in the AWS CDK Workshop documentation.

## Escape hatch
<a name="escape-hatch.35ec269e-416a-5c3c-b27c-197c17ebe3db"></a>

You can use an escape hatch in the AWS CDK to go up an abstraction level so that you can access the lower level of constructs. Escape hatches are used to extend the construct for features which are not exposed with the current version of AWS but available in CloudFormation.

We recommend that you use an escape hatch in the following scenarios:
+ An AWS service feature is available through CloudFormation, but there are no `Construct` constructs for it.
+ An AWS service feature is available through CloudFormation and there are `Construct` constructs for the service, but these don't yet expose the feature. Because `Construct` constructs are developed "by hand," they may sometimes lag behind the CloudFormation resource constructs.

The following example code shows a common use case for using an escape hatch. In this example, the functionality that's not yet implemented in the higher-level construct is for adding `httpPutResponseHopLimit` for autoscaling `LaunchConfiguration`.

```
const launchConfig = autoscaling.onDemandASG.node.findChild("LaunchConfig") as CfnLaunchConfiguration;
            launchConfig.metadataOptions = {
                   httpPutResponseHopLimit: autoscalingConfig.httpPutResponseHopLimit|| 2
            }
```

The preceding code example shows the following workflow:

1. You define your `AutoScalingGroup` by using an L2 construct. The L2 construct doesn't support updating the `httpPutResponseHopLimit`, so you must use an escape hatch.

1. You use the `node.findChild()` method to locate the specific `LaunchConfig` child of the L2 `AutoScalingGroup` construct and cast it as the `CfnLaunchConfiguration` resource.

1. You can now set the `launchConfig.metadataOptions` property on the L1 `CfnLaunchConfiguration`.

## Custom resources
<a name="custom-resources.f0c92d6b-e506-53e7-9f2c-22e1b2255287"></a>

You can use custom resources to write custom provisioning logic in templates that CloudFormation runs whenever you create, update (if you changed the custom resource), or delete stacks. For example, you can use a custom resource if you want to include resources that aren't available in the AWS CDK. That way you can still manage all your related resources in a single stack.

Building a custom resource involves writing a Lambda function that responds to a resource's CREATE, UPDATE, and DELETE lifecycle events. If your custom resource must make only a single API call, consider using the [AwsCustomResource](https://github.com/awslabs/aws-cdk/tree/master/packages/%40aws-cdk/custom-resources) construct. This makes it possible to perform arbitrary SDK calls during a CloudFormation deployment. Otherwise, we suggest that you write your own Lambda function to perform the work that you must get done.

For more information on custom resources, see [Custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) in the CloudFormation documentation. For an example of how to use a custom resource, see the [Custom Resource](https://github.com/aws-samples/aws-cdk-examples/tree/master/typescript/custom-resource/) repository on GitHub.

The following example shows how to create a custom resource class to initiate a Lambda function and send CloudFormation a success or fail signal.

```
import cdk = require('aws-cdk-lib');
import customResources = require('aws-cdk-lib/custom-resources');
import lambda = require('aws-cdk-lib/aws-lambda');
import { Construct } from 'constructs';

import fs = require('fs');

export interface MyCustomResourceProps {
    /**
     * Message to echo
     */
    message: string;
}

export class MyCustomResource extends Construct {
    public readonly response: string;

    constructor(scope: Construct, id: string, props: MyCustomResourceProps) {
        super(scope, id);

        const fn = new lambda.SingletonFunction(this, 'Singleton', {
            uuid: 'f7d4f730-4ee1-11e8-9c2d-fa7ae01bbebc',
            code: new lambda.InlineCode(fs.readFileSync('custom-resource-handler.py', { encoding: 'utf-8' })),
            handler: 'index.main',
            timeout: cdk.Duration.seconds(300),
            runtime: lambda.Runtime.PYTHON_3_6,
        });

        const provider = new customResources.Provider(this, 'Provider', {
            onEventHandler: fn,
        });

        const resource = new cdk.CustomResource(this, 'Resource', {
            serviceToken: provider.serviceToken,
            properties: props,
        });

        this.response = resource.getAtt('Response').toString();
    }
}
```

The following example shows the main logic of the custom resource.

```
def main(event, context):
    import logging as log
    import cfnresponse
    log.getLogger().setLevel(log.INFO)

    # This needs to change if there are to be multiple resources in the same stack
    physical_id = 'TheOnlyCustomResource'

    try:
        log.info('Input event: %s', event)

        # Check if this is a Create and we're failing Creates
        if event['RequestType'] == 'Create' and event['ResourceProperties'].get('FailCreate', False):
            raise RuntimeError('Create failure requested')

        # Do the thing
        message = event['ResourceProperties']['Message']
        attributes = {
            'Response': 'You said "%s"' % message
        }

        cfnresponse.send(event, context, cfnresponse.SUCCESS, attributes, physical_id)
    except Exception as e:
        log.exception(e)
        # cfnresponse's error message is always "see CloudWatch"
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, physical_id)
```

The following example shows how the AWS CDK stack calls the custom resource.

```
import cdk = require('aws-cdk-lib');
import { MyCustomResource } from './my-custom-resource';

/**
 * A stack that sets up MyCustomResource and shows how to get an attribute from it
 */
class MyStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const resource = new MyCustomResource(this, 'DemoResource', {
      message: 'CustomResource says hello',
    });

    // Publish the custom resource output
    new cdk.CfnOutput(this, 'ResponseMessage', {
      description: 'The message that came back from the Custom Resource',
      value: resource.response
    });
  }
}

const app = new cdk.App();
new MyStack(app, 'CustomResourceDemoStack');
app.synth();
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
