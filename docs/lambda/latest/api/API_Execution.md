---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_Execution.html
---

# Execution
<a name="API_Execution"></a>

Information about a [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html).

## Contents
<a name="API_Execution_Contents"></a>

 ** DurableExecutionArn **   <a name="lambda-Type-Execution-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) of the durable execution, if this execution is a durable execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`
Required: Yes

 ** DurableExecutionName **   <a name="lambda-Type-Execution-DurableExecutionName"></a>
The unique name of the durable execution, if one was provided when the execution was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** FunctionArn **   <a name="lambda-Type-Execution-FunctionArn"></a>
The Amazon Resource Name (ARN) of the Lambda function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** StartTimestamp **   <a name="lambda-Type-Execution-StartTimestamp"></a>
The date and time when the durable execution started, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: Yes

 ** Status **   <a name="lambda-Type-Execution-Status"></a>
The current status of the durable execution.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT | STOPPED`
Required: Yes

 ** EndTimestamp **   <a name="lambda-Type-Execution-EndTimestamp"></a>
The date and time when the durable execution ended, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: No

 ** KMSKeyArn **   <a name="lambda-Type-Execution-KMSKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`
Required: No

## See Also
<a name="API_Execution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/Execution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/Execution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/Execution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
