---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateOrganizationConfiguration.html
---

# UpdateOrganizationConfiguration
<a name="API_UpdateOrganizationConfiguration"></a>

Updates the configurations for your Amazon Inspector organization.

## Request Syntax
<a name="API_UpdateOrganizationConfiguration_RequestSyntax"></a>

```
POST /organizationconfiguration/update HTTP/1.1
Content-type: application/json

{
   "autoEnable": {
      "codeRepository": {{boolean}},
      "ec2": {{boolean}},
      "ecr": {{boolean}},
      "lambda": {{boolean}},
      "lambdaCode": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateOrganizationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateOrganizationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [autoEnable](#API_UpdateOrganizationConfiguration_RequestSyntax) **   <a name="inspector2-UpdateOrganizationConfiguration-request-autoEnable"></a>
Defines which scan types are enabled automatically for new members of your Amazon Inspector organization.
Type: [AutoEnable](API_AutoEnable.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateOrganizationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "autoEnable": {
      "codeRepository": boolean,
      "ec2": boolean,
      "ecr": boolean,
      "lambda": boolean,
      "lambdaCode": boolean
   }
}
```

## Response Elements
<a name="API_UpdateOrganizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autoEnable](#API_UpdateOrganizationConfiguration_ResponseSyntax) **   <a name="inspector2-UpdateOrganizationConfiguration-response-autoEnable"></a>
The updated status of scan types automatically enabled for new members of your Amazon Inspector organization.
Type: [AutoEnable](API_AutoEnable.md) object

## Errors
<a name="API_UpdateOrganizationConfiguration_Errors"></a>

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
<a name="API_UpdateOrganizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/UpdateOrganizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/UpdateOrganizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateOrganizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/UpdateOrganizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateOrganizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/UpdateOrganizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/UpdateOrganizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/UpdateOrganizationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/UpdateOrganizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateOrganizationConfiguration)
