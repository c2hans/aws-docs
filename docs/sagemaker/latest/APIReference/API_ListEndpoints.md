---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEndpoints.html
---

# ListEndpoints
<a name="API_ListEndpoints"></a>

Lists endpoints.

## Request Syntax
<a name="API_ListEndpoints_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "LastModifiedTimeAfter": {{number}},
   "LastModifiedTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-CreationTimeAfter"></a>
A filter that returns only endpoints with a creation time greater than or equal to the specified time (timestamp).
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-CreationTimeBefore"></a>
A filter that returns only endpoints that were created before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-LastModifiedTimeAfter"></a>
 A filter that returns only endpoints that were modified after the specified timestamp.
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-LastModifiedTimeBefore"></a>
 A filter that returns only endpoints that were modified before the specified timestamp.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-MaxResults"></a>
The maximum number of endpoints to return in the response. This value defaults to 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-NameContains"></a>
A string in endpoint names. This filter returns only endpoints whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [NextToken](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-NextToken"></a>
If the result of a `ListEndpoints` request was truncated, the response includes a `NextToken`. To retrieve the next set of endpoints, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-SortBy"></a>
Sorts the list of results. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-SortOrder"></a>
The sort order for results. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListEndpoints_RequestSyntax) **   <a name="sagemaker-ListEndpoints-request-StatusEquals"></a>
 A filter that returns only endpoints with the specified status.
Type: String
Valid Values: `OutOfService | Creating | Updating | SystemUpdating | RollingBack | InService | Deleting | Failed | UpdateRollbackFailed`
Required: No

## Response Syntax
<a name="API_ListEndpoints_ResponseSyntax"></a>

```
{
   "Endpoints": [
      {
         "CreationTime": number,
         "EndpointArn": "string",
         "EndpointName": "string",
         "EndpointStatus": "string",
         "LastModifiedTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Endpoints](#API_ListEndpoints_ResponseSyntax) **   <a name="sagemaker-ListEndpoints-response-Endpoints"></a>
 An array or endpoint objects.
Type: Array of [EndpointSummary](API_EndpointSummary.md) objects

 ** [NextToken](#API_ListEndpoints_ResponseSyntax) **   <a name="sagemaker-ListEndpoints-response-NextToken"></a>
 If the response is truncated, SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
