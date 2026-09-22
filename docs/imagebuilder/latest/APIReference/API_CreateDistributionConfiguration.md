---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateDistributionConfiguration.html
---

# CreateDistributionConfiguration
<a name="API_CreateDistributionConfiguration"></a>

Creates a new distribution configuration. Distribution configurations define and configure the outputs for your images, including the target Regions, accounts, and settings for each Region.

## Request Syntax
<a name="API_CreateDistributionConfiguration_RequestSyntax"></a>

```
PUT /CreateDistributionConfiguration HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
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
   ],
   "dryRun": {{boolean}},
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDistributionConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDistributionConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateDistributionConfiguration-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_CreateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateDistributionConfiguration-request-description"></a>
The description of the distribution configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [distributions](#API_CreateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateDistributionConfiguration-request-distributions"></a>
The distribution settings for the configuration. Each entry defines how output images are distributed in one target AWS Region. A Region can appear at most once in the list.
Type: Array of [Distribution](API_Distribution.md) objects
Required: Yes

 ** [dryRun](#API_CreateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateDistributionConfiguration-request-dryRun"></a>
Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a `DryRunOperationException` error response.
Type: Boolean
Required: No

 ** [name](#API_CreateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateDistributionConfiguration-request-name"></a>
The name of the distribution configuration. Distribution configuration names must be unique to your account in each AWS Region. Image Builder generates the distribution configuration ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [tags](#API_CreateDistributionConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateDistributionConfiguration-request-tags"></a>
The tags of the distribution configuration.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDistributionConfiguration_ResponseSyntax"></a>

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
<a name="API_CreateDistributionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateDistributionConfiguration_ResponseSyntax) **   <a name="imagebuilder-CreateDistributionConfiguration-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [distributionConfigurationArn](#API_CreateDistributionConfiguration_ResponseSyntax) **   <a name="imagebuilder-CreateDistributionConfiguration-response-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that was created by this request.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`

 ** [requestId](#API_CreateDistributionConfiguration_ResponseSyntax) **   <a name="imagebuilder-CreateDistributionConfiguration-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateDistributionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** DryRunOperationException **
The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.
HTTP Status Code: 412

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

 ** ResourceAlreadyExistsException **
The resource that you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded the number of permitted resources or operations for this service. For service quotas, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder).
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_CreateDistributionConfiguration_Examples"></a>

### Create a distribution configuration
<a name="API_CreateDistributionConfiguration_Example_1"></a>

The following example creates a distribution configuration that distributes the output AMI to two Regions. The AMI name includes the build date, so that repeated builds create unique AMI names.

#### Sample Request
<a name="API_CreateDistributionConfiguration_Example_1_Request"></a>

```
PUT /CreateDistributionConfiguration HTTP/1.1
Content-type: application/json

{
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
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444"
}
```

#### Sample Response
<a name="API_CreateDistributionConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "ca5312ad-a273-4c8c-817e-042941a5762d",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
    "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution"
}
```

### Create a distribution configuration with launch permissions and a launch template update
<a name="API_CreateDistributionConfiguration_Example_2"></a>

The following example creates a distribution configuration that distributes the output AMI to two Regions. In us-east-1, it shares the AMI with another AWS account. In us-west-2, it sets the new AMI as the default version of your launch template.

#### Sample Request
<a name="API_CreateDistributionConfiguration_Example_2_Request"></a>

```
PUT /CreateDistributionConfiguration HTTP/1.1
Content-type: application/json

{
    "name": "my-example-distribution",
    "description": "Distributes the output AMI to two Regions and shares it with another account",
    "distributions": [
        {
            "region": "us-west-2",
            "amiDistributionConfiguration": {
                "name": "my-example-image-{{ imagebuilder:buildDate }}"
            },
            "launchTemplateConfigurations": [
                {
                    "launchTemplateId": "lt-1234567890abcdef0",
                    "setDefaultVersion": true
                }
            ]
        },
        {
            "region": "us-east-1",
            "amiDistributionConfiguration": {
                "name": "my-example-image-{{ imagebuilder:buildDate }}",
                "launchPermission": {
                    "userIds": ["444455556666"]
                }
            }
        }
    ],
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE56789"
}
```

#### Sample Response
<a name="API_CreateDistributionConfiguration_Example_2_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "13c97ae8-8e39-4e12-af78-25e70def0933",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE56789",
    "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution"
}
```

## See Also
<a name="API_CreateDistributionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CreateDistributionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CreateDistributionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CreateDistributionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CreateDistributionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CreateDistributionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CreateDistributionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CreateDistributionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CreateDistributionConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateDistributionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateDistributionConfiguration)
