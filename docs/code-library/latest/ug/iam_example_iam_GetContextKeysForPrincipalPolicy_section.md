---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam_GetContextKeysForPrincipalPolicy_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetContextKeysForPrincipalPolicy` with a CLI
<a name="iam_example_iam_GetContextKeysForPrincipalPolicy_section"></a>

The following code examples show how to use `GetContextKeysForPrincipalPolicy`.

------
#### [ CLI ]

**AWS CLI**
**To list the context keys referenced by all policies associated with an IAM principal**
The following `get-context-keys-for-principal-policy` command retrieves all policies that are attached to the user `saanvi` and any groups she is a member of. It then parses each and lists the context keys used by those policies. Use this command to identify which context key values you must supply to successfully use the `simulate-custom-policy` and `simulate-principal-policy` commands. You can also retrieve the list of context keys used by an arbitrary JSON policy by using the `get-context-keys-for-custom-policy` command.

```
aws iam get-context-keys-for-principal-policy \
   --policy-source-arn {{arn:aws:iam::123456789012:user/saanvi}}
```
Output:

```
{
    "ContextKeyNames": [
        "aws:username",
        "aws:CurrentTime"
    ]
}
```
For more information, see [Using the IAM Policy Simulator (AWS CLI and AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html#policies-simulator-using-api) in the *AWS IAM User Guide*.
+  For API details, see [GetContextKeysForPrincipalPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-context-keys-for-principal-policy.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example fetches all the context keys present in the provided policy json and the policies attached to IAM entity(user/role etc.). For -PolicyInputList you can provide multiple values list as comma separated values. **

```
$policy1 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}'
$policy2 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/"}}'
Get-IAMContextKeysForPrincipalPolicy -PolicyInputList $policy1,$policy2 -PolicySourceArn arn:aws:iam::852640994763:user/TestUser
```
+  For API details, see [GetContextKeysForPrincipalPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example fetches all the context keys present in the provided policy json and the policies attached to IAM entity(user/role etc.). For -PolicyInputList you can provide multiple values list as comma separated values. **

```
$policy1 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}'
$policy2 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/"}}'
Get-IAMContextKeysForPrincipalPolicy -PolicyInputList $policy1,$policy2 -PolicySourceArn arn:aws:iam::852640994763:user/TestUser
```
+  For API details, see [GetContextKeysForPrincipalPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
