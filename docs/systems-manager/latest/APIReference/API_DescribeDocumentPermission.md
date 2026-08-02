---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeDocumentPermission.html
---

# DescribeDocumentPermission
<a name="API_DescribeDocumentPermission"></a>

Describes the permissions for a AWS Systems Manager document (SSM document). If you created the document, you are the owner. If a document is shared, it can either be shared privately (by specifying a user's AWS account ID) or publicly (*All*).

## Request Syntax
<a name="API_DescribeDocumentPermission_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "Name": "{{string}}",
   "NextToken": "{{string}}",
   "PermissionType": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDocumentPermission_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeDocumentPermission_RequestSyntax) **   <a name="systemsmanager-DescribeDocumentPermission-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [Name](#API_DescribeDocumentPermission_RequestSyntax) **   <a name="systemsmanager-DescribeDocumentPermission-request-Name"></a>
The name of the document for which you are the owner.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

 ** [NextToken](#API_DescribeDocumentPermission_RequestSyntax) **   <a name="systemsmanager-DescribeDocumentPermission-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [PermissionType](#API_DescribeDocumentPermission_RequestSyntax) **   <a name="systemsmanager-DescribeDocumentPermission-request-PermissionType"></a>
The permission type for the document. The permission type can be *Share*.
Type: String
Valid Values: `Share`
Required: Yes

## Response Syntax
<a name="API_DescribeDocumentPermission_ResponseSyntax"></a>

```
{
   "AccountIds": [ "string" ],
   "AccountSharingInfoList": [
      {
         "AccountId": "string",
         "SharedDocumentVersion": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDocumentPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountIds](#API_DescribeDocumentPermission_ResponseSyntax) **   <a name="systemsmanager-DescribeDocumentPermission-response-AccountIds"></a>
The account IDs that have permission to use this document. The ID can be either an AWS account number or `all`.
Type: Array of strings
Array Members: Maximum number of 20 items.
Pattern: `(?i)all|[0-9]{12}`

 ** [AccountSharingInfoList](#API_DescribeDocumentPermission_ResponseSyntax) **   <a name="systemsmanager-DescribeDocumentPermission-response-AccountSharingInfoList"></a>
A list of AWS accounts where the current document is shared and the version shared with each account.
Type: Array of [AccountSharingInfo](API_AccountSharingInfo.md) objects

 ** [NextToken](#API_DescribeDocumentPermission_ResponseSyntax) **   <a name="systemsmanager-DescribeDocumentPermission-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_DescribeDocumentPermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentOperation **
You attempted to delete a document while it is still shared. You must stop sharing the document before you can delete it.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

 ** InvalidPermissionType **
The permission type isn't supported. *Share* is the only supported permission type.
HTTP Status Code: 400

## Examples
<a name="API_DescribeDocumentPermission_Examples"></a>

### Example
<a name="API_DescribeDocumentPermission_Example_1"></a>

This example illustrates one usage of DescribeDocumentPermission.

#### Sample Request
<a name="API_DescribeDocumentPermission_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeDocumentPermission
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T182653Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 50

{
    "Name": "Example",
    "PermissionType": "Share"
}
```

#### Sample Response
<a name="API_DescribeDocumentPermission_Example_1_Response"></a>

```
{
    "AccountIds": [],
    "AccountSharingInfoList": []
}
```

## See Also
<a name="API_DescribeDocumentPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeDocumentPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeDocumentPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeDocumentPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeDocumentPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeDocumentPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeDocumentPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeDocumentPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeDocumentPermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeDocumentPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeDocumentPermission)
