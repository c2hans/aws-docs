---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetContractInformation.html
---

# GetContractInformation
<a name="API_billing_GetContractInformation"></a>

Returns information about a specific private pricing contract, including its term (duration), eligible payer accounts, investment accounts, and legal entities. This operation is read-only.

## Request Syntax
<a name="API_billing_GetContractInformation_RequestSyntax"></a>

```
{
   "contractArn": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_GetContractInformation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [contractArn](#API_billing_GetContractInformation_RequestSyntax) **   <a name="awscostmanagement-billing_GetContractInformation-request-contractArn"></a>
The Amazon Resource Name (ARN) of the contract to retrieve information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `arn:aws[a-z-]*:billing::[0-9]{12}:contract/[a-zA-Z0-9_\+=\.\@-]{0,70}[a-zA-Z0-9]`
Required: Yes

## Response Syntax
<a name="API_billing_GetContractInformation_ResponseSyntax"></a>

```
{
   "contract": { ... }
}
```

## Response Elements
<a name="API_billing_GetContractInformation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contract](#API_billing_GetContractInformation_ResponseSyntax) **   <a name="awscostmanagement-billing_GetContractInformation-response-contract"></a>
The contract details such as term (duration), eligible payer accounts, investment accounts, and legal entities.
Type: [ContractDetails](API_billing_ContractDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_billing_GetContractInformation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
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
<a name="API_billing_GetContractInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/GetContractInformation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/GetContractInformation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/GetContractInformation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/GetContractInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/GetContractInformation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/GetContractInformation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/GetContractInformation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/GetContractInformation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/GetContractInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/GetContractInformation)
