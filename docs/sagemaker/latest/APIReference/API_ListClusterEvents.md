---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterEvents.html
---

# ListClusterEvents
<a name="API_ListClusterEvents"></a>

Retrieves a list of event summaries for a specified HyperPod cluster. The operation supports filtering, sorting, and pagination of results. This functionality is only supported when the `NodeProvisioningMode` is set to `Continuous`.

## Request Syntax
<a name="API_ListClusterEvents_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "InstanceGroupName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "NodeId": "{{string}}",
   "ResourceType": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusterEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_ListClusterEvents_RequestSyntax) **   <a name="sagemaker-ListClusterEvents-request-ClusterName"></a>
The name or Amazon Resource Name (ARN) of the HyperPod cluster for which to list events.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [InstanceGroupName](#API_ListClusterEvents_RequestSyntax) **   <a name="sagemaker-ListClusterEvents-request-InstanceGroupName"></a>
The name of the instance group to filter events. If specified, only events related to this instance group are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [MaxResults](#API_ListClusterEvents_RequestSyntax) **   <a name="sagemaker-ListClusterEvents-request-MaxResults"></a>
The maximum number of events to return in the response. Valid range is 1 to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListClusterEvents_RequestSyntax) **   <a name="sagemaker-ListClusterEvents-request-NextToken"></a>
A token to retrieve the next set of results. This token is obtained from the output of a previous `ListClusterEvents` call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [NodeId](#API_ListClusterEvents_RequestSyntax) **   <a name="sagemaker-ListClusterEvents-request-NodeId"></a>
The EC2 instance ID to filter events. If specified, only events related to this instance are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: No

 ** [ResourceType](#API_ListClusterEvents_RequestSyntax) **   <a name="sagemaker-ListClusterEvents-request-ResourceType"></a>
The type of resource for which to filter events. Valid values are `Cluster`, `InstanceGroup`, or `Instance`.
Type: String
Valid Values: `Cluster | InstanceGroup | Instance`
Required: No

 ** [SortBy](#API_ListClusterEvents_RequestSyntax) **   <a name="sagemaker-ListClusterEvents-request-SortBy"></a>
The field to use for sorting the event list. Currently, the only supported value is `EventTime`.
Type: String
Valid Values: `EventTime`
Required: No

 ** [SortOrder](#API_ListClusterEvents_RequestSyntax) **   <a name="sagemaker-ListClusterEvents-request-SortOrder"></a>
The order in which to sort the results. Valid values are `Ascending` or `Descending` (the default is `Descending`).
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListClusterEvents_ResponseSyntax"></a>

```
{
   "Events": [
      {
         "ClusterArn": "string",
         "ClusterName": "string",
         "Description": "string",
         "EventId": "string",
         "EventLevel": "string",
         "InstanceGroupName": "string",
         "InstanceId": "string",
         "ResourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClusterEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Events](#API_ListClusterEvents_ResponseSyntax) **   <a name="sagemaker-ListClusterEvents-response-Events"></a>
A list of event summaries matching the specified criteria.
Type: Array of [ClusterEventSummary](API_ClusterEventSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_ListClusterEvents_ResponseSyntax) **   <a name="sagemaker-ListClusterEvents-response-NextToken"></a>
A token to retrieve the next set of results. Include this token in subsequent `ListClusterEvents` calls to fetch more events.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListClusterEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListClusterEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListClusterEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListClusterEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListClusterEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListClusterEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListClusterEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListClusterEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListClusterEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListClusterEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListClusterEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListClusterEvents)
