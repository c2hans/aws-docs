---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_StartConfigurationChecks.html
---

# StartConfigurationChecks
<a name="API_StartConfigurationChecks"></a>

Initiates configuration check operations against a specified application.

## Request Syntax
<a name="API_StartConfigurationChecks_RequestSyntax"></a>

```
POST /start-configuration-checks HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}",
   "ConfigurationCheckIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StartConfigurationChecks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartConfigurationChecks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_StartConfigurationChecks_RequestSyntax) **   <a name="ssmsap-StartConfigurationChecks-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: Yes

 ** [ConfigurationCheckIds](#API_StartConfigurationChecks_RequestSyntax) **   <a name="ssmsap-StartConfigurationChecks-request-ConfigurationCheckIds"></a>
The list of configuration checks to perform.
Type: Array of strings
Valid Values: `SAP_CHECK_01 | SAP_CHECK_02 | SAP_CHECK_03`
Required: No

## Response Syntax
<a name="API_StartConfigurationChecks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationCheckOperations": [
      {
         "ApplicationId": "string",
         "ConfigurationCheckDescription": "string",
         "ConfigurationCheckId": "string",
         "ConfigurationCheckName": "string",
         "EndTime": number,
         "Id": "string",
         "RuleStatusCounts": {
            "Failed": number,
            "Info": number,
            "Passed": number,
            "Unknown": number,
            "Warning": number
         },
         "StartTime": number,
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_StartConfigurationChecks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationCheckOperations](#API_StartConfigurationChecks_ResponseSyntax) **   <a name="ssmsap-StartConfigurationChecks-response-ConfigurationCheckOperations"></a>
The configuration check operations that were started.
Type: Array of [ConfigurationCheckOperation](API_ConfigurationCheckOperation.md) objects

## Errors
<a name="API_StartConfigurationChecks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A conflict has occurred.
HTTP Status Code: 409

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource is not available.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartConfigurationChecks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/StartConfigurationChecks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/StartConfigurationChecks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/StartConfigurationChecks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/StartConfigurationChecks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/StartConfigurationChecks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/StartConfigurationChecks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/StartConfigurationChecks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/StartConfigurationChecks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/StartConfigurationChecks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/StartConfigurationChecks)
