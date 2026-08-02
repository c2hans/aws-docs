---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_DeleteEntitlement.html
---

# DeleteEntitlement
<a name="API_DeleteEntitlement"></a>

Deletes a Windows Server License entitlement for virtual machines in an Amazon EVS environment. Deleting an entitlement stops usage tracking for the specified virtual machines.

## Request Syntax
<a name="API_DeleteEntitlement_RequestSyntax"></a>

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
<a name="API_DeleteEntitlement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [connectorId](#API_DeleteEntitlement_RequestSyntax) **   <a name="evs-DeleteEntitlement-request-connectorId"></a>
A unique ID for the connector associated with the entitlement.
Type: String
Pattern: `(cnctr-[a-zA-Z0-9]{10})`
Required: Yes

 ** [entitlementType](#API_DeleteEntitlement_RequestSyntax) **   <a name="evs-DeleteEntitlement-request-entitlementType"></a>
The type of entitlement to delete.
Type: String
Valid Values: `WINDOWS_SERVER`
Required: Yes

 ** [environmentId](#API_DeleteEntitlement_RequestSyntax) **   <a name="evs-DeleteEntitlement-request-environmentId"></a>
A unique ID for the environment that the entitlement belongs to.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [vmIds](#API_DeleteEntitlement_RequestSyntax) **   <a name="evs-DeleteEntitlement-request-vmIds"></a>
The list of VMware vSphere virtual machine managed object IDs to delete entitlements for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 4. Maximum length of 1024.
Pattern: `vm-[0-9]+`
Required: Yes

 ** [clientToken](#API_DeleteEntitlement_RequestSyntax) **   <a name="evs-DeleteEntitlement-request-clientToken"></a>
This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.
A unique, case-sensitive identifier that you provide to ensure the idempotency of the entitlement deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[!-~]+`
Required: No

## Response Syntax
<a name="API_DeleteEntitlement_ResponseSyntax"></a>

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
<a name="API_DeleteEntitlement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entitlements](#API_DeleteEntitlement_ResponseSyntax) **   <a name="evs-DeleteEntitlement-response-entitlements"></a>
A list of the deleted entitlements.
Type: Array of [VmEntitlement](API_VmEntitlement.md) objects

## Errors
<a name="API_DeleteEntitlement_Errors"></a>

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
<a name="API_DeleteEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/DeleteEntitlement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/DeleteEntitlement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/DeleteEntitlement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/DeleteEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/DeleteEntitlement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/DeleteEntitlement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/DeleteEntitlement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/DeleteEntitlement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/DeleteEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/DeleteEntitlement)
