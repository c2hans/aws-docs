---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementRequestTerms.html
---

# GetAgreementRequestTerms

Retrieves the terms proposed for an agreement request, such as pricing, legal, and renewal terms. The acceptor, or the management account or a delegated administrator of the acceptor's AWS organization, can call this operation. This operation is similar to `GetAgreementTerms`, but it takes an `agreementRequestId` instead of an `agreementId`.

## Request Syntax
<a name="API_marketplace-agreements_GetAgreementRequestTerms_RequestSyntax"></a>

```
{
   "agreementRequestId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_GetAgreementRequestTerms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementRequestId](#API_marketplace-agreements_GetAgreementRequestTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestTerms-request-agreementRequestId"></a>
The unique identifier of the agreement request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`
Required: Yes

 ** [maxResults](#API_marketplace-agreements_GetAgreementRequestTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestTerms-request-maxResults"></a>
The maximum number of terms to return in the response.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_GetAgreementRequestTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestTerms-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_GetAgreementRequestTerms_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "terms": [
      { ... }
   ]
}
```

## Response Elements
<a name="API_marketplace-agreements_GetAgreementRequestTerms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [terms](#API_marketplace-agreements_GetAgreementRequestTerms_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestTerms-response-terms"></a>
The terms proposed for the agreement request. The terms are fixed when the agreement request is created.
Type: Array of [AgreementRequestTerm](API_marketplace-agreements_AgreementRequestTerm.md) objects

 ** [nextToken](#API_marketplace-agreements_GetAgreementRequestTerms_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestTerms-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_GetAgreementRequestTerms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** message **
Description of the error.
 ** reason **
The reason for the access denied exception.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 403

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
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 429

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
<a name="API_marketplace-agreements_GetAgreementRequestTerms_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_GetAgreementRequestTerms_Example_1"></a>

This example illustrates one usage of GetAgreementRequestTerms.

```
{
    "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78"
}
```

### Sample response
<a name="API_marketplace-agreements_GetAgreementRequestTerms_Example_2"></a>

This example illustrates one usage of GetAgreementRequestTerms.

```
{
    "terms": [
        {
            "legalTerm": {
                "type": "LegalTerm",
                "id": "term-EXAMPLE3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f",
                "documents": [
                    {
                        "type": "CustomEula",
                        "url": "URL"
                    }
                ]
            }
        },
        {
            "configurableUpfrontPricingTerm": {
                "type": "ConfigurableUpfrontPricingTerm",
                "id": "term-EXAMPLE1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d",
                "currencyCode": "USD",
                "rateCards": [
                    {
                        "selector": {
                            "type": "Duration",
                            "value": "P12M"
                        },
                        "constraints": {
                            "multipleDimensionSelection": "Allowed",
                            "quantityConfiguration": "Allowed"
                        },
                        "rateCard": [
                            {
                                "dimensionKey": "AdminUsers",
                                "price": "10"
                            },
                            {
                                "dimensionKey": "ReadOnlyUsers",
                                "price": "5"
                            }
                        ]
                    }
                ],
                "configuration": {
                    "selectorValue": "P12M",
                    "dimensions": [
                        {
                            "dimensionKey": "AdminUsers",
                            "dimensionValue": 5
                        },
                        {
                            "dimensionKey": "ReadOnlyUsers",
                            "dimensionValue": 10
                        }
                    ]
                }
            }
        },
        {
            "renewalTerm": {
                "type": "RenewalTerm",
                "id": "term-EXAMPLE2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e",
                "configuration": {
                    "enableAutoRenew": false
                }
            }
        }
    ],
    "nextToken": null
}
```

## See Also
<a name="API_marketplace-agreements_GetAgreementRequestTerms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/GetAgreementRequestTerms)
