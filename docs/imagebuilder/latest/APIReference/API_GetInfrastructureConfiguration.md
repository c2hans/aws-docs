---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetInfrastructureConfiguration.html
---

# GetInfrastructureConfiguration
<a name="API_GetInfrastructureConfiguration"></a>

Retrieves an infrastructure configuration.

## Request Syntax
<a name="API_GetInfrastructureConfiguration_RequestSyntax"></a>

```
GET /GetInfrastructureConfiguration?infrastructureConfigurationArn={{infrastructureConfigurationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInfrastructureConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [infrastructureConfigurationArn](#API_GetInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-GetInfrastructureConfiguration-request-uri-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that you want to retrieve.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

## Request Body
<a name="API_GetInfrastructureConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInfrastructureConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "infrastructureConfiguration": {
      "arn": "string",
      "dateCreated": "string",
      "dateUpdated": "string",
      "description": "string",
      "instanceMetadataOptions": {
         "httpPutResponseHopLimit": number,
         "httpTokens": "string"
      },
      "instanceProfileName": "string",
      "instanceTypes": [ "string" ],
      "keyPair": "string",
      "logging": {
         "s3Logs": {
            "s3BucketName": "string",
            "s3KeyPrefix": "string"
         }
      },
      "name": "string",
      "placement": {
         "availabilityZone": "string",
         "hostId": "string",
         "hostResourceGroupArn": "string",
         "tenancy": "string"
      },
      "resourceTags": {
         "string" : "string"
      },
      "securityGroupIds": [ "string" ],
      "snsTopicArn": "string",
      "subnetId": "string",
      "tags": {
         "string" : "string"
      },
      "terminateInstanceOnFailure": boolean
   },
   "requestId": "string"
}
```

## Response Elements
<a name="API_GetInfrastructureConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [infrastructureConfiguration](#API_GetInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-GetInfrastructureConfiguration-response-infrastructureConfiguration"></a>
The infrastructure configuration object.
Type: [InfrastructureConfiguration](API_InfrastructureConfiguration.md) object

 ** [requestId](#API_GetInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-GetInfrastructureConfiguration-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetInfrastructureConfiguration_Errors"></a>

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
<a name="API_GetInfrastructureConfiguration_Examples"></a>

### Get the details of an infrastructure configuration
<a name="API_GetInfrastructureConfiguration_Example_1"></a>

The following example retrieves an infrastructure configuration that specifies the instance types, instance profile, and instance metadata options that Image Builder uses for build and test instances.

#### Sample Request
<a name="API_GetInfrastructureConfiguration_Example_1_Request"></a>

```
GET /GetInfrastructureConfiguration?infrastructureConfigurationArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Ainfrastructure-configuration%2Fmy-example-infrastructure-configuration HTTP/1.1
```

#### Sample Response
<a name="API_GetInfrastructureConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "7ba25cd0-0735-4f44-bc67-2f231e96503f",
    "infrastructureConfiguration": {
        "arn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure-configuration",
        "name": "my-example-infrastructure-configuration",
        "description": "Infrastructure configuration for my application image builds",
        "instanceTypes": [
            "m5.large",
            "m5.xlarge"
        ],
        "instanceProfileName": "EC2InstanceProfileForImageBuilder",
        "terminateInstanceOnFailure": true,
        "dateCreated": "2026-09-09T19:36:48.933Z",
        "resourceTags": {
            "CostCenter": "12345"
        },
        "instanceMetadataOptions": {
            "httpTokens": "required",
            "httpPutResponseHopLimit": 2
        },
        "tags": {
            "Environment": "test"
        }
    }
}
```

## See Also
<a name="API_GetInfrastructureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetInfrastructureConfiguration)
