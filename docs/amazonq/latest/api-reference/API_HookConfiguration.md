---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_HookConfiguration.html
---

# HookConfiguration
<a name="API_HookConfiguration"></a>

Provides the configuration information for invoking a Lambda function in AWS Lambda to alter document metadata and content when ingesting documents into Amazon Q Business.

You can configure your Lambda function using the `PreExtractionHookConfiguration` parameter if you want to apply advanced alterations on the original or raw documents.

If you want to apply advanced alterations on the Amazon Q Business structured documents, you must configure your Lambda function using `PostExtractionHookConfiguration`.

You can only invoke one Lambda function. However, this function can invoke other functions it requires.

For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).

## Contents
<a name="API_HookConfiguration_Contents"></a>

 ** invocationCondition **   <a name="qbusiness-Type-HookConfiguration-invocationCondition"></a>
The condition used for when a Lambda function should be invoked.
For example, you can specify a condition that if there are empty date-time values, then Amazon Q Business should invoke a function that inserts the current date-time.
Type: [DocumentAttributeCondition](API_DocumentAttributeCondition.md) object
Required: No

 ** lambdaArn **   <a name="qbusiness-Type-HookConfiguration-lambdaArn"></a>
The Amazon Resource Name (ARN) of the Lambda function during ingestion. For more information, see [Using Lambda functions for Amazon Q Business document enrichment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-lambda-operations.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:lambda:[a-z-]*-[0-9]:[0-9]{12}:function:[a-zA-Z0-9-_]+(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?(:[a-zA-Z0-9-_]+)?`
Required: No

 ** roleArn **   <a name="qbusiness-Type-HookConfiguration-roleArn"></a>
The Amazon Resource Name (ARN) of a role with permission to run `PreExtractionHookConfiguration` and `PostExtractionHookConfiguration` for altering document metadata and content during the document ingestion process.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** s3BucketName **   <a name="qbusiness-Type-HookConfiguration-s3BucketName"></a>
Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see [Data contracts for Lambda functions](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html#cde-lambda-operations-data-contracts).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: No

## See Also
<a name="API_HookConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/HookConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/HookConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/HookConfiguration)
