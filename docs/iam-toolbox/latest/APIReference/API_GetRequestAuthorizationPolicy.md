---
source_url: https://docs.aws.amazon.com/iam-toolbox/latest/APIReference/API_GetRequestAuthorizationPolicy.html
---

# GetRequestAuthorizationPolicy

Retrieves a policy that was evaluated for a specific access denied request. The operation returns the structured JSON document of the policy that was captured with the original authorization request. It doesn't retrieve the current version of the policy.

For some AWS services and policy types, the returned policy document includes all actions relevant to the service that processed the denied request, but might omit actions for other services.

Specify the authorization ID from the access denied error message and the policy URI returned by `GetRequestAuthorizationDetails` for the same authorization ID.

Access depends on the account and organization recorded for the principal that made the denied request. If an organization was recorded, the calling principal must belong to that organization. Otherwise, the calling principal must belong to the recorded account.

To use this operation, you must have the `iam:GetRequestAuthorizationPolicy` permission.

## Request Syntax
<a name="API_GetRequestAuthorizationPolicy_RequestSyntax"></a>

```
GET /authorization-details/{{authorizationId}}/policy?policyUri={{policyUri}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRequestAuthorizationPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [authorizationId](#API_GetRequestAuthorizationPolicy_RequestSyntax) **   <a name="iamtoolbox-GetRequestAuthorizationPolicy-request-uri-authorizationId"></a>
The authorization ID received in the access denied error message. This ID identifies the request whose evaluated policy you want to retrieve.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[0123456789abcdefghijklmnopqrstuvwxyz]+`
Required: Yes

 ** [policyUri](#API_GetRequestAuthorizationPolicy_RequestSyntax) **   <a name="iamtoolbox-GetRequestAuthorizationPolicy-request-uri-policyUri"></a>
The URI of the policy to retrieve. Use the `uri` value from the `policies` list returned by `GetRequestAuthorizationDetails` for the same authorization ID.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_GetRequestAuthorizationPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRequestAuthorizationPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policyDocument": JSON value
}
```

## Response Elements
<a name="API_GetRequestAuthorizationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyDocument](#API_GetRequestAuthorizationPolicy_ResponseSyntax) **   <a name="iamtoolbox-GetRequestAuthorizationPolicy-response-policyDocument"></a>
The policy document evaluated for the denied request, returned as a JSON object.
For some AWS services and policy types, this document includes all actions relevant to the service that processed the denied request, but might omit actions for other services.
Type: JSON value

## Errors
<a name="API_GetRequestAuthorizationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request. Try again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested policy or authorization details do not exist in this region or have expired. Verify that the authorization ID from the access denied error message is correct and the call is made in the region where the denial occurred. Ensure that the calling principal belongs to the same account or organization as the original denied request. If you specified a policy URI, verify that it is from the `policies` list that `GetRequestAuthorizationDetails` returns for the same authorization ID.
HTTP Status Code: 404

 ** ValidationException **
The request is malformed or is missing one or more required parameters. Check the request parameters and try again.
HTTP Status Code: 400

## Examples
<a name="API_GetRequestAuthorizationPolicy_Examples"></a>

### Example – Retrieve the policy for an explicitly denied iam:GetUser request
<a name="API_GetRequestAuthorizationPolicy_Example_1"></a>

This example illustrates one usage of GetRequestAuthorizationPolicy.

#### Sample Request
<a name="API_GetRequestAuthorizationPolicy_Example_1_Request"></a>

```
{
  "authorizationId": "z9y8x7w6v5u4t3s2r1q0",
  "policyUri": "arn:aws:iam::aws:policy/AWSDenyAll"
}
```

#### Sample Response
<a name="API_GetRequestAuthorizationPolicy_Example_1_Response"></a>

```
{
  "policyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "DenyAll",
        "Effect": "Deny",
        "Action": "*",
        "Resource": "*"
      }
    ]
  }
}
```

## See Also
<a name="API_GetRequestAuthorizationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-toolbox-2018-05-10/GetRequestAuthorizationPolicy)
