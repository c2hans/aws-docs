---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_UpdateRelationship.html
---

# UpdateRelationship
<a name="API_channel_UpdateRelationship"></a>

Updates the properties of a partner relationship.

## Request Syntax
<a name="API_channel_UpdateRelationship_RequestSyntax"></a>

```
{
   "catalog": "{{string}}",
   "displayName": "{{string}}",
   "identifier": "{{string}}",
   "programManagementAccountIdentifier": "{{string}}",
   "requestedSupportPlan": { ... },
   "revision": "{{string}}"
}
```

## Request Parameters
<a name="API_channel_UpdateRelationship_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [catalog](#API_channel_UpdateRelationship_RequestSyntax) **   <a name="AWSPartnerCentral-channel_UpdateRelationship-request-catalog"></a>
The catalog identifier for the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: Yes

 ** [identifier](#API_channel_UpdateRelationship_RequestSyntax) **   <a name="AWSPartnerCentral-channel_UpdateRelationship-request-identifier"></a>
The unique identifier of the relationship to update.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/pma-[a-z0-9]{13}/relationship/)?rs-[a-z0-9]{13}`
Required: Yes

 ** [programManagementAccountIdentifier](#API_channel_UpdateRelationship_RequestSyntax) **   <a name="AWSPartnerCentral-channel_UpdateRelationship-request-programManagementAccountIdentifier"></a>
The identifier of the program management account associated with the relationship.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/)?pma-[a-z0-9]{13}`
Required: Yes

 ** [displayName](#API_channel_UpdateRelationship_RequestSyntax) **   <a name="AWSPartnerCentral-channel_UpdateRelationship-request-displayName"></a>
The new display name for the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** [requestedSupportPlan](#API_channel_UpdateRelationship_RequestSyntax) **   <a name="AWSPartnerCentral-channel_UpdateRelationship-request-requestedSupportPlan"></a>
The updated support plan for the relationship.
Type: [SupportPlan](API_channel_SupportPlan.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [revision](#API_channel_UpdateRelationship_RequestSyntax) **   <a name="AWSPartnerCentral-channel_UpdateRelationship-request-revision"></a>
The current revision number of the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]*`
Required: No

## Response Syntax
<a name="API_channel_UpdateRelationship_ResponseSyntax"></a>

```
{
   "relationshipDetail": {
      "arn": "string",
      "displayName": "string",
      "id": "string",
      "revision": "string"
   }
}
```

## Response Elements
<a name="API_channel_UpdateRelationship_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [relationshipDetail](#API_channel_UpdateRelationship_ResponseSyntax) **   <a name="AWSPartnerCentral-channel_UpdateRelationship-response-relationshipDetail"></a>
Details of the updated relationship.
Type: [UpdateRelationshipDetail](API_channel_UpdateRelationshipDetail.md) object

## Errors
<a name="API_channel_UpdateRelationship_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** message **
A message describing the access denial.
 ** reason **
The reason for the access denial.
HTTP Status Code: 400

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** message **
A message describing the conflict.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
 ** message **
A message describing the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** message **
A message describing the resource not found error.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to too many requests being sent in a short period.
 ** message **
A message describing the throttling error.
 ** quotaCode **
The quota code associated with the throttling error.
 ** serviceCode **
The service code associated with the throttling error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation due to invalid input parameters.
 ** fieldList **
A list of fields that failed validation.
 ** message **
A message describing the validation error.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_channel_UpdateRelationship_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-channel-2024-03-18/UpdateRelationship)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-channel-2024-03-18/UpdateRelationship)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/UpdateRelationship)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-channel-2024-03-18/UpdateRelationship)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/UpdateRelationship)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-channel-2024-03-18/UpdateRelationship)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-channel-2024-03-18/UpdateRelationship)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-channel-2024-03-18/UpdateRelationship)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-channel-2024-03-18/UpdateRelationship)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/UpdateRelationship)
