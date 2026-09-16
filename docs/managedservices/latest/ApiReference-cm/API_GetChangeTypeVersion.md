---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_GetChangeTypeVersion.html
---

# GetChangeTypeVersion
<a name="API_GetChangeTypeVersion"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Returns information about the specified change type; optionally, you can specify a change type version identifier. By default, the most recent version of the change type is returned.

The information returned includes:
+ Execution approval requirements (`ApprovalCondition`)
+ Whether execution of the change is automated or manual (`AutomationStatus`)
+ Change type deprecation information (`DeprecationMessage` and `DeprecationTime`)
+ An estimate of the time required for execution of the change (`ExpectedExecutionDurationInMinutes`)
+ The parameters that can be specified for the change (`ExecutionInputSchema`)

For more information and examples, see [Understanding Change Types](https://docs.aws.amazon.com/managedservices/latest/userguide/understanding-cts.html) in the *AWS Managed Services User Guide*.

## Request Syntax
<a name="API_GetChangeTypeVersion_RequestSyntax"></a>

```
{
   "ChangeTypeId": "{{string}}",
   "Locale": "{{string}}",
   "Version": "{{string}}"
}
```

## Request Parameters
<a name="API_GetChangeTypeVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeTypeId](#API_GetChangeTypeVersion_RequestSyntax) **   <a name="amscm-GetChangeTypeVersion-request-ChangeTypeId"></a>
The unique ID of the change type, in the form ct-2ty5seo8rxfsc.
Type: String
Required: Yes

 ** [Locale](#API_GetChangeTypeVersion_RequestSyntax) **   <a name="amscm-GetChangeTypeVersion-request-Locale"></a>
The locale (language) to return information in. The default is English. **Note:** For future use; not currently implemented.
Type: String
Required: No

 ** [Version](#API_GetChangeTypeVersion_RequestSyntax) **   <a name="amscm-GetChangeTypeVersion-request-Version"></a>
The version identifier of the change type to return.
If you use the AWS CLI and want to specify a change type version in the request, you must use extra double hyphens (--) to cause the CLI to interpret the `--version` parameter correctly (and not interpret it as a base AWS CLI option). Any base AWS CLI options and parameters (not specific to the AWS Managed Services API), such as `--output` or `--profile`, must appear before the double hyphen. The simplest way to do this is by putting the double hyphens immediately before the `get-change-type-version` command. For example: `aws amscm --output text -- get-change-type-version --version 1.0`
This special treatment applies only if you specify the parameter on the command line; no special treatment is necessary if you provide parameters in JSON format.
Type: String
Required: No

## Response Syntax
<a name="API_GetChangeTypeVersion_ResponseSyntax"></a>

```
{
   "ChangeTypeVersion": {
      "AccessLevel": {
         "Id": "string",
         "Name": "string"
      },
      "ApprovalCondition": {
         "AwsApproval": {
            "Id": "string",
            "Name": "string"
         },
         "CustomerApproval": {
            "Id": "string",
            "Name": "string"
         }
      },
      "AutomationStatus": {
         "Id": "string",
         "Name": "string"
      },
      "ChangeTypeId": "string",
      "CreatedTime": "string",
      "DeprecationMessage": "string",
      "DeprecationTime": "string",
      "ExecutionInputSchema": "string",
      "ExecutionOutputSchema": "string",
      "ExpectedExecutionDurationInMinutes": number,
      "Name": "string",
      "Version": "string"
   }
}
```

## Response Elements
<a name="API_GetChangeTypeVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeTypeVersion](#API_GetChangeTypeVersion_ResponseSyntax) **   <a name="amscm-GetChangeTypeVersion-response-ChangeTypeVersion"></a>
Information about the specified version of the change type.
Type: [ChangeTypeVersion](API_ChangeTypeVersion.md) object

## Errors
<a name="API_GetChangeTypeVersion_Errors"></a>

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
<a name="API_GetChangeTypeVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/GetChangeTypeVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/GetChangeTypeVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/GetChangeTypeVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/GetChangeTypeVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/GetChangeTypeVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/GetChangeTypeVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/GetChangeTypeVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/GetChangeTypeVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/GetChangeTypeVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/GetChangeTypeVersion)
