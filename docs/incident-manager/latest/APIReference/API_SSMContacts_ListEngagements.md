---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListEngagements.html
---

# ListEngagements
<a name="API_SSMContacts_ListEngagements"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists all engagements that have happened in an incident.

## Request Syntax
<a name="API_SSMContacts_ListEngagements_RequestSyntax"></a>

```
{
   "IncidentId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TimeRangeValue": {
      "EndTime": {{number}},
      "StartTime": {{number}}
   }
}
```

## Request Parameters
<a name="API_SSMContacts_ListEngagements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IncidentId](#API_SSMContacts_ListEngagements_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListEngagements-request-IncidentId"></a>
The Amazon Resource Name (ARN) of the incident you're listing engagements for.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`
Required: No

 ** [MaxResults](#API_SSMContacts_ListEngagements_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListEngagements-request-MaxResults"></a>
The maximum number of engagements per page of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** [NextToken](#API_SSMContacts_ListEngagements_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListEngagements-request-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [TimeRangeValue](#API_SSMContacts_ListEngagements_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListEngagements-request-TimeRangeValue"></a>
The time range to lists engagements for an incident.
Type: [TimeRange](API_SSMContacts_TimeRange.md) object
Required: No

## Response Syntax
<a name="API_SSMContacts_ListEngagements_ResponseSyntax"></a>

```
{
   "Engagements": [
      {
         "ContactArn": "string",
         "EngagementArn": "string",
         "IncidentId": "string",
         "Sender": "string",
         "StartTime": number,
         "StopTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SSMContacts_ListEngagements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Engagements](#API_SSMContacts_ListEngagements_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListEngagements-response-Engagements"></a>
A list of each engagement that occurred during the specified time range of an incident.
Type: Array of [Engagement](API_SSMContacts_Engagement.md) objects

 ** [NextToken](#API_SSMContacts_ListEngagements_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListEngagements-response-NextToken"></a>
The pagination token to continue to the next page of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`

## Errors
<a name="API_SSMContacts_ListEngagements_Errors"></a>

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
<a name="API_SSMContacts_ListEngagements_Examples"></a>

### Example
<a name="API_SSMContacts_ListEngagements_Example_1"></a>

This example illustrates one usage of ListEngagements.

#### Sample Request
<a name="API_SSMContacts_ListEngagements_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.ListEngagements
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.list-engagements
X-Amz-Date: 20220816T191844Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220816/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2

{}
```

#### Sample Response
<a name="API_SSMContacts_ListEngagements_Example_1_Response"></a>

```
{
    "Engagements": [
        {
            "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/test_escalation_plan/27bd86cf-6d50-49d2-a9ab-da39bEXAMPLE",
            "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/test_escalation_plan",
            "Sender": "cli",
            "StartTime": "2022-08-16T18:48:50.153000+00:00"
        }
    ]
}
```

## See Also
<a name="API_SSMContacts_ListEngagements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/ListEngagements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/ListEngagements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ListEngagements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/ListEngagements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ListEngagements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/ListEngagements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/ListEngagements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/ListEngagements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/ListEngagements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ListEngagements)
