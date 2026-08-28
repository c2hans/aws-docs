---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_emr-containers_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon EMR on EKS examples using AWS CLI
<a name="cli_2_emr-containers_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon EMR on EKS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `update-role-trust-policy`
<a name="emr-containers_UpdateRoleTrustPolicy_cli_2_topic"></a>

The following code example shows how to use `update-role-trust-policy`.

**AWS CLI**
**To update the trust policy of an IAM Role to be used with Amazon EMR on EKS**
This example command updates the trust policy of a role named **example\_iam\_role** such that it can be used with Amazon EMR on EKS with **example\_namespace** namespace from an EKS cluster named **example\_cluster**.
Command:

```
aws emr-containers update-role-trust-policy \
    --cluster example_cluster \
    --namespace example_namespace \
    --role-name example_iam_role
```
Output:

```
If the trust policy has already been updated, then the output will be:
Trust policy statement already exists for role example_iam_role. No
changes were made!

If the trust policy has not been updated yet, then the output will be:
Successfully updated trust policy of role example_iam_role.
```
+  For API details, see [UpdateRoleTrustPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/update-role-trust-policy.html) in *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
