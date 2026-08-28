---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionRedrivenEventDetails.html
---

# ExecutionRedrivenEventDetails
<a name="API_ExecutionRedrivenEventDetails"></a>

Contains details about a redriven execution.

## Contents
<a name="API_ExecutionRedrivenEventDetails_Contents"></a>

 ** redriveCount **   <a name="StepFunctions-Type-ExecutionRedrivenEventDetails-redriveCount"></a>
The number of times you've redriven an execution. If you have not yet redriven an execution, the `redriveCount` is 0. This count is not updated for redrives that failed to start or are pending to be redriven.
Type: Integer
Required: No

## See Also
<a name="API_ExecutionRedrivenEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ExecutionRedrivenEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ExecutionRedrivenEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ExecutionRedrivenEventDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
