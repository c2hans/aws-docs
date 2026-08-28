---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ChainedInvokeStartedDetails.html
---

# ChainedInvokeStartedDetails
<a name="API_ChainedInvokeStartedDetails"></a>

Contains details about a chained function invocation that has started execution, including start time and execution context.

## Contents
<a name="API_ChainedInvokeStartedDetails_Contents"></a>

 ** FunctionName **   <a name="lambda-Type-ChainedInvokeStartedDetails-FunctionName"></a>
The name or ARN of the Lambda function being invoked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** DurableExecutionArn **   <a name="lambda-Type-ChainedInvokeStartedDetails-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) that identifies the durable execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`
Required: No

 ** ExecutedVersion **   <a name="lambda-Type-ChainedInvokeStartedDetails-ExecutedVersion"></a>
The version of the function that was executed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(\$LATEST(\.PUBLISHED)?|[0-9]+)`
Required: No

 ** Input **   <a name="lambda-Type-ChainedInvokeStartedDetails-Input"></a>
The JSON input payload provided to the chained invocation.
Type: [EventInput](API_EventInput.md) object
Required: No

 ** TenantId **   <a name="lambda-Type-ChainedInvokeStartedDetails-TenantId"></a>
The tenant identifier for the chained invocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\._:\/=+\-@ ]+`
Required: No

## See Also
<a name="API_ChainedInvokeStartedDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ChainedInvokeStartedDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ChainedInvokeStartedDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ChainedInvokeStartedDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
