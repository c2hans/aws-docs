---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html
---

# CreateRfc
<a name="API_CreateRfc"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Creates a new RFC.

To create a request for change, begin by calling [CreateRfc](#API_CreateRfc). After creating the basic RFC and before submitting it, you can add or update information (`Description`, `ExpectedOutcome`, `ImplementationPlan`, `RollbackPlan`, and `WorstCaseScenario`) by using the `UpdateRfc` operation ([UpdateRfc](API_UpdateRfc.md)).

When all necessary information has been added, use [SubmitRfc](API_SubmitRfc.md) to activate the RFC.

**Note**
Although only the change type (`ChangeTypeId` and `ChangeTypeVersion`) and `Title` are required to initially create an RFC, you must provide values for these fields (either in the original [CreateRfc](#API_CreateRfc) call or by using the corresponding `UpdateRfc` ([UpdateRfc](API_UpdateRfc.md) operation) before calling [SubmitRfc](API_SubmitRfc.md):
 `RequestedStartTime` ([CreateRfc](#API_CreateRfc) and `RequestedEndTime`, if you want to schedule the RFC. If scheduling is unimportant, leave off these values and execution begins as soon as the RFC is approved. This is part of a feature known as ASAP, or un-scheduled RFC.
 `ExecutionParameters` that comply with the JSON `ExecutionInputSchema` of the change type that is associated with the RFC ([CreateRfc](#API_CreateRfc) or [UpdateRfc](API_UpdateRfc.md))

For more information and examples, see [Change Management](https://docs.aws.amazon.com/managedservices/latest/userguide/change-mgmt.html) in the *AWS Managed Services User Guide*.

## Request Syntax
<a name="API_CreateRfc_RequestSyntax"></a>

```
{
   "ChangeTypeId": "{{string}}",
   "ChangeTypeVersion": "{{string}}",
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
   "RollbackPlan": "{{string}}",
   "Title": "{{string}}",
   "WorstCaseScenario": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateRfc_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeTypeId](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-ChangeTypeId"></a>
The unique ID of the change type, in the form ct-2ty5seo8rxfsc.
Type: String
Required: Yes

 ** [ChangeTypeVersion](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-ChangeTypeVersion"></a>
The version of the change type for the request; for example, "1.0".
Type: String
Required: Yes

 ** [Description](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-Description"></a>
The description of the RFC.
Type: String
Required: No

 ** [ExecutionParameters](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-ExecutionParameters"></a>
The parameters that are required to execute the RFC, submitted in JSON format.
Type: String
Required: No

 ** [ExpectedOutcome](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-ExpectedOutcome"></a>
A description of the effects of the change.
Type: String
Required: No

 ** [ImplementationPlan](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-ImplementationPlan"></a>
The actions or steps required to implement the change (for change types that are not automated).
Type: String
Required: No

 ** [Notification](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-Notification"></a>
Create a notification for an existing RFC.
Type: [RfcNotification](API_RfcNotification.md) object
Required: No

 ** [RequestedEndTime](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-RequestedEndTime"></a>
The end of the change window, expressed in ISO 8601 format. The default format is the *basic* format (`YYYYMMDDThhmmssZ`). For example, 2017/02/27 at 2:30 PM would be 20170227T143000Z. An RFC does not fail if the requested end time is exceeded.
Type: String
Required: No

 ** [RequestedStartTime](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-RequestedStartTime"></a>
The start of the change window, expressed in ISO 8601 format. The default format is the *basic* format (`YYYYMMDDThhmmssZ`). For example, 2017/02/27 at 2:10 PM would be 20170227T141000Z. For best results, set the requested start time to at least 10 minutes after you expect to submit the automated RFC. For review required change types, you must set a start time that's at least 24 hours after you expect to submit the RFC. Alternatively, you can use the ASAP option, which causes the RFC to execute as soon as it's approved. To use the ASAP option, don't specify a start time. If the RFC doesn't pass syntax or other checks before the requested start time (if one is set), then the RFC is canceled.
Type: String
Required: No

 ** [RollbackPlan](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-RollbackPlan"></a>
The actions or steps required to undo the change.
Type: String
Required: No

 ** [Title](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-Title"></a>
A name for the RFC; this is displayed as the subject of the RFC in the AMS console.
Type: String
Required: Yes

 ** [WorstCaseScenario](#API_CreateRfc_RequestSyntax) **   <a name="amscm-CreateRfc-request-WorstCaseScenario"></a>
A description of the most unfavorable outcome of the change.
Type: String
Required: No

## Response Syntax
<a name="API_CreateRfc_ResponseSyntax"></a>

```
{
   "RfcId": "string"
}
```

## Response Elements
<a name="API_CreateRfc_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RfcId](#API_CreateRfc_ResponseSyntax) **   <a name="amscm-CreateRfc-response-RfcId"></a>
The unique ID (UUID) of the RFC that was created.
Type: String

## Errors
<a name="API_CreateRfc_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateRfc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/CreateRfc)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/CreateRfc)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/CreateRfc)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/CreateRfc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/CreateRfc)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/CreateRfc)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/CreateRfc)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/CreateRfc)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/CreateRfc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/CreateRfc)
