---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetMpaTeamAssociation.html
---

# GetMpaTeamAssociation
<a name="API_GetMpaTeamAssociation"></a>

Returns the Multi-Party Approval (MPA) team association for a protected operation.

 **Cross-account use:** This operation can't be used across different AWS accounts.

 **Related operations:**
+  [AssociateMpaTeam](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AssociateMpaTeam.html)
+  [DisassociateMpaTeam](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisassociateMpaTeam.html)

## Request Syntax
<a name="API_GetMpaTeamAssociation_RequestSyntax"></a>

```
{
   "Action": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMpaTeamAssociation_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Action](#API_GetMpaTeamAssociation_RequestSyntax) **   <a name="paymentcryptography-GetMpaTeamAssociation-request-Action"></a>
The protected operation whose MPA team association you want to retrieve. Currently, the only supported value is `IMPORT_ROOT_PUBLIC_KEY_CERTIFICATE`.
Type: String
Valid Values: `IMPORT_ROOT_PUBLIC_KEY_CERTIFICATE`
Required: Yes

## Response Syntax
<a name="API_GetMpaTeamAssociation_ResponseSyntax"></a>

```
{
   "MpaTeamAssociation": {
      "Action": "string",
      "AssociationState": "string",
      "MpaStatus": {
         "InitiationDate": number,
         "MpaSessionArn": "string",
         "Status": "string",
         "StatusMessage": "string"
      },
      "MpaTeamArn": "string"
   }
}
```

## Response Elements
<a name="API_GetMpaTeamAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MpaTeamAssociation](#API_GetMpaTeamAssociation_ResponseSyntax) **   <a name="paymentcryptography-GetMpaTeamAssociation-response-MpaTeamAssociation"></a>
The details of the MPA team association.
Type: [MpaTeamAssociation](API_MpaTeamAssociation.md) object

## Errors
<a name="API_GetMpaTeamAssociation_Errors"></a>

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific AWS Payment Cryptography action you're attempting.
HTTP Status Code: 400

 ** ConflictException **
This request can cause an inconsistent state for the resource.
The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
This indicates a server-side error within the AWS Payment Cryptography service. If this error persists, contact support for assistance.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was denied due to resource not found.
The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.
 ** ResourceId **
The identifier of the resource that was not found.
This field contains the specific resource identifier (such as a key ARN or alias name) that could not be located.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
This request would cause a service quota to be exceeded.
You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
The AWS Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
You have exceeded the rate limits for AWS Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.
HTTP Status Code: 400

 ** ValidationException **
The request was denied due to an invalid request error.
One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.
HTTP Status Code: 400

## See Also
<a name="API_GetMpaTeamAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/GetMpaTeamAssociation)
