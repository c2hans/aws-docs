---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListContacts.html
---

# ListContacts
<a name="API_SSMContacts_ListContacts"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists all contacts and escalation plans in Incident Manager.

## Request Syntax
<a name="API_SSMContacts_ListContacts_RequestSyntax"></a>

```
{
   "AliasPrefix": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_ListContacts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AliasPrefix](#API_SSMContacts_ListContacts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListContacts-request-AliasPrefix"></a>
Used to list only contacts who's aliases start with the specified prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-z0-9_\-]*$`
Required: No

 ** [MaxResults](#API_SSMContacts_ListContacts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListContacts-request-MaxResults"></a>
The maximum number of contacts and escalation plans per page of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** [NextToken](#API_SSMContacts_ListContacts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListContacts-request-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [Type](#API_SSMContacts_ListContacts_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListContacts-request-Type"></a>
The type of contact.
Type: String
Valid Values: `PERSONAL | ESCALATION | ONCALL_SCHEDULE`
Required: No

## Response Syntax
<a name="API_SSMContacts_ListContacts_ResponseSyntax"></a>

```
{
   "Contacts": [
      {
         "Alias": "string",
         "ContactArn": "string",
         "DisplayName": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SSMContacts_ListContacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Contacts](#API_SSMContacts_ListContacts_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListContacts-response-Contacts"></a>
A list of the contacts and escalation plans in your Incident Manager account.
Type: Array of [Contact](API_SSMContacts_Contact.md) objects

 ** [NextToken](#API_SSMContacts_ListContacts_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListContacts-response-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`

## Errors
<a name="API_SSMContacts_ListContacts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_SSMContacts_ListContacts_Examples"></a>

### Example
<a name="API_SSMContacts_ListContacts_Example_1"></a>

This example illustrates one usage of ListContacts.

#### Sample Request
<a name="API_SSMContacts_ListContacts_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.ListContacts
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.list-contacts
X-Amz-Date: 20220816T215005Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220816/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2

{}
```

#### Sample Response
<a name="API_SSMContacts_ListContacts_Example_1_Response"></a>

```
{
    "Contacts": [
        {
            "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
            "Alias": "akuam",
            "DisplayName": "Akua Mansa",
            "Type": "PERSONAL"
        },
        {
            "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/test_escalation_plan",
            "Alias": "test_escalation_plan",
            "DisplayName": "Test Escalation Plan",
            "Type": "ESCALATION"
        }
    ]
}
```

## See Also
<a name="API_SSMContacts_ListContacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/ListContacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/ListContacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ListContacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/ListContacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ListContacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/ListContacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/ListContacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/ListContacts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/ListContacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ListContacts)
