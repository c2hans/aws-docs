---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_AccountLimit.html
---

# AccountLimit
<a name="API_AccountLimit"></a>

Limits that are related to concurrency and storage. All file and storage sizes are in bytes.

## Contents
<a name="API_AccountLimit_Contents"></a>

 ** CodeSizeUnzipped **   <a name="lambda-Type-AccountLimit-CodeSizeUnzipped"></a>
The maximum size of a function's deployment package and layers when they're extracted.
Type: Long
Required: No

 ** CodeSizeZipped **   <a name="lambda-Type-AccountLimit-CodeSizeZipped"></a>
The maximum size of a deployment package when it's uploaded directly to Lambda. Use Amazon S3 for larger files.
Type: Long
Required: No

 ** ConcurrentExecutions **   <a name="lambda-Type-AccountLimit-ConcurrentExecutions"></a>
The maximum number of simultaneous function executions.
Type: Integer
Required: No

 ** TotalCodeSize **   <a name="lambda-Type-AccountLimit-TotalCodeSize"></a>
The amount of storage space that you can use for all deployment packages and layer archives.
Type: Long
Required: No

 ** UnreservedConcurrentExecutions **   <a name="lambda-Type-AccountLimit-UnreservedConcurrentExecutions"></a>
The maximum number of simultaneous function executions, minus the capacity that's reserved for individual functions with [PutFunctionConcurrency](API_PutFunctionConcurrency.md).
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_AccountLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/AccountLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/AccountLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/AccountLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
