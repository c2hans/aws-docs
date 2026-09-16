---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_GetRotationOverride.html
---

# GetRotationOverride
<a name="API_SSMContacts_GetRotationOverride"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves information about an override to an on-call rotation.

## Request Syntax
<a name="API_SSMContacts_GetRotationOverride_RequestSyntax"></a>

```
{
   "RotationId": "{{string}}",
   "RotationOverrideId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_GetRotationOverride_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RotationId](#API_SSMContacts_GetRotationOverride_RequestSyntax) **   <a name="IncidentManager-SSMContacts_GetRotationOverride-request-RotationId"></a>
The Amazon Resource Name (ARN) of the overridden rotation to retrieve information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [RotationOverrideId](#API_SSMContacts_GetRotationOverride_RequestSyntax) **   <a name="IncidentManager-SSMContacts_GetRotationOverride-request-RotationOverrideId"></a>
The Amazon Resource Name (ARN) of the on-call rotation override to retrieve information about.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 39.
Pattern: `([a-fA-Z0-9]{8,11}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}){1}`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_GetRotationOverride_ResponseSyntax"></a>

```
{
   "CreateTime": number,
   "EndTime": number,
   "NewContactIds": [ "string" ],
   "RotationArn": "string",
   "RotationOverrideId": "string",
   "StartTime": number
}
```

## Response Elements
<a name="API_SSMContacts_GetRotationOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_SSMContacts_GetRotationOverride_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotationOverride-response-CreateTime"></a>
The date and time when the override was created.
Type: Timestamp

 ** [EndTime](#API_SSMContacts_GetRotationOverride_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotationOverride-response-EndTime"></a>
The date and time when the override ends.
Type: Timestamp

 ** [NewContactIds](#API_SSMContacts_GetRotationOverride_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotationOverride-response-NewContactIds"></a>
The Amazon Resource Names (ARNs) of the contacts assigned to the override of the on-call rotation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [RotationArn](#API_SSMContacts_GetRotationOverride_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotationOverride-response-RotationArn"></a>
The Amazon Resource Name (ARN) of the on-call rotation that was overridden.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [RotationOverrideId](#API_SSMContacts_GetRotationOverride_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotationOverride-response-RotationOverrideId"></a>
The Amazon Resource Name (ARN) of the override to an on-call rotation.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 39.
Pattern: `([a-fA-Z0-9]{8,11}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}){1}`

 ** [StartTime](#API_SSMContacts_GetRotationOverride_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetRotationOverride-response-StartTime"></a>
The date and time when the override goes into effect.
Type: Timestamp

## Errors
<a name="API_SSMContacts_GetRotationOverride_Errors"></a>

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
<a name="API_SSMContacts_GetRotationOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/GetRotationOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/GetRotationOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/GetRotationOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/GetRotationOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/GetRotationOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/GetRotationOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/GetRotationOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/GetRotationOverride)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/GetRotationOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/GetRotationOverride)
