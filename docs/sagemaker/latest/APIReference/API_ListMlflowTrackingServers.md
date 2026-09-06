---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMlflowTrackingServers.html
---

# ListMlflowTrackingServers
<a name="API_ListMlflowTrackingServers"></a>

Lists all MLflow Tracking Servers.

## Request Syntax
<a name="API_ListMlflowTrackingServers_RequestSyntax"></a>

```
{
   "CreatedAfter": {{number}},
   "CreatedBefore": {{number}},
   "MaxResults": {{number}},
   "MlflowVersion": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "TrackingServerStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMlflowTrackingServers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatedAfter](#API_ListMlflowTrackingServers_RequestSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-request-CreatedAfter"></a>
Use the `CreatedAfter` filter to only list tracking servers created after a specific date and time. Listed tracking servers are shown with a date and time such as `"2024-03-16T01:46:56+00:00"`. The `CreatedAfter` parameter takes in a Unix timestamp. To convert a date and time into a Unix timestamp, see [EpochConverter](https://www.epochconverter.com/).
Type: Timestamp
Required: No

 ** [CreatedBefore](#API_ListMlflowTrackingServers_RequestSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-request-CreatedBefore"></a>
Use the `CreatedBefore` filter to only list tracking servers created before a specific date and time. Listed tracking servers are shown with a date and time such as `"2024-03-16T01:46:56+00:00"`. The `CreatedBefore` parameter takes in a Unix timestamp. To convert a date and time into a Unix timestamp, see [EpochConverter](https://www.epochconverter.com/).
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListMlflowTrackingServers_RequestSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-request-MaxResults"></a>
The maximum number of tracking servers to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MlflowVersion](#API_ListMlflowTrackingServers_RequestSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-request-MlflowVersion"></a>
Filter for tracking servers using the specified MLflow version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `[0-9]*.[0-9]*.[0-9]*`
Required: No

 ** [NextToken](#API_ListMlflowTrackingServers_RequestSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-request-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListMlflowTrackingServers_RequestSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-request-SortBy"></a>
Filter for trackings servers sorting by name, creation time, or creation status.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListMlflowTrackingServers_RequestSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-request-SortOrder"></a>
Change the order of the listed tracking servers. By default, tracking servers are listed in `Descending` order by creation time. To change the list order, you can specify `SortOrder` to be `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [TrackingServerStatus](#API_ListMlflowTrackingServers_RequestSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-request-TrackingServerStatus"></a>
Filter for tracking servers with a specified creation status.
Type: String
Valid Values: `Creating | Created | CreateFailed | Updating | Updated | UpdateFailed | Deleting | DeleteFailed | Stopping | Stopped | StopFailed | Starting | Started | StartFailed | MaintenanceInProgress | MaintenanceComplete | MaintenanceFailed`
Required: No

## Response Syntax
<a name="API_ListMlflowTrackingServers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TrackingServerSummaries": [
      {
         "CreationTime": number,
         "IsActive": "string",
         "LastModifiedTime": number,
         "MlflowVersion": "string",
         "TrackingServerArn": "string",
         "TrackingServerName": "string",
         "TrackingServerStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListMlflowTrackingServers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListMlflowTrackingServers_ResponseSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-response-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [TrackingServerSummaries](#API_ListMlflowTrackingServers_ResponseSyntax) **   <a name="sagemaker-ListMlflowTrackingServers-response-TrackingServerSummaries"></a>
A list of tracking servers according to chosen filters.
Type: Array of [TrackingServerSummary](API_TrackingServerSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListMlflowTrackingServers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListMlflowTrackingServers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListMlflowTrackingServers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListMlflowTrackingServers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListMlflowTrackingServers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListMlflowTrackingServers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListMlflowTrackingServers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListMlflowTrackingServers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListMlflowTrackingServers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListMlflowTrackingServers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListMlflowTrackingServers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListMlflowTrackingServers)
