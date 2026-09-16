---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListDocumentVersions.html
---

# ListDocumentVersions
<a name="API_ListDocumentVersions"></a>

List all versions for a document.

## Request Syntax
<a name="API_ListDocumentVersions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "Name": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDocumentVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDocumentVersions_RequestSyntax) **   <a name="systemsmanager-ListDocumentVersions-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [Name](#API_ListDocumentVersions_RequestSyntax) **   <a name="systemsmanager-ListDocumentVersions-request-Name"></a>
The name of the document. You can specify an Amazon Resource Name (ARN).
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** [NextToken](#API_ListDocumentVersions_RequestSyntax) **   <a name="systemsmanager-ListDocumentVersions-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_ListDocumentVersions_ResponseSyntax"></a>

```
{
   "DocumentVersions": [
      {
         "CreatedDate": number,
         "DisplayName": "string",
         "DocumentFormat": "string",
         "DocumentVersion": "string",
         "IsDefaultVersion": boolean,
         "Name": "string",
         "ReviewStatus": "string",
         "Status": "string",
         "StatusInformation": "string",
         "VersionName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDocumentVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DocumentVersions](#API_ListDocumentVersions_ResponseSyntax) **   <a name="systemsmanager-ListDocumentVersions-response-DocumentVersions"></a>
The document versions.
Type: Array of [DocumentVersionInfo](API_DocumentVersionInfo.md) objects
Array Members: Minimum number of 1 item.

 ** [NextToken](#API_ListDocumentVersions_ResponseSyntax) **   <a name="systemsmanager-ListDocumentVersions-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_ListDocumentVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_ListDocumentVersions_Examples"></a>

### Example
<a name="API_ListDocumentVersions_Example_1"></a>

This example illustrates one usage of ListDocumentVersions.

#### Sample Request
<a name="API_ListDocumentVersions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListDocumentVersions
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T151751Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 30

{
    "Name": "AWS-UpdateSSMAgent"
}
```

#### Sample Response
<a name="API_ListDocumentVersions_Example_1_Response"></a>

```
{
    "DocumentVersions": [
        {
            "CreatedDate": 1486594364.541,
            "DisplayName": "ExampleDoc",
            "DocumentFormat": "JSON",
            "DocumentVersion": "1",
            "IsDefaultVersion": true,
            "Name": "AWS-UpdateSSMAgent",
            "Status": "Active"
        }
    ]
}
```

## See Also
<a name="API_ListDocumentVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListDocumentVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListDocumentVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListDocumentVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListDocumentVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListDocumentVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListDocumentVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListDocumentVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListDocumentVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListDocumentVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListDocumentVersions)
