---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RejectRfc.html
---

# RejectRfc
<a name="API_RejectRfc"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Marks the specified RFC as rejected. The alternate operation to `ApproveRfc`.

An RFC with a CT of "Execution mode: Manual" requires approval; rarely it requires customer response, either approval or rejection. If your response is explicitly required, the `Approval Status: CustomerApproval Pending` RFC status is in the RFC execution output, but you receive no other notice. You must explicitly reject or approve the RFC by running this operation or the ApproveRfc operation.

## Request Syntax
<a name="API_RejectRfc_RequestSyntax"></a>

```
{
   "Reason": "{{string}}",
   "RfcId": "{{string}}"
}
```

## Request Parameters
<a name="API_RejectRfc_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Reason](#API_RejectRfc_RequestSyntax) **   <a name="amscm-RejectRfc-request-Reason"></a>
The reason for the rejection.
If an RFC is rejected or canceled, the reason for the action appears in the `RfcReason`.
Type: String
Required: Yes

 ** [RfcId](#API_RejectRfc_RequestSyntax) **   <a name="amscm-RejectRfc-request-RfcId"></a>
The unique ID (UUID) of the RFC to reject.
Type: String
Required: Yes

## Response Elements
<a name="API_RejectRfc_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RejectRfc_Errors"></a>

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
<a name="API_RejectRfc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/RejectRfc)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/RejectRfc)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/RejectRfc)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/RejectRfc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/RejectRfc)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/RejectRfc)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/RejectRfc)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/RejectRfc)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/RejectRfc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/RejectRfc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
