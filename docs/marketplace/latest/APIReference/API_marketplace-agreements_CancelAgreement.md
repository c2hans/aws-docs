---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_CancelAgreement.html
---

# CancelAgreement
<a name="API_marketplace-agreements_CancelAgreement"></a>

Allows an acceptor to cancel an active agreement. Not all agreements are eligible for cancellation. Use the error response to determine why a cancellation request was rejected.

## Request Syntax
<a name="API_marketplace-agreements_CancelAgreement_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_CancelAgreement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_CancelAgreement_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_CancelAgreement-request-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

## Response Elements
<a name="API_marketplace-agreements_CancelAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_marketplace-agreements_CancelAgreement_Errors"></a>

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
<a name="API_marketplace-agreements_CancelAgreement_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_CancelAgreement_Example_1"></a>

This example illustrates one usage of CancelAgreement.

```
{
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95"
}
```

### Sample response
<a name="API_marketplace-agreements_CancelAgreement_Example_2"></a>

This example illustrates one usage of CancelAgreement.

```
{}
```

## See Also
<a name="API_marketplace-agreements_CancelAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/CancelAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/CancelAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/CancelAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/CancelAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/CancelAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/CancelAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/CancelAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/CancelAgreement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/CancelAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/CancelAgreement)
