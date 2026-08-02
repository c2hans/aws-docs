---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AssociateAccounts.html
---

# AssociateAccounts
<a name="API_AssociateAccounts"></a>

Connects an array of account IDs in a consolidated billing family to a predefined billing group. The account IDs must be a part of the consolidated billing family during the current month, and not already associated with another billing group. The maximum number of accounts that can be associated in one call is 30.

## Request Syntax
<a name="API_AssociateAccounts_RequestSyntax"></a>

```
POST /associate-accounts HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "Arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateAccounts_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateAccounts_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_AssociateAccounts_RequestSyntax) **   <a name="billingconductor-AssociateAccounts-request-AccountIds"></a>
 The associating array of account IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Pattern: `[0-9]{12}`
Required: Yes

 ** [Arn](#API_AssociateAccounts_RequestSyntax) **   <a name="billingconductor-AssociateAccounts-request-Arn"></a>
 The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: Yes

## Response Syntax
<a name="API_AssociateAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_AssociateAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_AssociateAccounts_ResponseSyntax) **   <a name="billingconductor-AssociateAccounts-response-Arn"></a>
 The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`

## Errors
<a name="API_AssociateAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can cause an inconsistent state by updating or deleting a resource.
 ** Reason **
Reason for the inconsistent state.
 ** ResourceId **
Identifier of the resource in use.
 ** ResourceType **
Type of the resource in use.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing a request.
 ** RetryAfterSeconds **
Number of seconds you can retry after the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
 ** ResourceId **
Resource identifier that was not found.
 ** ResourceType **
Resource type that was not found.
HTTP Status Code: 404

 ** ServiceLimitExceededException **
The request would cause a service limit to exceed.
 ** LimitCode **
The unique code identifier of the service limit that is being exceeded.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
The unique code for the service of the limit that is being exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Number of seconds you can safely retry after the call.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't match with the constraints specified by AWS services.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason the request's validation failed.
HTTP Status Code: 400

## See Also
<a name="API_AssociateAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/AssociateAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/AssociateAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/AssociateAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/AssociateAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/AssociateAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/AssociateAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/AssociateAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/AssociateAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/AssociateAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/AssociateAccounts)
