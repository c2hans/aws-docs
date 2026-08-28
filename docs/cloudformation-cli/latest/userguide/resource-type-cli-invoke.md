---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-invoke.html
---

# invoke
<a name="resource-type-cli-invoke"></a>

## Description
<a name="resource-type-cli-invoke-description"></a>

Performs contract tests on the specified handler of an extension type.

## Synopsis
<a name="resource-type-cli-invoke-synopsis"></a>

```
$ cfn invoke
    [--endpoint <value>]
    [--function-name <value>]
    [--region <value>]
    [--max-reinvoke <value>]
    action
    request
```

## Options
<a name="resource-type-cli-invoke-options"></a>

`--endpoint <value>`

The endpoint at which the type can be invoked. Alternately, you can also specify an actual Lambda endpoint and function name in your AWS account.

Default: `http://127.0.0.1.3001`

`--function-name <value>`

The logical Lambda function name in the AWS SAM template. Alternately, you can also specify an actual Lambda endpoint and function name in your AWS account.

Default: `TypeFunction`

`--region <value>`

The region to configure the client to interact with.

Default: `us-east-1`

`--max-reinvoke <value>`

Maximum number of `IN_PROGRESS` re-invocations allowed before exiting. If not specified, will continue to re-invoke until terminal status is reached.

`action`

Which single handler to invoke.

Values: `CREATE` \| `READ` \| `UPDATE` \| `DELETE` \| `LIST`

`request`

File path to a JSON file containing the request with which to invoke the function.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
