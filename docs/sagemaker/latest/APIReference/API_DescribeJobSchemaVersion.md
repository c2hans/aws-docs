---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeJobSchemaVersion.html
---

# DescribeJobSchemaVersion
<a name="API_DescribeJobSchemaVersion"></a>

Returns the JSON schema for a specified job category and schema version. Use this schema to validate your `JobConfigDocument` before calling `CreateJob`. If you don't specify a schema version, the latest version is returned. The schema defines required fields, allowed values, and constraints for the job configuration.

The following operations are related to `DescribeJobSchemaVersion`:
+  `ListJobSchemaVersions`
+  `CreateJob`

## Request Syntax
<a name="API_DescribeJobSchemaVersion_RequestSyntax"></a>

```
{
   "JobCategory": "{{string}}",
   "JobConfigSchemaVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeJobSchemaVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobCategory](#API_DescribeJobSchemaVersion_RequestSyntax) **   <a name="sagemaker-DescribeJobSchemaVersion-request-JobCategory"></a>
The category of the job schema to describe.
Type: String
Valid Values: `AgentRFT | AgentRFTEvaluation`
Required: Yes

 ** [JobConfigSchemaVersion](#API_DescribeJobSchemaVersion_RequestSyntax) **   <a name="sagemaker-DescribeJobSchemaVersion-request-JobConfigSchemaVersion"></a>
The version of the schema to retrieve. If not specified, the latest version is returned.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 16.
Pattern: `\d+\.\d+\.\d+`
Required: No

## Response Syntax
<a name="API_DescribeJobSchemaVersion_ResponseSyntax"></a>

```
{
   "JobCategory": "string",
   "JobConfigSchema": "string",
   "JobConfigSchemaVersion": "string"
}
```

## Response Elements
<a name="API_DescribeJobSchemaVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobCategory](#API_DescribeJobSchemaVersion_ResponseSyntax) **   <a name="sagemaker-DescribeJobSchemaVersion-response-JobCategory"></a>
The category of the job schema.
Type: String
Valid Values: `AgentRFT | AgentRFTEvaluation`

 ** [JobConfigSchema](#API_DescribeJobSchemaVersion_ResponseSyntax) **   <a name="sagemaker-DescribeJobSchemaVersion-response-JobConfigSchema"></a>
The JSON schema document that defines the structure of the job configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.

 ** [JobConfigSchemaVersion](#API_DescribeJobSchemaVersion_ResponseSyntax) **   <a name="sagemaker-DescribeJobSchemaVersion-response-JobConfigSchemaVersion"></a>
The version of the schema.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 16.
Pattern: `\d+\.\d+\.\d+`

## Errors
<a name="API_DescribeJobSchemaVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeJobSchemaVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeJobSchemaVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeJobSchemaVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeJobSchemaVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeJobSchemaVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeJobSchemaVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeJobSchemaVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeJobSchemaVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeJobSchemaVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeJobSchemaVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeJobSchemaVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
