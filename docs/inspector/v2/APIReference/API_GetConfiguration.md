---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetConfiguration.html
---

# GetConfiguration
<a name="API_GetConfiguration"></a>

Retrieves setting configurations for Amazon Inspector scans. If you specify an `accountId`, this operation returns the scan configuration for that member account. You must be the delegated administrator for the specified member account. If you do not specify an `accountId`, this operation returns your own scan configuration.

## Request Syntax
<a name="API_GetConfiguration_RequestSyntax"></a>

```
POST /configuration/get HTTP/1.1
Content-type: application/json

{
   "accountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountId](#API_GetConfiguration_RequestSyntax) **   <a name="inspector2-GetConfiguration-request-accountId"></a>
The 12-digit AWS account ID of the member account whose scan configuration you want to retrieve. When specified, you must be the delegated administrator for this member account. If not specified, the operation returns your own configuration.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## Response Syntax
<a name="API_GetConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ec2Configuration": {
      "scanModeState": {
         "scanMode": "string",
         "scanModeStatus": "string"
      },
      "vmScannerState": {
         "activated": boolean,
         "activatedAt": number,
         "status": "string"
      }
   },
   "ecrConfiguration": {
      "rescanDurationState": {
         "pullDateRescanDuration": "string",
         "pullDateRescanMode": "string",
         "rescanDuration": "string",
         "status": "string",
         "updatedAt": number
      }
   }
}
```

## Response Elements
<a name="API_GetConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ec2Configuration](#API_GetConfiguration_ResponseSyntax) **   <a name="inspector2-GetConfiguration-response-ec2Configuration"></a>
Specifies how the Amazon EC2 automated scan mode is currently configured for your environment.
Type: [Ec2ConfigurationState](API_Ec2ConfigurationState.md) object

 ** [ecrConfiguration](#API_GetConfiguration_ResponseSyntax) **   <a name="inspector2-GetConfiguration-response-ecrConfiguration"></a>
Specifies how the ECR automated re-scan duration is currently configured for your environment.
Type: [EcrConfigurationState](API_EcrConfigurationState.md) object

## Errors
<a name="API_GetConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetConfiguration)
