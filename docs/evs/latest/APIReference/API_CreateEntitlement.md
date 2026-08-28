---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEntitlement.html
---

# CreateEntitlement
<a name="API_CreateEntitlement"></a>

Creates a Windows Server License entitlement for virtual machines in an Amazon EVS environment using the provided vCenter Server connector. This is an asynchronous operation. Amazon EVS validates the specified virtual machines before starting usage tracking.

## Request Syntax
<a name="API_CreateEntitlement_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "connectorId": "{{string}}",
   "entitlementType": "{{string}}",
   "environmentId": "{{string}}",
   "vmIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateEntitlement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [connectorId](#API_CreateEntitlement_RequestSyntax) **   <a name="evs-CreateEntitlement-request-connectorId"></a>
A unique ID for the connector associated with the entitlement.
Type: String
Pattern: `(cnctr-[a-zA-Z0-9]{10})`
Required: Yes

 ** [entitlementType](#API_CreateEntitlement_RequestSyntax) **   <a name="evs-CreateEntitlement-request-entitlementType"></a>
The type of entitlement to create.
Type: String
Valid Values: `WINDOWS_SERVER`
Required: Yes

 ** [environmentId](#API_CreateEntitlement_RequestSyntax) **   <a name="evs-CreateEntitlement-request-environmentId"></a>
A unique ID for the environment to create the entitlement in.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [vmIds](#API_CreateEntitlement_RequestSyntax) **   <a name="evs-CreateEntitlement-request-vmIds"></a>
The list of VMware vSphere virtual machine managed object IDs to create entitlements for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 4. Maximum length of 1024.
Pattern: `vm-[0-9]+`
Required: Yes

 ** [clientToken](#API_CreateEntitlement_RequestSyntax) **   <a name="evs-CreateEntitlement-request-clientToken"></a>
This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.
A unique, case-sensitive identifier that you provide to ensure the idempotency of the entitlement creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[!-~]+`
Required: No

## Response Syntax
<a name="API_CreateEntitlement_ResponseSyntax"></a>

```
{
   "entitlements": [
      {
         "connectorId": "string",
         "environmentId": "string",
         "errorDetail": {
            "errorCode": "string",
            "errorMessage": "string"
         },
         "lastSyncedAt": number,
         "startedAt": number,
         "status": "string",
         "stoppedAt": number,
         "type": "string",
         "vmId": "string",
         "vmName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateEntitlement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entitlements](#API_CreateEntitlement_ResponseSyntax) **   <a name="evs-CreateEntitlement-response-entitlements"></a>
A list of the created entitlements.
Type: Array of [VmEntitlement](API_VmEntitlement.md) objects

## Errors
<a name="API_CreateEntitlement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a `state` of `DELETED`.
 ** message **
Describes the error encountered.
 ** resourceId **
The ID of the resource that could not be found.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 400

 [ThrottlingException](API_ThrottlingException.md)
The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.
 ** message **
Describes the error encountered.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.
 ** fieldList **
A list of fields that didn't validate.
 ** message **
Describes the error encountered.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/CreateEntitlement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/CreateEntitlement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/CreateEntitlement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/CreateEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/CreateEntitlement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/CreateEntitlement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/CreateEntitlement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/CreateEntitlement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/CreateEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/CreateEntitlement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
