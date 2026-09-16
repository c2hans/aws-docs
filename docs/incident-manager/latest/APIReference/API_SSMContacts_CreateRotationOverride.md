---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_CreateRotationOverride.html
---

# CreateRotationOverride
<a name="API_SSMContacts_CreateRotationOverride"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Creates an override for a rotation in an on-call schedule.

## Request Syntax
<a name="API_SSMContacts_CreateRotationOverride_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "IdempotencyToken": "{{string}}",
   "NewContactIds": [ "{{string}}" ],
   "RotationId": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_SSMContacts_CreateRotationOverride_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndTime](#API_SSMContacts_CreateRotationOverride_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotationOverride-request-EndTime"></a>
The date and time when the override ends.
Type: Timestamp
Required: Yes

 ** [IdempotencyToken](#API_SSMContacts_CreateRotationOverride_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotationOverride-request-IdempotencyToken"></a>
A token that ensures that the operation is called only once with the specified details.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [NewContactIds](#API_SSMContacts_CreateRotationOverride_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotationOverride-request-NewContactIds"></a>
The Amazon Resource Names (ARNs) of the contacts to replace those in the current on-call rotation with.
If you want to include any current team members in the override shift, you must include their ARNs in the new contact ID list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [RotationId](#API_SSMContacts_CreateRotationOverride_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotationOverride-request-RotationId"></a>
The Amazon Resource Name (ARN) of the rotation to create an override for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [StartTime](#API_SSMContacts_CreateRotationOverride_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotationOverride-request-StartTime"></a>
The date and time when the override goes into effect.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_SSMContacts_CreateRotationOverride_ResponseSyntax"></a>

```
{
   "RotationOverrideId": "string"
}
```

## Response Elements
<a name="API_SSMContacts_CreateRotationOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RotationOverrideId](#API_SSMContacts_CreateRotationOverride_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_CreateRotationOverride-response-RotationOverrideId"></a>
The Amazon Resource Name (ARN) of the created rotation override.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 39.
Pattern: `([a-fA-Z0-9]{8,11}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}){1}`

## Errors
<a name="API_SSMContacts_CreateRotationOverride_Errors"></a>

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

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_SSMContacts_CreateRotationOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/CreateRotationOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/CreateRotationOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/CreateRotationOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/CreateRotationOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/CreateRotationOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/CreateRotationOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/CreateRotationOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/CreateRotationOverride)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/CreateRotationOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/CreateRotationOverride)
