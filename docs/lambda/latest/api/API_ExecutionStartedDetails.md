---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ExecutionStartedDetails.html
---

# ExecutionStartedDetails
<a name="API_ExecutionStartedDetails"></a>

Details about a durable execution that started.

## Contents
<a name="API_ExecutionStartedDetails_Contents"></a>

 ** ExecutionTimeout **   <a name="lambda-Type-ExecutionStartedDetails-ExecutionTimeout"></a>
The maximum amount of time that the durable execution is allowed to run, in seconds.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Input **   <a name="lambda-Type-ExecutionStartedDetails-Input"></a>
The input payload provided for the durable execution.
Type: [EventInput](API_EventInput.md) object
Required: Yes

## See Also
<a name="API_ExecutionStartedDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ExecutionStartedDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ExecutionStartedDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ExecutionStartedDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
