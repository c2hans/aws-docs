---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_AssociationStateReason.html
---

# AssociationStateReason
<a name="API_AssociationStateReason"></a>

Indicates the reason that the association deployment failed, including the error code and error message.

## Contents
<a name="API_AssociationStateReason_Contents"></a>

 ** ErrorCode **   <a name="WorkSpaces-Type-AssociationStateReason-ErrorCode"></a>
The error code of the association deployment failure.
Type: String
Valid Values: `ValidationError.InsufficientDiskSpace | ValidationError.InsufficientMemory | ValidationError.UnsupportedOperatingSystem | DeploymentError.InternalServerError | DeploymentError.WorkspaceUnreachable | ValidationError.ApplicationOldVersionExists`
Required: No

 ** ErrorMessage **   <a name="WorkSpaces-Type-AssociationStateReason-ErrorMessage"></a>
The error message of the association deployment failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_AssociationStateReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/AssociationStateReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/AssociationStateReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/AssociationStateReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
