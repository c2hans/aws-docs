---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchAssociateCodeSecurityScanConfiguration.html
---

# BatchAssociateCodeSecurityScanConfiguration
<a name="API_BatchAssociateCodeSecurityScanConfiguration"></a>

Associates multiple code repositories with an Amazon Inspector code security scan configuration.

## Request Syntax
<a name="API_BatchAssociateCodeSecurityScanConfiguration_RequestSyntax"></a>

```
POST /codesecurity/scan-configuration/batch/associate HTTP/1.1
Content-type: application/json

{
   "associateConfigurationRequests": [
      {
         "resource": { ... },
         "scanConfigurationArn": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchAssociateCodeSecurityScanConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchAssociateCodeSecurityScanConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associateConfigurationRequests](#API_BatchAssociateCodeSecurityScanConfiguration_RequestSyntax) **   <a name="inspector2-BatchAssociateCodeSecurityScanConfiguration-request-associateConfigurationRequests"></a>
A list of code repositories to associate with the specified scan configuration.
Type: Array of [AssociateConfigurationRequest](API_AssociateConfigurationRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_BatchAssociateCodeSecurityScanConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedAssociations": [
      {
         "resource": { ... },
         "scanConfigurationArn": "string",
         "statusCode": "string",
         "statusMessage": "string"
      }
   ],
   "successfulAssociations": [
      {
         "resource": { ... },
         "scanConfigurationArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchAssociateCodeSecurityScanConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedAssociations](#API_BatchAssociateCodeSecurityScanConfiguration_ResponseSyntax) **   <a name="inspector2-BatchAssociateCodeSecurityScanConfiguration-response-failedAssociations"></a>
Details of any code repositories that failed to be associated with the scan configuration.
Type: Array of [FailedAssociationResult](API_FailedAssociationResult.md) objects

 ** [successfulAssociations](#API_BatchAssociateCodeSecurityScanConfiguration_ResponseSyntax) **   <a name="inspector2-BatchAssociateCodeSecurityScanConfiguration-response-successfulAssociations"></a>
Details of code repositories that were successfully associated with the scan configuration.
Type: Array of [SuccessfulAssociationResult](API_SuccessfulAssociationResult.md) objects

## Errors
<a name="API_BatchAssociateCodeSecurityScanConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred. This exception occurs when the same resource is being modified by concurrent requests.
HTTP Status Code: 409

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
<a name="API_BatchAssociateCodeSecurityScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/BatchAssociateCodeSecurityScanConfiguration)
