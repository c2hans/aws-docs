---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListLineageGroups.html
---

# ListLineageGroups
<a name="API_ListLineageGroups"></a>

A list of lineage groups shared with your AWS account. For more information, see [ Cross-Account Lineage Tracking ](https://docs.aws.amazon.com/sagemaker/latest/dg/xaccount-lineage-tracking.html) in the *Amazon SageMaker Developer Guide*.

## Request Syntax
<a name="API_ListLineageGroups_RequestSyntax"></a>

```
{
   "CreatedAfter": {{number}},
   "CreatedBefore": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLineageGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatedAfter](#API_ListLineageGroups_RequestSyntax) **   <a name="sagemaker-ListLineageGroups-request-CreatedAfter"></a>
A timestamp to filter against lineage groups created after a certain point in time.
Type: Timestamp
Required: No

 ** [CreatedBefore](#API_ListLineageGroups_RequestSyntax) **   <a name="sagemaker-ListLineageGroups-request-CreatedBefore"></a>
A timestamp to filter against lineage groups created before a certain point in time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListLineageGroups_RequestSyntax) **   <a name="sagemaker-ListLineageGroups-request-MaxResults"></a>
The maximum number of endpoints to return in the response. This value defaults to 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListLineageGroups_RequestSyntax) **   <a name="sagemaker-ListLineageGroups-request-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of algorithms, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListLineageGroups_RequestSyntax) **   <a name="sagemaker-ListLineageGroups-request-SortBy"></a>
The parameter by which to sort the results. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListLineageGroups_RequestSyntax) **   <a name="sagemaker-ListLineageGroups-request-SortOrder"></a>
The sort order for the results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListLineageGroups_ResponseSyntax"></a>

```
{
   "LineageGroupSummaries": [
      {
         "CreationTime": number,
         "DisplayName": "string",
         "LastModifiedTime": number,
         "LineageGroupArn": "string",
         "LineageGroupName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLineageGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LineageGroupSummaries](#API_ListLineageGroups_ResponseSyntax) **   <a name="sagemaker-ListLineageGroups-response-LineageGroupSummaries"></a>
A list of lineage groups and their properties.
Type: Array of [LineageGroupSummary](API_LineageGroupSummary.md) objects

 ** [NextToken](#API_ListLineageGroups_ResponseSyntax) **   <a name="sagemaker-ListLineageGroups-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of algorithms, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListLineageGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListLineageGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListLineageGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListLineageGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListLineageGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListLineageGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListLineageGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListLineageGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListLineageGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListLineageGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListLineageGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListLineageGroups)
