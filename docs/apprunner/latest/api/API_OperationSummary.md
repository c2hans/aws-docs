---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_OperationSummary.html
---

# OperationSummary
<a name="API_OperationSummary"></a>

Provides summary information for an operation that occurred on an AWS App Runner service.

## Contents
<a name="API_OperationSummary_Contents"></a>

 ** EndedAt **   <a name="apprunner-Type-OperationSummary-EndedAt"></a>
The time when the operation ended. It's in the Unix time stamp format.
Type: Timestamp
Required: No

 ** Id **   <a name="apprunner-Type-OperationSummary-Id"></a>
A unique ID of this operation. It's unique in the scope of the App Runner service.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
Required: No

 ** StartedAt **   <a name="apprunner-Type-OperationSummary-StartedAt"></a>
The time when the operation started. It's in the Unix time stamp format.
Type: Timestamp
Required: No

 ** Status **   <a name="apprunner-Type-OperationSummary-Status"></a>
The current state of the operation.
Type: String
Valid Values: `PENDING | IN_PROGRESS | FAILED | SUCCEEDED | ROLLBACK_IN_PROGRESS | ROLLBACK_FAILED | ROLLBACK_SUCCEEDED`
Required: No

 ** TargetArn **   <a name="apprunner-Type-OperationSummary-TargetArn"></a>
The Amazon Resource Name (ARN) of the resource that the operation acted on (for example, an App Runner service).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** Type **   <a name="apprunner-Type-OperationSummary-Type"></a>
The type of operation. It indicates a specific action that occured.
Type: String
Valid Values: `START_DEPLOYMENT | CREATE_SERVICE | PAUSE_SERVICE | RESUME_SERVICE | DELETE_SERVICE | UPDATE_SERVICE`
Required: No

 ** UpdatedAt **   <a name="apprunner-Type-OperationSummary-UpdatedAt"></a>
The time when the operation was last updated. It's in the Unix time stamp format.
Type: Timestamp
Required: No

## See Also
<a name="API_OperationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/OperationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/OperationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/OperationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
