---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetDistributionConfiguration.html
---

# GetDistributionConfiguration
<a name="API_GetDistributionConfiguration"></a>

Retrieves a distribution configuration.

## Request Syntax
<a name="API_GetDistributionConfiguration_RequestSyntax"></a>

```
GET /GetDistributionConfiguration?distributionConfigurationArn={{distributionConfigurationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDistributionConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [distributionConfigurationArn](#API_GetDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-GetDistributionConfiguration-request-uri-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that you want to retrieve.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`
Required: Yes

## Request Body
<a name="API_GetDistributionConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDistributionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "distributionConfiguration": {
      "arn": "string",
      "dateCreated": "string",
      "dateUpdated": "string",
      "description": "string",
      "distributions": [
         {
            "amiDistributionConfiguration": {
               "amiTags": {
                  "string" : "string"
               },
               "description": "string",
               "kmsKeyId": "string",
               "launchPermission": {
                  "organizationalUnitArns": [ "string" ],
                  "organizationArns": [ "string" ],
                  "userGroups": [ "string" ],
                  "userIds": [ "string" ]
               },
               "name": "string",
               "targetAccountIds": [ "string" ]
            },
            "containerDistributionConfiguration": {
               "containerTags": [ "string" ],
               "description": "string",
               "targetRepository": {
                  "repositoryName": "string",
                  "service": "string"
               }
            },
            "fastLaunchConfigurations": [
               {
                  "accountId": "string",
                  "enabled": boolean,
                  "launchTemplate": {
                     "launchTemplateId": "string",
                     "launchTemplateName": "string",
                     "launchTemplateVersion": "string"
                  },
                  "maxParallelLaunches": number,
                  "snapshotConfiguration": {
                     "targetResourceCount": number
                  }
               }
            ],
            "launchTemplateConfigurations": [
               {
                  "accountId": "string",
                  "launchTemplateId": "string",
                  "setDefaultVersion": boolean
               }
            ],
            "licenseConfigurationArns": [ "string" ],
            "region": "string",
            "s3ExportConfiguration": {
               "diskImageFormat": "string",
               "roleName": "string",
               "s3Bucket": "string",
               "s3Prefix": "string"
            },
            "ssmParameterConfigurations": [
               {
                  "amiAccountId": "string",
                  "dataType": "string",
                  "parameterName": "string"
               }
            ]
         }
      ],
      "name": "string",
      "tags": {
         "string" : "string"
      },
      "timeoutMinutes": number
   },
   "requestId": "string"
}
```

## Response Elements
<a name="API_GetDistributionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [distributionConfiguration](#API_GetDistributionConfiguration_ResponseSyntax) **   <a name="imagebuilder-GetDistributionConfiguration-response-distributionConfiguration"></a>
The distribution configuration object.
Type: [DistributionConfiguration](API_DistributionConfiguration.md) object

 ** [requestId](#API_GetDistributionConfiguration_ResponseSyntax) **   <a name="imagebuilder-GetDistributionConfiguration-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetDistributionConfiguration_Errors"></a>

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

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_GetDistributionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetDistributionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetDistributionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetDistributionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetDistributionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetDistributionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetDistributionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetDistributionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetDistributionConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetDistributionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetDistributionConfiguration)
