---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeRuntimeVersions.html
---

# DescribeRuntimeVersions
<a name="API_DescribeRuntimeVersions"></a>

Returns a list of Synthetics canary runtime versions. For more information, see [ Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html).

## Request Syntax
<a name="API_DescribeRuntimeVersions_RequestSyntax"></a>

```
POST /runtime-versions HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeRuntimeVersions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeRuntimeVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeRuntimeVersions_RequestSyntax) **   <a name="synthetics-DescribeRuntimeVersions-request-MaxResults"></a>
Specify this parameter to limit how many runs are returned each time you use the `DescribeRuntimeVersions` operation. If you omit this parameter, the default of 100 is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRuntimeVersions_RequestSyntax) **   <a name="synthetics-DescribeRuntimeVersions-request-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent `DescribeRuntimeVersions` operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 252.
Required: No

## Response Syntax
<a name="API_DescribeRuntimeVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RuntimeVersions": [
      {
         "DeprecationDate": number,
         "Description": "string",
         "ReleaseDate": number,
         "VersionName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRuntimeVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRuntimeVersions_ResponseSyntax) **   <a name="synthetics-DescribeRuntimeVersions-response-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent `DescribeRuntimeVersions` operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 252.

 ** [RuntimeVersions](#API_DescribeRuntimeVersions_ResponseSyntax) **   <a name="synthetics-DescribeRuntimeVersions-response-RuntimeVersions"></a>
An array of objects that display the details about each Synthetics canary runtime version.
Type: Array of [RuntimeVersion](API_RuntimeVersion.md) objects

## Errors
<a name="API_DescribeRuntimeVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRuntimeVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/DescribeRuntimeVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/DescribeRuntimeVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/DescribeRuntimeVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/DescribeRuntimeVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/DescribeRuntimeVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/DescribeRuntimeVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/DescribeRuntimeVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/DescribeRuntimeVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/DescribeRuntimeVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/DescribeRuntimeVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
