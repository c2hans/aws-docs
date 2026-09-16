---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfcCorrespondence.html
---

# CreateRfcCorrespondence
<a name="API_CreateRfcCorrespondence"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Create the correspondence for an RFC.

## Request Syntax
<a name="API_CreateRfcCorrespondence_RequestSyntax"></a>

```
{
   "AttachmentIds": [ "{{string}}" ],
   "Content": "{{string}}",
   "RfcId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateRfcCorrespondence_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttachmentIds](#API_CreateRfcCorrespondence_RequestSyntax) **   <a name="amscm-CreateRfcCorrespondence-request-AttachmentIds"></a>
The attachment identifiers for an RFC correspondence request.
Type: Array of strings
Required: No

 ** [Content](#API_CreateRfcCorrespondence_RequestSyntax) **   <a name="amscm-CreateRfcCorrespondence-request-Content"></a>
The content for an RFC correspondence request.
Type: String
Required: Yes

 ** [RfcId](#API_CreateRfcCorrespondence_RequestSyntax) **   <a name="amscm-CreateRfcCorrespondence-request-RfcId"></a>
The RFC identifier for an RFC correspondence request.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateRfcCorrespondence_ResponseSyntax"></a>

```
{
   "CorrespondenceId": "string",
   "RfcId": "string"
}
```

## Response Elements
<a name="API_CreateRfcCorrespondence_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CorrespondenceId](#API_CreateRfcCorrespondence_ResponseSyntax) **   <a name="amscm-CreateRfcCorrespondence-response-CorrespondenceId"></a>
The correspondence identifier in an RFC correspondence response.
Type: String

 ** [RfcId](#API_CreateRfcCorrespondence_ResponseSyntax) **   <a name="amscm-CreateRfcCorrespondence-response-RfcId"></a>
The RFC identifier in an RFC correspondence response.
Type: String

## Errors
<a name="API_CreateRfcCorrespondence_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

 ** InvalidRfcStateException **
The RFC is not in a state that allows the requested operation. Actual status code: 409
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource could not be located. Actual status code: 404
HTTP Status Code: 400

## See Also
<a name="API_CreateRfcCorrespondence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/CreateRfcCorrespondence)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/CreateRfcCorrespondence)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/CreateRfcCorrespondence)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/CreateRfcCorrespondence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/CreateRfcCorrespondence)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/CreateRfcCorrespondence)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/CreateRfcCorrespondence)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/CreateRfcCorrespondence)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/CreateRfcCorrespondence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/CreateRfcCorrespondence)
