---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterOperations.html
---

# ListClusterOperations
<a name="API_ListClusterOperations"></a>

Retrieves a list of operation summaries for a specified HyperPod cluster, such as scaling operations and deep health checks. The operation supports filtering, sorting, and pagination of results.

## Request Syntax
<a name="API_ListClusterOperations_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "Status": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusterOperations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_ListClusterOperations_RequestSyntax) **   <a name="sagemaker-ListClusterOperations-request-ClusterName"></a>
The name or Amazon Resource Name (ARN) of the HyperPod cluster for which to list operations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `((arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}))`
Required: Yes

 ** [CreationTimeAfter](#API_ListClusterOperations_RequestSyntax) **   <a name="sagemaker-ListClusterOperations-request-CreationTimeAfter"></a>
The start of the time range for filtering operations. Only operations created after this time are included in the results.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListClusterOperations_RequestSyntax) **   <a name="sagemaker-ListClusterOperations-request-CreationTimeBefore"></a>
The end of the time range for filtering operations. Only operations created before this time are included in the results.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListClusterOperations_RequestSyntax) **   <a name="sagemaker-ListClusterOperations-request-MaxResults"></a>
The maximum number of operations to return in the response. Valid range is 1 to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListClusterOperations_RequestSyntax) **   <a name="sagemaker-ListClusterOperations-request-NextToken"></a>
A token to retrieve the next set of results. This token is obtained from the output of a previous `ListClusterOperations` call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListClusterOperations_RequestSyntax) **   <a name="sagemaker-ListClusterOperations-request-SortBy"></a>
The field to use for sorting the operation list. Currently, the only supported value is `CreationTime`.
Type: String
Valid Values: `CreationTime`
Required: No

 ** [SortOrder](#API_ListClusterOperations_RequestSyntax) **   <a name="sagemaker-ListClusterOperations-request-SortOrder"></a>
The order in which to sort the results. Valid values are `Ascending` or `Descending` (the default is `Descending`).
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [Status](#API_ListClusterOperations_RequestSyntax) **   <a name="sagemaker-ListClusterOperations-request-Status"></a>
The operation status to filter by. If specified, only operations with this status are returned. Valid values are `InProgress`, `Superseded`, or `Done`.
Type: String
Valid Values: `InProgress | Superseded | Done`
Required: No

 ** [Type](#API_ListClusterOperations_RequestSyntax) **   <a name="sagemaker-ListClusterOperations-request-Type"></a>
The operation type to filter by. If specified, only operations of this type are returned. Valid values are `Scaling` or `DeepHealthCheck`.
Type: String
Valid Values: `Scaling | DeepHealthCheck`
Required: No

## Response Syntax
<a name="API_ListClusterOperations_ResponseSyntax"></a>

```
{
   "ClusterOperationSummaries": [
      {
         "ClusterArn": "string",
         "CreationTime": number,
         "OperationId": "string",
         "Status": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClusterOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterOperationSummaries](#API_ListClusterOperations_ResponseSyntax) **   <a name="sagemaker-ListClusterOperations-response-ClusterOperationSummaries"></a>
A list of operation summaries matching the specified criteria.
Type: Array of [ClusterOperationSummary](API_ClusterOperationSummary.md) objects

 ** [NextToken](#API_ListClusterOperations_ResponseSyntax) **   <a name="sagemaker-ListClusterOperations-response-NextToken"></a>
A token to retrieve the next set of results. Include this token in subsequent `ListClusterOperations` calls to fetch more operations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListClusterOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListClusterOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListClusterOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListClusterOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListClusterOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListClusterOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListClusterOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListClusterOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListClusterOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListClusterOperations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListClusterOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListClusterOperations)
