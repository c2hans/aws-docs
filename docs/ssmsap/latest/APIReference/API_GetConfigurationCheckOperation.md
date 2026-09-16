---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetConfigurationCheckOperation.html
---

# GetConfigurationCheckOperation
<a name="API_GetConfigurationCheckOperation"></a>

Gets the details of a configuration check operation by specifying the operation ID.

## Request Syntax
<a name="API_GetConfigurationCheckOperation_RequestSyntax"></a>

```
POST /get-configuration-check-operation HTTP/1.1
Content-type: application/json

{
   "OperationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetConfigurationCheckOperation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetConfigurationCheckOperation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [OperationId](#API_GetConfigurationCheckOperation_RequestSyntax) **   <a name="ssmsap-GetConfigurationCheckOperation-request-OperationId"></a>
The ID of the configuration check operation.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`
Required: Yes

## Response Syntax
<a name="API_GetConfigurationCheckOperation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationCheckOperation": {
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
}
```

## Response Elements
<a name="API_GetConfigurationCheckOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationCheckOperation](#API_GetConfigurationCheckOperation_ResponseSyntax) **   <a name="ssmsap-GetConfigurationCheckOperation-response-ConfigurationCheckOperation"></a>
Returns the details of a configuration check operation.
Type: [ConfigurationCheckOperation](API_ConfigurationCheckOperation.md) object

## Errors
<a name="API_GetConfigurationCheckOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetConfigurationCheckOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/GetConfigurationCheckOperation)
