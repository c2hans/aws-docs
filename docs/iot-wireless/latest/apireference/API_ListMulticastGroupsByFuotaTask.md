---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListMulticastGroupsByFuotaTask.html
---

# ListMulticastGroupsByFuotaTask
<a name="API_ListMulticastGroupsByFuotaTask"></a>

List all multicast groups associated with a FUOTA task.

## Request Syntax
<a name="API_ListMulticastGroupsByFuotaTask_RequestSyntax"></a>

```
GET /fuota-tasks/{{Id}}/multicast-groups?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMulticastGroupsByFuotaTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListMulticastGroupsByFuotaTask_RequestSyntax) **   <a name="iotwireless-ListMulticastGroupsByFuotaTask-request-uri-Id"></a>
The ID of a FUOTA task.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [MaxResults](#API_ListMulticastGroupsByFuotaTask_RequestSyntax) **   <a name="iotwireless-ListMulticastGroupsByFuotaTask-request-uri-MaxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 0. Maximum value of 250.

 ** [NextToken](#API_ListMulticastGroupsByFuotaTask_RequestSyntax) **   <a name="iotwireless-ListMulticastGroupsByFuotaTask-request-uri-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Length Constraints: Maximum length of 4096.

## Request Body
<a name="API_ListMulticastGroupsByFuotaTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMulticastGroupsByFuotaTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MulticastGroupList": [
      {
         "Id": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMulticastGroupsByFuotaTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MulticastGroupList](#API_ListMulticastGroupsByFuotaTask_ResponseSyntax) **   <a name="iotwireless-ListMulticastGroupsByFuotaTask-response-MulticastGroupList"></a>
List of multicast groups associated with a FUOTA task.
Type: Array of [MulticastGroupByFuotaTask](API_MulticastGroupByFuotaTask.md) objects

 ** [NextToken](#API_ListMulticastGroupsByFuotaTask_ResponseSyntax) **   <a name="iotwireless-ListMulticastGroupsByFuotaTask-response-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Type: String
Length Constraints: Maximum length of 4096.

## Errors
<a name="API_ListMulticastGroupsByFuotaTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListMulticastGroupsByFuotaTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ListMulticastGroupsByFuotaTask)
