---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Execution.html
---

# Execution
<a name="API_Execution"></a>

Information about Diagnostic Tool Execution.

## Contents
<a name="API_Execution_Contents"></a>

 ** creationTime **   <a name="diagnostictools-Type-Execution-creationTime"></a>
Execution Creation timestamp in Epoch format.
Type: Timestamp
Required: Yes

 ** executionId **   <a name="diagnostictools-Type-Execution-executionId"></a>
Resource Identifier for Execution initiated via StartExecution Operation.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `e-[a-zA-Z0-9]{10}`
Required: Yes

 ** parameters **   <a name="diagnostictools-Type-Execution-parameters"></a>
Diagnostic Tool Execution Input parameters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32764.
Required: Yes

 ** requesterArn **   <a name="diagnostictools-Type-Execution-requesterArn"></a>
IAM User ARN of user/role who initiated the Execution.
Type: String
Required: Yes

 ** requesterId **   <a name="diagnostictools-Type-Execution-requesterId"></a>
IAM User ID who initiated the Execution.
Type: String
Required: Yes

 ** requestState **   <a name="diagnostictools-Type-Execution-requestState"></a>
Indicate state of Execution.
Type: String
Valid Values: `ACCEPTED | SUBMITTED | REJECTED`
Required: Yes

 ** roleArn **   <a name="diagnostictools-Type-Execution-roleArn"></a>
The Execution role used by AWS Diagnostic Tools during Diagnostic Tool invocation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z0-9-]*:iam::\d{12}:role\/[\w\-\/.@+=,]{1,65}`
Required: Yes

 ** storageRegion **   <a name="diagnostictools-Type-Execution-storageRegion"></a>
The AWS Regions where Execution result will be stored.
Type: String
Valid Values: `us-east-2 | us-west-2 | eu-west-1`
Required: Yes

 ** toolId **   <a name="diagnostictools-Type-Execution-toolId"></a>
Tool Id associated with Execution.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `\w+`
Required: Yes

 ** toolVersionId **   <a name="diagnostictools-Type-Execution-toolVersionId"></a>
Diagnostic Tool version identifier associated with tool artifact.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 17.
Pattern: `[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}`
Required: Yes

 ** status **   <a name="diagnostictools-Type-Execution-status"></a>
The Execution Status.
Type: String
Valid Values: `CREATED | IN_PROGRESS | SUCCESSFUL | FAILED | CANCELLED | TIMED_OUT`
Required: No

 ** targetRegions **   <a name="diagnostictools-Type-Execution-targetRegions"></a>
The AWS Regions targeted by the Diagnostic Tool Execution.
Type: Array of strings
Required: No

## See Also
<a name="API_Execution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/Execution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/Execution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/Execution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Diagnostic Tools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query diagnostic-tools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
