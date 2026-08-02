---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmCustomerAgreement.html
---

# ConfirmCustomerAgreement
<a name="API_ConfirmCustomerAgreement"></a>

 The confirmation of the terms of agreement when creating the connection/link aggregation group (LAG).

## Request Syntax
<a name="API_ConfirmCustomerAgreement_RequestSyntax"></a>

```
{
   "agreementName": "{{string}}"
}
```

## Request Parameters
<a name="API_ConfirmCustomerAgreement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [agreementName](#API_ConfirmCustomerAgreement_RequestSyntax) **   <a name="DX-ConfirmCustomerAgreement-request-agreementName"></a>
 The name of the customer agreement.
Type: String
Length Constraints: Maximum length of 100.
Required: No

## Response Syntax
<a name="API_ConfirmCustomerAgreement_ResponseSyntax"></a>

```
{
   "status": "string"
}
```

## Response Elements
<a name="API_ConfirmCustomerAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_ConfirmCustomerAgreement_ResponseSyntax) **   <a name="DX-ConfirmCustomerAgreement-response-status"></a>
 The status of the customer agreement when the connection was created. This will be either `signed` or `unsigned`.
Type: String
Length Constraints: Maximum length of 30.

## Errors
<a name="API_ConfirmCustomerAgreement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_ConfirmCustomerAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/ConfirmCustomerAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/ConfirmCustomerAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/ConfirmCustomerAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/ConfirmCustomerAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/ConfirmCustomerAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/ConfirmCustomerAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/ConfirmCustomerAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/ConfirmCustomerAgreement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/ConfirmCustomerAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/ConfirmCustomerAgreement)
