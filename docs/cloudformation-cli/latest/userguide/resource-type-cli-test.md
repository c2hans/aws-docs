---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-test.html
---

# test
<a name="resource-type-cli-test"></a>

## Description
<a name="resource-type-cli-test-description"></a>

Performs contract tests on the handlers of an extension type.

## Synopsis
<a name="resource-type-cli-test-synopsis"></a>

```
$ cfn test
    [--endpoint <value>]
    [--function-name <value>]
    [--region <value>]
    [--role-arn <value>]
    [-- -k <value>]
    [-- --tb=<value>]
    [--enforce-timeout <value>]
```

## Options
<a name="resource-type-cli-test-options"></a>

`--endpoint <value>`

The endpoint at which the type can be invoked. Alternately, you can also specify an actual Lambda endpoint and function name in your AWS account.

Default: `http://127.0.0.1.3001`

`--function-name <value>`

The logical Lambda function name in the AWS SAM template. Alternately, you can also specify an actual Lambda endpoint and function name in your AWS account.

Default: `TestEntrypoint`

`--region <value>`

The region to use for temporary credentials.

Default: `us-east-1`

`--role-arn <value>`

The Amazon Resource Name (ARN) of the IAM execution role for the contract tests to assume and use when performing operations.

If you don't specify an execution role, the contract tests use the environment credentials or the credentials specified in the [Boto 3 credentials chain](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html).

`-- -k <value>`

Runs a single unit test. For more information, see [Using `-k expr` to select tests based on their name](https://doc.pytest.org/en/latest/example/markers.html#using-k-expr-to-select-tests-based-on-their-name) from the `pytest` documentation.

`-- --tb=<value>`

*Default*: `auto`

The following are valid values for the traceback. For more information, see [Modifying Python traceback printing](https://docs.pytest.org/en/6.2.x/usage.html#modifying-python-traceback-printing) from the `pytest` documentation.
+ *auto* – `long` tracebacks for the first and last entry, but `short` tracebacks for all other entries.
+ *long* – exhaustive and informative traceback formatting.
+ *short* – shorter traceback format.
+ *line* – only one line per failure.
+ *native* – standard library formatting.
+ *no* – no traceback.

`--enforce-timeout <value>`

Sets the read and list timeout to 60 seconds and the create, update, and delete handler timeouts to 120 seconds.

## Examples
<a name="resource-type-cli-test-examples"></a>

The following command performs contract tests on the handlers of the extension type.

```
$ cfn test
```

The following command runs one contract test at a time.

```
$ cfn test -- -k {{test-name}}
```

The following command increases the timeout time when running contract tests.

```
$ cfn test --enforce-timeout {{60}}
```

The following command combines the contract test and timeout time.

```
$ cfn test --enforce-timeout 60 -- -k {{test-name}}
```

The following command starts a Lambda service and uses the test command to perform contract tests.

```
$ sam local start-lambda
$ cfn test -v --enforce-timeout 90
```
