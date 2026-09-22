---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateDistributionConfiguration.html
---

# UpdateDistributionConfiguration
<a name="API_UpdateDistributionConfiguration"></a>

Updates a distribution configuration. Distribution configurations define and configure the outputs for your images, including the target Regions, accounts, and settings for each Region.

**Note**
This operation doesn't support selective updates. The request replaces the stored configuration, so include every setting that you want to keep.

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
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
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
The distribution settings for the configuration. Each entry defines how output images are distributed in one target AWS Region. A Region can appear at most once in the list. This list replaces the configuration's existing distributions entirely.
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
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
You have specified a combination of parameters that isn't valid. For example, two mutually exclusive parameters, or a parameter without its required companion parameter. Review the error message for details.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_UpdateDistributionConfiguration_Examples"></a>

### Update a distribution configuration
<a name="API_UpdateDistributionConfiguration_Example_1"></a>

The following example replaces the distribution settings for the specified configuration with a single distribution that names the output AMI with the build date.

#### Sample Request
<a name="API_UpdateDistributionConfiguration_Example_1_Request"></a>

```
PUT /UpdateDistributionConfiguration HTTP/1.1
Content-type: application/json

{
    "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution",
    "distributions": [
        {
            "region": "us-west-2",
            "amiDistributionConfiguration": {
                "name": "my-example-image-{{ imagebuilder:buildDate }}"
            }
        }
    ],
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLEccccc"
}
```

#### Sample Response
<a name="API_UpdateDistributionConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "97d5c3e8-93d6-424c-90e0-bab18b20bf54",
    "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution"
}
```

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
