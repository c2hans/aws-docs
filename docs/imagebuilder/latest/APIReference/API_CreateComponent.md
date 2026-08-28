---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html
---

# CreateComponent
<a name="API_CreateComponent"></a>

Creates a new component that can be used to build, validate, test, and assess your image. The component is based on a YAML document that you specify using exactly one of the following methods:
+ Inline, using the `data` property in the request body.
+ A URL that points to a YAML document file stored in Amazon S3, using the `uri` property in the request body.

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
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
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
Validates the required permissions for the operation and the request parameters, without actually making the request, and provides an error response. Upon a successful request, the error response is `DryRunOperationException`.
Type: Boolean
Required: No

 ** [kmsKeyId](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-kmsKeyId"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [name](#API_CreateComponent_RequestSyntax) **   <a name="imagebuilder-CreateComponent-request-name"></a>
The name of the component.
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
 **Assignment:** For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.
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
The `uri` of a YAML component document file. This must be an S3 URL (`s3://bucket/key`), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.
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
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [latestVersionReferences](#API_CreateComponent_ResponseSyntax) **   <a name="imagebuilder-CreateComponent-response-latestVersionReferences"></a>
The resource ARNs with different wildcard variations of semantic versioning.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_CreateComponent_ResponseSyntax) **   <a name="imagebuilder-CreateComponent-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
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
You have specified two or more mutually exclusive parameters. Review the error message for details.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** InvalidVersionNumberException **
Your version number is out of bounds or does not follow the required syntax.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded the number of permitted resources or operations for this service. For service quotas, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder).
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

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
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
