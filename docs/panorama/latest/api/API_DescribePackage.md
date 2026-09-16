---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_DescribePackage.html
---

# DescribePackage
<a name="API_DescribePackage"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns information about a package.

## Request Syntax
<a name="API_DescribePackage_RequestSyntax"></a>

```
GET /packages/metadata/{{PackageId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PackageId](#API_DescribePackage_RequestSyntax) **   <a name="panorama-DescribePackage-request-uri-PackageId"></a>
The package's ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\/]+`
Required: Yes

## Request Body
<a name="API_DescribePackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedTime": number,
   "PackageId": "string",
   "PackageName": "string",
   "ReadAccessPrincipalArns": [ "string" ],
   "StorageLocation": {
      "BinaryPrefixLocation": "string",
      "Bucket": "string",
      "GeneratedPrefixLocation": "string",
      "ManifestPrefixLocation": "string",
      "RepoPrefixLocation": "string"
   },
   "Tags": {
      "string" : "string"
   },
   "WriteAccessPrincipalArns": [ "string" ]
}
```

## Response Elements
<a name="API_DescribePackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribePackage_ResponseSyntax) **   <a name="panorama-DescribePackage-response-Arn"></a>
The package's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [CreatedTime](#API_DescribePackage_ResponseSyntax) **   <a name="panorama-DescribePackage-response-CreatedTime"></a>
When the package was created.
Type: Timestamp

 ** [PackageId](#API_DescribePackage_ResponseSyntax) **   <a name="panorama-DescribePackage-response-PackageId"></a>
The package's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\/]+`

 ** [PackageName](#API_DescribePackage_ResponseSyntax) **   <a name="panorama-DescribePackage-response-PackageName"></a>
The package's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [ReadAccessPrincipalArns](#API_DescribePackage_ResponseSyntax) **   <a name="panorama-DescribePackage-response-ReadAccessPrincipalArns"></a>
ARNs of accounts that have read access to the package.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:[a-z0-9][-.a-z0-9]{0,62}:iam::[0-9]{12}:[a-zA-Z0-9+=,.@\-_/]+`

 ** [StorageLocation](#API_DescribePackage_ResponseSyntax) **   <a name="panorama-DescribePackage-response-StorageLocation"></a>
The package's storage location.
Type: [StorageLocation](API_StorageLocation.md) object

 ** [Tags](#API_DescribePackage_ResponseSyntax) **   <a name="panorama-DescribePackage-response-Tags"></a>
The package's tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`

 ** [WriteAccessPrincipalArns](#API_DescribePackage_ResponseSyntax) **   <a name="panorama-DescribePackage-response-WriteAccessPrincipalArns"></a>
ARNs of accounts that have write access to the package.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:[a-z0-9][-.a-z0-9]{0,62}:iam::[0-9]{12}:[a-zA-Z0-9+=,.@\-_/]+`

## Errors
<a name="API_DescribePackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** ConflictException **
The target resource is in use.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 404

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_DescribePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/DescribePackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/DescribePackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/DescribePackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/DescribePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/DescribePackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/DescribePackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/DescribePackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/DescribePackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/DescribePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/DescribePackage)
