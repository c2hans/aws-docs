---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListRotationOverrides.html
---

# ListRotationOverrides
<a name="API_SSMContacts_ListRotationOverrides"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves a list of overrides currently specified for an on-call rotation.

## Request Syntax
<a name="API_SSMContacts_ListRotationOverrides_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RotationId": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_SSMContacts_ListRotationOverrides_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndTime](#API_SSMContacts_ListRotationOverrides_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListRotationOverrides-request-EndTime"></a>
The date and time for the end of a time range for listing overrides.
Type: Timestamp
Required: Yes

 ** [MaxResults](#API_SSMContacts_ListRotationOverrides_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListRotationOverrides-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1024.
Required: No

 ** [NextToken](#API_SSMContacts_ListRotationOverrides_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListRotationOverrides-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [RotationId](#API_SSMContacts_ListRotationOverrides_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListRotationOverrides-request-RotationId"></a>
The Amazon Resource Name (ARN) of the rotation to retrieve information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [StartTime](#API_SSMContacts_ListRotationOverrides_RequestSyntax) **   <a name="IncidentManager-SSMContacts_ListRotationOverrides-request-StartTime"></a>
The date and time for the beginning of a time range for listing overrides.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_SSMContacts_ListRotationOverrides_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RotationOverrides": [
      {
         "CreateTime": number,
         "EndTime": number,
         "NewContactIds": [ "string" ],
         "RotationOverrideId": "string",
         "StartTime": number
      }
   ]
}
```

## Response Elements
<a name="API_SSMContacts_ListRotationOverrides_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SSMContacts_ListRotationOverrides_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListRotationOverrides-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`

 ** [RotationOverrides](#API_SSMContacts_ListRotationOverrides_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_ListRotationOverrides-response-RotationOverrides"></a>
A list of rotation overrides in the specified time range.
Type: Array of [RotationOverride](API_SSMContacts_RotationOverride.md) objects

## Errors
<a name="API_SSMContacts_ListRotationOverrides_Errors"></a>

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
<a name="API_SSMContacts_ListRotationOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/ListRotationOverrides)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/ListRotationOverrides)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ListRotationOverrides)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/ListRotationOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ListRotationOverrides)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/ListRotationOverrides)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/ListRotationOverrides)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/ListRotationOverrides)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/ListRotationOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ListRotationOverrides)
