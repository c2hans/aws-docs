---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementEntitlements.html
---

# GetAgreementEntitlements
<a name="API_marketplace-agreements_GetAgreementEntitlements"></a>

Obtains details about the entitlements of an agreement.

## Request Syntax
<a name="API_marketplace-agreements_GetAgreementEntitlements_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_GetAgreementEntitlements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_GetAgreementEntitlements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementEntitlements-request-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [maxResults](#API_marketplace-agreements_GetAgreementEntitlements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementEntitlements-request-maxResults"></a>
The maximum number of agreement entitlements to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_GetAgreementEntitlements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementEntitlements-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_GetAgreementEntitlements_ResponseSyntax"></a>

```
{
   "agreementEntitlements": [
      {
         "licenseArn": "string",
         "registrationToken": "string",
         "resource": {
            "id": "string",
            "type": "string"
         },
         "status": "string",
         "statusReasonCode": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_GetAgreementEntitlements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementEntitlements](#API_marketplace-agreements_GetAgreementEntitlements_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementEntitlements-response-agreementEntitlements"></a>
A list of agreement entitlements which are part of the latest agreement.
Type: Array of [AgreementEntitlement](API_marketplace-agreements_AgreementEntitlement.md) objects

 ** [nextToken](#API_marketplace-agreements_GetAgreementEntitlements_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementEntitlements-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_GetAgreementEntitlements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** message **
Description of the error.
 ** reason **
The reason for the access denied exception.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error during processing of request.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
 ** resourceId **
The unique identifier for the resource.
 ** resourceType **
The type of resource.
HTTP Status Code: 400

 ** ThrottlingException **
Request was denied due to request throttling.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fields **
The fields associated with the error.
 ** message **
Description of the error.
 ** reason **
The reason associated with the error.
 ** requestId **
The unique identifier associated with the error.
HTTP Status Code: 400

## Examples
<a name="API_marketplace-agreements_GetAgreementEntitlements_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_GetAgreementEntitlements_Example_1"></a>

This example illustrates one usage of GetAgreementEntitlements.

```
{
    "agreementId": "agmt-EXAMPLE0aa6-4e42-8715-6a1EXAMPLE95"
}
```

### Sample response
<a name="API_marketplace-agreements_GetAgreementEntitlements_Example_2"></a>

This example illustrates one usage of GetAgreementEntitlements.

```
{
    "agreementEntitlements": [
        {
            "resource": {
                "id": "prod-EXAMPLE",
                "type": "SaaSProduct"
            },
            "status": "PROVISIONED",
            "statusReasonCode": "AGREEMENT_ACTIVE",
            "type": "AWS::Marketplace::Usage",
            "registrationToken": "EXAMPLE-registration-token",
            "licenseArn": "arn:aws:license-manager::123456789012:license/lic-EXAMPLE01234abcd"
        },
        {
            "resource": {
                "id": "prod-EXAMPLE",
                "type": "SaaSProduct"
            },
            "status": "PENDING",
            "statusReasonCode": "PROVISIONING_IN_PROGRESS",
            "type": "AWS::Marketplace::Discount",
            "registrationToken": null,
            "licenseArn": null
        }
    ],
    "nextToken": null
}
```

## See Also
<a name="API_marketplace-agreements_GetAgreementEntitlements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/GetAgreementEntitlements)
