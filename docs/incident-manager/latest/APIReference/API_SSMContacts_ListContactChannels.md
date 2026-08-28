---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListContactChannels.html
---

# ListContactChannels
<a name="API_SSMContacts_ListContactChannels"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists all contact channels for the specified contact.

## Request Syntax
<a name="API_SSMContacts_ListContactChannels_RequestSyntax"></a>

```
{
   "ContactId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_ListContactChannels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactId](#API_SSMContacts_ListContactChannels_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListContactChannels-request-ContactId"></a>
The Amazon Resource Name (ARN) of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [MaxResults](#API_SSMContacts_ListContactChannels_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListContactChannels-request-MaxResults"></a>
The maximum number of contact channels per page.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** [NextToken](#API_SSMContacts_ListContactChannels_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListContactChannels-request-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

## Response Syntax
<a name="API_SSMContacts_ListContactChannels_ResponseSyntax"></a>

```
{
   "ContactChannels": [
      {
         "ActivationStatus": "string",
         "ContactArn": "string",
         "ContactChannelArn": "string",
         "DeliveryAddress": {
            "SimpleAddress": "string"
         },
         "Name": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SSMContacts_ListContactChannels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactChannels](#API_SSMContacts_ListContactChannels_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListContactChannels-response-ContactChannels"></a>
A list of contact channels related to the specified contact.
Type: Array of [ContactChannel](API_SSMContacts_ContactChannel.md) objects

 ** [NextToken](#API_SSMContacts_ListContactChannels_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListContactChannels-response-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`

## Errors
<a name="API_SSMContacts_ListContactChannels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 400

 ** DataEncryptionException **
The operation failed to due an encryption key error.
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
<a name="API_SSMContacts_ListContactChannels_Examples"></a>

### Example
<a name="API_SSMContacts_ListContactChannels_Example_1"></a>

This example illustrates one usage of ListContactChannels.

#### Sample Request
<a name="API_SSMContacts_ListContactChannels_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.ListContactChannels
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.list-contact-channels
X-Amz-Date: 20220812T180323Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220812/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 74

{
	"ContactId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam"
}
```

#### Sample Response
<a name="API_SSMContacts_ListContactChannels_Example_1_Response"></a>

```
{
    "ContactChannels": [
        {
            "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/31111aa5-9b84-4591-a5a6-5a8f9EXAMPLE",
            "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
            "Name": "akuas email-test",
            "Type": "EMAIL",
            "DeliveryAddress": {
                "SimpleAddress": "akuam@example.com"
            },
            "ActivationStatus": "ACTIVATED"
        },
        {
            "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE",
            "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
            "Name": "akuas sms-test",
            "Type": "SMS",
            "DeliveryAddress": {
                "SimpleAddress": "+15005550199"
            },
            "ActivationStatus": "ACTIVATED"
        }
    ]
}
```

## See Also
<a name="API_SSMContacts_ListContactChannels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/ListContactChannels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/ListContactChannels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ListContactChannels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/ListContactChannels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ListContactChannels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/ListContactChannels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/ListContactChannels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/ListContactChannels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/ListContactChannels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ListContactChannels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
