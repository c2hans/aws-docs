---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListPrincipalsForPolicy.html
---

# ListPrincipalsForPolicy

Lists the Amazon Quick Sight principals that have a governance policy. This operation returns paginated results. A page can contain fewer results than `MaxResults`, or none, and still include a `NextToken`. Continue to call the operation until the response doesn't include a `NextToken`. We recommend that you use pagination to make sure that the operation returns quickly and successfully.

Results are eventually consistent and might not reflect recent changes. If the policy has no assignments, the response contains an empty `Principals` list. If the policy doesn't exist, the request fails with a `ResourceNotFoundException`.

## Request Syntax
<a name="API_ListPrincipalsForPolicy_RequestSyntax"></a>

```
GET /governance-policy-mgmt/accounts/{{AccountId}}/policy-assignments/by-policy?MaxResults={{MaxResults}}&NextToken={{NextToken}}&PolicyArn={{PolicyArn}}&PrincipalType={{PrincipalType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPrincipalsForPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountId](#API_ListPrincipalsForPolicy_RequestSyntax) **   <a name="QS-ListPrincipalsForPolicy-request-uri-AccountId"></a>
The ID of the AWS account that contains the policy.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [MaxResults](#API_ListPrincipalsForPolicy_RequestSyntax) **   <a name="QS-ListPrincipalsForPolicy-request-uri-MaxResults"></a>
The maximum number of results to return in a single call. Valid range is 1–100. If you don't specify a value, the operation returns up to 100 results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListPrincipalsForPolicy_RequestSyntax) **   <a name="QS-ListPrincipalsForPolicy-request-uri-NextToken"></a>
The token returned by a previous call. Use it to get the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [PolicyArn](#API_ListPrincipalsForPolicy_RequestSyntax) **   <a name="QS-ListPrincipalsForPolicy-request-uri-PolicyArn"></a>
The ARN of the policy.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`
Required: Yes

 ** [PrincipalType](#API_ListPrincipalsForPolicy_RequestSyntax) **   <a name="QS-ListPrincipalsForPolicy-request-uri-PrincipalType"></a>
An optional filter that limits the results to principals of the specified type. If you don't specify a value, the operation returns principals of all types. You can specify one of the following values:
+  `USER` – An Amazon Quick Sight user.
+  `GROUP` – An Amazon Quick Sight group.
+  `ACCOUNT` – The Amazon Quick Sight account.
Valid Values: `USER | GROUP | ACCOUNT`

## Request Body
<a name="API_ListPrincipalsForPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPrincipalsForPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Principals": [
      {
         "PrincipalArn": "string",
         "PrincipalType": "string",
         "Revision": number,
         "UpdatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListPrincipalsForPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Principals](#API_ListPrincipalsForPolicy_ResponseSyntax) **   <a name="QS-ListPrincipalsForPolicy-response-Principals"></a>
A list of principals that the policy is assigned to.
Type: Array of [PolicyPrincipal](API_PolicyPrincipal.md) objects

 ** [NextToken](#API_ListPrincipalsForPolicy_ResponseSyntax) **   <a name="QS-ListPrincipalsForPolicy-response-NextToken"></a>
The token for the next page of results. This value is absent if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListPrincipalsForPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** FieldList **
A list of the request fields that failed validation.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

## See Also
<a name="API_ListPrincipalsForPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListPrincipalsForPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListPrincipalsForPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListPrincipalsForPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListPrincipalsForPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListPrincipalsForPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListPrincipalsForPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListPrincipalsForPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListPrincipalsForPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListPrincipalsForPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListPrincipalsForPolicy)
