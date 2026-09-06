---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_GetRfc.html
---

# GetRfc
<a name="API_GetRfc"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Returns information about the specified RFC ID.

## Request Syntax
<a name="API_GetRfc_RequestSyntax"></a>

```
{
   "Locale": "{{string}}",
   "RfcId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRfc_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Locale](#API_GetRfc_RequestSyntax) **   <a name="amscm-GetRfc-request-Locale"></a>
The locale (language) to return information in. The default is English. **Note:** For future use; not currently implemented.
Type: String
Required: No

 ** [RfcId](#API_GetRfc_RequestSyntax) **   <a name="amscm-GetRfc-request-RfcId"></a>
The unique ID (UUID) of the RFC
Type: String
Required: Yes

## Response Syntax
<a name="API_GetRfc_ResponseSyntax"></a>

```
{
   "Rfc": {
      "ActionState": {
         "Id": "string",
         "Name": "string"
      },
      "ActualExecutionTimeRange": {
         "EndTime": "string",
         "StartTime": "string"
      },
      "ApprovalState": {
         "AwsApprovalStatus": {
            "Id": "string",
            "Name": "string"
         },
         "CustomerApprovalStatus": {
            "Id": "string",
            "Name": "string"
         }
      },
      "AutomationStatus": {
         "Id": "string",
         "Name": "string"
      },
      "ChangeTypeId": "string",
      "ChangeTypeVersion": "string",
      "CreatedBy": "string",
      "CreatedTime": "string",
      "Description": "string",
      "ExecutionOutput": "string",
      "ExecutionParameters": "string",
      "ExpectedOutcome": "string",
      "ImplementationPlan": "string",
      "LastCorrespondenceTime": "string",
      "LastModifiedBy": "string",
      "LastModifiedTime": "string",
      "LastSubmittedTime": "string",
      "Notification": {
         "Email": {
            "EmailRecipients": [ "string" ]
         }
      },
      "RequestedExecutionTimeRange": {
         "EndTime": "string",
         "StartTime": "string"
      },
      "RestrictedExecutionTimesOverride": {
         "Id": "string",
         "Name": "string"
      },
      "RfcId": "string",
      "RollbackPlan": "string",
      "Status": {
         "Id": "string",
         "Name": "string"
      },
      "StatusReason": "string",
      "Title": "string",
      "WorstCaseScenario": "string"
   }
}
```

## Response Elements
<a name="API_GetRfc_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Rfc](#API_GetRfc_ResponseSyntax) **   <a name="amscm-GetRfc-response-Rfc"></a>
Information about the RFC.
Type: [Rfc](API_Rfc.md) object

## Errors
<a name="API_GetRfc_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource could not be located. Actual status code: 404
HTTP Status Code: 400

## See Also
<a name="API_GetRfc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/GetRfc)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/GetRfc)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/GetRfc)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/GetRfc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/GetRfc)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/GetRfc)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/GetRfc)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/GetRfc)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/GetRfc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/GetRfc)
