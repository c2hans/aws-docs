---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCisScanConfiguration.html
---

# CreateCisScanConfiguration
<a name="API_CreateCisScanConfiguration"></a>

Creates a CIS scan configuration.

## Request Syntax
<a name="API_CreateCisScanConfiguration_RequestSyntax"></a>

```
POST /cis/scan-configuration/create HTTP/1.1
Content-type: application/json

{
   "scanName": "{{string}}",
   "schedule": { ... },
   "securityLevel": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targets": {
      "accountIds": [ "{{string}}" ],
      "targetResourceTags": {
         "{{string}}" : [ "{{string}}" ]
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateCisScanConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCisScanConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [scanName](#API_CreateCisScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCisScanConfiguration-request-scanName"></a>
The scan name for the CIS scan configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [schedule](#API_CreateCisScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCisScanConfiguration-request-schedule"></a>
The schedule for the CIS scan configuration.
Type: [Schedule](API_Schedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [securityLevel](#API_CreateCisScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCisScanConfiguration-request-securityLevel"></a>
 The security level for the CIS scan configuration. Security level refers to the Benchmark levels that CIS assigns to a profile.
Type: String
Valid Values: `LEVEL_1 | LEVEL_2`
Required: Yes

 ** [tags](#API_CreateCisScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCisScanConfiguration-request-tags"></a>
The tags for the CIS scan configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [targets](#API_CreateCisScanConfiguration_RequestSyntax) **   <a name="inspector2-CreateCisScanConfiguration-request-targets"></a>
The targets for the CIS scan configuration.
Type: [CreateCisTargets](API_CreateCisTargets.md) object
Required: Yes

## Response Syntax
<a name="API_CreateCisScanConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "scanConfigurationArn": "string"
}
```

## Response Elements
<a name="API_CreateCisScanConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scanConfigurationArn](#API_CreateCisScanConfiguration_ResponseSyntax) **   <a name="inspector2-CreateCisScanConfiguration-response-scanConfigurationArn"></a>
The scan configuration ARN for the CIS scan configuration.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-[0-9]{1}:[0-9]{12}:owner/(o-[a-z0-9]+|[0-9]{12})/cis-configuration/[0-9a-fA-F-]+`

## Errors
<a name="API_CreateCisScanConfiguration_Errors"></a>

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
<a name="API_CreateCisScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/CreateCisScanConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/CreateCisScanConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CreateCisScanConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/CreateCisScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CreateCisScanConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/CreateCisScanConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/CreateCisScanConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/CreateCisScanConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/CreateCisScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CreateCisScanConfiguration)
