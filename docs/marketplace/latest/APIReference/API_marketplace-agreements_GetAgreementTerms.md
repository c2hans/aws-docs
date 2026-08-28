---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementTerms.html
---

# GetAgreementTerms
<a name="API_marketplace-agreements_GetAgreementTerms"></a>

Obtains details about the terms in an agreement that you participated in as proposer or acceptor.

The details include:
+  `TermType` – The type of term, such as `LegalTerm`, `RenewalTerm`, or `ConfigurableUpfrontPricingTerm`.
+  `TermID` – The ID of the particular term, which is common between offer and agreement.
+  `TermPayload` – The key information contained in the term, such as the EULA for `LegalTerm` or pricing and dimensions for various pricing terms, such as `ConfigurableUpfrontPricingTerm` or `UsageBasedPricingTerm`.
+  `Configuration` – The buyer/acceptor's selection at the time of agreement creation, such as the number of units purchased for a dimension or setting the `EnableAutoRenew` flag.

## Request Syntax
<a name="API_marketplace-agreements_GetAgreementTerms_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_GetAgreementTerms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_GetAgreementTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementTerms-request-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [maxResults](#API_marketplace-agreements_GetAgreementTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementTerms-request-maxResults"></a>
The maximum number of agreements to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_GetAgreementTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementTerms-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_GetAgreementTerms_ResponseSyntax"></a>

```
{
   "acceptedTerms": [
      { ... }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_GetAgreementTerms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [acceptedTerms](#API_marketplace-agreements_GetAgreementTerms_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementTerms-response-acceptedTerms"></a>
A subset of terms proposed by the proposer that have been accepted by the acceptor as part of the agreement creation.
Type: Array of [AcceptedTerm](API_marketplace-agreements_AcceptedTerm.md) objects

 ** [nextToken](#API_marketplace-agreements_GetAgreementTerms_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementTerms-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_GetAgreementTerms_Errors"></a>

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
<a name="API_marketplace-agreements_GetAgreementTerms_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_GetAgreementTerms_Example_1"></a>

This example illustrates one usage of GetAgreementTerms.

```
{
   "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95"
}
```

### Sample response
<a name="API_marketplace-agreements_GetAgreementTerms_Example_2"></a>

This example illustrates one usage of GetAgreementTerms.

```
{
    "AcceptedTerms": [{
            "ConfigurableUpfrontPricingTerm": {
                "Type": "ConfigurableUpfrontPricingTerm",
                "CurrencyCode": "USD",
                "RateCards": [{
                        "Selector": {
                            "Type": "Duration",
                            "Value": "P24M"
                        },
                        "Constraints": {
                            "MultipleDimensionSelection": "Allowed",
                            "QuantityConfiguration": "Allowed"
                        },
                        "RateCard": [{
                                "DimensionKey": "AdminUsers",
                                "Price": "0.5"
                            },
                            {
                                "DimensionKey": "ReadOnlyUsers",
                                "Price": "1"
                            }
                        ]
                    },
                    {
                        "Selector": {
                            "Type": "Duration",
                            "Value": "P36M"
                        },
                        "Constraints": {
                            "MultipleDimensionSelection": "Allowed",
                            "QuantityConfiguration": "Allowed"
                        },
                        "RateCard": [{
                                "DimensionKey": "AdminUsers",
                                "Price": "1"
                            },
                            {
                                "DimensionKey": "ReadOnlyUsers",
                                "Price": "2"
                            }
                        ]
                    }
                ],
                "Configuration": {
                    "Dimensions": [{
                        "DimensionKey": "AdminUsers",
                        "DimensionValue": 1
                    }],
                    "SelectorValue": "P24M"
                }
            }
        },
        {
            "RenewalTerm": {
                "Type": "RenewalTerm",
                "Configuration": {
                    "EnableAutoRenew": false
                }
            }
        },
        {
            "VariablePaymentTerm": {
                "Type": "VariablePaymentTerm",
                "CurrencyCode": "USD",
                "MaxTotalChargeAmount": "50",
                "Configuration": {
                    "ExpirationDuration": "P10D",
                    "PaymentRequestApprovalStrategy": "AUTO_APPROVE_ON_EXPIRATION"
                }
            }
        },
        {
            "legalTerm": {
                "type": "LegalTerm",
                "documents": [{
                    "type": "CustomEula",
                    "url": "URL"
                }]
            }
        },
        {
            "netPaymentTerm": {
                "type": "NetPaymentTerm",
                "id": "term-EXAMPLE1234abcd",
                "paymentDuePeriod": "P60D"
            }
        }

    ],
    "nextToken": null
}
```

## See Also
<a name="API_marketplace-agreements_GetAgreementTerms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/GetAgreementTerms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/GetAgreementTerms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/GetAgreementTerms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/GetAgreementTerms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementTerms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/GetAgreementTerms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/GetAgreementTerms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/GetAgreementTerms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementTerms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/GetAgreementTerms)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
