---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_SubmitRfc.html
---

# SubmitRfc
<a name="API_SubmitRfc"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Submits the specified RFC, and optionally specifies whether to observe default execution settings.

## Request Syntax
<a name="API_SubmitRfc_RequestSyntax"></a>

```
{
   "RestrictedExecutionTimesOverrideId": "{{string}}",
   "RfcId": "{{string}}"
}
```

## Request Parameters
<a name="API_SubmitRfc_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RestrictedExecutionTimesOverrideId](#API_SubmitRfc_RequestSyntax) **   <a name="amscm-SubmitRfc-request-RestrictedExecutionTimesOverrideId"></a>
The ID of a value that indicates how the change should observe default execution settings. Possible values: `NoOverrides` \| `OverrideRestrictedTimeRanges`. The default is `NoOverrides`.
Type: String
Required: No

 ** [RfcId](#API_SubmitRfc_RequestSyntax) **   <a name="amscm-SubmitRfc-request-RfcId"></a>
The unique ID (UUID) of the RFC to submit.
Type: String
Required: Yes

## Response Elements
<a name="API_SubmitRfc_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SubmitRfc_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

 ** InvalidRfcScheduleException **
The specified schedule is not valid. Actual status code: 409
HTTP Status Code: 400

 ** InvalidRfcStateException **
The RFC is not in a state that allows the requested operation. Actual status code: 409
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource could not be located. Actual status code: 404
HTTP Status Code: 400

## See Also
<a name="API_SubmitRfc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/SubmitRfc)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/SubmitRfc)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/SubmitRfc)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/SubmitRfc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/SubmitRfc)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/SubmitRfc)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/SubmitRfc)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/SubmitRfc)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/SubmitRfc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/SubmitRfc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
