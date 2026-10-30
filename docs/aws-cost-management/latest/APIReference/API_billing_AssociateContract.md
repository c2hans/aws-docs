---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_AssociateContract.html
---

# AssociateContract
<a name="API_billing_AssociateContract"></a>

Private Pricing contracts let eligible payer accounts manage private pricing agreements with AWS. This operation associates a private pricing contract with the caller's AWS account. The caller must be a payer (management) account listed on the contract. This operation is idempotent, so retrying a request that already succeeded is safe.

## Request Syntax
<a name="API_billing_AssociateContract_RequestSyntax"></a>

```
{
   "contractArn": "{{string}}",
   "contractDocumentId": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_AssociateContract_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [contractArn](#API_billing_AssociateContract_RequestSyntax) **   <a name="awscostmanagement-billing_AssociateContract-request-contractArn"></a>
The Amazon Resource Name (ARN) of the contract to associate with your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `arn:aws[a-z-]*:billing::[0-9]{12}:contract/[a-zA-Z0-9_\+=\.\@-]{0,70}[a-zA-Z0-9]`
Required: Yes

 ** [contractDocumentId](#API_billing_AssociateContract_RequestSyntax) **   <a name="awscostmanagement-billing_AssociateContract-request-contractDocumentId"></a>
The contract ID from the contract document. It can be found in the top right corner of your contract's pages. This value confirms that you have access to the contract you are associating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Response Elements
<a name="API_billing_AssociateContract_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_billing_AssociateContract_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
 The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
 ** resourceId **
 The identifier for the service resource associated with the request.
 ** resourceType **
 The type of resource associated with the request.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
 ** resourceId **
 Value is a list of resource IDs that were not found.
 ** resourceType **
 Value is the type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_billing_AssociateContract_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/AssociateContract)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/AssociateContract)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/AssociateContract)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/AssociateContract)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/AssociateContract)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/AssociateContract)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/AssociateContract)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/AssociateContract)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/AssociateContract)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/AssociateContract)
