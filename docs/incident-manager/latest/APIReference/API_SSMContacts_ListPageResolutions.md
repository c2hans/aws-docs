---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListPageResolutions.html
---

# ListPageResolutions
<a name="API_SSMContacts_ListPageResolutions"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Returns the resolution path of an engagement. For example, the escalation plan engaged in an incident might target an on-call schedule that includes several contacts in a rotation, but just one contact on-call when the incident starts. The resolution path indicates the hierarchy of *escalation plan > on-call schedule > contact*.

## Request Syntax
<a name="API_SSMContacts_ListPageResolutions_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "PageId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_ListPageResolutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_SSMContacts_ListPageResolutions_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPageResolutions-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [PageId](#API_SSMContacts_ListPageResolutions_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListPageResolutions-request-PageId"></a>
The Amazon Resource Name (ARN) of the contact engaged for the incident.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_ListPageResolutions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PageResolutions": [
      {
         "ContactArn": "string",
         "StageIndex": number,
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SSMContacts_ListPageResolutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SSMContacts_ListPageResolutions_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListPageResolutions-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`

 ** [PageResolutions](#API_SSMContacts_ListPageResolutions_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListPageResolutions-response-PageResolutions"></a>
Information about the resolution for an engagement.
Type: Array of [ResolutionContact](API_SSMContacts_ResolutionContact.md) objects

## Errors
<a name="API_SSMContacts_ListPageResolutions_Errors"></a>

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

## See Also
<a name="API_SSMContacts_ListPageResolutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/ListPageResolutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/ListPageResolutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ListPageResolutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/ListPageResolutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ListPageResolutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/ListPageResolutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/ListPageResolutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/ListPageResolutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/ListPageResolutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ListPageResolutions)
