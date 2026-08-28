---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_StackInstance.html
---

# StackInstance
<a name="API_StackInstance"></a>

An AWS CloudFormation stack, in a specific account and Region, that's part of a stack set operation. A stack instance is a reference to an attempted or actual stack in a given account within a given Region. A stack instance can exist without a stack—for example, if the stack couldn't be created for some reason. A stack instance is associated with only one stack set. Each stack instance contains the ID of its associated stack set, as well as the ID of the actual stack and the stack status.

## Contents
<a name="API_StackInstance_Contents"></a>

 ** Account **   <a name="servicecatalog-Type-StackInstance-Account"></a>
The name of the AWS account that the stack instance is associated with.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** Region **   <a name="servicecatalog-Type-StackInstance-Region"></a>
The name of the AWS Region that the stack instance is associated with.
Type: String
Required: No

 ** StackInstanceStatus **   <a name="servicecatalog-Type-StackInstance-StackInstanceStatus"></a>
The status of the stack instance, in terms of its synchronization with its associated stack set.
+  `INOPERABLE`: A `DeleteStackInstances` operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further `UpdateStackSet` operations. You might need to perform a `DeleteStackInstances` operation, with `RetainStacks` set to true, to delete the stack instance, and then delete the stack manually.
+  `OUTDATED`: The stack isn't currently up to date with the stack set because either the associated stack failed during a `CreateStackSet` or `UpdateStackSet` operation, or the stack was part of a `CreateStackSet` or `UpdateStackSet` operation that failed or was stopped before the stack was created or updated.
+  `CURRENT`: The stack is currently up to date with the stack set.
Type: String
Valid Values: `CURRENT | OUTDATED | INOPERABLE`
Required: No

## See Also
<a name="API_StackInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/StackInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/StackInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/StackInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
