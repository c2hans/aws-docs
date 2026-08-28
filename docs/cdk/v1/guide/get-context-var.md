---
source_url: https://docs.aws.amazon.com/cdk/v1/guide/get-context-var.html
---

This is the AWS CDK v1 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and will now only receive critical bug fixes and security patches. New features will be developed for CDK v2 exclusively. Support for CDK v1 will end entirely on June 1, 2023. [Migrate to CDK v2](work-with-cdk-v2.md) to have access to the latest features and fixes.

# Get a value from a context variable
<a name="get-context-var"></a>

You can specify a context variable either as part of an AWS CDK CLI command, or in `cdk.json`.

To create a command line context variable, use the **--context** (**-c**) option, as shown in the following example.

```
cdk synth -c bucket_name=mygroovybucket
```

To specify the same context variable and value in the `cdk.json` file, use the following code.

```
{
  "context": {
    "bucket_name": "myotherbucket"
  }
}
```

To get the value of a context variable in your app, use the `TryGetContext` method in the context of a construct (that is, when `this`, or `self` in Python, is an instance of some construct). The example gets the context value **bucket\_name**. If the requested value is not defined, `TryGetContext` returns `undefined` (`None` in Python; `null` in Java and C\#; `nil` in Go) rather than raising an exception.

------
#### [ TypeScript ]

```
const bucket_name = this.node.tryGetContext('bucket_name');
```

------
#### [ JavaScript ]

```
const bucket_name = this.node.tryGetContext('bucket_name');
```

------
#### [ Python ]

```
bucket_name = self.node.try_get_context("bucket_name")
```

------
#### [ Java ]

```
String bucketName = (String)this.getNode().tryGetContext("bucket_name");
```

------
#### [ C\# ]

```
var bucketName = this.Node.TryGetContext("bucket_name");
```

------

Outside the context of a construct, you can access the context variable from the app object, like this.

------
#### [ TypeScript ]

```
const app = new cdk.App();
const bucket_name = app.node.tryGetContext('bucket_name')
```

------
#### [ JavaScript ]

```
const app = new cdk.App();
const bucket_name = app.node.tryGetContext('bucket_name');
```

------
#### [ Python ]

```
app = cdk.App()
bucket_name = app.node.try_get_context("bucket_name")
```

------
#### [ Java ]

```
App app = App();
String bucketName = (String)app.getNode().tryGetContext("bucket_name");
```

------
#### [ C\# ]

```
app = App();
var bucketName = app.Node.TryGetContext("bucket_name");
```

------

For more details on working with context variables, see [Runtime context](context.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
