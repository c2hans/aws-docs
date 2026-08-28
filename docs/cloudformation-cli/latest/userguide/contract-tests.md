---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/contract-tests.html
---

# Contract tests for resource types
<a name="contract-tests"></a>

As part of testing your resource, the CloudFormation CLI performs a suite of tests, each written to test a requirement contained in the [resource type handler contract](resource-type-test-contract.md). Each handler invocation is expected to follow the general requirements for that handler listed in the contract. This topic lists tests that explicitly test some more specific requirements.

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
