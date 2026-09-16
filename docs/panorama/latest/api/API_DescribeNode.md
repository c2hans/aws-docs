---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_DescribeNode.html
---

# DescribeNode
<a name="API_DescribeNode"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns information about a node.

## Request Syntax
<a name="API_DescribeNode_RequestSyntax"></a>

```
GET /nodes/{{NodeId}}?OwnerAccount={{OwnerAccount}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeNode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NodeId](#API_DescribeNode_RequestSyntax) **   <a name="panorama-DescribeNode-request-uri-NodeId"></a>
The node's ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: Yes

 ** [OwnerAccount](#API_DescribeNode_RequestSyntax) **   <a name="panorama-DescribeNode-request-uri-OwnerAccount"></a>
The account ID of the node's owner.
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9a-z\_]+`

## Request Body
<a name="API_DescribeNode_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeNode_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssetName": "string",
   "Category": "string",
   "CreatedTime": number,
   "Description": "string",
   "LastUpdatedTime": number,
   "Name": "string",
   "NodeId": "string",
   "NodeInterface": {
      "Inputs": [
         {
            "DefaultValue": "string",
            "Description": "string",
            "MaxConnections": number,
            "Name": "string",
            "Type": "string"
         }
      ],
      "Outputs": [
         {
            "Description": "string",
            "Name": "string",
            "Type": "string"
         }
      ]
   },
   "OwnerAccount": "string",
   "PackageArn": "string",
   "PackageId": "string",
   "PackageName": "string",
   "PackageVersion": "string",
   "PatchVersion": "string"
}
```

## Response Elements
<a name="API_DescribeNode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssetName](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-AssetName"></a>
The node's asset name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [Category](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-Category"></a>
The node's category.
Type: String
Valid Values: `BUSINESS_LOGIC | ML_MODEL | MEDIA_SOURCE | MEDIA_SINK`

 ** [CreatedTime](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-CreatedTime"></a>
When the node was created.
Type: Timestamp

 ** [Description](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-Description"></a>
The node's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [LastUpdatedTime](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-LastUpdatedTime"></a>
When the node was updated.
Type: Timestamp

 ** [Name](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-Name"></a>
The node's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [NodeId](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-NodeId"></a>
The node's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\.]+`

 ** [NodeInterface](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-NodeInterface"></a>
The node's interface.
Type: [NodeInterface](API_NodeInterface.md) object

 ** [OwnerAccount](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-OwnerAccount"></a>
The account ID of the node's owner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9a-z\_]+`

 ** [PackageArn](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-PackageArn"></a>
The node's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [PackageId](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-PackageId"></a>
The node's package ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\/]+`

 ** [PackageName](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-PackageName"></a>
The node's package name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [PackageVersion](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-PackageVersion"></a>
The node's package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`

 ** [PatchVersion](#API_DescribeNode_ResponseSyntax) **   <a name="panorama-DescribeNode-response-PatchVersion"></a>
The node's patch version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9]+`

## Errors
<a name="API_DescribeNode_Errors"></a>

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
<a name="API_DescribeNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/DescribeNode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/DescribeNode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/DescribeNode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/DescribeNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/DescribeNode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/DescribeNode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/DescribeNode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/DescribeNode)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/DescribeNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/DescribeNode)
