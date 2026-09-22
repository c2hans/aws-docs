---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImageRecipe.html
---

# CreateImageRecipe
<a name="API_CreateImageRecipe"></a>

Creates a new image recipe. Image recipes define how images are configured, tested, and assessed.

## Request Syntax
<a name="API_CreateImageRecipe_RequestSyntax"></a>

```
PUT /CreateImageRecipe HTTP/1.1
Content-type: application/json

{
   "additionalInstanceConfiguration": {
      "systemsManagerAgent": {
         "uninstallAfterBuild": {{boolean}}
      },
      "userDataOverride": "{{string}}"
   },
   "amiTags": {
      "{{string}}" : "{{string}}"
   },
   "amiWatermarks": [ "{{string}}" ],
   "blockDeviceMappings": [
      {
         "deviceName": "{{string}}",
         "ebs": {
            "deleteOnTermination": {{boolean}},
            "encrypted": {{boolean}},
            "iops": {{number}},
            "kmsKeyId": "{{string}}",
            "snapshotId": "{{string}}",
            "throughput": {{number}},
            "volumeSize": {{number}},
            "volumeType": "{{string}}"
         },
         "noDevice": "{{string}}",
         "virtualName": "{{string}}"
      }
   ],
   "clientToken": "{{string}}",
   "components": [
      {
         "componentArn": "{{string}}",
         "parameters": [
            {
               "name": "{{string}}",
               "value": [ "{{string}}" ]
            }
         ]
      }
   ],
   "description": "{{string}}",
   "dryRun": {{boolean}},
   "name": "{{string}}",
   "parentImage": "{{string}}",
   "semanticVersion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "workingDirectory": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateImageRecipe_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateImageRecipe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalInstanceConfiguration](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-additionalInstanceConfiguration"></a>
The additional settings and launch scripts for your build instances.
Type: [AdditionalInstanceConfiguration](API_AdditionalInstanceConfiguration.md) object
Required: No

 ** [amiTags](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-amiTags"></a>
Tags that are applied to the AMI that Image Builder creates during the Build phase prior to image distribution.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [amiWatermarks](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-amiWatermarks"></a>
The AMI watermark names to attach to the output AMI from this recipe. AMI watermarks are lineage markers. They automatically propagate to derivative AMIs when the source AMI is copied or distributed across Regions or accounts.
AMI watermarks are supported only for image recipes. AMIs with watermarks cannot be made public.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[A-Za-z0-9()\[\]./'@_\-][A-Za-z0-9 ()\[\]./'@_\-]{1,126}[A-Za-z0-9()\[\]./'@_\-]$`
Required: No

 ** [blockDeviceMappings](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-blockDeviceMappings"></a>
The block device mappings that Image Builder applies to the build instance and the output AMI. For example, you can override the size of the base image's root volume or attach additional EBS volumes.
Type: Array of [InstanceBlockDeviceMapping](API_InstanceBlockDeviceMapping.md) objects
Required: No

 ** [clientToken](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [components](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-components"></a>
The components included in the image recipe. Components are optional. A recipe with no components bakes the base image without additional customization. You can specify each component only one time in a recipe. Components with a status of `DEPRECATED` or `DISABLED` can't be added to new recipes.
Type: Array of [ComponentConfiguration](API_ComponentConfiguration.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [description](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-description"></a>
The description of the image recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [dryRun](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-dryRun"></a>
Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a `DryRunOperationException` error response.
Type: Boolean
Required: No

 ** [name](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-name"></a>
The name of the image recipe. The recipe name, combined with the semantic version, must be unique to your account in each AWS Region. Image Builder generates the image recipe ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [parentImage](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-parentImage"></a>
The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:
+ AMI ID
+ Image Builder image Amazon Resource Name (ARN)
+  AWS Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:`, followed by the parameter name or ARN.
+  AWS Marketplace product ID
If you enter an AMI ID or an SSM parameter that contains the AMI ID, you must have access to the AMI. The AMI must also be in the Region where you're creating the recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [semanticVersion](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-semanticVersion"></a>
The semantic version of the image recipe. This version follows the semantic version syntax.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
 **Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
Type: String
Pattern: `^(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: Yes

 ** [tags](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-tags"></a>
The tags of the image recipe.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [workingDirectory](#API_CreateImageRecipe_RequestSyntax) **   <a name="imagebuilder-CreateImageRecipe-request-workingDirectory"></a>
The working directory used during build and test workflows. If you don't specify a working directory, Image Builder uses `/tmp` for Linux and macOS build instances, and `C:/` for Windows build instances.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_CreateImageRecipe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "imageRecipeArn": "string",
   "latestVersionReferences": {
      "latestMajorVersionArn": "string",
      "latestMinorVersionArn": "string",
      "latestPatchVersionArn": "string",
      "latestVersionArn": "string"
   },
   "requestId": "string"
}
```

## Response Elements
<a name="API_CreateImageRecipe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateImageRecipe_ResponseSyntax) **   <a name="imagebuilder-CreateImageRecipe-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [imageRecipeArn](#API_CreateImageRecipe_ResponseSyntax) **   <a name="imagebuilder-CreateImageRecipe-response-imageRecipeArn"></a>
The Amazon Resource Name (ARN) of the image recipe that was created by this request.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`

 ** [latestVersionReferences](#API_CreateImageRecipe_ResponseSyntax) **   <a name="imagebuilder-CreateImageRecipe-response-latestVersionReferences"></a>
A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_CreateImageRecipe_ResponseSyntax) **   <a name="imagebuilder-CreateImageRecipe-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateImageRecipe_Errors"></a>

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

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** InvalidVersionNumberException **
Your version number is out of bounds or does not follow the required syntax.
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
<a name="API_CreateImageRecipe_Examples"></a>

### Create an image recipe
<a name="API_CreateImageRecipe_Example_1"></a>

The following example creates an image recipe that applies a custom component on top of the latest Amazon Linux 2023 base image.

#### Sample Request
<a name="API_CreateImageRecipe_Example_1_Request"></a>

```
PUT /CreateImageRecipe HTTP/1.1
Content-type: application/json

{
    "name": "my-example-recipe",
    "semanticVersion": "1.0.0",
    "description": "An image recipe that installs my application on Amazon Linux 2023",
    "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/amazon-linux-2023-x86/x.x.x",
    "components": [
        {
            "componentArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/1"
        }
    ],
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
}
```

#### Sample Response
<a name="API_CreateImageRecipe_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "89f4af2f-4f28-45e6-a9d8-abeba591df6a",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0"
    }
}
```

### Create an image recipe with component parameters and block device mappings
<a name="API_CreateImageRecipe_Example_2"></a>

The following example creates an image recipe that configures its components and storage. The `AppVersion` component parameter selects the application version to install. The block device mapping increases the root volume to an encrypted 30 GiB gp3 volume.

#### Sample Request
<a name="API_CreateImageRecipe_Example_2_Request"></a>

```
PUT /CreateImageRecipe HTTP/1.1
Content-type: application/json

{
    "name": "my-example-recipe",
    "semanticVersion": "1.1.0",
    "description": "Installs a specific version of my application on Amazon Linux 2023 with a larger encrypted root volume",
    "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/amazon-linux-2023-x86/x.x.x",
    "components": [
        {
            "componentArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-parameterized-component/1.0.0/1",
            "parameters": [
                {
                    "name": "AppVersion",
                    "value": ["2.5.0"]
                }
            ]
        }
    ],
    "blockDeviceMappings": [
        {
            "deviceName": "/dev/xvda",
            "ebs": {
                "volumeSize": 30,
                "volumeType": "gp3",
                "encrypted": true,
                "deleteOnTermination": true
            }
        }
    ],
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE20202"
}
```

#### Sample Response
<a name="API_CreateImageRecipe_Example_2_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "e3bdc054-d12e-4578-a847-68a18da724ca",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE20202",
    "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.1.0",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.1.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.1.0"
    }
}
```

## See Also
<a name="API_CreateImageRecipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CreateImageRecipe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CreateImageRecipe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CreateImageRecipe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CreateImageRecipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CreateImageRecipe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CreateImageRecipe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CreateImageRecipe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CreateImageRecipe)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateImageRecipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateImageRecipe)
