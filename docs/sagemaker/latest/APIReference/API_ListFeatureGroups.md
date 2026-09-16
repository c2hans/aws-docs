---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListFeatureGroups.html
---

# ListFeatureGroups
<a name="API_ListFeatureGroups"></a>

List `FeatureGroup`s based on given filter and order.

## Request Syntax
<a name="API_ListFeatureGroups_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "FeatureGroupStatusEquals": "{{string}}",
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "OfflineStoreStatusEquals": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFeatureGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListFeatureGroups_RequestSyntax) **   <a name="sagemaker-ListFeatureGroups-request-CreationTimeAfter"></a>
Use this parameter to search for `FeatureGroups`s created after a specific date and time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListFeatureGroups_RequestSyntax) **   <a name="sagemaker-ListFeatureGroups-request-CreationTimeBefore"></a>
Use this parameter to search for `FeatureGroups`s created before a specific date and time.
Type: Timestamp
Required: No

 ** [FeatureGroupStatusEquals](#API_ListFeatureGroups_RequestSyntax) **   <a name="sagemaker-ListFeatureGroups-request-FeatureGroupStatusEquals"></a>
A `FeatureGroup` status. Filters by `FeatureGroup` status.
Type: String
Valid Values: `Creating | Created | CreateFailed | Deleting | DeleteFailed`
Required: No

 ** [MaxResults](#API_ListFeatureGroups_RequestSyntax) **   <a name="sagemaker-ListFeatureGroups-request-MaxResults"></a>
The maximum number of results returned by `ListFeatureGroups`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListFeatureGroups_RequestSyntax) **   <a name="sagemaker-ListFeatureGroups-request-NameContains"></a>
A string that partially matches one or more `FeatureGroup`s names. Filters `FeatureGroup`s by name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [NextToken](#API_ListFeatureGroups_RequestSyntax) **   <a name="sagemaker-ListFeatureGroups-request-NextToken"></a>
A token to resume pagination of `ListFeatureGroups` results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [OfflineStoreStatusEquals](#API_ListFeatureGroups_RequestSyntax) **   <a name="sagemaker-ListFeatureGroups-request-OfflineStoreStatusEquals"></a>
An `OfflineStore` status. Filters by `OfflineStore` status.
Type: String
Valid Values: `Active | Blocked | Disabled`
Required: No

 ** [SortBy](#API_ListFeatureGroups_RequestSyntax) **   <a name="sagemaker-ListFeatureGroups-request-SortBy"></a>
The value on which the feature group list is sorted.
Type: String
Valid Values: `Name | FeatureGroupStatus | OfflineStoreStatus | CreationTime`
Required: No

 ** [SortOrder](#API_ListFeatureGroups_RequestSyntax) **   <a name="sagemaker-ListFeatureGroups-request-SortOrder"></a>
The order in which feature groups are listed.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListFeatureGroups_ResponseSyntax"></a>

```
{
   "FeatureGroupSummaries": [
      {
         "FeatureGroupArn": "string",
         "FeatureGroupName": "string",
         "FeatureGroupStatus": "string",
         "OfflineStoreStatus": {
            "BlockedReason": "string",
            "Status": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFeatureGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FeatureGroupSummaries](#API_ListFeatureGroups_ResponseSyntax) **   <a name="sagemaker-ListFeatureGroups-response-FeatureGroupSummaries"></a>
A summary of feature groups.
Type: Array of [FeatureGroupSummary](API_FeatureGroupSummary.md) objects

 ** [NextToken](#API_ListFeatureGroups_ResponseSyntax) **   <a name="sagemaker-ListFeatureGroups-response-NextToken"></a>
A token to resume pagination of `ListFeatureGroups` results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListFeatureGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListFeatureGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListFeatureGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListFeatureGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListFeatureGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListFeatureGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListFeatureGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListFeatureGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListFeatureGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListFeatureGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListFeatureGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListFeatureGroups)
