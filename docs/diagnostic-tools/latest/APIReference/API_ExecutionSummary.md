---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ExecutionSummary.html
---

# ExecutionSummary
<a name="API_ExecutionSummary"></a>

Information about the Execution.

## Contents
<a name="API_ExecutionSummary_Contents"></a>

 ** creationTime **   <a name="diagnostictools-Type-ExecutionSummary-creationTime"></a>
Describe Execution Creation Time.
Type: Timestamp
Required: Yes

 ** executionId **   <a name="diagnostictools-Type-ExecutionSummary-executionId"></a>
Resource Identifier for Execution initiated via StartExecution Operation.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `e-[a-zA-Z0-9]{10}`
Required: Yes

 ** requesterArn **   <a name="diagnostictools-Type-ExecutionSummary-requesterArn"></a>
The Execution role used by AWS Diagnostic Tools during Diagnostic Tool invocation.
Type: String
Required: Yes

 ** requesterId **   <a name="diagnostictools-Type-ExecutionSummary-requesterId"></a>
IAM User ID who initiated the Execution.
Type: String
Required: Yes

 ** requestState **   <a name="diagnostictools-Type-ExecutionSummary-requestState"></a>
Indicate state of Execution.
Type: String
Valid Values: `ACCEPTED | SUBMITTED | REJECTED`
Required: Yes

 ** roleArn **   <a name="diagnostictools-Type-ExecutionSummary-roleArn"></a>
The Execution role used by AWS Diagnostic Tools during Diagnostic Tool invocation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z0-9-]*:iam::\d{12}:role\/[\w\-\/.@+=,]{1,65}`
Required: Yes

 ** storageRegion **   <a name="diagnostictools-Type-ExecutionSummary-storageRegion"></a>
The AWS Regions targeted by the Diagnostic Tool Execution.
Type: String
Valid Values: `us-east-2 | us-west-2 | eu-west-1`
Required: Yes

 ** toolId **   <a name="diagnostictools-Type-ExecutionSummary-toolId"></a>
Tool Id associated with Execution.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `\w+`
Required: Yes

 ** toolVersionId **   <a name="diagnostictools-Type-ExecutionSummary-toolVersionId"></a>
Diagnostic Tool version identifier associated with tool artifact.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 17.
Pattern: `[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}`
Required: Yes

 ** status **   <a name="diagnostictools-Type-ExecutionSummary-status"></a>
The Execution Status.
Type: String
Valid Values: `CREATED | IN_PROGRESS | SUCCESSFUL | FAILED | CANCELLED | TIMED_OUT`
Required: No

 ** targetRegions **   <a name="diagnostictools-Type-ExecutionSummary-targetRegions"></a>
Describe Execution Target Regions.
Type: Array of strings
Required: No

## See Also
<a name="API_ExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/ExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/ExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/ExecutionSummary)
