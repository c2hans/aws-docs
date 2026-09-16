---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetConfigurationPolicyAssociations.html
---

# BatchGetConfigurationPolicyAssociations
<a name="API_BatchGetConfigurationPolicyAssociations"></a>

 Returns associations between an AWS Security Hub CSPM configuration and a batch of target accounts, organizational units, or the root. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. A configuration can refer to a configuration policy or to a self-managed configuration.

## Request Syntax
<a name="API_BatchGetConfigurationPolicyAssociations_RequestSyntax"></a>

```
POST /configurationPolicyAssociation/batchget HTTP/1.1
Content-type: application/json

{
   "ConfigurationPolicyAssociationIdentifiers": [
      {
         "Target": { ... }
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchGetConfigurationPolicyAssociations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetConfigurationPolicyAssociations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationPolicyAssociationIdentifiers](#API_BatchGetConfigurationPolicyAssociations_RequestSyntax) **   <a name="securityhub-BatchGetConfigurationPolicyAssociations-request-ConfigurationPolicyAssociationIdentifiers"></a>
 Specifies one or more target account IDs, organizational unit (OU) IDs, or the root ID to retrieve associations for.
Type: Array of [ConfigurationPolicyAssociation](API_ConfigurationPolicyAssociation.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchGetConfigurationPolicyAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationPolicyAssociations": [
      {
         "AssociationStatus": "string",
         "AssociationStatusMessage": "string",
         "AssociationType": "string",
         "ConfigurationPolicyId": "string",
         "TargetId": "string",
         "TargetType": "string",
         "UpdatedAt": "string"
      }
   ],
   "UnprocessedConfigurationPolicyAssociations": [
      {
         "ConfigurationPolicyAssociationIdentifiers": {
            "Target": { ... }
         },
         "ErrorCode": "string",
         "ErrorReason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetConfigurationPolicyAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationPolicyAssociations](#API_BatchGetConfigurationPolicyAssociations_ResponseSyntax) **   <a name="securityhub-BatchGetConfigurationPolicyAssociations-response-ConfigurationPolicyAssociations"></a>
 Describes associations for the target accounts, OUs, or the root.
Type: Array of [ConfigurationPolicyAssociationSummary](API_ConfigurationPolicyAssociationSummary.md) objects

 ** [UnprocessedConfigurationPolicyAssociations](#API_BatchGetConfigurationPolicyAssociations_ResponseSyntax) **   <a name="securityhub-BatchGetConfigurationPolicyAssociations-response-UnprocessedConfigurationPolicyAssociations"></a>
 An array of configuration policy associations, one for each configuration policy association identifier, that was specified in the request but couldn’t be processed due to an error.
Type: Array of [UnprocessedConfigurationPolicyAssociation](API_UnprocessedConfigurationPolicyAssociation.md) objects

## Errors
<a name="API_BatchGetConfigurationPolicyAssociations_Errors"></a>

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
<a name="API_BatchGetConfigurationPolicyAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchGetConfigurationPolicyAssociations)
