---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_DescribeOrganizationConfiguration.html
---

# DescribeOrganizationConfiguration
<a name="API_DescribeOrganizationConfiguration"></a>

Describe Amazon Inspector configuration settings for an AWS organization.

## Request Syntax
<a name="API_DescribeOrganizationConfiguration_RequestSyntax"></a>

```
POST /organizationconfiguration/describe HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeOrganizationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeOrganizationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeOrganizationConfiguration_ResponseSyntax"></a>

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
   },
   "maxAccountLimitReached": boolean
}
```

## Response Elements
<a name="API_DescribeOrganizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autoEnable](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="inspector2-DescribeOrganizationConfiguration-response-autoEnable"></a>
The scan types are automatically enabled for new members of your organization.
Type: [AutoEnable](API_AutoEnable.md) object

 ** [maxAccountLimitReached](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="inspector2-DescribeOrganizationConfiguration-response-maxAccountLimitReached"></a>
Represents whether your organization has reached the maximum AWS account limit for Amazon Inspector.
Type: Boolean

## Errors
<a name="API_DescribeOrganizationConfiguration_Errors"></a>

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
<a name="API_DescribeOrganizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/DescribeOrganizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/DescribeOrganizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/DescribeOrganizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/DescribeOrganizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/DescribeOrganizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/DescribeOrganizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/DescribeOrganizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/DescribeOrganizationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/DescribeOrganizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/DescribeOrganizationConfiguration)
