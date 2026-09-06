---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHubs.html
---

# ListHubs
<a name="API_ListHubs"></a>

List all existing hubs.

## Request Syntax
<a name="API_ListHubs_RequestSyntax"></a>

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
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListHubs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListHubs_RequestSyntax) **   <a name="sagemaker-ListHubs-request-CreationTimeAfter"></a>
Only list hubs that were created after the time specified.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListHubs_RequestSyntax) **   <a name="sagemaker-ListHubs-request-CreationTimeBefore"></a>
Only list hubs that were created before the time specified.
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListHubs_RequestSyntax) **   <a name="sagemaker-ListHubs-request-LastModifiedTimeAfter"></a>
Only list hubs that were last modified after the time specified.
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListHubs_RequestSyntax) **   <a name="sagemaker-ListHubs-request-LastModifiedTimeBefore"></a>
Only list hubs that were last modified before the time specified.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListHubs_RequestSyntax) **   <a name="sagemaker-ListHubs-request-MaxResults"></a>
The maximum number of hubs to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListHubs_RequestSyntax) **   <a name="sagemaker-ListHubs-request-NameContains"></a>
Only list hubs with names that contain the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListHubs_RequestSyntax) **   <a name="sagemaker-ListHubs-request-NextToken"></a>
If the response to a previous `ListHubs` request was truncated, the response includes a `NextToken`. To retrieve the next set of hubs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListHubs_RequestSyntax) **   <a name="sagemaker-ListHubs-request-SortBy"></a>
Sort hubs by either name or creation time.
Type: String
Valid Values: `HubName | CreationTime | HubStatus | AccountIdOwner`
Required: No

 ** [SortOrder](#API_ListHubs_RequestSyntax) **   <a name="sagemaker-ListHubs-request-SortOrder"></a>
Sort hubs by ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListHubs_ResponseSyntax"></a>

```
{
   "HubSummaries": [
      {
         "CreationTime": number,
         "HubArn": "string",
         "HubDescription": "string",
         "HubDisplayName": "string",
         "HubName": "string",
         "HubSearchKeywords": [ "string" ],
         "HubStatus": "string",
         "LastModifiedTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHubs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubSummaries](#API_ListHubs_ResponseSyntax) **   <a name="sagemaker-ListHubs-response-HubSummaries"></a>
The summaries of the listed hubs.
Type: Array of [HubInfo](API_HubInfo.md) objects

 ** [NextToken](#API_ListHubs_ResponseSyntax) **   <a name="sagemaker-ListHubs-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of hubs, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListHubs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListHubs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListHubs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListHubs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListHubs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListHubs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListHubs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListHubs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListHubs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListHubs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListHubs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListHubs)
