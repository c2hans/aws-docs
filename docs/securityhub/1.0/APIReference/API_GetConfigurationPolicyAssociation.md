---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetConfigurationPolicyAssociation.html
---

# GetConfigurationPolicyAssociation
<a name="API_GetConfigurationPolicyAssociation"></a>

 Returns the association between a configuration and a target account, organizational unit, or the root. The configuration can be a configuration policy or self-managed behavior. Only the AWS Security Hub CSPM delegated administrator can invoke this operation from the home Region.

## Request Syntax
<a name="API_GetConfigurationPolicyAssociation_RequestSyntax"></a>

```
POST /configurationPolicyAssociation/get HTTP/1.1
Content-type: application/json

{
   "Target": { ... }
}
```

## URI Request Parameters
<a name="API_GetConfigurationPolicyAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetConfigurationPolicyAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Target](#API_GetConfigurationPolicyAssociation_RequestSyntax) **   <a name="securityhub-GetConfigurationPolicyAssociation-request-Target"></a>
 The target account ID, organizational unit ID, or the root ID to retrieve the association for.
Type: [Target](API_Target.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_GetConfigurationPolicyAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssociationStatus": "string",
   "AssociationStatusMessage": "string",
   "AssociationType": "string",
   "ConfigurationPolicyId": "string",
   "TargetId": "string",
   "TargetType": "string",
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_GetConfigurationPolicyAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationStatus](#API_GetConfigurationPolicyAssociation_ResponseSyntax) **   <a name="securityhub-GetConfigurationPolicyAssociation-response-AssociationStatus"></a>
 The current status of the association between the specified target and the configuration.
Type: String
Valid Values: `PENDING | SUCCESS | FAILED`

 ** [AssociationStatusMessage](#API_GetConfigurationPolicyAssociation_ResponseSyntax) **   <a name="securityhub-GetConfigurationPolicyAssociation-response-AssociationStatusMessage"></a>
 The explanation for a `FAILED` value for `AssociationStatus`.
Type: String
Pattern: `.*\S.*`

 ** [AssociationType](#API_GetConfigurationPolicyAssociation_ResponseSyntax) **   <a name="securityhub-GetConfigurationPolicyAssociation-response-AssociationType"></a>
 Indicates whether the association between the specified target and the configuration was directly applied by the Security Hub CSPM delegated administrator or inherited from a parent.
Type: String
Valid Values: `INHERITED | APPLIED`

 ** [ConfigurationPolicyId](#API_GetConfigurationPolicyAssociation_ResponseSyntax) **   <a name="securityhub-GetConfigurationPolicyAssociation-response-ConfigurationPolicyId"></a>
 The universally unique identifier (UUID) of a configuration policy. For self-managed behavior, the value is `SELF_MANAGED_SECURITY_HUB`.
Type: String
Pattern: `.*\S.*`

 ** [TargetId](#API_GetConfigurationPolicyAssociation_ResponseSyntax) **   <a name="securityhub-GetConfigurationPolicyAssociation-response-TargetId"></a>
 The target account ID, organizational unit ID, or the root ID for which the association is retrieved.
Type: String
Pattern: `.*\S.*`

 ** [TargetType](#API_GetConfigurationPolicyAssociation_ResponseSyntax) **   <a name="securityhub-GetConfigurationPolicyAssociation-response-TargetType"></a>
 Specifies whether the target is an AWS account, organizational unit, or the organization root.
Type: String
Valid Values: `ACCOUNT | ORGANIZATIONAL_UNIT | ROOT`

 ** [UpdatedAt](#API_GetConfigurationPolicyAssociation_ResponseSyntax) **   <a name="securityhub-GetConfigurationPolicyAssociation-response-UpdatedAt"></a>
 The date and time, in UTC and ISO 8601 format, that the configuration policy association was last updated.
Type: Timestamp

## Errors
<a name="API_GetConfigurationPolicyAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_GetConfigurationPolicyAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetConfigurationPolicyAssociation)
