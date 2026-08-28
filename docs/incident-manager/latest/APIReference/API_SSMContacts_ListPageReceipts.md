---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListPageReceipts.html
---

# ListPageReceipts
<a name="API_SSMContacts_ListPageReceipts"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists all of the engagements to contact channels that have been acknowledged.

## Request Syntax
<a name="API_SSMContacts_ListPageReceipts_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PageId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_ListPageReceipts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_SSMContacts_ListPageReceipts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPageReceipts-request-MaxResults"></a>
The maximum number of acknowledgements per page of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** [NextToken](#API_SSMContacts_ListPageReceipts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPageReceipts-request-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [PageId](#API_SSMContacts_ListPageReceipts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPageReceipts-request-PageId"></a>
The Amazon Resource Name (ARN) of the engagement to a specific contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_ListPageReceipts_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Receipts": [
      {
         "ContactChannelArn": "string",
         "ReceiptInfo": "string",
         "ReceiptTime": number,
         "ReceiptType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SSMContacts_ListPageReceipts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SSMContacts_ListPageReceipts_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListPageReceipts-response-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`

 ** [Receipts](#API_SSMContacts_ListPageReceipts_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListPageReceipts-response-Receipts"></a>
A list of each acknowledgement.
Type: Array of [Receipt](API_SSMContacts_Receipt.md) objects

## Errors
<a name="API_SSMContacts_ListPageReceipts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource that doesn't exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_SSMContacts_ListPageReceipts_Examples"></a>

### Example
<a name="API_SSMContacts_ListPageReceipts_Example_1"></a>

This example illustrates one usage of ListPageReceipts.

#### Sample Request
<a name="API_SSMContacts_ListPageReceipts_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.ListPageReceipts
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.list-page-receipts
X-Amz-Date: 20220816T223512Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220816/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 105

{
	"PageId": "arn:aws:ssm-contacts:us-east-2:111122223333:page/akuam/2f92b456-2350-442b-95e7-ed8b09c0b4ac"
}
```

#### Sample Response
<a name="API_SSMContacts_ListPageReceipts_Example_1_Response"></a>

```
{
    "Receipts": [
        {
            "ReceiptType": "READ",
            "ReceiptTime": "2022-08-16T19:11:58.746000+00:00"
        },
        {
            "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE",
            "ReceiptType": "SENT",
            "ReceiptTime": "2022-08-16T18:54:50.952000+00:00"
        },
        {
            "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE",
            "ReceiptType": "SENT",
            "ReceiptTime": "2022-08-16T18:57:52.058000+00:00"
        },
        {
            "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE",
            "ReceiptType": "SENT",
            "ReceiptTime": "2022-08-16T18:56:51.688000+00:00"
        },
        {
            "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE",
            "ReceiptType": "SENT",
            "ReceiptTime": "2022-08-16T18:55:51.265000+00:00"
        },
        {
            "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE",
            "ReceiptType": "SENT",
            "ReceiptTime": "2022-08-16T18:53:50.469000+00:00"
        }
    ]
}
```

## See Also
<a name="API_SSMContacts_ListPageReceipts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/ListPageReceipts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/ListPageReceipts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ListPageReceipts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/ListPageReceipts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ListPageReceipts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/ListPageReceipts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/ListPageReceipts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/ListPageReceipts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/ListPageReceipts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ListPageReceipts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
