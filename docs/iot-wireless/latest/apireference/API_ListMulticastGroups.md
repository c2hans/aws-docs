---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListMulticastGroups.html
---

# ListMulticastGroups
<a name="API_ListMulticastGroups"></a>

Lists the multicast groups registered to your AWS account.

## Request Syntax
<a name="API_ListMulticastGroups_RequestSyntax"></a>

```
GET /multicast-groups?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMulticastGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListMulticastGroups_RequestSyntax) **   <a name="iotwireless-ListMulticastGroups-request-uri-MaxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 0. Maximum value of 250.

 ** [NextToken](#API_ListMulticastGroups_RequestSyntax) **   <a name="iotwireless-ListMulticastGroups-request-uri-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Length Constraints: Maximum length of 4096.

## Request Body
<a name="API_ListMulticastGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMulticastGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MulticastGroupList": [
      {
         "Arn": "string",
         "Id": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMulticastGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MulticastGroupList](#API_ListMulticastGroups_ResponseSyntax) **   <a name="iotwireless-ListMulticastGroups-response-MulticastGroupList"></a>
List of multicast groups.
Type: Array of [MulticastGroup](API_MulticastGroup.md) objects

 ** [NextToken](#API_ListMulticastGroups_ResponseSyntax) **   <a name="iotwireless-ListMulticastGroups-response-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Type: String
Length Constraints: Maximum length of 4096.

## Errors
<a name="API_ListMulticastGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListMulticastGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/ListMulticastGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/ListMulticastGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ListMulticastGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/ListMulticastGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ListMulticastGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/ListMulticastGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/ListMulticastGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/ListMulticastGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/ListMulticastGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ListMulticastGroups)
