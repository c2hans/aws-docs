---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ResourcePermission.html
---

# ResourcePermission
<a name="API_ResourcePermission"></a>

Permission for the resource.

## Contents
<a name="API_ResourcePermission_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Actions **   <a name="QS-Type-ResourcePermission-Actions"></a>
The IAM action to grant or revoke permissions on.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** Principal **   <a name="QS-Type-ResourcePermission-Principal"></a>
The Amazon Resource Name (ARN) of the principal. This can be one of the following:
+ The ARN of an Quick Sight user or group associated with a data source or dataset. (This is common.)
+ The ARN of an Quick Sight user, group, or namespace associated with an analysis, dashboard, template, or theme. Namespace sharing is not supported for action connectors. (This is common.)
+ The ARN of an AWS account root: This is an IAM ARN rather than a Quick Sight ARN. Use this option only to share resources (templates) across AWS accounts. Account root sharing is not supported for action connectors. (This is less common.)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_ResourcePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ResourcePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ResourcePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ResourcePermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
