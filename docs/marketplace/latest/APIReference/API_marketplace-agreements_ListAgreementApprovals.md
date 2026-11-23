---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ListAgreementApprovals.html
---

# ListAgreementApprovals

Lists agreement approvals available to you as a buyer. Use `REQUESTER` as the `partyType` to list the agreement approvals that your account started. Use `AWS_ORGANIZATION_ADMIN` to list the agreement approvals in your AWS organization, if your account is the management account or a delegated administrator of the organization. You can filter the results by agreement request, approval type, and status.

## Request Syntax
<a name="API_marketplace-agreements_ListAgreementApprovals_RequestSyntax"></a>

```
{
   "agreementRequestId": "{{string}}",
   "approvalType": "{{string}}",
   "catalog": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "partyType": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_ListAgreementApprovals_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [partyType](#API_marketplace-agreements_ListAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementApprovals-request-partyType"></a>
The party type for the agreement approvals. Required parameter. Use `REQUESTER` to list agreement approvals for agreement requests that you created, or `AWS_ORGANIZATION_ADMIN` to list agreement approvals as an AWS Organizations administrator.
Type: String
Valid Values: `REQUESTER | AWS_ORGANIZATION_ADMIN`
Required: Yes

 ** [agreementRequestId](#API_marketplace-agreements_ListAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementApprovals-request-agreementRequestId"></a>
An optional parameter to filter agreement approvals for a specific agreement request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`
Required: No

 ** [approvalType](#API_marketplace-agreements_ListAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementApprovals-request-approvalType"></a>
An optional parameter to filter agreement approvals by type. The only valid value is `BUYER_AGREEMENT_APPROVAL`.
Type: String
Valid Values: `BUYER_AGREEMENT_APPROVAL`
Required: No

 ** [catalog](#API_marketplace-agreements_ListAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementApprovals-request-catalog"></a>
An optional parameter to filter agreement approvals by catalog (for example, `AWSMarketplace`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** [maxResults](#API_marketplace-agreements_ListAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementApprovals-request-maxResults"></a>
The maximum number of agreement approvals to return in a single response (1-50). Default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_ListAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementApprovals-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

 ** [status](#API_marketplace-agreements_ListAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementApprovals-request-status"></a>
An optional parameter to filter agreement approvals by status. Valid values include `PENDING_APPROVAL`, `APPROVED`, `REJECTED`, `EXPIRED`, and `CANCELLED`. If you don't specify a status, agreement approvals of all statuses are returned.
Type: String
Valid Values: `PENDING_APPROVAL | APPROVED | REJECTED | EXPIRED | CANCELLED`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_ListAgreementApprovals_ResponseSyntax"></a>

```
{
   "items": [
      {
         "agreementApprovalId": "string",
         "agreementRequestId": "string",
         "approvalNeededBy": number,
         "approvalType": "string",
         "createdAt": number,
         "expiresAt": number,
         "name": "string",
         "startedAt": number,
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_ListAgreementApprovals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_marketplace-agreements_ListAgreementApprovals_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementApprovals-response-items"></a>
An array of `AgreementApprovalSummary` objects containing summary information about each agreement approval.
Type: Array of [AgreementApprovalSummary](API_marketplace-agreements_AgreementApprovalSummary.md) objects

 ** [nextToken](#API_marketplace-agreements_ListAgreementApprovals_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementApprovals-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_ListAgreementApprovals_Errors"></a>

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
<a name="API_marketplace-agreements_ListAgreementApprovals_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_ListAgreementApprovals_Example_1"></a>

This example illustrates one usage of ListAgreementApprovals.

```
{
    "partyType": "REQUESTER",
    "status": "PENDING_APPROVAL",
    "maxResults": 10
}
```

### Sample response
<a name="API_marketplace-agreements_ListAgreementApprovals_Example_2"></a>

This example illustrates one usage of ListAgreementApprovals.

```
{
    "items": [
        {
            "approvalType": "BUYER_AGREEMENT_APPROVAL",
            "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78",
            "agreementApprovalId": "apr-EXAMPLE9s0t1u2v3w4x",
            "name": "Example Analytics Platform sold by Example Corp",
            "status": "PENDING_APPROVAL",
            "createdAt": 1736935800,
            "updatedAt": 1737022200,
            "startedAt": 1736935800,
            "expiresAt": 1739527800,
            "approvalNeededBy": 1739527800
        }
    ],
    "nextToken": null
}
```

## See Also
<a name="API_marketplace-agreements_ListAgreementApprovals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/ListAgreementApprovals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/ListAgreementApprovals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ListAgreementApprovals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/ListAgreementApprovals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ListAgreementApprovals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/ListAgreementApprovals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/ListAgreementApprovals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/ListAgreementApprovals)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/ListAgreementApprovals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ListAgreementApprovals)
