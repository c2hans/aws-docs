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
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_GetDistributionConfiguration_Examples"></a>

### Get the details of a distribution configuration
<a name="API_GetDistributionConfiguration_Example_1"></a>

The following example retrieves a distribution configuration that distributes the output AMI to two Regions.

#### Sample Request
<a name="API_GetDistributionConfiguration_Example_1_Request"></a>

```
GET /GetDistributionConfiguration?distributionConfigurationArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Adistribution-configuration%2Fmy-example-distribution HTTP/1.1
```

#### Sample Response
<a name="API_GetDistributionConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "2d0a8dc0-99d5-4d7a-af7a-d1aeafd71c2e",
    "distributionConfiguration": {
        "arn": "arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution",
        "name": "my-example-distribution",
        "description": "Copies the output AMI to a second Region",
        "distributions": [
            {
                "region": "us-west-2",
                "amiDistributionConfiguration": {
                    "name": "my-example-image-{{ imagebuilder:buildDate }}"
                }
            },
            {
                "region": "us-east-1",
                "amiDistributionConfiguration": {
                    "name": "my-example-image-{{ imagebuilder:buildDate }}"
                }
            }
        ],
        "timeoutMinutes": 720,
        "dateCreated": "2026-09-09T19:37:37.231Z",
        "tags": {}
    }
}
```

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
