---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementRequestApprovalPlans.html
---

# GetAgreementRequestApprovalPlans

Retrieves the approval plans that apply to an agreement request. Only the acceptor of the agreement request can call this operation. Each approval plan lists its approval levels and the approvers at each level. Pass the `planReference` of an approval plan to `StartAgreementApprovals` to start an agreement approval for it.

## Request Syntax
<a name="API_marketplace-agreements_GetAgreementRequestApprovalPlans_RequestSyntax"></a>

```
{
   "agreementRequestId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_GetAgreementRequestApprovalPlans_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementRequestId](#API_marketplace-agreements_GetAgreementRequestApprovalPlans_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestApprovalPlans-request-agreementRequestId"></a>
The unique identifier of the agreement request to retrieve the approval plans for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`
Required: Yes

 ** [maxResults](#API_marketplace-agreements_GetAgreementRequestApprovalPlans_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestApprovalPlans-request-maxResults"></a>
The maximum number of approval plans to return in a single response (1-50). Default is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_GetAgreementRequestApprovalPlans_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestApprovalPlans-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_GetAgreementRequestApprovalPlans_ResponseSyntax"></a>

```
{
   "items": [
      { ... }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_GetAgreementRequestApprovalPlans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_marketplace-agreements_GetAgreementRequestApprovalPlans_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestApprovalPlans-response-items"></a>
An array of `AgreementApprovalPlan` objects, one for each approval plan that applies to the agreement request.
Type: Array of [AgreementApprovalPlan](API_marketplace-agreements_AgreementApprovalPlan.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [nextToken](#API_marketplace-agreements_GetAgreementRequestApprovalPlans_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequestApprovalPlans-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_GetAgreementRequestApprovalPlans_Errors"></a>

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
<a name="API_marketplace-agreements_GetAgreementRequestApprovalPlans_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_GetAgreementRequestApprovalPlans_Example_1"></a>

This example illustrates one usage of GetAgreementRequestApprovalPlans.

```
{
    "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78"
}
```

### Sample response
<a name="API_marketplace-agreements_GetAgreementRequestApprovalPlans_Example_2"></a>

This example illustrates one usage of GetAgreementRequestApprovalPlans.

```
{
    "items": [
        {
            "buyerAgreementApprovalPlan": {
                "planReference": "aplan-EXAMPLE7g8h9i0j1k2l",
                "name": "Software purchases over 10000 USD",
                "levels": [
                    {
                        "name": "Budget owner review",
                        "groups": [
                            {
                                "approvalCriteria": {
                                    "requiredApprovalCount": 1
                                },
                                "approvers": [
                                    {
                                        "emailApprover": {
"emailAddress": "richard_roe@example.com",
                                            "name": "Richard Roe"
                                        }
                                    },
                                    {
                                        "awsOrganizationAdminApprover": {
                                            "organizationId": "o-exampleab12"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "Procurement review",
                        "groups": [
                            {
                                "approvalCriteria": {
                                    "requiredApprovalCount": 1
                                },
                                "approvers": [
                                    {
                                        "procurementToolApprover": {
"name": "Example procurement system"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    ],
    "nextToken": null
}
```

## See Also
<a name="API_marketplace-agreements_GetAgreementRequestApprovalPlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans)
