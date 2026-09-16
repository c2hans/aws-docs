---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelPackageGroups.html
---

# ListModelPackageGroups
<a name="API_ListModelPackageGroups"></a>

Gets a list of the model groups in your AWS account.

## Request Syntax
<a name="API_ListModelPackageGroups_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "CrossAccountFilterOption": "{{string}}",
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModelPackageGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListModelPackageGroups_RequestSyntax) **   <a name="sagemaker-ListModelPackageGroups-request-CreationTimeAfter"></a>
A filter that returns only model groups created after the specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListModelPackageGroups_RequestSyntax) **   <a name="sagemaker-ListModelPackageGroups-request-CreationTimeBefore"></a>
A filter that returns only model groups created before the specified time.
Type: Timestamp
Required: No

 ** [CrossAccountFilterOption](#API_ListModelPackageGroups_RequestSyntax) **   <a name="sagemaker-ListModelPackageGroups-request-CrossAccountFilterOption"></a>
A filter that returns either model groups shared with you or model groups in your own account. When the value is `CrossAccount`, the results show the resources made discoverable to you from other accounts. When the value is `SameAccount` or `null`, the results show resources from your account. The default is `SameAccount`.
Type: String
Valid Values: `SameAccount | CrossAccount`
Required: No

 ** [MaxResults](#API_ListModelPackageGroups_RequestSyntax) **   <a name="sagemaker-ListModelPackageGroups-request-MaxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListModelPackageGroups_RequestSyntax) **   <a name="sagemaker-ListModelPackageGroups-request-NameContains"></a>
A string in the model group name. This filter returns only model groups whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListModelPackageGroups_RequestSyntax) **   <a name="sagemaker-ListModelPackageGroups-request-NextToken"></a>
If the result of the previous `ListModelPackageGroups` request was truncated, the response includes a `NextToken`. To retrieve the next set of model groups, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListModelPackageGroups_RequestSyntax) **   <a name="sagemaker-ListModelPackageGroups-request-SortBy"></a>
The field to sort results by. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListModelPackageGroups_RequestSyntax) **   <a name="sagemaker-ListModelPackageGroups-request-SortOrder"></a>
The sort order for results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListModelPackageGroups_ResponseSyntax"></a>

```
{
   "ModelPackageGroupSummaryList": [
      {
         "CreationTime": number,
         "ManagedConfiguration": {
            "ManagedStorageType": "string"
         },
         "ModelPackageGroupArn": "string",
         "ModelPackageGroupDescription": "string",
         "ModelPackageGroupName": "string",
         "ModelPackageGroupStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModelPackageGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelPackageGroupSummaryList](#API_ListModelPackageGroups_ResponseSyntax) **   <a name="sagemaker-ListModelPackageGroups-response-ModelPackageGroupSummaryList"></a>
A list of summaries of the model groups in your AWS account.
Type: Array of [ModelPackageGroupSummary](API_ModelPackageGroupSummary.md) objects

 ** [NextToken](#API_ListModelPackageGroups_ResponseSyntax) **   <a name="sagemaker-ListModelPackageGroups-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of model groups, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModelPackageGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListModelPackageGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModelPackageGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModelPackageGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModelPackageGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModelPackageGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModelPackageGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModelPackageGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModelPackageGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModelPackageGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModelPackageGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModelPackageGroups)
