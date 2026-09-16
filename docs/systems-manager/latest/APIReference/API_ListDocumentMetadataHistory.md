---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListDocumentMetadataHistory.html
---

# ListDocumentMetadataHistory
<a name="API_ListDocumentMetadataHistory"></a>

**Important**
 AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html).

Information about approval reviews for a version of a change template in Change Manager.

## Request Syntax
<a name="API_ListDocumentMetadataHistory_RequestSyntax"></a>

```
{
   "DocumentVersion": "{{string}}",
   "MaxResults": {{number}},
   "Metadata": "{{string}}",
   "Name": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDocumentMetadataHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentVersion](#API_ListDocumentMetadataHistory_RequestSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-request-DocumentVersion"></a>
The version of the change template.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [MaxResults](#API_ListDocumentMetadataHistory_RequestSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [Metadata](#API_ListDocumentMetadataHistory_RequestSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-request-Metadata"></a>
The type of data for which details are being requested. Currently, the only supported value is `DocumentReviews`.
Type: String
Valid Values: `DocumentReviews`
Required: Yes

 ** [Name](#API_ListDocumentMetadataHistory_RequestSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-request-Name"></a>
The name of the change template.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

 ** [NextToken](#API_ListDocumentMetadataHistory_RequestSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_ListDocumentMetadataHistory_ResponseSyntax"></a>

```
{
   "Author": "string",
   "DocumentVersion": "string",
   "Metadata": {
      "ReviewerResponse": [
         {
            "Comment": [
               {
                  "Content": "string",
                  "Type": "string"
               }
            ],
            "CreateTime": number,
            "Reviewer": "string",
            "ReviewStatus": "string",
            "UpdatedTime": number
         }
      ]
   },
   "Name": "string",
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDocumentMetadataHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Author](#API_ListDocumentMetadataHistory_ResponseSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-response-Author"></a>
The user ID of the person in the organization who requested the review of the change template.
Type: String

 ** [DocumentVersion](#API_ListDocumentMetadataHistory_ResponseSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-response-DocumentVersion"></a>
The version of the change template.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`

 ** [Metadata](#API_ListDocumentMetadataHistory_ResponseSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-response-Metadata"></a>
Information about the response to the change template approval request.
Type: [DocumentMetadataResponseInfo](API_DocumentMetadataResponseInfo.md) object

 ** [Name](#API_ListDocumentMetadataHistory_ResponseSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-response-Name"></a>
The name of the change template.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`

 ** [NextToken](#API_ListDocumentMetadataHistory_ResponseSyntax) **   <a name="systemsmanager-ListDocumentMetadataHistory-response-NextToken"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: String

## Errors
<a name="API_ListDocumentMetadataHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentVersion **
The document version isn't valid or doesn't exist.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_ListDocumentMetadataHistory_Examples"></a>

### Example
<a name="API_ListDocumentMetadataHistory_Example_1"></a>

This example illustrates one usage of ListDocumentMetadataHistory.

#### Sample Request
<a name="API_ListDocumentMetadataHistory_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListDocumentMetadataHistory
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240730T154930Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240730/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 68

{
    "Name": "MyChangeManagerTemplate",
    "Metadata": "DocumentReviews"
}
```

#### Sample Response
<a name="API_ListDocumentMetadataHistory_Example_1_Response"></a>

```
{
    "Name": "MyChangeManagerTemplate",
    "DocumentVersion": "1",
    "Author": "arn:aws:iam::111122223333:user/JohnDoe",
    "Metadata": {
        "ReviewerResponse": [
            {
                "CreateTime": "2024-07-30T11:58:28.025000-07:00",
                "UpdatedTime": "2024-07-30T12:01:19.274000-07:00",
                "ReviewStatus": "APPROVED",
                "Comment": [
                    {
                        "Type": "COMMENT",
                        "Content": "I approve this template version"
                    }
                ],
                "Reviewer": "arn:aws:iam::111122223333:user/ShirleyRodriguez"
            },
            {
                "CreateTime": "2024-07-30T11:58:28.025000-07:00",
                "UpdatedTime": "2024-07-30T11:58:28.025000-07:00",
                "ReviewStatus": "PENDING"
            }
        ]
    }
}
```

## See Also
<a name="API_ListDocumentMetadataHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListDocumentMetadataHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListDocumentMetadataHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListDocumentMetadataHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListDocumentMetadataHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListDocumentMetadataHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListDocumentMetadataHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListDocumentMetadataHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListDocumentMetadataHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListDocumentMetadataHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListDocumentMetadataHistory)
