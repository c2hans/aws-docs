---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/contract-tests.html
---

# Contract tests for resource types
<a name="contract-tests"></a>

As part of testing your resource, the CloudFormation CLI performs a suite of tests, each written to test a requirement contained in the [resource type handler contract](resource-type-test-contract.md). Each handler invocation is expected to follow the general requirements for that handler listed in the contract. This topic lists tests that explicitly test some more specific requirements.

When you run the contract tests with the `--v2` flag, the CloudFormation CLI runs the test suite described in [Contract tests performed with the --v2 flag](#contract-tests-v2). Tests run with `--v2` additionally validate your resource schema, your test input files, and the live state of provisioned resources. When you register a resource type, it must pass the `--v2` tests. This requirement applies to all newly registered resource types.

## `create` handler tests
<a name="contract-tests-create"></a>

The CloudFormation CLI performs the following contract tests for `create` handlers.

| Test | Description |
| --- | --- |
| `contract_create_create` | Creates a resource, waits for the resource creation to complete, and then creates the resource again with the expectation that the second create operation will fail with the `AlreadyExists` error code. This test isn't run for resources if the primary identifier or any additional identifiers are read-only. |
| `contract_create_read` | Creates a resource, waits for the resource creation to complete, and then reads the created resource to ensure that the input to the `create` handler is equal to the output from the `read` handler. The comparison ignores any read-only/generated properties in the `read` output, as create input can't specify these. It also ignores any write-only properties in the create input, as these are removed from read output to avoid security issues. |
| `contract_create_delete` | Creates a resource, waits for the resource creation to complete, and then deletes the created resource. It also checks if the create input is equal to the create output (which is then used for delete input), with the exception of readOnly and writeOnly properties. |
| `contract_create_list` | Creates a resource, waits for the resource creation to complete, and then lists out the resources with the expectation that the created resource exists in the returned list. |

## `update` handler tests
<a name="contract-tests-update"></a>

The CloudFormation CLI performs the following contract tests for `update` handlers.

| Test | Description |
| --- | --- |
| `contract_update_read` | Creates a resource, updates the resource, and then reads the resource to check that the update was made by comparing the read output with the update input. The comparison excludes read-only and write-only properties because they can't be included in the update input and read output, respectively. |
| `contract_update_list` | Creates a resource, updates the resource, and then lists the resource to check that the updated resource exists in the returned list. |
| `contract_update_without_create` | Updates a resource without creating it first. The test expects the update operation to fail with the `NotFound` error code. |

## `delete` handler tests
<a name="contract-tests-delete"></a>

The CloudFormation CLI performs the following contract tests for `delete` handlers.

| Test | Description |
| --- | --- |
| `contract_delete_create` | Creates a resource, deletes the resource, and then creates the resource again with the expectation that the deletion was successful and a new resource can be created. The CloudFormation CLI performs this contract test for resources with create-only primary identifiers. |
| `contract_delete_update` | Creates a resource, deletes the resource, and then updates the resource with the expectation that the update operation will fail with the `NotFound` error code. |
| `contract_delete_read` | Creates a resource, deletes the resource, and then reads the resource with the expectation that the read operation will fail with the `NotFound` error code. |
| `contract_delete_list` | Creates a resource, deletes the resource, and then lists the resource with the expectation that the returned list doesn't contain the deleted resource. |
| `contract_delete_delete` | Creates a resource, deletes the resource, and then deletes the resource again with the expectation that the second delete operation will fail with the `NotFound` error code. |

## Contract tests performed with the --v2 flag
<a name="contract-tests-v2"></a>

When you run `cfn test --v2`, the CloudFormation CLI automatically selects the applicable tests based on the handlers and properties declared in your resource type schema. In addition to handler tests, the `--v2` suite validates your resource schema and your test input files. It also verifies the live state of resources after mutating operations by reading them back.

### Schema validation tests
<a name="contract-tests-v2-schema"></a>

The following table describes the schema validation tests that the `--v2` suite performs.

| Test | Description |
| --- | --- |
| Schema linter checks | Validates the resource schema against the resource schema validation rules. Each failed check reports the rule, message, and schema path. |
| Schema backward-compatibility checks | Compares the schema against your previously registered schema version and fails on breaking changes, such as removed properties, tightened constraints, or a changed primary identifier. |

### `create` handler tests
<a name="contract-tests-v2-create"></a>

The following table describes the `create` handler tests that the `--v2` suite performs.

| Test | Description |
| --- | --- |
| `test_create` | Creates a resource and expects `SUCCESS` with a model containing a valid primary identifier. |
| `test_create_create` | While the first resource exists, invokes the `create` handler again with identical desired properties and expects `FAILED` with an `AlreadyExists` error code. |
| `test_create_create_primary_id_check` | If the second create returns `SUCCESS` instead, the returned primary identifier must identify a new, distinct resource — the handler must not adopt the existing resource. |
| `test_create_read` | Reads the original resource after the second create (and after any rollback delete) and expects `SUCCESS` — creating or rolling back one resource must not affect another. |
| `test_create_create_read` | After a successful create, a subsequent `read` request for the created resource must succeed. |
| `test_create_with_read_response_lcs` | Reads the created resource, removes read-only properties from the output, and uses the result as the desired state for a new create. The create must succeed, proving that read output is usable as a template. |

### `read` output tests
<a name="contract-tests-v2-read"></a>

These assertions are applied to `read` responses throughout the suite.

| Test | Description |
| --- | --- |
| `test_read_input_output_negative_match` | A `read` response must not return fewer properties, or different values, than the request that produced the state. |
| `test_read_return_readonly_properties` | Every property in `readOnlyProperties` must be returned in a `read` response. |
| `test_read_return_write_only_properties` | Properties in `writeOnlyProperties` must not be returned in a `read` response. |
| `test_read_output_over_schema` | The `read` response model must conform to the shape of the resource schema. |
| `test_read_return_all_schema_properties_using_one_or_more_inputs` | The union of all successful `read` responses across the suite must cover every schema-defined property (excluding write-only and exempted properties). Supply additional input files if a single input can't exercise every property. |

### `update` handler tests
<a name="contract-tests-v2-update"></a>

The following table describes the `update` handler tests that the `--v2` suite performs.

| Test | Description |
| --- | --- |
| `test_update` | Creates a resource, applies the update input, and expects the update to return `SUCCESS`. |
| `test_update_read` | After a successful update, a `read` using the primary identifier returned by the update must succeed. |
| `test_update_primary_id_check` | The primary identifier returned by the update must equal the identifier returned by the create. |
| `test_read_by_create_equals_read_by_update` | A `read` using the create-returned identifier and a `read` using the update-returned identifier must return identical models. |
| `test_update_list` | After a successful update, a `list` operation must return `SUCCESS` and contain the updated resource's primary identifier. |

### `delete` handler tests
<a name="contract-tests-v2-delete"></a>

The following table describes the `delete` handler tests that the `--v2` suite performs.

| Test | Description |
| --- | --- |
| `test_create_delete` | Creates a resource and expects a subsequent delete to return `SUCCESS`. |
| `test_delete_read` | After a successful delete, a `read` for the deleted resource must return `FAILED` with a `NotFound` error code. |
| `test_delete_update` | After a successful delete, an `update` for the deleted resource must return `FAILED` with a `NotFound` error code. |
| `test_delete_delete` | After a successful delete, a second `delete` must return `FAILED` with a `NotFound` error code. |
| `test_delete_list` | After a successful delete, the deleted resource must not appear in `list` results. |
| `test_delete_create` | After a successful delete, creating the resource again must not fail with `AlreadyExists` or `InternalFailure`. |

### `list` handler tests
<a name="contract-tests-v2-list"></a>

The following table describes the `list` handler tests that the `--v2` suite performs.

| Test | Description |
| --- | --- |
| `test_create_list` | After a successful create, a `list` operation must return `SUCCESS` and contain the created resource's primary identifier. |
| `test_create_list_read` | Every primary identifier returned by `list` must be readable — a `read` for a listed identifier must not return `NotFound`. |

### Test input validation
<a name="contract-tests-v2-inputs"></a>

The following table describes the test input validation checks that the `--v2` suite performs.

| Test | Description |
| --- | --- |
| `no_hardcoded_regions` | Test input files must not contain hardcoded Region names; use the `{{region}}` template variable instead. |
| `no_hardcoded_account_ids` | Test input files must not contain hardcoded account IDs; use the `{{account}}` template variable or an allowed placeholder account ID. |
| `no_hardcoded_partitions` | Test input files must not contain hardcoded partition names; use the `{{partition}}` template variable. |

**Property coverage**

Your create and update inputs together must exercise the properties declared in your schema. Missing or invalid coverage is reported per property path.

**Note**
The `{{region}}`, `{{account}}`, and `{{partition}}` template variables apply to input files used with `--v2`. With the default `cfn test` command, `{{ }}` expressions in input and override files refer to CloudFormation stack exports in your account.
