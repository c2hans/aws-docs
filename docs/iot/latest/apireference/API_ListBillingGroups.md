---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListBillingGroups.html
---

# ListBillingGroups
<a name="API_ListBillingGroups"></a>

Lists the billing groups you have created.

Requires permission to access the [ListBillingGroups](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListBillingGroups_RequestSyntax"></a>

```
GET /billing-groups?maxResults={{maxResults}}&namePrefixFilter={{namePrefixFilter}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBillingGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListBillingGroups_RequestSyntax) **   <a name="iot-ListBillingGroups-request-uri-maxResults"></a>
The maximum number of results to return per request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [namePrefixFilter](#API_ListBillingGroups_RequestSyntax) **   <a name="iot-ListBillingGroups-request-uri-namePrefixFilter"></a>
Limit the results to billing groups whose names have the given prefix.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [nextToken](#API_ListBillingGroups_RequestSyntax) **   <a name="iot-ListBillingGroups-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

## Request Body
<a name="API_ListBillingGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBillingGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "billingGroups": [
      {
         "groupArn": "string",
         "groupName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBillingGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billingGroups](#API_ListBillingGroups_ResponseSyntax) **   <a name="iot-ListBillingGroups-response-billingGroups"></a>
The list of billing groups.
Type: Array of [GroupNameAndArn](API_GroupNameAndArn.md) objects

 ** [nextToken](#API_ListBillingGroups_ResponseSyntax) **   <a name="iot-ListBillingGroups-response-nextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String

## Errors
<a name="API_ListBillingGroups_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListBillingGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListBillingGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListBillingGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListBillingGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListBillingGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListBillingGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListBillingGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListBillingGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListBillingGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListBillingGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListBillingGroups)
