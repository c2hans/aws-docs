---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListJobSchemaVersions.html
---

# ListJobSchemaVersions
<a name="API_ListJobSchemaVersions"></a>

Lists available configuration schema versions for a specified job category. Use the schema versions with `DescribeJobSchemaVersion` to retrieve the full schema document.

The following operations are related to `ListJobSchemaVersions`:
+  `DescribeJobSchemaVersion`
+  `CreateJob`

## Request Syntax
<a name="API_ListJobSchemaVersions_RequestSyntax"></a>

```
{
   "JobCategory": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListJobSchemaVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobCategory](#API_ListJobSchemaVersions_RequestSyntax) **   <a name="sagemaker-ListJobSchemaVersions-request-JobCategory"></a>
The category of job schemas to list.
Type: String
Valid Values: `AgentRFT | AgentRFTEvaluation`
Required: Yes

 ** [MaxResults](#API_ListJobSchemaVersions_RequestSyntax) **   <a name="sagemaker-ListJobSchemaVersions-request-MaxResults"></a>
The maximum number of schema versions to return in the response. The default value is 5.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListJobSchemaVersions_RequestSyntax) **   <a name="sagemaker-ListJobSchemaVersions-request-NextToken"></a>
If the previous response was truncated, this token retrieves the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListJobSchemaVersions_ResponseSyntax"></a>

```
{
   "JobConfigSchemas": [
      {
         "JobConfigSchemaVersion": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListJobSchemaVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobConfigSchemas](#API_ListJobSchemaVersions_ResponseSyntax) **   <a name="sagemaker-ListJobSchemaVersions-response-JobConfigSchemas"></a>
An array of `JobConfigSchemaVersionSummary` objects listing the available schema versions.
Type: Array of [JobConfigSchemaVersionSummary](API_JobConfigSchemaVersionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_ListJobSchemaVersions_ResponseSyntax) **   <a name="sagemaker-ListJobSchemaVersions-response-NextToken"></a>
If the response is truncated, this token retrieves the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListJobSchemaVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListJobSchemaVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListJobSchemaVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListJobSchemaVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListJobSchemaVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListJobSchemaVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListJobSchemaVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListJobSchemaVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListJobSchemaVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListJobSchemaVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListJobSchemaVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListJobSchemaVersions)
