---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/resources.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Resources and the AWS CDK
<a name="resources"></a>

 *Resources* are what you configure to use AWS services in your applications. Resources are a feature of AWS CloudFormation. By configuring resources and their properties in a AWS CloudFormation template, you can deploy to AWS CloudFormation to provision your resources. With the AWS Cloud Development Kit (AWS CDK), you can configure resources through constructs. You then deploy your CDK app, which involves synthesizing a AWS CloudFormation template and deploying to AWS CloudFormation to provision your resources.

## Configuring resources using constructs
<a name="resources-configure"></a>

As described in [AWS CDK Constructs](constructs.md), the AWS CDK provides a rich class library of constructs, called *constructs*, that represent all AWS resources.

To create an instance of a resource using its corresponding construct, pass in the scope as the first argument, the logical ID of the construct, and a set of configuration properties (props). For example, here’s how to create an Amazon SQS queue with AWS KMS encryption using the [`sqs.Queue`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html) construct from the AWS Construct Library.

**Example**

```
import * as sqs from '@aws-cdk/aws-sqs';

new sqs.Queue(this, 'MyQueue', {
    encryption: sqs.QueueEncryption.KMS_MANAGED
});
```

```
const sqs = require('@aws-cdk/aws-sqs');

new sqs.Queue(this, 'MyQueue', {
    encryption: sqs.QueueEncryption.KMS_MANAGED
});
```

```
import aws_cdk.aws_sqs as sqs

sqs.Queue(self, "MyQueue", encryption=sqs.QueueEncryption.KMS_MANAGED)
```

```
import software.amazon.awscdk.services.sqs.*;

Queue.Builder.create(this, "MyQueue").encryption(
        QueueEncryption.KMS_MANAGED).build();
```

```
using Amazon.CDK.AWS.SQS;

new Queue(this, "MyQueue", new QueueProps
{
    Encryption = QueueEncryption.KMS_MANAGED
});
```

```
import (
  "github.com/aws/aws-cdk-go/awscdk/v2"
  "github.com/aws/jsii-runtime-go"
  sqs "github.com/aws/aws-cdk-go/awscdk/v2/awssqs"
)

sqs.NewQueue(stack, jsii.String("MyQueue"), &sqs.QueueProps{
  Encryption: sqs.QueueEncryption_KMS_MANAGED,
})
```

Some configuration props are optional, and in many cases have default values. In some cases, all props are optional, and the last argument can be omitted entirely.

### Resource attributes
<a name="resources-attributes"></a>

Most resources in the AWS Construct Library expose attributes, which are resolved at deployment time by AWS CloudFormation. Attributes are exposed in the form of properties on the resource classes with the type name as a prefix. The following example shows how to get the URL of an Amazon SQS queue using the `queueUrl` (Python: `queue_url`) property.

**Example**

```
import * as sqs from '@aws-cdk/aws-sqs';

const queue = new sqs.Queue(this, 'MyQueue');
const url = queue.queueUrl; // => A string representing a deploy-time value
```

```
const sqs = require('@aws-cdk/aws-sqs');

const queue = new sqs.Queue(this, 'MyQueue');
const url = queue.queueUrl; // => A string representing a deploy-time value
```

```
import aws_cdk.aws_sqs as sqs

queue = sqs.Queue(self, "MyQueue")
url = queue.queue_url # => A string representing a deploy-time value
```

```
Queue queue = new Queue(this, "MyQueue");
String url = queue.getQueueUrl();    // => A string representing a deploy-time value
```

```
var queue = new Queue(this, "MyQueue");
var url = queue.QueueUrl; // => A string representing a deploy-time value
```

```
import (
  "github.com/aws/aws-cdk-go/awscdk/v2"
  "github.com/aws/jsii-runtime-go"
  sqs "github.com/aws/aws-cdk-go/awscdk/v2/awssqs"
)

queue := sqs.NewQueue(stack, jsii.String("MyQueue"), &sqs.QueueProps{})
url := queue.QueueUrl() // => A string representing a deploy-time value
```

See [Tokens and the AWS CDK](tokens.md) for information about how the AWS CDK encodes deploy-time attributes as strings.

## Referencing resources
<a name="resources-referencing"></a>

When configuring resources, you will often have to reference properties of another resource. The following are examples:
+ An Amazon Elastic Container Service (Amazon ECS) resource requires a reference to the cluster on which it runs.
+ An Amazon CloudFront distribution requires a reference to the Amazon Simple Storage Service (Amazon S3) bucket containing the source code.

You can reference resources in any of the following ways:
+ By passing a resource defined in your CDK app, either in the same stack or in a different one
+ By passing a proxy object referencing a resource defined in your AWS account, created from a unique identifier of the resource (such as an ARN)

If the property of a construct represents a construct for another resource, its type is that of the interface type of the construct. For example, the Amazon ECS construct takes a property `cluster` of type `ecs.ICluster`. Another example, is the CloudFront distribution construct that takes a property `sourceBucket` (Python: `source_bucket`) of type `s3.IBucket`.

You can directly pass any resource object of the proper type defined in the same AWS CDK app. The following example defines an Amazon ECS cluster and then uses it to define an Amazon ECS service.

**Example**

```
const cluster = new ecs.Cluster(this, 'Cluster', { /*...*/ });

const service = new ecs.Ec2Service(this, 'Service', { cluster: cluster });
```

```
const cluster = new ecs.Cluster(this, 'Cluster', { /*...*/ });

const service = new ecs.Ec2Service(this, 'Service', { cluster: cluster });
```

```
cluster = ecs.Cluster(self, "Cluster")

service = ecs.Ec2Service(self, "Service", cluster=cluster)
```

```
Cluster cluster = new Cluster(this, "Cluster");
Ec2Service service = new Ec2Service(this, "Service",
        new Ec2ServiceProps.Builder().cluster(cluster).build());
```

```
var cluster = new Cluster(this, "Cluster");
var service = new Ec2Service(this, "Service", new Ec2ServiceProps { Cluster = cluster });
```

```
import (
  "github.com/aws/aws-cdk-go/awscdk/v2"
  "github.com/aws/jsii-runtime-go"
  ecs "github.com/aws/aws-cdk-go/awscdk/v2/awsecs"
)

cluster := ecs.NewCluster(stack, jsii.String("MyCluster"), &ecs.ClusterProps{})
service := ecs.NewEc2Service(stack, jsii.String("MyService"), &ecs.Ec2ServiceProps{
  Cluster: cluster,
})
```

### Referencing resources in a different stack
<a name="resource-stack"></a>

You can refer to resources in a different stack, as long as they are defined in the same app. The stacks can be in the same or different AWS environments (accounts and regions). The following pattern is generally used:
+ Store a reference to the construct as an attribute of the stack that produces the resource. (To get a reference to the current construct’s stack, use `Stack.of(this)`.)
+ Pass this reference to the constructor of the stack that consumes the resource as a parameter or a property. The consuming stack then passes it as a property to any construct that needs it.

The following example defines a stack `stack1`. This stack defines an Amazon S3 bucket and stores a reference to the bucket construct as an attribute of the stack. Then the app defines a second stack, `stack2`, which accepts a bucket at instantiation. `stack2` might, for example, define an AWS Glue Table that uses the bucket for data storage.

**Example**

```
const prod = { account: '123456789012', region: 'us-east-1' };

const stack1 = new StackThatProvidesABucket(app, 'Stack1', { env: prod });

// stack2 will take a property { bucket: IBucket }
const stack2 = new StackThatExpectsABucket(app, 'Stack2', {
  bucket: stack1.bucket,
  env: prod
});
```

```
const prod = { account: '123456789012', region: 'us-east-1' };

const stack1 = new StackThatProvidesABucket(app, 'Stack1', { env: prod });

// stack2 will take a property { bucket: IBucket }
const stack2 = new StackThatExpectsABucket(app, 'Stack2', {
  bucket: stack1.bucket,
  env: prod
});
```

```
prod = core.Environment(account="123456789012", region="us-east-1")

stack1 = StackThatProvidesABucket(app, "Stack1", env=prod)

# stack2 will take a property "bucket"
stack2 = StackThatExpectsABucket(app, "Stack2", bucket=stack1.bucket, env=prod)
```

```
// Helper method to build an environment
static Environment makeEnv(String account, String region) {
    return Environment.builder().account(account).region(region)
            .build();
}

App app = new App();

Environment prod = makeEnv("123456789012", "us-east-1");

StackThatProvidesABucket stack1 = new StackThatProvidesABucket(app, "Stack1",
        StackProps.builder().env(prod).build());

// stack2 will take an argument "bucket"
StackThatExpectsABucket stack2 = new StackThatExpectsABucket(app, "Stack,",
        StackProps.builder().env(prod).build(), stack1.bucket);
```

```
Amazon.CDK.Environment makeEnv(string account, string region)
{
    return new Amazon.CDK.Environment { Account = account, Region = region };
}

var prod = makeEnv(account: "123456789012", region: "us-east-1");

var stack1 = new StackThatProvidesABucket(app, "Stack1", new StackProps { Env = prod });

// stack2 will take a property "bucket"
var stack2 = new StackThatExpectsABucket(app, "Stack2", new StackProps { Env = prod,
    bucket = stack1.Bucket});
```

If the AWS CDK determines that the resource is in the same environment, but in a different stack, it automatically synthesizes AWS CloudFormation [exports](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html) in the producing stack and an [`Fn::ImportValue`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html) in the consuming stack to transfer that information from one stack to the other. This is a **strong** reference—the default behavior. You can control the strength of cross-stack references to avoid dependency deadlocks.

#### Reference strength
<a name="resources-reference-strength"></a>

Every cross-stack reference has a **strength** that determines the CloudFormation mechanism used and the coupling between stacks:

 **Strong** (default)
The producing stack creates a CloudFormation export and the consuming stack uses `Fn::ImportValue`. This means the producing stack cannot be updated to remove the export while any consumer still imports it. CloudFormation enforces this constraint.

 **Weak**
The consuming stack uses [`Fn::GetStackOutput`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getstackoutput.html) to read outputs directly from the producing stack. No export coupling is created; either stack can be updated or deleted independently.

 **Both**
A transitional state for migrating from strong to weak. The producing stack retains its export (so existing strong consumers aren’t broken), while the consuming stack switches to `Fn::GetStackOutput`.

#### The dependency deadlock (deadly embrace)
<a name="resources-deadlock"></a>

Strong references can create a deadlock that prevents stack updates. This happens because CloudFormation cannot remove an export while another stack still imports it—and the consuming stack cannot be updated to stop importing until the export already exists. You might see an error like:

```
Export Stack1:ExportsOutputFnGetAtt-****** cannot be deleted as it is in use by Stack2
```

This commonly occurs when you try to remove a shared resource or restructure your stacks. Weak references avoid this problem entirely, because they do not create exports.

#### Controlling reference strength
<a name="resources-controlling-strength"></a>

You can control reference strength at three scopes: app-wide, per-resource, or per-usage.

##### App-wide default
<a name="_app_wide_default"></a>

Set the following context key in `cdk.json` to change the default for all cross-stack references in the app:

```
{
  "context": {
    "@aws-cdk/core:defaultCrossStackReferences": "weak"
  }
}
```

##### Per-resource
<a name="_per_resource"></a>

Override the strength for all references pointing at a specific resource using `CrossStackReferences.of(resource).produce(strength)`:

**Example**

```
declare const bucket: s3.Bucket;
CrossStackReferences.of(bucket).produce(ReferenceStrength.WEAK);
```

```
const { CrossStackReferences, ReferenceStrength } = require('aws-cdk-lib');

CrossStackReferences.of(bucket).produce(ReferenceStrength.WEAK);
```

```
from aws_cdk import CrossStackReferences, ReferenceStrength

CrossStackReferences.of(bucket).produce(ReferenceStrength.WEAK)
```

```
import software.amazon.awscdk.CrossStackReferences;
import software.amazon.awscdk.ReferenceStrength;

CrossStackReferences.of(bucket).produce(ReferenceStrength.WEAK);
```

```
using Amazon.CDK;

CrossStackReferences.Of(bucket).Produce(ReferenceStrength.WEAK);
```

```
import "github.com/aws/aws-cdk-go/awscdk/v2"

awscdk.CrossStackReferences_Of(bucket).Produce(awscdk.ReferenceStrength_WEAK)
```

All references to `bucket` from other stacks will now use `Fn::GetStackOutput` regardless of the app-wide default.

##### Per-usage
<a name="_per_usage"></a>

Override the strength of a single reference at the point of consumption using `Stack.consumeReference()`:

**Example**

```
declare const topic: sns.Topic;

const consumer = new Stack(app, 'Consumer', {
  env: { account: '123456789012', region: 'us-east-1' },
});
new sns.Subscription(consumer, 'Subscription', {
  topic: sns.Topic.fromTopicArn(consumer, 'Topic',
    Stack.consumeReference(topic.topicArn, ReferenceStrength.WEAK)),
  endpoint: 'https://example.com/webhook',
  protocol: sns.SubscriptionProtocol.HTTPS,
});
```

```
const { Stack, ReferenceStrength } = require('aws-cdk-lib');
const sns = require('aws-cdk-lib/aws-sns');
const subscriptions = require('aws-cdk-lib/aws-sns-subscriptions');

const consumer = new Stack(app, 'Consumer', {
  env: { account: '123456789012', region: 'us-east-1' },
});
new sns.Subscription(consumer, 'Subscription', {
  topic: sns.Topic.fromTopicArn(consumer, 'Topic',
    Stack.consumeReference(topic.topicArn, ReferenceStrength.WEAK)),
  endpoint: 'https://example.com/webhook',
  protocol: sns.SubscriptionProtocol.HTTPS,
});
```

```
from aws_cdk import Stack, ReferenceStrength
import aws_cdk.aws_sns as sns

consumer = Stack(app, "Consumer",
    env=core.Environment(account="123456789012", region="us-east-1")
)
sns.Subscription(consumer, "Subscription",
    topic=sns.Topic.from_topic_arn(consumer, "Topic",
        Stack.consume_reference(topic.topic_arn, ReferenceStrength.WEAK)),
    endpoint="https://example.com/webhook",
    protocol=sns.SubscriptionProtocol.HTTPS
)
```

```
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.ReferenceStrength;
import software.amazon.awscdk.services.sns.*;

Stack consumer = new Stack(app, "Consumer", StackProps.builder()
        .env(Environment.builder().account("123456789012").region("us-east-1").build())
        .build());
Subscription.Builder.create(consumer, "Subscription")
        .topic(Topic.fromTopicArn(consumer, "Topic",
            Stack.consumeReference(topic.getTopicArn(), ReferenceStrength.WEAK)))
        .endpoint("https://example.com/webhook")
        .protocol(SubscriptionProtocol.HTTPS)
        .build();
```

```
using Amazon.CDK;
using Amazon.CDK.AWS.SNS;

var consumer = new Stack(app, "Consumer", new StackProps
{
    Env = new Amazon.CDK.Environment { Account = "123456789012", Region = "us-east-1" }
});
new Subscription(consumer, "Subscription", new SubscriptionProps
{
    Topic = Topic.FromTopicArn(consumer, "Topic",
        Stack.ConsumeReference(topic.TopicArn, ReferenceStrength.WEAK)),
    Endpoint = "https://example.com/webhook",
    Protocol = SubscriptionProtocol.HTTPS
});
```

```
import (
  "github.com/aws/aws-cdk-go/awscdk/v2"
  "github.com/aws/aws-cdk-go/awscdk/v2/awssns"
  "github.com/aws/jsii-runtime-go"
)

consumer := awscdk.NewStack(app, jsii.String("Consumer"), &awscdk.StackProps{
  Env: &awscdk.Environment{Account: jsii.String("123456789012"), Region: jsii.String("us-east-1")},
})
awssns.NewSubscription(consumer, jsii.String("Subscription"), &awssns.SubscriptionProps{
  Topic: awssns.Topic_FromTopicArn(consumer, jsii.String("Topic"),
    awscdk.Stack_ConsumeReference(topic.TopicArn(), awscdk.ReferenceStrength_WEAK)),
  Endpoint: jsii.String("https://example.com/webhook"),
  Protocol: awssns.SubscriptionProtocol_HTTPS,
})
```

Use `Stack.consumeListReference()` for string list references.

##### Scoped override
<a name="_scoped_override"></a>

You can also set the reference strength for a subtree of constructs using `CrossStackReferences.of(scope).consume(strength)`. All cross-stack references consumed within that scope will use the specified strength.

#### Migrating from strong to weak references
<a name="resources-migrating-strength"></a>

If you already have deployed stacks with strong references, you cannot switch directly to weak—CloudFormation would fail because the export is still in use. Instead, use a two-phase migration through the `BOTH` transitional state.

Which API to use depends on your goal:
+  **Removing a single reference** (but keeping both stacks and the resource in place)—use `Stack.consumeReference()` to weaken only that specific usage.
+  **Removing or restructuring the producing resource**—use `CrossStackReferences.of(producer).produce()` to weaken all references pointing at that resource at once.

Both approaches follow the same two-phase pattern described below. The examples show the per-resource approach. For per-usage, wrap the reference with `Stack.consumeReference(ref, ReferenceStrength.BOTH)` in Phase 1 and `Stack.consumeReference(ref, ReferenceStrength.WEAK)` in Phase 2.

##### Phase 1: Deploy with `BOTH`
<a name="_phase_1_deploy_with_both"></a>

Switch the reference strength to `BOTH`. This makes the consuming stack start using `Fn::GetStackOutput`, but keeps the export in the producing stack so the transition is safe:

**Example**

```
declare const bucket: s3.Bucket;
CrossStackReferences.of(bucket).produce(ReferenceStrength.BOTH);
```

```
const { CrossStackReferences, ReferenceStrength } = require('aws-cdk-lib');

CrossStackReferences.of(bucket).produce(ReferenceStrength.BOTH);
```

```
from aws_cdk import CrossStackReferences, ReferenceStrength

CrossStackReferences.of(bucket).produce(ReferenceStrength.BOTH)
```

```
import software.amazon.awscdk.CrossStackReferences;
import software.amazon.awscdk.ReferenceStrength;

CrossStackReferences.of(bucket).produce(ReferenceStrength.BOTH);
```

```
using Amazon.CDK;

CrossStackReferences.Of(bucket).Produce(ReferenceStrength.BOTH);
```

```
import "github.com/aws/aws-cdk-go/awscdk/v2"

awscdk.CrossStackReferences_Of(bucket).Produce(awscdk.ReferenceStrength_BOTH)
```

Deploy both stacks.

##### Phase 2: Deploy with `WEAK`
<a name="_phase_2_deploy_with_weak"></a>

Now that no consumer uses `Fn::ImportValue`, the export can be safely removed. Switch to `WEAK`:

**Example**

```
declare const bucket: s3.Bucket;
CrossStackReferences.of(bucket).produce(ReferenceStrength.WEAK);
```

```
const { CrossStackReferences, ReferenceStrength } = require('aws-cdk-lib');

CrossStackReferences.of(bucket).produce(ReferenceStrength.WEAK);
```

```
from aws_cdk import CrossStackReferences, ReferenceStrength

CrossStackReferences.of(bucket).produce(ReferenceStrength.WEAK)
```

```
import software.amazon.awscdk.CrossStackReferences;
import software.amazon.awscdk.ReferenceStrength;

CrossStackReferences.of(bucket).produce(ReferenceStrength.WEAK);
```

```
using Amazon.CDK;

CrossStackReferences.Of(bucket).Produce(ReferenceStrength.WEAK);
```

```
import "github.com/aws/aws-cdk-go/awscdk/v2"

awscdk.CrossStackReferences_Of(bucket).Produce(awscdk.ReferenceStrength_WEAK)
```

Deploy both stacks. The export is removed and the reference is now fully weak.

After this migration, you can freely remove, move, or restructure the resource without hitting the deadly embrace.

#### Manual workaround (legacy)
<a name="resources-deadlock-manual"></a>

If you are not yet using reference strength controls, you can work around the deadlock manually. Remove the use of the shared resource from the consuming stack. Then manually add the same export to the producing stack using exactly the same logical ID as the automatically generated export. Deploy both stacks to remove the `Fn::ImportValue`. Then remove the manual export (and the shared resource if it’s no longer needed) and deploy both stacks again. The stack’s [`exportValue()`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.Stack.html#exportwbrvalueexportedvalue-options) method is a convenient way to create the manual export for this purpose.

### Referencing resources in your AWS account
<a name="resources-external"></a>

Suppose you want to use a resource already available in your AWS account in your AWS CDK app. This might be a resource that was defined through the console, an AWS SDK, directly with AWS CloudFormation, or in a different AWS CDK application. You can turn the resource’s ARN (or another identifying attribute, or group of attributes) into a proxy object. The proxy object serves as a reference to the resource by calling a static factory method on the resource’s class.

When you create such a proxy, the external resource **does not** become a part of your AWS CDK app. Therefore, changes you make to the proxy in your AWS CDK app do not affect the deployed resource. The proxy can, however, be passed to any AWS CDK method that requires a resource of that type.

The following example shows how to reference a bucket based on an existing bucket with the ARN `arn:aws:s3:::amzn-s3-demo-bucket1`, and an Amazon Virtual Private Cloud based on an existing VPC having a specific ID.

**Example**

```
// Construct a proxy for a bucket by its name (must be same account)
s3.Bucket.fromBucketName(this, 'MyBucket', 'amzn-s3-demo-bucket1');

// Construct a proxy for a bucket by its full ARN (can be another account)
s3.Bucket.fromBucketArn(this, 'MyBucket', 'arn:aws:s3:::amzn-s3-demo-bucket1');

// Construct a proxy for an existing VPC from its attribute(s)
ec2.Vpc.fromVpcAttributes(this, 'MyVpc', {
  vpcId: 'vpc-1234567890abcde',
});
```

```
// Construct a proxy for a bucket by its name (must be same account)
s3.Bucket.fromBucketName(this, 'MyBucket', 'amzn-s3-demo-bucket1');

// Construct a proxy for a bucket by its full ARN (can be another account)
s3.Bucket.fromBucketArn(this, 'MyBucket', 'arn:aws:s3:::amzn-s3-demo-bucket1');

// Construct a proxy for an existing VPC from its attribute(s)
ec2.Vpc.fromVpcAttributes(this, 'MyVpc', {
  vpcId: 'vpc-1234567890abcde'
});
```

```
# Construct a proxy for a bucket by its name (must be same account)
s3.Bucket.from_bucket_name(self, "MyBucket", "amzn-s3-demo-bucket1")

# Construct a proxy for a bucket by its full ARN (can be another account)
s3.Bucket.from_bucket_arn(self, "MyBucket", "arn:aws:s3:::amzn-s3-demo-bucket1")

# Construct a proxy for an existing VPC from its attribute(s)
ec2.Vpc.from_vpc_attributes(self, "MyVpc", vpc_id="vpc-1234567890abcdef")
```

```
// Construct a proxy for a bucket by its name (must be same account)
Bucket.fromBucketName(this, "MyBucket", "amzn-s3-demo-bucket1");

// Construct a proxy for a bucket by its full ARN (can be another account)
Bucket.fromBucketArn(this, "MyBucket",
        "arn:aws:s3:::amzn-s3-demo-bucket1");

// Construct a proxy for an existing VPC from its attribute(s)
Vpc.fromVpcAttributes(this, "MyVpc", VpcAttributes.builder()
        .vpcId("vpc-1234567890abcdef").build());
```

```
// Construct a proxy for a bucket by its name (must be same account)
Bucket.FromBucketName(this, "MyBucket", "amzn-s3-demo-bucket1");

// Construct a proxy for a bucket by its full ARN (can be another account)
Bucket.FromBucketArn(this, "MyBucket", "arn:aws:s3:::amzn-s3-demo-bucket1");

// Construct a proxy for an existing VPC from its attribute(s)
Vpc.FromVpcAttributes(this, "MyVpc", new VpcAttributes
{
    VpcId = "vpc-1234567890abcdef"
});
```

```
// Define a proxy for a bucket by its name (must be same account)
s3.Bucket_FromBucketName(stack, jsii.String("MyBucket"), jsii.String("amzn-s3-demo-bucket1"))

// Define a proxy for a bucket by its full ARN (can be another account)
s3.Bucket_FromBucketArn(stack, jsii.String("MyBucket"), jsii.String("arn:aws:s3:::amzn-s3-demo-bucket1"))

// Define a proxy for an existing VPC from its attributes
ec2.Vpc_FromVpcAttributes(stack, jsii.String("MyVpc"), &ec2.VpcAttributes{
  VpcId: jsii.String("vpc-1234567890abcde"),
})
```

Let’s take a closer look at the [`Vpc.fromLookup()`](https://docs.aws.amazon.com/cdk/api/v1/docs/@aws-cdk_aws-ec2.Vpc.html#static-fromwbrlookupscope-id-options) method. Because the `ec2.Vpc` construct is complex, there are many ways you might want to select the VPC to be used with your CDK app. To address this, the VPC construct has a `fromLookup` static method (Python: `from_lookup`) that lets you look up the desired Amazon VPC by querying your AWS account at synthesis time.

To use `Vpc.fromLookup()`, the system that synthesizes the stack must have access to the account that owns the Amazon VPC. This is because the CDK Toolkit queries the account to find the right Amazon VPC at synthesis time.

Furthermore, `Vpc.fromLookup()` works only in stacks that are defined with an explicit **account** and **region** (see [Environments for the AWS CDK](environments.md)). If the AWS CDK tries to look up an Amazon VPC from an [environment-agnostic stack](stacks.md#stack-api), the CDK Toolkit doesn’t know which environment to query to find the VPC.

You must provide `Vpc.fromLookup()` attributes sufficient to uniquely identify a VPC in your AWS account. For example, there can only ever be one default VPC, so it’s sufficient to specify the VPC as the default.

**Example**

```
ec2.Vpc.fromLookup(this, 'DefaultVpc', {
  isDefault: true
});
```

```
ec2.Vpc.fromLookup(this, 'DefaultVpc', {
  isDefault: true
});
```

```
ec2.Vpc.from_lookup(self, "DefaultVpc", is_default=True)
```

```
Vpc.fromLookup(this, "DefaultVpc", VpcLookupOptions.builder()
        .isDefault(true).build());
```

```
Vpc.FromLookup(this, id = "DefaultVpc", new VpcLookupOptions { IsDefault = true });
```

```
ec2.Vpc_FromLookup(this, jsii.String("DefaultVpc"), &ec2.VpcLookupOptions{
  IsDefault: jsii.Bool(true),
})
```

You can also use the `tags` property to query for VPCs by tag. You can add tags to the Amazon VPC at the time of its creation by using AWS CloudFormation or the AWS CDK. You can edit tags at any time after creation by using the AWS Management Console, the AWS CLI, or an AWS SDK. In addition to any tags you add yourself, the AWS CDK automatically adds the following tags to all VPCs it creates.
+  **Name** – The name of the VPC.
+  **aws-cdk:subnet-name** – The name of the subnet.
+  **aws-cdk:subnet-type** – The type of the subnet: Public, Private, or Isolated.

**Example**

```
ec2.Vpc.fromLookup(this, 'PublicVpc',
    {tags: {'aws-cdk:subnet-type': "Public"}});
```

```
ec2.Vpc.fromLookup(this, 'PublicVpc',
    {tags: {'aws-cdk:subnet-type': "Public"}});
```

```
ec2.Vpc.from_lookup(self, "PublicVpc",
    tags={"aws-cdk:subnet-type": "Public"})
```

```
Vpc.fromLookup(this, "PublicVpc", VpcLookupOptions.builder()
        .tags(java.util.Map.of("aws-cdk:subnet-type", "Public"))  // Java 9 or later
        .build());
```

```
Vpc.FromLookup(this, id: "PublicVpc", new VpcLookupOptions
{
    Tags = new Dictionary<string, string> { ["aws-cdk:subnet-type"] = "Public" }
});
```

```
ec2.Vpc_FromLookup(this, jsii.String("DefaultVpc"), &ec2.VpcLookupOptions{
  Tags: &map[string]*string{"aws-cdk:subnet-type": jsii.String("Public")},
})
```

Results of `Vpc.fromLookup()` are cached in the project’s `cdk.context.json` file. (See [Context values and the AWS CDK](context.md).) Commit this file to version control so that your app will continue to refer to the same Amazon VPC. This works even if you later change the attributes of your VPCs in a way that would result in a different VPC being selected. This is particularly important if you’re deploying the stack in an environment that doesn’t have access to the AWS account that defines the VPC, such as [CDK Pipelines](cdk-pipeline.md).

Although you can use an external resource anywhere you’d use a similar resource defined in your AWS CDK app, you cannot modify it. For example, calling `addToResourcePolicy` (Python: `add_to_resource_policy`) on an external `s3.Bucket` does nothing.

## Resource physical names
<a name="resources-physical-names"></a>

The logical names of resources in AWS CloudFormation are different from the names of resources that are shown in the AWS Management Console after they’re deployed by AWS CloudFormation. The AWS CDK calls these final names *physical names*.

For example, AWS CloudFormation might create the Amazon S3 bucket with the logical ID `Stack2MyBucket4DD88B4F` and the physical name `stack2MyBucket4dd88b4f-iuv1rbv9z3to`.

You can specify a physical name when creating constructs that represent resources by using the property `<resourceType>Name`. The following example creates an Amazon S3 bucket with the physical name `amzn-s3-demo-bucket`.

**Example**

```
const bucket = new s3.Bucket(this, 'MyBucket', {
  bucketName: 'amzn-s3-demo-bucket',
});
```

```
const bucket = new s3.Bucket(this, 'MyBucket', {
  bucketName: 'amzn-s3-demo-bucket'
});
```

```
bucket = s3.Bucket(self, "MyBucket", bucket_name="amzn-s3-demo-bucket")
```

```
Bucket bucket = Bucket.Builder.create(this, "MyBucket")
        .bucketName("amzn-s3-demo-bucket").build();
```

```
var bucket = new Bucket(this, "MyBucket", new BucketProps { BucketName = "amzn-s3-demo-bucket" });
```

```
bucket := s3.NewBucket(this, jsii.String("MyBucket"), &s3.BucketProps{
  BucketName: jsii.String("amzn-s3-demo-bucket"),
})
```

Assigning physical names to resources has some disadvantages in AWS CloudFormation. Most importantly, any changes to deployed resources that require a resource replacement, such as changes to a resource’s properties that are immutable after creation, will fail if a resource has a physical name assigned. If you end up in that state, the only solution is to delete the AWS CloudFormation stack, then deploy the AWS CDK app again. See the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html) for details.

In some cases, such as when creating an AWS CDK app with cross-environment references, physical names are required for the AWS CDK to function correctly. In those cases, if you don’t want to bother with coming up with a physical name yourself, you can let the AWS CDK name it for you. To do so, use the special value `PhysicalName.GENERATE_IF_NEEDED`, as follows.

**Example**

```
const bucket = new s3.Bucket(this, 'MyBucket', {
  bucketName: core.PhysicalName.GENERATE_IF_NEEDED,
});
```

```
const bucket = new s3.Bucket(this, 'MyBucket', {
  bucketName: core.PhysicalName.GENERATE_IF_NEEDED
});
```

```
bucket = s3.Bucket(self, "MyBucket",
                         bucket_name=core.PhysicalName.GENERATE_IF_NEEDED)
```

```
Bucket bucket = Bucket.Builder.create(this, "MyBucket")
        .bucketName(PhysicalName.GENERATE_IF_NEEDED).build();
```

```
var bucket = new Bucket(this, "MyBucket", new BucketProps
    { BucketName = PhysicalName.GENERATE_IF_NEEDED });
```

```
bucket := s3.NewBucket(this, jsii.String("MyBucket"), &s3.BucketProps{
  BucketName: awscdk.PhysicalName_GENERATE_IF_NEEDED(),
})
```

## Passing unique resource identifiers
<a name="resources-identifiers"></a>

Whenever possible, you should pass resources by reference, as described in the previous section. However, there are cases where you have no other choice but to refer to a resource by one of its attributes. Example use cases include the following:
+ When you are using low-level AWS CloudFormation resources.
+ When you need to expose resources to the runtime components of an AWS CDK application, such as when referring to Lambda functions through environment variables.

These identifiers are available as attributes on the resources, such as the following.

**Example**

```
bucket.bucketName
lambdaFunc.functionArn
securityGroup.groupArn
```

```
bucket.bucketName
lambdaFunc.functionArn
securityGroup.groupArn
```

```
bucket.bucket_name
lambda_func.function_arn
security_group_arn
```
The Java AWS CDK binding uses getter methods for attributes.

```
bucket.getBucketName()
lambdaFunc.getFunctionArn()
securityGroup.getGroupArn()
```

```
bucket.BucketName
lambdaFunc.FunctionArn
securityGroup.GroupArn
```

```
bucket.BucketName()
fn.FunctionArn()
```

The following example shows how to pass a generated bucket name to an AWS Lambda function.

**Example**

```
const bucket = new s3.Bucket(this, 'Bucket');

new lambda.Function(this, 'MyLambda', {
  // ...
  environment: {
    BUCKET_NAME: bucket.bucketName,
  },
});
```

```
const bucket = new s3.Bucket(this, 'Bucket');

new lambda.Function(this, 'MyLambda', {
  // ...
  environment: {
    BUCKET_NAME: bucket.bucketName
  }
});
```

```
bucket = s3.Bucket(self, "Bucket")

lambda.Function(self, "MyLambda", environment=dict(BUCKET_NAME=bucket.bucket_name))
```

```
final Bucket bucket = new Bucket(this, "Bucket");

Function.Builder.create(this, "MyLambda")
        .environment(java.util.Map.of(    // Java 9 or later
                "BUCKET_NAME", bucket.getBucketName()))
        .build();
```

```
var bucket = new Bucket(this, "Bucket");

new Function(this, "MyLambda", new FunctionProps
{
    Environment = new Dictionary<string, string>
    {
        ["BUCKET_NAME"] = bucket.BucketName
    }
});
```

```
bucket := s3.NewBucket(this, jsii.String("Bucket"), &s3.BucketProps{})
lambda.NewFunction(this, jsii.String("MyLambda"), &lambda.FunctionProps{
  Environment: &map[string]*string{"BUCKET_NAME": bucket.BucketName()},
})
```

## Granting permissions between resources
<a name="resources-grants"></a>

Higher-level constructs make least-privilege permissions achievable by offering simple, intent-based APIs to express permission requirements. For example, many constructs offer grant methods that you can use to grant an entity (such as an IAM role or user) permission to work with the resource, without having to manually create IAM permission statements.

Grant methods are available through Grants classes (such as `BucketGrants` for Amazon S3 buckets). These classes work with both L1 and L2 constructs. L2 constructs expose a `grants` property for convenience, but you can also create a Grants class directly from an L1 construct. You can combine Grants classes with [Mixins](mixins.md) to get L2-like convenience on L1 constructs.

The following example creates the permissions to allow a Lambda function’s execution role to read and write objects to a particular Amazon S3 bucket. If the Amazon S3 bucket is encrypted with an AWS KMS key, this method also grants permissions to the Lambda function’s execution role to decrypt with the key.

**Example**

```
if (bucket.grants.readWrite(func).success) {
  // ...
}
```

```
if ( bucket.grants.readWrite(func).success) {
  // ...
}
```

```
if bucket.grants.read_write(func).success:
    # ...
```

```
if (bucket.getGrants().readWrite(func).getSuccess()) {
    // ...
}
```

```
if (bucket.Grants.ReadWrite(func).Success)
{
    // ...
}
```

```
if *bucket.Grants().ReadWrite(function, nil).Success() {
  // ...
}
```

The grant methods return an `iam.Grant` object. Use the `success` attribute of the `Grant` object to determine whether the grant was effectively applied (for example, it may not have been applied on [external resources](#resources-referencing)). You can also use the `assertSuccess` (Python: `assert_success`) method of the `Grant` object to enforce that the grant was successfully applied.

If a specific grant method isn’t available for the particular use case, you can use a generic grant method to define a new grant with a specified list of actions.

The following example shows how to grant a Lambda function access to the Amazon DynamoDB `CreateBackup` action.

**Example**

```
table.grants.actions(func, 'dynamodb:CreateBackup');
```

```
table.grants.actions(func, 'dynamodb:CreateBackup');
```

```
table.grants.actions(func, "dynamodb:CreateBackup")
```

```
table.getGrants().actions(func, "dynamodb:CreateBackup");
```

```
table.Grants.Actions(func, "dynamodb:CreateBackup");
```

```
table := dynamodb.NewTable(this, jsii.String("MyTable"), &dynamodb.TableProps{})
table.Grants().Actions(function, jsii.String("dynamodb:CreateBackup"))
```

Many resources, such as Lambda functions, require a role to be assumed when executing code. A configuration property enables you to specify an `iam.IRole`. If no role is specified, the function automatically creates a role specifically for this use. You can then use grant methods on the resources to add statements to the role.

The grant methods are built using lower-level APIs for handling with IAM policies. Policies are modeled as [PolicyDocument](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.PolicyDocument.html) objects. Add statements directly to roles (or a construct’s attached role) using the `addToRolePolicy` method (Python: `add_to_role_policy`), or to a resource’s policy (such as a `Bucket` policy) using the `addToResourcePolicy` (Python: `add_to_resource_policy`) method.

## Resource metrics and alarms
<a name="resources-metrics"></a>

Many resources emit CloudWatch metrics that can be used to set up monitoring dashboards and alarms. Higher-level constructs have metric methods that let you access the metrics without looking up the correct name to use.

The following example shows how to define an alarm when the `ApproximateNumberOfMessagesNotVisible` of an Amazon SQS queue exceeds 100.

**Example**

```
import * as cw from '@aws-cdk/aws-cloudwatch';
import * as sqs from '@aws-cdk/aws-sqs';
import { Duration } from '@aws-cdk/core';

const queue = new sqs.Queue(this, 'MyQueue');

const metric = queue.metricApproximateNumberOfMessagesNotVisible({
  label: 'Messages Visible (Approx)',
  period: Duration.minutes(5),
  // ...
});
metric.createAlarm(this, 'TooManyMessagesAlarm', {
  comparisonOperator: cw.ComparisonOperator.GREATER_THAN_THRESHOLD,
  threshold: 100,
  // ...
});
```

```
const cw = require('@aws-cdk/aws-cloudwatch');
const sqs = require('@aws-cdk/aws-sqs');
const { Duration } = require('@aws-cdk/core');

const queue = new sqs.Queue(this, 'MyQueue');

const metric = queue.metricApproximateNumberOfMessagesNotVisible({
  label: 'Messages Visible (Approx)',
  period: Duration.minutes(5)
  // ...
});
metric.createAlarm(this, 'TooManyMessagesAlarm', {
  comparisonOperator: cw.ComparisonOperator.GREATER_THAN_THRESHOLD,
  threshold: 100
  // ...
});
```

```
import aws_cdk.aws_cloudwatch as cw
import aws_cdk.aws_sqs as sqs
from aws_cdk.core import Duration

queue = sqs.Queue(self, "MyQueue")
metric = queue.metric_approximate_number_of_messages_not_visible(
    label="Messages Visible (Approx)",
    period=Duration.minutes(5),
    # ...
)
metric.create_alarm(self, "TooManyMessagesAlarm",
    comparison_operator=cw.ComparisonOperator.GREATER_THAN_THRESHOLD,
    threshold=100,
    # ...
)
```

```
import software.amazon.awscdk.core.Duration;
import software.amazon.awscdk.services.sqs.Queue;
import software.amazon.awscdk.services.cloudwatch.Metric;
import software.amazon.awscdk.services.cloudwatch.MetricOptions;
import software.amazon.awscdk.services.cloudwatch.CreateAlarmOptions;
import software.amazon.awscdk.services.cloudwatch.ComparisonOperator;

Queue queue = new Queue(this, "MyQueue");

Metric metric = queue
        .metricApproximateNumberOfMessagesNotVisible(MetricOptions.builder()
                .label("Messages Visible (Approx)")
                .period(Duration.minutes(5)).build());

metric.createAlarm(this, "TooManyMessagesAlarm", CreateAlarmOptions.builder()
                .comparisonOperator(ComparisonOperator.GREATER_THAN_THRESHOLD)
                .threshold(100)
                // ...
                .build());
```

```
using cdk = Amazon.CDK;
using cw = Amazon.CDK.AWS.CloudWatch;
using sqs = Amazon.CDK.AWS.SQS;

var queue = new sqs.Queue(this, "MyQueue");
var metric = queue.MetricApproximateNumberOfMessagesNotVisible(new cw.MetricOptions
{
    Label = "Messages Visible (Approx)",
    Period = cdk.Duration.Minutes(5),
    // ...
});
metric.CreateAlarm(this, "TooManyMessagesAlarm", new cw.CreateAlarmOptions
{
    ComparisonOperator = cw.ComparisonOperator.GREATER_THAN_THRESHOLD,
    Threshold = 100,
    // ..
});
```

```
import (
  "github.com/aws/aws-cdk-go/awscdk/v2"
  "github.com/aws/jsii-runtime-go"
  cw "github.com/aws/aws-cdk-go/awscdk/v2/awscloudwatch"
  sqs "github.com/aws/aws-cdk-go/awscdk/v2/awssqs"
)

queue := sqs.NewQueue(this, jsii.String("MyQueue"), &sqs.QueueProps{})
metric := queue.MetricApproximateNumberOfMessagesNotVisible(&cw.MetricOptions{
  Label: jsii.String("Messages Visible (Approx)"),
  Period: awscdk.Duration_Minutes(jsii.Number(5)),
})

metric.CreateAlarm(this, jsii.String("TooManyMessagesAlarm"), &cw.CreateAlarmOptions{
  ComparisonOperator: cw.ComparisonOperator_GREATER_THAN_THRESHOLD,
  Threshold: jsii.Number(100),
})
```

If there is no method for a particular metric, you can use the general metric method to specify the metric name manually.

Metrics can also be added to CloudWatch dashboards. See [CloudWatch](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch-readme.html).

## Network traffic
<a name="resources-traffic"></a>

In many cases, you must enable permissions on a network for an application to work, such as when the compute infrastructure needs to access the persistence layer. Resources that establish or listen for connections expose methods that enable traffic flows, including setting security group rules or network ACLs.

 [IConnectable](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IConnectable.html) resources have a `connections` property that is the gateway to network traffic rules configuration.

You enable data to flow on a given network path by using `allow` methods. The following example enables HTTPS connections to the web and incoming connections from the Amazon EC2 Auto Scaling group `fleet2`.

**Example**

```
import * as asg from '@aws-cdk/aws-autoscaling';
import * as ec2 from '@aws-cdk/aws-ec2';

const fleet1: asg.AutoScalingGroup = asg.AutoScalingGroup(/*...*/);

// Allow surfing the (secure) web
fleet1.connections.allowTo(new ec2.Peer.anyIpv4(), new ec2.Port({ fromPort: 443, toPort: 443 }));

const fleet2: asg.AutoScalingGroup = asg.AutoScalingGroup(/*...*/);
fleet1.connections.allowFrom(fleet2, ec2.Port.AllTraffic());
```

```
const asg = require('@aws-cdk/aws-autoscaling');
const ec2 = require('@aws-cdk/aws-ec2');

const fleet1 = asg.AutoScalingGroup();

// Allow surfing the (secure) web
fleet1.connections.allowTo(new ec2.Peer.anyIpv4(), new ec2.Port({ fromPort: 443, toPort: 443 }));

const fleet2 = asg.AutoScalingGroup();
fleet1.connections.allowFrom(fleet2, ec2.Port.AllTraffic());
```

```
import aws_cdk.aws_autoscaling as asg
import aws_cdk.aws_ec2 as ec2

fleet1 = asg.AutoScalingGroup( ... )

# Allow surfing the (secure) web
fleet1.connections.allow_to(ec2.Peer.any_ipv4(),
  ec2.Port(PortProps(from_port=443, to_port=443)))

fleet2 = asg.AutoScalingGroup( ... )
fleet1.connections.allow_from(fleet2, ec2.Port.all_traffic())
```

```
import software.amazon.awscdk.services.autoscaling.AutoScalingGroup;
import software.amazon.awscdk.services.ec2.Peer;
import software.amazon.awscdk.services.ec2.Port;

AutoScalingGroup fleet1 = AutoScalingGroup.Builder.create(this, "MyFleet")
        /* ... */.build();

// Allow surfing the (secure) Web
fleet1.getConnections().allowTo(Peer.anyIpv4(),
        Port.Builder.create().fromPort(443).toPort(443).build());

AutoScalingGroup fleet2 = AutoScalingGroup.Builder.create(this, "MyFleet2")
        /* ... */.build();
fleet1.getConnections().allowFrom(fleet2, Port.allTraffic());
```

```
using cdk = Amazon.CDK;
using asg = Amazon.CDK.AWS.AutoScaling;
using ec2 = Amazon.CDK.AWS.EC2;

// Allow surfing the (secure) Web
var fleet1 = new asg.AutoScalingGroup(this, "MyFleet", new asg.AutoScalingGroupProps { /* ... */ });
fleet1.Connections.AllowTo(ec2.Peer.AnyIpv4(), new ec2.Port(new ec2.PortProps
  { FromPort = 443, ToPort = 443 }));

var fleet2 = new asg.AutoScalingGroup(this, "MyFleet2", new asg.AutoScalingGroupProps { /* ... */ });
fleet1.Connections.AllowFrom(fleet2, ec2.Port.AllTraffic());
```

```
import (
  "github.com/aws/aws-cdk-go/awscdk/v2"
  "github.com/aws/jsii-runtime-go"
  autoscaling "github.com/aws/aws-cdk-go/awscdk/v2/awsautoscaling"
  ec2 "github.com/aws/aws-cdk-go/awscdk/v2/awsec2"
)

fleet1 := autoscaling.NewAutoScalingGroup(this, jsii.String("MyFleet1"), &autoscaling.AutoScalingGroupProps{})
fleet1.Connections().AllowTo(ec2.Peer_AnyIpv4(),ec2.NewPort(&ec2.PortProps{ FromPort: jsii.Number(443), ToPort: jsii.Number(443) }),jsii.String("secure web"))

fleet2 := autoscaling.NewAutoScalingGroup(this, jsii.String("MyFleet2"), &autoscaling.AutoScalingGroupProps{})
fleet1.Connections().AllowFrom(fleet2, ec2.Port_AllTraffic(),jsii.String("all traffic"))
```

Certain resources have default ports associated with them. Examples include the listener of a load balancer on the public port, and the ports on which the database engine accepts connections for instances of an Amazon RDS database. In such cases, you can enforce tight network control without having to manually specify the port. To do so, use the `allowDefaultPortFrom` and `allowToDefaultPort` methods (Python: `allow_default_port_from`, `allow_to_default_port`).

The following example shows how to enable connections from any IPV4 address, and a connection from an Auto Scaling group to access a database.

**Example**

```
listener.connections.allowDefaultPortFromAnyIpv4('Allow public access');

fleet.connections.allowToDefaultPort(rdsDatabase, 'Fleet can access database');
```

```
listener.connections.allowDefaultPortFromAnyIpv4('Allow public access');

fleet.connections.allowToDefaultPort(rdsDatabase, 'Fleet can access database');
```

```
listener.connections.allow_default_port_from_any_ipv4("Allow public access")

fleet.connections.allow_to_default_port(rds_database, "Fleet can access database")
```

```
listener.getConnections().allowDefaultPortFromAnyIpv4("Allow public access");

fleet.getConnections().AllowToDefaultPort(rdsDatabase, "Fleet can access database");
```

```
listener.Connections.AllowDefaultPortFromAnyIpv4("Allow public access");

fleet.Connections.AllowToDefaultPort(rdsDatabase, "Fleet can access database");
```

```
listener.Connections().AllowDefaultPortFromAnyIpv4(jsii.String("Allow public Access"))
fleet.Connections().AllowToDefaultPort(rdsDatabase, jsii.String("Fleet can access database"))
```

## Event handling
<a name="resources-events"></a>

Some resources can act as event sources. Use the `addEventNotification` method (Python: `add_event_notification`) to register an event target to a particular event type emitted by the resource. In addition to this, `addXxxNotification` methods offer a simple way to register a handler for common event types.

The following example shows how to trigger a Lambda function when an object is added to an Amazon S3 bucket.

**Example**

```
import * as s3nots from '@aws-cdk/aws-s3-notifications';

const handler = new lambda.Function(this, 'Handler', { /*…*/ });
const bucket = new s3.Bucket(this, 'Bucket');
bucket.addObjectCreatedNotification(new s3nots.LambdaDestination(handler));
```

```
const s3nots = require('@aws-cdk/aws-s3-notifications');

const handler = new lambda.Function(this, 'Handler', { /*…*/ });
const bucket = new s3.Bucket(this, 'Bucket');
bucket.addObjectCreatedNotification(new s3nots.LambdaDestination(handler));
```

```
import aws_cdk.aws_s3_notifications as s3_nots

handler = lambda_.Function(self, "Handler", ...)
bucket = s3.Bucket(self, "Bucket")
bucket.add_object_created_notification(s3_nots.LambdaDestination(handler))
```

```
import software.amazon.awscdk.services.s3.Bucket;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.s3.notifications.LambdaDestination;

Function handler = Function.Builder.create(this, "Handler")/* ... */.build();
Bucket bucket = new Bucket(this, "Bucket");
bucket.addObjectCreatedNotification(new LambdaDestination(handler));
```

```
using lambda = Amazon.CDK.AWS.Lambda;
using s3 = Amazon.CDK.AWS.S3;
using s3Nots = Amazon.CDK.AWS.S3.Notifications;

var handler = new lambda.Function(this, "Handler", new lambda.FunctionProps { .. });
var bucket = new s3.Bucket(this, "Bucket");
bucket.AddObjectCreatedNotification(new s3Nots.LambdaDestination(handler));
```

```
import (
  "github.com/aws/aws-cdk-go/awscdk/v2"
  "github.com/aws/jsii-runtime-go"
  s3 "github.com/aws/aws-cdk-go/awscdk/v2/awss3"
  s3nots "github.com/aws/aws-cdk-go/awscdk/v2/awss3notifications"
)

handler := lambda.NewFunction(this, jsii.String("MyFunction"), &lambda.FunctionProps{})
bucket := s3.NewBucket(this, jsii.String("Bucket"), &s3.BucketProps{})
bucket.AddObjectCreatedNotification(s3nots.NewLambdaDestination(handler), nil)
```

## Removal policies
<a name="resources-removal"></a>

Resources that maintain persistent data, such as databases, Amazon S3 buckets, and Amazon ECR registries, have a *removal policy*. The removal policy indicates whether to delete persistent objects when the AWS CDK stack that contains them is destroyed. The values specifying the removal policy are available through the `RemovalPolicy` enumeration in the AWS CDK `core` module.

**Note**
Resources besides those that store data persistently might also have a `removalPolicy` that is used for a different purpose. For example, a Lambda function version uses a `removalPolicy` attribute to determine whether a given version is retained when a new version is deployed. These have different meanings and defaults compared to the removal policy on an Amazon S3 bucket or DynamoDB table.

| Value | Meaning |
| --- | --- |
|  `RemovalPolicy.RETAIN`  | Keep the contents of the resource when destroying the stack (default). The resource is orphaned from the stack and must be deleted manually. If you attempt to re-deploy the stack while the resource still exists, you will receive an error message due to a name conflict. |
|  `RemovalPolicy.DESTROY`  | The resource will be destroyed along with the stack. |

 AWS CloudFormation does not remove Amazon S3 buckets that contain files even if their removal policy is set to `DESTROY`. Attempting to do so is an AWS CloudFormation error. To have the AWS CDK delete all files from the bucket before destroying it, set the bucket’s `autoDeleteObjects` property to `true`.

Following is an example of creating an Amazon S3 bucket with `RemovalPolicy` of `DESTROY` and `autoDeleteOjbects` set to `true`.

**Example**

```
import * as cdk from '@aws-cdk/core';
import * as s3 from '@aws-cdk/aws-s3';

export class CdkTestStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const bucket = new s3.Bucket(this, 'Bucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true
    });
  }
}
```

```
const cdk = require('@aws-cdk/core');
const s3 = require('@aws-cdk/aws-s3');

class CdkTestStack extends cdk.Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    const bucket = new s3.Bucket(this, 'Bucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true
    });
  }
}

module.exports = { CdkTestStack }
```

```
import aws_cdk.core as cdk
import aws_cdk.aws_s3 as s3

class CdkTestStack(cdk.stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, "Bucket",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True)
```

```
software.amazon.awscdk.core.*;
import software.amazon.awscdk.services.s3.*;

public class CdkTestStack extends Stack {
    public CdkTestStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public CdkTestStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        Bucket.Builder.create(this, "Bucket")
                .removalPolicy(RemovalPolicy.DESTROY)
                .autoDeleteObjects(true).build();
    }
}
```

```
using Amazon.CDK;
using Amazon.CDK.AWS.S3;

public CdkTestStack(Construct scope, string id, IStackProps props) : base(scope, id, props)
{
    new Bucket(this, "Bucket", new BucketProps {
        RemovalPolicy = RemovalPolicy.DESTROY,
        AutoDeleteObjects = true
    });
}
```

```
import (
  "github.com/aws/aws-cdk-go/awscdk/v2"
  "github.com/aws/jsii-runtime-go"
  s3 "github.com/aws/aws-cdk-go/awscdk/v2/awss3"
)

s3.NewBucket(this, jsii.String("Bucket"), &s3.BucketProps{
  RemovalPolicy: awscdk.RemovalPolicy_DESTROY,
  AutoDeleteObjects: jsii.Bool(true),
})
```

You can also apply a removal policy directly to the underlying AWS CloudFormation resource via the `applyRemovalPolicy()` method. This method is available on some stateful resources that do not have a `removalPolicy` property in their L2 resource’s props. Examples include the following:
+  AWS CloudFormation stacks
+ Amazon Cognito user pools
+ Amazon DocumentDB database instances
+ Amazon EC2 volumes
+ Amazon OpenSearch Service domains
+ Amazon FSx file systems
+ Amazon SQS queues

**Example**

```
const resource = bucket.node.findChild('Resource') as cdk.CfnResource;
resource.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY);
```

```
const resource = bucket.node.findChild('Resource');
resource.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY);
```

```
resource = bucket.node.find_child('Resource')
resource.apply_removal_policy(cdk.RemovalPolicy.DESTROY);
```

```
CfnResource resource = (CfnResource)bucket.node.findChild("Resource");
resource.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY);
```

```
var resource = (CfnResource)bucket.node.findChild('Resource');
resource.ApplyRemovalPolicy(cdk.RemovalPolicy.DESTROY);
```

**Note**
The AWS CDK’s `RemovalPolicy` translates to AWS CloudFormation’s `DeletionPolicy`. However, the default in AWS CDK is to retain the data, which is the opposite of the AWS CloudFormation default.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
