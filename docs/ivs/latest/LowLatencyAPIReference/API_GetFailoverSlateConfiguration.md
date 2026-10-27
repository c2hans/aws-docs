---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetFailoverSlateConfiguration.html
---

# GetFailoverSlateConfiguration
<a name="API_GetFailoverSlateConfiguration"></a>

Gets the failover slate configuration for the specified ARN.

## Request Syntax
<a name="API_GetFailoverSlateConfiguration_RequestSyntax"></a>

```
POST /GetFailoverSlateConfiguration HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetFailoverSlateConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetFailoverSlateConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_GetFailoverSlateConfiguration_RequestSyntax) **   <a name="ivs-GetFailoverSlateConfiguration-request-arn"></a>
ARN of the failover slate configuration to be retrieved.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:failover-slate-configuration/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetFailoverSlateConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failoverSlateConfiguration": {
      "activationThresholdSeconds": number,
      "arn": "string",
      "maxSlateDisplaySeconds": number,
      "minSlateDisplaySeconds": number,
      "name": "string",
      "state": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_GetFailoverSlateConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failoverSlateConfiguration](#API_GetFailoverSlateConfiguration_ResponseSyntax) **   <a name="ivs-GetFailoverSlateConfiguration-response-failoverSlateConfiguration"></a>
The failover slate configuration that was retrieved.
Type: [FailoverSlateConfiguration](API_FailoverSlateConfiguration.md) object

## Errors
<a name="API_GetFailoverSlateConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetFailoverSlateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/GetFailoverSlateConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/GetFailoverSlateConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/GetFailoverSlateConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/GetFailoverSlateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/GetFailoverSlateConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/GetFailoverSlateConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/GetFailoverSlateConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/GetFailoverSlateConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/GetFailoverSlateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/GetFailoverSlateConfiguration)
