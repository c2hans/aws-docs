---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html
---

# CreateComponent
<a name="API_CreateComponent"></a>

Creates a new component that can be used to build, validate, test, and assess your image. The component is based on a YAML document that you specify using exactly one of the following methods:
+ Inline, using the `data` property in the request body.
+ A URL that points to a YAML document file stored in Amazon S3, using the `uri` property in the request body.

Image Builder determines the component type from the document. If the document contains a single phase named `test`, the component type is `TEST`. Otherwise, the component type is `BUILD`.

## Request Syntax
<a name="API_CreateComponent_RequestSyntax"></a>

```
PUT /CreateComponent HTTP/1.1
Content-type: application/json

{
   "changeDescription": "{{string}}",
   "clientToken": "{{string}}",
   "data": "{{string}}",
   "description": "{{string}}",
   "dryRun": {{boolean}},
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "platform": "{{string}}",
   "semanticVersion": "{{string}}",
   "supportedOsVersions": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "uri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateComponent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateComponent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [changeDescription](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-changeDescription"></a>
The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [clientToken](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [data](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-data"></a>
Component `data` contains inline YAML document content for the component. Alternatively, you can specify the `uri` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16000.
Pattern: `[^\x00]+`
Required: No

 ** [description](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-description"></a>
Describes the contents of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [dryRun](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-dryRun"></a>
Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a `DryRunOperationException` error response.
Type: Boolean
Required: No

 ** [kmsKeyId](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-kmsKeyId"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*. If you don't specify a key, Image Builder encrypts the component data with a KMS key that Image Builder owns.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [name](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-name"></a>
The name of the component. Image Builder generates the component ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If a component with the same name and semantic version already exists in your account in the same AWS Region, the request creates a new build version for it. If the content is also identical to the latest build version, the request fails because the component already exists.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [platform](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-platform"></a>
The operating system platform of the component.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: Yes

 ** [semanticVersion](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-semanticVersion"></a>
The semantic version of the component. This version follows the semantic version syntax.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
 **Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: Yes

 ** [supportedOsVersions](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-supportedOsVersions"></a>
The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1.
Required: No

 ** [tags](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-tags"></a>
The tags that apply to the component.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [uri](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-uri"></a>
The `uri` of a YAML component document file. This must be an S3 URL (`s3://bucket/key`), and you must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota for component size, which is 64 KB by default.
Alternatively, you can specify the YAML document inline, using the component `data` property. You cannot specify both properties.
Type: String
Required: No

## Response Syntax
<a name="API_CreateComponent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "componentBuildVersionArn": "string",
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
<a name="API_CreateComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateComponent_ResponseSyntax) **   <a name="imagebuilder-CreateComponent-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [componentBuildVersionArn](#API_CreateComponent_ResponseSyntax) **   <a name="imagebuilder-CreateComponent-response-componentBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the component that the request created.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [latestVersionReferences](#API_CreateComponent_ResponseSyntax) **   <a name="imagebuilder-CreateComponent-response-latestVersionReferences"></a>
A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_CreateComponent_ResponseSyntax) **   <a name="imagebuilder-CreateComponent-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateComponent_Errors"></a>

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

 ** InvalidVersionNumberException **
Your version number is out of bounds or does not follow the required syntax.
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
<a name="API_CreateComponent_Examples"></a>

### Create a component from an inline document
<a name="API_CreateComponent_Example_1"></a>

The following example creates a build component from a YAML document provided inline in the request.

#### Sample Request
<a name="API_CreateComponent_Example_1_Request"></a>

```
PUT /CreateComponent HTTP/1.1
Content-type: application/json

{
    "name": "my-example-component",
    "semanticVersion": "1.0.0",
    "description": "Installs the latest version of my application",
    "platform": "Linux",
    "data": "name: InstallMyApp\ndescription: Installs my application\nschemaVersion: 1.0\nphases:\n  - name: build\n    steps:\n      - name: InstallApp\n        action: ExecuteBash\n        inputs:\n          commands:\n            - sudo yum -y install my-app\n",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

#### Sample Response
<a name="API_CreateComponent_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "e769f240-fb6a-4253-88d1-20a80cbe787d",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "componentBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/1",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0"
    }
}
```

### Create a component from a document stored in Amazon S3
<a name="API_CreateComponent_Example_2"></a>

The following example creates a component from a YAML definition document that's stored in an Amazon S3 bucket. The definition document for this component includes an `AppVersion` parameter that recipes can set when they include the component.

#### Sample Request
<a name="API_CreateComponent_Example_2_Request"></a>

```
PUT /CreateComponent HTTP/1.1
Content-type: application/json

{
    "name": "my-example-parameterized-component",
    "semanticVersion": "1.0.0",
    "description": "Installs a configurable version of my application",
    "platform": "Linux",
    "uri": "s3://amzn-s3-demo-bucket/components/install-my-app.yaml",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE10101"
}
```

#### Sample Response
<a name="API_CreateComponent_Example_2_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "0cec8e32-a5c6-4aeb-ac3a-6471c8a2a8a9",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE10101",
    "componentBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-parameterized-component/1.0.0/1",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-parameterized-component/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-parameterized-component/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-parameterized-component/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-parameterized-component/1.0.0"
    }
}
```

## See Also
<a name="API_CreateComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateComponent)
