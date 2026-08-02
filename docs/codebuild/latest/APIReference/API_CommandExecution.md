---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CommandExecution.html
---

# CommandExecution
<a name="API_CommandExecution"></a>

Contains command execution information.

## Contents
<a name="API_CommandExecution_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** command **   <a name="CodeBuild-Type-CommandExecution-command"></a>
The command that needs to be executed.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** endTime **   <a name="CodeBuild-Type-CommandExecution-endTime"></a>
When the command execution process ended, expressed in Unix time format.
Type: Timestamp
Required: No

 ** exitCode **   <a name="CodeBuild-Type-CommandExecution-exitCode"></a>
The exit code to return upon completion.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** id **   <a name="CodeBuild-Type-CommandExecution-id"></a>
The ID of the command execution.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** logs **   <a name="CodeBuild-Type-CommandExecution-logs"></a>
Information about build logs in CloudWatch Logs.
Type: [LogsLocation](API_LogsLocation.md) object
Required: No

 ** sandboxArn **   <a name="CodeBuild-Type-CommandExecution-sandboxArn"></a>
A `sandboxArn`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** sandboxId **   <a name="CodeBuild-Type-CommandExecution-sandboxId"></a>
A `sandboxId`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** standardErrContent **   <a name="CodeBuild-Type-CommandExecution-standardErrContent"></a>
The text written by the command to stderr.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** standardOutputContent **   <a name="CodeBuild-Type-CommandExecution-standardOutputContent"></a>
The text written by the command to stdout.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** startTime **   <a name="CodeBuild-Type-CommandExecution-startTime"></a>
When the command execution process started, expressed in Unix time format.
Type: Timestamp
Required: No

 ** status **   <a name="CodeBuild-Type-CommandExecution-status"></a>
The status of the command execution.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** submitTime **   <a name="CodeBuild-Type-CommandExecution-submitTime"></a>
When the command execution process was initially submitted, expressed in Unix time format.
Type: Timestamp
Required: No

 ** type **   <a name="CodeBuild-Type-CommandExecution-type"></a>
The command type.
Type: String
Valid Values: `SHELL`
Required: No

## See Also
<a name="API_CommandExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/CommandExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/CommandExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/CommandExecution)
