---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListManagedResources.html
---

# ListManagedResources
<a name="API_ListManagedResources"></a>

Lists all the resources in your AWS account in this AWS Region that are managed for zonal shifts in Amazon Application Recovery Controller, and information about them. The information includes the zonal autoshift status for the resource, as well as the Amazon Resource Name (ARN), the Availability Zones that each resource is deployed in, and the resource name.

## Request Syntax
<a name="API_ListManagedResources_RequestSyntax"></a>

```
GET /managedresources?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedResources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListManagedResources_RequestSyntax) **   <a name="zonalshift-ListManagedResources-request-uri-maxResults"></a>
The number of objects that you want to return with this call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListManagedResources_RequestSyntax) **   <a name="zonalshift-ListManagedResources-request-uri-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.

## Request Body
<a name="API_ListManagedResources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "appliedWeights": {
            "string" : number
         },
         "arn": "string",
         "autoshifts": [
            {
               "appliedStatus": "string",
               "awayFrom": "string",
               "startTime": number
            }
         ],
         "availabilityZones": [ "string" ],
         "name": "string",
         "practiceRunStatus": "string",
         "zonalAutoshiftStatus": "string",
         "zonalShifts": [
            {
               "appliedStatus": "string",
               "awayFrom": "string",
               "comment": "string",
               "expiryTime": number,
               "practiceRunOutcome": "string",
               "resourceIdentifier": "string",
               "shiftType": "string",
               "startTime": number,
               "zonalShiftId": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListManagedResources_ResponseSyntax) **   <a name="zonalshift-ListManagedResources-response-items"></a>
The items in the response list.
Type: Array of [ManagedResourceSummary](API_ManagedResourceSummary.md) objects

 ** [nextToken](#API_ListManagedResources_ResponseSyntax) **   <a name="zonalshift-ListManagedResources-response-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String

## Errors
<a name="API_ListManagedResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
There was an internal server error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_ListManagedResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/ListManagedResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/ListManagedResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/ListManagedResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/ListManagedResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/ListManagedResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/ListManagedResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/ListManagedResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/ListManagedResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/ListManagedResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/ListManagedResources)
