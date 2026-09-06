---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/identifiers.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Identifiers and the AWS CDK
<a name="identifiers"></a>

When building AWS Cloud Development Kit (AWS CDK) apps, you will use many types of identifiers and names. To use the AWS CDK effectively and avoid errors, it is important to understand the types of identifiers.

Identifiers must be unique within the scope in which they are created; they do not need to be globally unique in your AWS CDK application.

If you attempt to create an identifier with the same value within the same scope, the AWS CDK throws an exception.

## Construct IDs
<a name="identifiers-construct-ids"></a>

The most common identifier, `id`, is the identifier passed as the second argument when instantiating a construct object. This identifier, like all identifiers, only needs to be unique within the scope in which it is created, which is the first argument when instantiating a construct object.

**Note**
The `id` of a stack is also the identifier that you use to refer to it in the [AWS CDK CLI reference](cli.md).

Let’s look at an example where we have two constructs with the identifier `MyBucket` in our app. The first is defined in the scope of the stack with the identifier `Stack1`. The second is defined in the scope of a stack with the identifier `Stack2`. Because they’re defined in different scopes, this doesn’t cause any conflict, and they can coexist in the same app without issues.

**Example**

```
import { App, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';

class MyStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps = {}) {
    super(scope, id, props);

    new s3.Bucket(this, 'MyBucket');
  }
}

const app = new App();
new MyStack(app, 'Stack1');
new MyStack(app, 'Stack2');
```

```
const { App , Stack } = require('aws-cdk-lib');
const s3 = require('aws-cdk-lib/aws-s3');

class MyStack extends Stack {
  constructor(scope, id, props = {}) {
    super(scope, id, props);

    new s3.Bucket(this, 'MyBucket');
  }
}

const app = new App();
new MyStack(app, 'Stack1');
new MyStack(app, 'Stack2');
```

```
from aws_cdk import App, Construct, Stack, StackProps
from constructs import Construct
from aws_cdk import aws_s3 as s3

class MyStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):

        super().__init__(scope, id, **kwargs)
        s3.Bucket(self, "MyBucket")

app = App()
MyStack(app, 'Stack1')
MyStack(app, 'Stack2')
```

```
// MyStack.java
package com.myorg;

import software.amazon.awscdk.App;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.constructs.Construct;
import software.amazon.awscdk.services.s3.Bucket;

public class MyStack extends Stack {
    public MyStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public MyStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);
        new Bucket(this, "MyBucket");
    }
}

// Main.java
package com.myorg;

import software.amazon.awscdk.App;

public class Main {
    public static void main(String[] args) {
        App app = new App();
        new MyStack(app, "Stack1");
        new MyStack(app, "Stack2");
    }
}
```

```
using Amazon.CDK;
using constructs;
using Amazon.CDK.AWS.S3;

public class MyStack : Stack
{
    public MyStack(Construct scope, string id, IStackProps props) : base(scope, id, props)
    {
        new Bucket(this, "MyBucket");
    }
}

class Program
{
    static void Main(string[] args)
    {
        var app = new App();
        new MyStack(app, "Stack1");
        new MyStack(app, "Stack2");
    }
}
```

## Paths
<a name="identifiers-paths"></a>

The constructs in an AWS CDK application form a hierarchy rooted in the `App` class. We refer to the collection of IDs from a given construct, its parent construct, its grandparent, and so on to the root of the construct tree, as a *path*.

The AWS CDK typically displays paths in your templates as a string. The IDs from the levels are separated by slashes, starting at the node immediately under the root `App` instance, which is usually a stack. For example, the paths of the two Amazon S3 bucket resources in the previous code example are `Stack1/MyBucket` and `Stack2/MyBucket`.

You can access the path of any construct programmatically, as shown in the following example. This gets the path of `myConstruct` (or `my_construct`, as Python developers would write it). Since IDs must be unique within the scope they are created, their paths are always unique within an AWS CDK application.

**Example**

```
const path: string = myConstruct.node.path;
```

```
const path = myConstruct.node.path;
```

```
path = my_construct.node.path
```

```
String path = myConstruct.getNode().getPath();
```

```
string path = myConstruct.Node.Path;
```

## Unique IDs
<a name="identifiers-unique-ids"></a>

 AWS CloudFormation requires that all logical IDs in a template be unique. Because of this, the AWS CDK must be able to generate a unique identifier for each construct in an application. Resources have paths that are globally unique (the names of all scopes from the stack to a specific resource). Therefore, the AWS CDK generates the necessary unique identifiers by concatenating the elements of the path and adding an 8-digit hash. (The hash is necessary to distinguish distinct paths, such as `A/B/C` and `A/BC`, that would result in the same AWS CloudFormation identifier. AWS CloudFormation identifiers are alphanumeric and cannot contain slashes or other separator characters.) The AWS CDK calls this string the *unique ID* of the construct.

In general, your AWS CDK app should not need to know about unique IDs. You can, however, access the unique ID of any construct programmatically, as shown in the following example.

**Example**

```
const uid: string = Names.uniqueId(myConstruct);
```

```
const uid = Names.uniqueId(myConstruct);
```

```
uid = Names.unique_id(my_construct)
```

```
String uid = Names.uniqueId(myConstruct);
```

```
string uid = Names.Uniqueid(myConstruct);
```

The *address* is another kind of unique identifier that uniquely distinguishes CDK resources. Derived from the SHA-1 hash of the path, it is not human-readable. However, its constant, relatively short length (always 42 hexadecimal characters) makes it useful in situations where the "traditional" unique ID might be too long. Some constructs may use the address in the synthesized AWS CloudFormation template instead of the unique ID. Again, your app generally should not need to know about its constructs' addresses, but you can retrieve a construct’s address as follows.

**Example**

```
const addr: string = myConstruct.node.addr;
```

```
const addr = myConstruct.node.addr;
```

```
addr = my_construct.node.addr
```

```
String addr = myConstruct.getNode().getAddr();
```

```
string addr = myConstruct.Node.Addr;
```

## Logical IDs
<a name="identifiers-logical-ids"></a>

When the AWS CDK synthesizes your app into an AWS CloudFormation template, it generates a *logical ID* for each resource. AWS CloudFormation uses logical IDs to identify resources within a template and to track them across deployments. Understanding how logical IDs are generated helps you avoid unintended resource replacements when you refactor your CDK code.

### How logical IDs are generated
<a name="identifiers-logical-id-generation"></a>

The AWS CDK generates logical IDs from the construct path by using the following algorithm:

1. Concatenate the path components from the construct tree, excluding the stack itself.

1. Apply heuristics to improve readability (see [Logical ID path component heuristics](#identifiers-logical-id-heuristics)).

1. Append an 8-character hash of the full path to ensure uniqueness.

The resulting format is:

```
<human-readable-portion><8-character-hash>
```

For example, a VPC private subnet route table might produce the logical ID `VPCPrivateSubnet2RouteTable0A19E10E`.

The following rules apply to logical ID generation:
+ The maximum length is 255 characters. The human-readable portion is capped at 240 characters.
+ The 8-character hash ensures that paths like `A/B/C` and `A/BC` — which concatenate to the same string — produce different logical IDs.
+ Resources that are direct children of the stack (single-component paths) use their name directly without a hash, as long as the name is 255 characters or fewer.

### Logical ID path component heuristics
<a name="identifiers-logical-id-heuristics"></a>

The AWS CDK applies the following heuristics to path components when it generates the human-readable portion of logical IDs.

 `Default` — removed entirely
If a path component is `Default`, the CDK removes it from both the human-readable portion and the hash input. This means that wrapping an existing construct inside a new construct — and naming the inner construct `Default` — produces the exact same logical ID as the original unwrapped construct. This is the key mechanism for safely refactoring flat code into higher-level constructs without changing deployed resource identities.

 `Resource` — hidden from human-readable portion only
If a path component is `Resource`, the CDK omits it from the human-readable portion but still includes it in the hash calculation. L1 (CloudFormation) constructs use `Resource` as their construct ID by convention. This keeps logical IDs shorter without losing uniqueness.

Duplicate consecutive components — deduplicated
If the preceding path component name ends with the current component name, the CDK skips the current component. This prevents redundant repetition in logical IDs.

### Use `Default` to preserve logical IDs when you refactor
<a name="identifiers-logical-id-refactoring"></a>

When you refactor a flat stack into higher-level constructs, you can use `Default` as the construct ID for the primary resource to preserve its logical ID. This prevents AWS CloudFormation from replacing the resource during deployment.

The following example shows a stack with resources that are defined directly:

**Example**

```
export class MyStack extends cdk.Stack {
  constructor(scope: Construct, id: string) {
    super(scope, id);
    new s3.Bucket(this, 'DataBucket');
    new lambda.Function(this, 'ProcessFunction', { /* ... */ });
  }
}
```

```
class MyStack extends cdk.Stack {
  constructor(scope, id) {
    super(scope, id);
    new s3.Bucket(this, 'DataBucket');
    new lambda.Function(this, 'ProcessFunction', { /* ... */ });
  }
}
```

```
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
)
from constructs import Construct

class MyStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        s3.Bucket(self, "DataBucket")
        _lambda.Function(self, "ProcessFunction", # ...
        )
```

```
package com.myorg;

import software.constructs.Construct;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.s3.Bucket;
import software.amazon.awscdk.services.lambda.Function;

public class MyStack extends Stack {
    public MyStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public MyStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);
        new Bucket(this, "DataBucket");
        Function.Builder.create(this, "ProcessFunction")
            // ...
            .build();
    }
}
```

```
using Amazon.CDK;
using Constructs;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.Lambda;

namespace MyApp
{
    public class MyStack : Stack
    {
        public MyStack(Construct scope, string id, StackProps props = null) : base(scope, id, props)
        {
            new Bucket(this, "DataBucket");
            new Function(this, "ProcessFunction", new FunctionProps
            {
                // ...
            });
        }
    }
}
```

```
package main

import (
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awslambda"
	"github.com/aws/aws-cdk-go/awscdk/v2/awss3"
	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

type MyStackProps struct {
	awscdk.StackProps
}

func NewMyStack(scope constructs.Construct, id string, props *MyStackProps) awscdk.Stack {
	stack := awscdk.NewStack(scope, &id, &props.StackProps)

	awss3.NewBucket(stack, jsii.String("DataBucket"), &awss3.BucketProps{})
	awslambda.NewFunction(stack, jsii.String("ProcessFunction"), &awslambda.FunctionProps{
		// ...
	})

	return stack
}
```

The bucket’s path is `MyStack/DataBucket/Resource`, which produces a logical ID of `DataBucket<hash>`.

You can extract the bucket into a higher-level construct and preserve the same logical ID by naming the inner construct `Default`:

**Example**

```
class DataPipeline extends Construct {
  constructor(scope: Construct, id: string) {
    super(scope, id);
    new s3.Bucket(this, 'Default');  // 'Default' is hidden from logical ID
    new lambda.Function(this, 'ProcessFunction', { /* ... */ });
  }
}

export class MyStack extends cdk.Stack {
  constructor(scope: Construct, id: string) {
    super(scope, id);
    new DataPipeline(this, 'DataBucket');
  }
}
```

```
class DataPipeline extends Construct {
  constructor(scope, id) {
    super(scope, id);
    new s3.Bucket(this, 'Default');  // 'Default' is hidden from logical ID
    new lambda.Function(this, 'ProcessFunction', { /* ... */ });
  }
}

class MyStack extends cdk.Stack {
  constructor(scope, id) {
    super(scope, id);
    new DataPipeline(this, 'DataBucket');
  }
}
```

```
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
)
from constructs import Construct

class DataPipeline(Construct):
    def __init__(self, scope: Construct, id: str) -> None:
        super().__init__(scope, id)
        s3.Bucket(self, "Default")  # 'Default' is hidden from logical ID
        _lambda.Function(self, "ProcessFunction", # ...
        )

class MyStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        DataPipeline(self, "DataBucket")
```

```
package com.myorg;

import software.constructs.Construct;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.s3.Bucket;
import software.amazon.awscdk.services.lambda.Function;

public class DataPipeline extends Construct {
    public DataPipeline(final Construct scope, final String id) {
        super(scope, id);
        new Bucket(this, "Default");  // 'Default' is hidden from logical ID
        Function.Builder.create(this, "ProcessFunction")
            // ...
            .build();
    }
}

public class MyStack extends Stack {
    public MyStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public MyStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);
        new DataPipeline(this, "DataBucket");
    }
}
```

```
using Amazon.CDK;
using Constructs;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.Lambda;

namespace MyApp
{
    public class DataPipeline : Construct
    {
        public DataPipeline(Construct scope, string id) : base(scope, id)
        {
            new Bucket(this, "Default");  // 'Default' is hidden from logical ID
            new Function(this, "ProcessFunction", new FunctionProps
            {
                // ...
            });
        }
    }

    public class MyStack : Stack
    {
        public MyStack(Construct scope, string id, StackProps props = null) : base(scope, id, props)
        {
            new DataPipeline(this, "DataBucket");
        }
    }
}
```

```
package main

import (
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awslambda"
	"github.com/aws/aws-cdk-go/awscdk/v2/awss3"
	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

type DataPipeline struct {
	constructs.Construct
}

func NewDataPipeline(scope constructs.Construct, id string) constructs.Construct {
	this := constructs.NewConstruct(scope, &id)

	// 'Default' is hidden from logical ID
	awss3.NewBucket(this, jsii.String("Default"), &awss3.BucketProps{})
	awslambda.NewFunction(this, jsii.String("ProcessFunction"), &awslambda.FunctionProps{
		// ...
	})

	return this
}

type MyStackProps struct {
	awscdk.StackProps
}

func NewMyStack(scope constructs.Construct, id string, props *MyStackProps) awscdk.Stack {
	stack := awscdk.NewStack(scope, &id, &props.StackProps)

	NewDataPipeline(stack, "DataBucket")

	return stack
}
```

The bucket’s path is now `MyStack/DataBucket/Default/Resource`. Because `Default` is removed from both the human-readable portion and the hash input, the logical ID remains `DataBucket<hash>` — identical to the original.

**Important**
You can have only one child with the ID `Default` per construct scope. If you need multiple resources at the same level, give them descriptive IDs. The `Default` pattern works best with single-responsibility constructs that have one primary resource.

### Limitations and considerations
<a name="identifiers-logical-id-considerations"></a>

Keep the following in mind when you work with logical IDs:
+ You can assign only one child per scope the `Default` construct ID.
+ If you change a construct ID after deployment, the logical ID changes, which causes AWS CloudFormation to replace the resource. Use `cdk diff` to verify changes before you deploy.
+ For cases where logical IDs have already changed, you can use the `cdk refactor` command to map old logical IDs to new ones. For more information, see [Preserve deployed resources when refactoring CDK code](refactor.md).
+ For more information about how logical IDs appear in synthesized templates, see [Generated logical IDs in your AWS CloudFormation template](configure-synth.md#how-synth-default-logical-ids).

### Logical ID stability
<a name="identifiers-logical-id-stability"></a>

Avoid changing the logical ID of a resource after it has been created. AWS CloudFormation identifies resources by their logical ID. Therefore, if you change the logical ID of a resource, AWS CloudFormation creates a new resource with the new logical ID, then deletes the existing one. Depending on the type of resource, this might cause service interruption, data loss, or both.
