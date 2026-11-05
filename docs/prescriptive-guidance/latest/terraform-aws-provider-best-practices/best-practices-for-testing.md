---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/best-practices-for-testing.html
---

# Best practices for testing
<a name="best-practices-for-testing"></a>

Testing catches mistakes before they reach an environment. Terraform provides two layers of checks. Validation in the configuration (variable validation, preconditions and postconditions, and `check` blocks) runs during every plan. The `terraform test` command (Terraform 1.6 and later) runs test files against a module, either with a mocked provider or by creating real resources. Run both in your pipeline, together with the formatting, linting, and scanning steps described in [Follow coding standards](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/structure.html#coding-standards).

## Validate inputs and assumptions in the configuration
<a name="validate-inputs-and-assumptions-in-the-configuration"></a>
+ **Variable validation** rejects a bad input before Terraform plans anything. Use it for rules about a single input, such as a name format.
+ **Preconditions and postconditions** in a resource's `lifecycle` block check assumptions about the resource or its environment, such as the Region that the provider uses. A failed condition stops the run.
+ **check blocks** (Terraform 1.5 and later) report a warning without stopping the run. Use them for ongoing checks, such as whether an endpoint responds.

In a `check` block, refer to input values rather than to resources that the same run creates. For example, a `check` block that reads a bucket with a data source should look it up by `var.name`, not by `aws_s3_bucket.this.id`. If it refers to the bucket resource, Terraform can't read it until after the apply, and plan-mode tests fail with `Check block assertion known after apply`.

## Write unit tests with mock providers
<a name="write-unit-tests-with-mock-providers"></a>

A `mock_provider` block (Terraform 1.7 and later) replaces the AWS Provider with generated values, so tests run in seconds and need no AWS credentials. Use mocks to test variable validation, conditions, and the values that the module computes. Inside `mock_provider`, `mock_data` and `mock_resource` blocks set the values that data sources and resources return.

The following test file checks that a module rejects a bucket name that breaks its `validation` rule for `var.name`. The run succeeds only if the validation fails:

```
mock_provider "aws" {}

run "uppercase_name_rejected" {
  command = plan

  variables {
    name = "Not_Valid"
  }

  expect_failures = [var.name]
}
```

To test a failed precondition or `check` block, list the resource or `check.<name>` in `expect_failures`. A run that fails more than one condition must list all of them.

In Terraform 1.17 and later, `mock_provider` also accepts `mock_ephemeral` blocks. With them, unit tests can run configurations that read secrets through ephemeral resources, such as the example in [Keep secrets out of state](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/security.html#keep-secrets-out-of-state), without calling the AWS provider. Set `secret_string` in a `mock_ephemeral "aws_secretsmanager_secret_version"` block.

## Write integration tests
<a name="write-integration-tests"></a>

Integration tests create real resources, check them, and then destroy them. Run them in a dedicated test account. In the test file, configure the provider with `allowed_account_ids` set to that account, and with default tags that identify test resources, so that you can find anything that a failed run leaves behind. Use `command = apply` in the `run` blocks, and assert on attributes that only AWS can set, such as ARNs.

`terraform test` destroys the resources that each test file creates, even when an assertion fails. Keep integration tests in their own file, such as `tests/integration.tftest.hcl`, so that you can run the fast unit tests on every commit and the integration tests on a schedule or before a release. To run one file, use `terraform test -filter=tests/unit.tftest.hcl`.

Use both kinds of test, because each catches what the other misses:
+ **Unit tests with mocks** are fast, low-cost, and safe to run on every commit, and they need no credentials. They can't tell you whether AWS accepts the configuration, because the mock returns whatever you tell it to.
+ **Integration tests** prove that the configuration works against real APIs, including quotas, permissions, and service behavior. They take minutes, cost money while the resources exist, need a test account and credentials, and can leave resources behind if a run is interrupted.

For more information, see [Tests](https://developer.hashicorp.com/terraform/language/tests) in the HashiCorp documentation and the AWS Prescriptive Guidance pattern [Test AWS infrastructure by using LocalStack and Terraform Tests](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/test-aws-infra-localstack-terraform.html).
