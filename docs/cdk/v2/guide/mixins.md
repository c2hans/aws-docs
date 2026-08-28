---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/mixins.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Mixins
<a name="mixins"></a>

Mixins are reusable features that you apply to constructs using the `.with()` method. They add features to both L1 (CloudFormation-level) and L2 (intent-based) constructs, such as versioning, auto-deleting objects, or blocking public access. Each mixin works on a single resource. To connect two resources, use [Facades](facades.md) instead.

Each mixin targets a specific resource type and is named after that resource. For example, `BucketVersioning` targets Amazon S3 buckets. You access mixins through the `mixins` namespace of each service module, such as `s3.mixins`.

## Apply Mixins
<a name="mixins-basic"></a>

You apply mixins using the `.with()` method, which is available on all constructs. You can chain multiple mixins together:

**Example**

```
import * as s3 from 'aws-cdk-lib/aws-s3';

const bucket = new s3.CfnBucket(this, 'MyBucket')
  .with(new s3.mixins.BucketVersioning())
  .with(new s3.mixins.BucketBlockPublicAccess());
```

```
const s3 = require('aws-cdk-lib/aws-s3');

const bucket = new s3.CfnBucket(this, 'MyBucket')
  .with(new s3.mixins.BucketVersioning())
  .with(new s3.mixins.BucketBlockPublicAccess());
```

```
import aws_cdk.aws_s3 as s3

bucket = s3.CfnBucket(self, "MyBucket") \
    .with_(s3.mixins.BucketVersioning()) \
    .with_(s3.mixins.BucketBlockPublicAccess())
```

```
import software.amazon.awscdk.services.s3.*;

CfnBucket bucket = new CfnBucket(this, "MyBucket");
bucket.with(new BucketVersioning());
bucket.with(new BucketBlockPublicAccess());
```

```
using Amazon.CDK.AWS.S3;

var bucket = new CfnBucket(this, "MyBucket");
bucket.With(new BucketVersioning());
bucket.With(new BucketBlockPublicAccess());
```

```
bucket := awss3.NewCfnBucket(stack, jsii.String("MyBucket"), nil)
bucket.With(awss3.NewBucketVersioning())
bucket.With(awss3.NewBucketBlockPublicAccess())
```

Each mixin declares which resource types it supports. If you apply a mixin to a construct it does not support, it is silently skipped. This means you can safely apply mixins broadly without worrying about type mismatches. If you need to ensure a mixin is applied, use [`requireAll()` or `requireAny()`](#mixins-advanced).

## Use Mixins with L1 and L2 constructs
<a name="mixins-l1-l2"></a>

Mixins work with both L1 and L2 constructs. When you apply a mixin to an L2 construct, it also applies to the L1 resource behind it.

The following example shows how to apply mixins to both L1 and L2 constructs:

**Example**

```
import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';

// Using a mixin with an L1 construct
new s3.CfnBucket(this, 'L1Bucket')
  .with(new s3.mixins.BucketVersioning());

// Using a mixin with an L2 construct
new s3.Bucket(this, 'L2Bucket', {
  removalPolicy: cdk.RemovalPolicy.DESTROY,
}).with(new s3.mixins.BucketAutoDeleteObjects());
```

```
const cdk = require('aws-cdk-lib');
const s3 = require('aws-cdk-lib/aws-s3');

// Using a mixin with an L1 construct
new s3.CfnBucket(this, 'L1Bucket')
  .with(new s3.mixins.BucketVersioning());

// Using a mixin with an L2 construct
new s3.Bucket(this, 'L2Bucket', {
  removalPolicy: cdk.RemovalPolicy.DESTROY,
}).with(new s3.mixins.BucketAutoDeleteObjects());
```

```
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3

# Using a mixin with an L1 construct
s3.CfnBucket(self, "L1Bucket") \
    .with_(s3.mixins.BucketVersioning())

# Using a mixin with an L2 construct
s3.Bucket(self, "L2Bucket",
    removal_policy=cdk.RemovalPolicy.DESTROY,
).with_(s3.mixins.BucketAutoDeleteObjects())
```

```
import software.amazon.awscdk.*;
import software.amazon.awscdk.services.s3.*;

// Using a mixin with an L1 construct
CfnBucket l1Bucket = new CfnBucket(this, "L1Bucket");
l1Bucket.with(new BucketVersioning());

// Using a mixin with an L2 construct
Bucket l2Bucket = Bucket.Builder.create(this, "L2Bucket")
        .removalPolicy(RemovalPolicy.DESTROY)
        .build();
l2Bucket.with(new BucketAutoDeleteObjects());
```

```
using Amazon.CDK;
using Amazon.CDK.AWS.S3;

// Using a mixin with an L1 construct
var l1Bucket = new CfnBucket(this, "L1Bucket");
l1Bucket.With(new BucketVersioning());

// Using a mixin with an L2 construct
var l2Bucket = new Bucket(this, "L2Bucket", new BucketProps
{
    RemovalPolicy = RemovalPolicy.DESTROY
});
l2Bucket.With(new BucketAutoDeleteObjects());
```

```
l1Bucket := awss3.NewCfnBucket(stack, jsii.String("L1Bucket"), nil)
l1Bucket.With(awss3.NewBucketVersioning())

l2Bucket := awss3.NewBucket(stack, jsii.String("L2Bucket"), &awss3.BucketProps{
    RemovalPolicy: awscdk.RemovalPolicy_DESTROY,
})
l2Bucket.With(awss3.NewBucketAutoDeleteObjects())
```

## Mixins vs. construct properties
<a name="mixins-vs-props"></a>

Mixins and construct properties work together. L2 construct properties set up a resource when you create it. Mixins can be applied at any time.

Use L2 construct properties when
You are using an L2 construct and the property you need is available. This is the simplest approach.

Use Mixins when
+ You are working with an L1 construct and want L2-like features.
+ You want to add a feature to an L2 construct that is not available as a property.
+ You want to apply the same feature across multiple constructs of different types.

Mixins do not replace construct properties. They cannot make a required property optional or change default values.

## Apply Mixins to multiple constructs
<a name="mixins-advanced"></a>

The `Mixins.of()` API provides more control over how mixins are applied across a scope. Instead of calling `.with()` on individual constructs, you can apply a mixin to all matching constructs in a stack or scope at once:

**Example**

```
import { Mixins } from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';

// Apply to all supported constructs in the stack
Mixins.of(stack).apply(new s3.mixins.BucketVersioning());
```

```
const { Mixins } = require('aws-cdk-lib');
const s3 = require('aws-cdk-lib/aws-s3');

// Apply to all supported constructs in the stack
Mixins.of(stack).apply(new s3.mixins.BucketVersioning());
```

```
from aws_cdk import Mixins
import aws_cdk.aws_s3 as s3

# Apply to all supported constructs in the stack
Mixins.of(stack).apply(s3.mixins.BucketVersioning())
```

```
import software.amazon.awscdk.Mixins;
import software.amazon.awscdk.services.s3.*;

// Apply to all supported constructs in the stack
Mixins.of(stack).apply(new BucketVersioning());
```

```
using Amazon.CDK;
using Amazon.CDK.AWS.S3;

// Apply to all supported constructs in the stack
Mixins.Of(stack).Apply(new BucketVersioning());
```

```
awscdk.Mixins_Of(stack, nil).Apply(awss3.NewBucketVersioning())
```

By default, constructs that don’t support the mixin are silently skipped. Use `requireAll()` to assert that the mixin is applied to every construct in the selection, or `requireAny()` to assert it is applied to at least one. This is useful for enforcing that resources have a required configuration:

**Example**

```
// Throws an error if any construct in the scope doesn't support the mixin
Mixins.of(stack)
  .requireAll()
  .apply(new s3.mixins.BucketVersioning());
```

```
// Throws an error if any construct in the scope doesn't support the mixin
Mixins.of(stack)
  .requireAll()
  .apply(new s3.mixins.BucketVersioning());
```

```
# Throws an error if any construct in the scope doesn't support the mixin
Mixins.of(stack) \
    .require_all() \
    .apply(s3.mixins.BucketVersioning())
```

```
// Throws an error if any construct in the scope doesn't support the mixin
Mixins.of(stack)
        .requireAll()
        .apply(new BucketVersioning());
```

```
// Throws an error if any construct in the scope doesn't support the mixin
Mixins.Of(stack)
    .RequireAll()
    .Apply(new BucketVersioning());
```

```
awscdk.Mixins_Of(stack, nil).RequireAll().Apply(awss3.NewBucketVersioning())
```

## Mixins and Aspects
<a name="mixins-aspects"></a>

Mixins and [Aspects](aspects.md) are related but serve different purposes:
+  **Mixins** are applied immediately when you call `.with()`. You choose exactly which constructs to apply them to.
+  **Aspects** apply during synthesis to all constructs in a scope. Use them for broad policies and checks.

Use Mixins to add a feature to specific constructs. Use Aspects to enforce rules or apply changes across your entire application.

## Related resources
<a name="mixins-related"></a>
+  [Facades](facades.md) – Connect resources with IAM principals and other services.
+  [Aspects](aspects.md) – Apply changes or validate constructs across your entire application.
+  [Constructs](constructs.md) – Learn about L1, L2, and L3 constructs.
+  [Customize constructs](cfn-layer.md) – Customize constructs with escape hatches and raw overrides.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
