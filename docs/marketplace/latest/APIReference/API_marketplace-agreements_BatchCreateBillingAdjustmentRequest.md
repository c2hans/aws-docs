---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BatchCreateBillingAdjustmentRequest.html
---

# BatchCreateBillingAdjustmentRequest
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest"></a>

Allows sellers (proposers) to submit billing adjustment requests for one or more invoices within an agreement. Each entry in the batch specifies an invoice and the adjustment amount. The operation returns successfully created adjustment request IDs and any errors for entries that failed to process.

**Note**
Each entry requires a unique `clientToken` for idempotency.

## Request Syntax
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_RequestSyntax"></a>

```
{
   "billingAdjustmentRequestEntries": [
      {
         "adjustmentAmount": "{{string}}",
         "adjustmentReasonCode": "{{string}}",
         "agreementId": "{{string}}",
         "clientToken": "{{string}}",
         "currencyCode": "{{string}}",
         "description": "{{string}}",
         "originalInvoiceId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [billingAdjustmentRequestEntries](#API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_BatchCreateBillingAdjustmentRequest-request-billingAdjustmentRequestEntries"></a>
A list of billing adjustment request entries. Each entry specifies the invoice and adjustment details.
Type: Array of [BatchCreateBillingAdjustmentRequestEntry](API_marketplace-agreements_BatchCreateBillingAdjustmentRequestEntry.md) objects
Required: Yes

## Response Syntax
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "clientToken": "string",
         "code": "string",
         "message": "string"
      }
   ],
   "items": [
      {
         "billingAdjustmentRequestId": "string",
         "clientToken": "string"
      }
   ]
}
```

## Response Elements
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_BatchCreateBillingAdjustmentRequest-response-errors"></a>
A list of errors for entries that failed validation, each containing the `clientToken`, error `code`, and `message`.
Type: Array of [BatchCreateBillingAdjustmentError](API_marketplace-agreements_BatchCreateBillingAdjustmentError.md) objects

 ** [items](#API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_BatchCreateBillingAdjustmentRequest-response-items"></a>
A list of successfully created billing adjustment items, each containing the `billingAdjustmentRequestId` and `clientToken`.
Type: Array of [BatchCreateBillingAdjustmentItem](API_marketplace-agreements_BatchCreateBillingAdjustmentItem.md) objects

## Errors
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_Errors"></a>

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

 ** ConflictException **
Request was denied due to a resource conflict.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
 ** resourceId **
The unique identifier of the resource involved in the conflict.
 ** resourceType **
The type of the resource involved in the conflict.
HTTP Status Code: 400

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
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_Example_1"></a>

This example illustrates one usage of BatchCreateBillingAdjustmentRequest.

```
{
    "billingAdjustmentRequestEntries": [
        {
            "originalInvoiceId": "E2E20230929a108cfae",
            "agreementId": "agmt-EXAMPLESvIzsqYMyQwI3",
            "adjustmentAmount": "500.00",
            "currencyCode": "USD",
            "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "adjustmentReasonCode": "OTHER",
            "description": "Customer requested adjustment due to service outage during critical business period."
        },
        {
            "originalInvoiceId": "E2E20230929b209dfbf",
            "agreementId": "agmt-EXAMPLESvIzsqYMyQwI3",
            "adjustmentAmount": "999999.00",
            "currencyCode": "USD",
            "clientToken": "d2a5e82e-a49b-4075-8c7f-EXAMPLE22222",
            "adjustmentReasonCode": "OTHER",
            "description": "Customer requested adjustment due to service outage during critical business period."
        }
    ]
}
```

### Sample response
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_Example_2"></a>

This example illustrates one usage of BatchCreateBillingAdjustmentRequest.

```
{
    "items": [
        {
            "billingAdjustmentRequestId": "ba-EXAMPLE1a2b3c4d5e",
            "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
    ],
    "errors": [
        {
            "clientToken": "d2a5e82e-a49b-4075-8c7f-EXAMPLE22222",
            "code": "VALIDATION_EXCEPTION",
            "message": "Refund amount $999999.00 exceeds maximum refundable amount $200.00"
        }
    ]
}
```

## See Also
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
