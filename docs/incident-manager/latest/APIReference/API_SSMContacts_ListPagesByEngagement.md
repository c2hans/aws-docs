---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListPagesByEngagement.html
---

# ListPagesByEngagement
<a name="API_SSMContacts_ListPagesByEngagement"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists the engagements to contact channels that occurred by engaging a contact.

## Request Syntax
<a name="API_SSMContacts_ListPagesByEngagement_RequestSyntax"></a>

```
{
   "EngagementId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_ListPagesByEngagement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EngagementId](#API_SSMContacts_ListPagesByEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPagesByEngagement-request-EngagementId"></a>
The Amazon Resource Name (ARN) of the engagement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [MaxResults](#API_SSMContacts_ListPagesByEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPagesByEngagement-request-MaxResults"></a>
The maximum number of engagements to contact channels to list per page of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** [NextToken](#API_SSMContacts_ListPagesByEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPagesByEngagement-request-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

## Response Syntax
<a name="API_SSMContacts_ListPagesByEngagement_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Pages": [
      {
         "ContactArn": "string",
         "DeliveryTime": number,
         "EngagementArn": "string",
         "IncidentId": "string",
         "PageArn": "string",
         "ReadTime": number,
         "Sender": "string",
         "SentTime": number
      }
   ]
}
```

## Response Elements
<a name="API_SSMContacts_ListPagesByEngagement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SSMContacts_ListPagesByEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListPagesByEngagement-response-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`

 ** [Pages](#API_SSMContacts_ListPagesByEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListPagesByEngagement-response-Pages"></a>
The list of engagements to contact channels.
Type: Array of [Page](API_SSMContacts_Page.md) objects

## Errors
<a name="API_SSMContacts_ListPagesByEngagement_Errors"></a>

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
<a name="API_SSMContacts_ListPagesByEngagement_Examples"></a>

### Example
<a name="API_SSMContacts_ListPagesByEngagement_Example_1"></a>

This example illustrates one usage of ListPagesByEngagement.

#### Sample Request
<a name="API_SSMContacts_ListPagesByEngagement_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.ListPagesByEngagement
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.list-pages-by-engagement
X-Amz-Date: 20220817T181950Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220817/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 132

{
	"EngagementId": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/test_escalation_plan/27bd86cf-6d50-49d2-a9ab-da39bEXAMPLE"
}
```

#### Sample Response
<a name="API_SSMContacts_ListPagesByEngagement_Example_1_Response"></a>

```
{
    "Pages": [
        {
            "PageArn": "arn:aws:ssm-contacts:us-east-2:111122223333:page/akuam/2f92b456-2350-442b-95e7-ed8b0EXAMPLE",
            "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/test_escalation_plan/27bd86cf-6d50-49d2-a9ab-da39bEXAMPLE",
            "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
            "Sender": "cli",
            "SentTime": "2022-08-16T18:57:52.058000+00:00",
            "ReadTime": "2022-08-16T19:11:58.746000+00:00"
        }
    ]
}
```

## See Also
<a name="API_SSMContacts_ListPagesByEngagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/ListPagesByEngagement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/ListPagesByEngagement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ListPagesByEngagement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/ListPagesByEngagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ListPagesByEngagement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/ListPagesByEngagement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/ListPagesByEngagement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/ListPagesByEngagement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/ListPagesByEngagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ListPagesByEngagement)
