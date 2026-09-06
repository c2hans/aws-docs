---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_UpdateRfc.html
---

# UpdateRfc
<a name="API_UpdateRfc"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Updates settings for the specified RFC ID. Updates non-null values.

## Request Syntax
<a name="API_UpdateRfc_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "ExecutionParameters": "{{string}}",
   "ExpectedOutcome": "{{string}}",
   "ImplementationPlan": "{{string}}",
   "Notification": {
      "Email": {
         "EmailRecipients": [ "{{string}}" ]
      }
   },
   "RequestedEndTime": "{{string}}",
   "RequestedStartTime": "{{string}}",
   "RfcId": "{{string}}",
   "RollbackPlan": "{{string}}",
   "Title": "{{string}}",
   "WorstCaseScenario": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateRfc_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-Description"></a>
The new description of the RFC.
Type: String
Required: No

 ** [ExecutionParameters](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-ExecutionParameters"></a>
The new parameters that are required to execute the RFC, submitted in JSON format.
Type: String
Required: No

 ** [ExpectedOutcome](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-ExpectedOutcome"></a>
A new description of the effects of the change.
Type: String
Required: No

 ** [ImplementationPlan](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-ImplementationPlan"></a>
The new actions or steps required to implement the change (for change types that are not automated).
Type: String
Required: No

 ** [Notification](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-Notification"></a>
Notice that an RFC has been updated.
Type: [RfcNotification](API_RfcNotification.md) object
Required: No

 ** [RequestedEndTime](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-RequestedEndTime"></a>
The new end of the change window, expressed in ISO 8601 format. The default format is the *basic* format (`YYYYMMDDThhmmssZ`). For example, 2017/02/27 at 2:30 PM would be 20170227T143000Z. An RFC does not fail if the requested end time is exceeded.
Type: String
Required: No

 ** [RequestedStartTime](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-RequestedStartTime"></a>
The new start of the change window, expressed in ISO 8601 format. The default format is the *basic* format (`YYYYMMDDThhmmssZ`). For example, 2017/02/27 at 2:10 PM would be 20170227T141000Z. For best results, set the requested start time to at least 10 minutes past the time that you expect to submit the RFC. For review required change types, you must set a start time that's at least 24 hours after you expect to submit the RFC. Alternatively, you can use the ASAP option, which causes the RFC to execute as soon as it's approved. To use the ASAP option, don't specify a start time. If the RFC doesn't pass syntax or other checks before the requested start time (if set), then the RFC is canceled.
Type: String
Required: No

 ** [RfcId](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-RfcId"></a>
The unique ID (UUID) of the RFC.
Type: String
Required: Yes

 ** [RollbackPlan](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-RollbackPlan"></a>
The new actions or steps required to undo the change.
Type: String
Required: No

 ** [Title](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-Title"></a>
A new name for the RFC; this is displayed as the subject of the RFC in the AMS console.
Type: String
Required: No

 ** [WorstCaseScenario](#API_UpdateRfc_RequestSyntax) **   <a name="amscm-UpdateRfc-request-WorstCaseScenario"></a>
A new description of the most unfavorable outcome of the change.
Type: String
Required: No

## Response Elements
<a name="API_UpdateRfc_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRfc_Errors"></a>

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
<a name="API_UpdateRfc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/UpdateRfc)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/UpdateRfc)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/UpdateRfc)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/UpdateRfc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/UpdateRfc)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/UpdateRfc)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/UpdateRfc)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/UpdateRfc)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/UpdateRfc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/UpdateRfc)
