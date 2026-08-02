---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListDeployments.html
---

# ListDeployments
<a name="API_ListDeployments"></a>

Lists the deployments that have been created.

## Request Syntax
<a name="API_ListDeployments_RequestSyntax"></a>

```
POST /listDeployments HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListDeployments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDeployments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListDeployments_RequestSyntax) **   <a name="launchwizard-ListDeployments-request-filters"></a>
Filters to scope the results. The following filters are supported:
+  `WORKLOAD_NAME` - The name used in deployments.
+  `DEPLOYMENT_STATUS` - `COMPLETED` \| `CREATING` \| `DELETE_IN_PROGRESS` \| `DELETE_INITIATING` \| `DELETE_FAILED` \| `DELETED` \| `FAILED` \| `IN_PROGRESS` \| `VALIDATING`
Type: Array of [DeploymentFilter](API_DeploymentFilter.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [maxResults](#API_ListDeployments_RequestSyntax) **   <a name="launchwizard-ListDeployments-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListDeployments_RequestSyntax) **   <a name="launchwizard-ListDeployments-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListDeployments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deployments": [
      {
         "createdAt": number,
         "id": "string",
         "modifiedAt": number,
         "name": "string",
         "patternName": "string",
         "status": "string",
         "workloadName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deployments](#API_ListDeployments_ResponseSyntax) **   <a name="launchwizard-ListDeployments-response-deployments"></a>
Lists the deployments.
Type: Array of [DeploymentDataSummary](API_DeploymentDataSummary.md) objects

 ** [nextToken](#API_ListDeployments_ResponseSyntax) **   <a name="launchwizard-ListDeployments-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListDeployments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on [re:Post](https://repost.aws/).
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/launch-wizard-2018-05-10/ListDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/launch-wizard-2018-05-10/ListDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/ListDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/launch-wizard-2018-05-10/ListDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/ListDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/launch-wizard-2018-05-10/ListDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/launch-wizard-2018-05-10/ListDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/launch-wizard-2018-05-10/ListDeployments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/launch-wizard-2018-05-10/ListDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/ListDeployments)
