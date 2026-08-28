---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_DeregisterAccountAssociation.html
---

# DeregisterAccountAssociation
<a name="API_DeregisterAccountAssociation"></a>

Deregister an account association from a managed thing.

## Request Syntax
<a name="API_DeregisterAccountAssociation_RequestSyntax"></a>

```
PUT /managed-thing-associations/deregister HTTP/1.1
Content-type: application/json

{
   "AccountAssociationId": "{{string}}",
   "ManagedThingId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeregisterAccountAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeregisterAccountAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountAssociationId](#API_DeregisterAccountAssociation_RequestSyntax) **   <a name="managedintegrations-DeregisterAccountAssociation-request-AccountAssociationId"></a>
The unique identifier of the account association to be deregistered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

 ** [ManagedThingId](#API_DeregisterAccountAssociation_RequestSyntax) **   <a name="managedintegrations-DeregisterAccountAssociation-request-ManagedThingId"></a>
The identifier of the managed thing to be deregistered from the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Response Syntax
<a name="API_DeregisterAccountAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeregisterAccountAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterAccountAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict with the request.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_DeregisterAccountAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/DeregisterAccountAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
