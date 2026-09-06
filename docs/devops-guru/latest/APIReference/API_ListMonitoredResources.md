---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListMonitoredResources.html
---

# ListMonitoredResources
<a name="API_ListMonitoredResources"></a>

 Returns the list of resources that are being monitored by DevOps Guru.

## Request Syntax
<a name="API_ListMonitoredResources_RequestSyntax"></a>

```
POST /monitoredResources HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "ResourcePermission": "{{string}}",
      "ResourceTypeFilters": [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListMonitoredResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListMonitoredResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListMonitoredResources_RequestSyntax) **   <a name="DevOpsGuru-ListMonitoredResources-request-Filters"></a>
 Filters to determine which monitored resources you want to retrieve. You can filter by resource type or resource permission status.
Type: [ListMonitoredResourcesFilters](API_ListMonitoredResourcesFilters.md) object
Required: No

 ** [MaxResults](#API_ListMonitoredResources_RequestSyntax) **   <a name="DevOpsGuru-ListMonitoredResources-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListMonitoredResources_RequestSyntax) **   <a name="DevOpsGuru-ListMonitoredResources-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

## Response Syntax
<a name="API_ListMonitoredResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MonitoredResourceIdentifiers": [
      {
         "LastUpdated": number,
         "MonitoredResourceName": "string",
         "ResourceCollection": {
            "CloudFormation": {
               "StackNames": [ "string" ]
            },
            "Tags": [
               {
                  "AppBoundaryKey": "string",
                  "TagValues": [ "string" ]
               }
            ]
         },
         "ResourcePermission": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMonitoredResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonitoredResourceIdentifiers](#API_ListMonitoredResources_ResponseSyntax) **   <a name="DevOpsGuru-ListMonitoredResources-response-MonitoredResourceIdentifiers"></a>
 Information about the resource that is being monitored, including the name of the resource, the type of resource, and whether or not permission is given to DevOps Guru to access that resource.
Type: Array of [MonitoredResourceIdentifier](API_MonitoredResourceIdentifier.md) objects

 ** [NextToken](#API_ListMonitoredResources_ResponseSyntax) **   <a name="DevOpsGuru-ListMonitoredResources-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

## Errors
<a name="API_ListMonitoredResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource could not be found
 ** ResourceId **
 The ID of the AWS resource that could not be found.
 ** ResourceType **
 The type of the AWS resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_ListMonitoredResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/ListMonitoredResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/ListMonitoredResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ListMonitoredResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/ListMonitoredResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ListMonitoredResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/ListMonitoredResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/ListMonitoredResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/ListMonitoredResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/ListMonitoredResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ListMonitoredResources)
