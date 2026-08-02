---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListResourcePolicies.html
---

# ListResourcePolicies
<a name="API_ListResourcePolicies"></a>

Returns a list of policies for a resource.

## Request Syntax
<a name="API_ListResourcePolicies_RequestSyntax"></a>

```
POST /resource-policies/{{ResourceArn}}/?List&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListResourcePolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListResourcePolicies_RequestSyntax) **   <a name="mpa-ListResourcePolicies-request-uri-MaxResults"></a>
The maximum number of items to return in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that you can retrieve the remaining results.
Valid Range: Minimum value of 1. Maximum value of 20.

 ** [NextToken](#API_ListResourcePolicies_RequestSyntax) **   <a name="mpa-ListResourcePolicies-request-uri-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a next call to the operation to get more output. You can repeat this until the `NextToken` response element returns `null`.
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [ResourceArn](#API_ListResourcePolicies_RequestSyntax) **   <a name="mpa-ListResourcePolicies-request-uri-ResourceArn"></a>
Amazon Resource Name (ARN) for the resource.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_ListResourcePolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListResourcePolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ResourcePolicies": [
      {
         "PolicyArn": "string",
         "PolicyName": "string",
         "PolicyType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourcePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourcePolicies_ResponseSyntax) **   <a name="mpa-ListResourcePolicies-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a next call to the operation to get more output. You can repeat this until the `NextToken` response element returns `null`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [ResourcePolicies](#API_ListResourcePolicies_ResponseSyntax) **   <a name="mpa-ListResourcePolicies-response-ResourcePolicies"></a>
An array of `ListResourcePoliciesResponseResourcePolicy` objects. Contains details about the policy for the resource.
Type: Array of [ListResourcePoliciesResponseResourcePolicy](API_ListResourcePoliciesResponseResourcePolicy.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListResourcePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You do not have sufficient access to perform this action. Check your permissions, and try again.
 ** Message **
Message for the `AccessDeniedException` error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error. Try your request again. If the problem persists, contact AWS Support.
 ** Message **
Message for the `InternalServerException` error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The specified resource doesn't exist. Check the resource ID, and try again.
 ** Message **
Message for the `ResourceNotFoundException` error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling.
 ** Message **
Message for the `ThrottlingException` error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
Message for the `ValidationException` error.
HTTP Status Code: 400

## See Also
<a name="API_ListResourcePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/ListResourcePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/ListResourcePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/ListResourcePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/ListResourcePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/ListResourcePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/ListResourcePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/ListResourcePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/ListResourcePolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/ListResourcePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/ListResourcePolicies)
