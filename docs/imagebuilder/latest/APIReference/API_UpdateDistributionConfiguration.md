---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateDistributionConfiguration.html
---

# UpdateDistributionConfiguration
<a name="API_UpdateDistributionConfiguration"></a>

Updates a distribution configuration. Distribution configurations define and configure the outputs of your pipeline.

## Request Syntax
<a name="API_UpdateDistributionConfiguration_RequestSyntax"></a>

```
PUT /UpdateDistributionConfiguration HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "distributionConfigurationArn": "{{string}}",
   "distributions": [
      {
         "amiDistributionConfiguration": {
            "amiTags": {
               "{{string}}" : "{{string}}"
            },
            "description": "{{string}}",
            "kmsKeyId": "{{string}}",
            "launchPermission": {
               "organizationalUnitArns": [ "{{string}}" ],
               "organizationArns": [ "{{string}}" ],
               "userGroups": [ "{{string}}" ],
               "userIds": [ "{{string}}" ]
            },
            "name": "{{string}}",
            "targetAccountIds": [ "{{string}}" ]
         },
         "containerDistributionConfiguration": {
            "containerTags": [ "{{string}}" ],
            "description": "{{string}}",
            "targetRepository": {
               "repositoryName": "{{string}}",
               "service": "{{string}}"
            }
         },
         "fastLaunchConfigurations": [
            {
               "accountId": "{{string}}",
               "enabled": {{boolean}},
               "launchTemplate": {
                  "launchTemplateId": "{{string}}",
                  "launchTemplateName": "{{string}}",
                  "launchTemplateVersion": "{{string}}"
               },
               "maxParallelLaunches": {{number}},
               "snapshotConfiguration": {
                  "targetResourceCount": {{number}}
               }
            }
         ],
         "launchTemplateConfigurations": [
            {
               "accountId": "{{string}}",
               "launchTemplateId": "{{string}}",
               "setDefaultVersion": {{boolean}}
            }
         ],
         "licenseConfigurationArns": [ "{{string}}" ],
         "region": "{{string}}",
         "s3ExportConfiguration": {
            "diskImageFormat": "{{string}}",
            "roleName": "{{string}}",
            "s3Bucket": "{{string}}",
            "s3Prefix": "{{string}}"
         },
         "ssmParameterConfigurations": [
            {
               "amiAccountId": "{{string}}",
               "dataType": "{{string}}",
               "parameterName": "{{string}}"
            }
         ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateDistributionConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateDistributionConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateDistributionConfiguration-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_UpdateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateDistributionConfiguration-request-description"></a>
The description of the distribution configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [distributionConfigurationArn](#API_UpdateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateDistributionConfiguration-request-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that you want to update.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [distributions](#API_UpdateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateDistributionConfiguration-request-distributions"></a>
The distributions of the distribution configuration.
Type: Array of [Distribution](API_Distribution.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateDistributionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "distributionConfigurationArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_UpdateDistributionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_UpdateDistributionConfiguration_ResponseSyntax) **   <a name="imagebuilder-UpdateDistributionConfiguration-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [distributionConfigurationArn](#API_UpdateDistributionConfiguration_ResponseSyntax) **   <a name="imagebuilder-UpdateDistributionConfiguration-response-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that was updated by this request.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`

 ** [requestId](#API_UpdateDistributionConfiguration_ResponseSyntax) **   <a name="imagebuilder-UpdateDistributionConfiguration-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_UpdateDistributionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
You have specified two or more mutually exclusive parameters. Review the error message for details.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_UpdateDistributionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/UpdateDistributionConfiguration)
