---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListManagedThings.html
---

# ListManagedThings
<a name="API_ListManagedThings"></a>

Listing all managed things with provision for filters.

## Request Syntax
<a name="API_ListManagedThings_RequestSyntax"></a>

```
GET /managed-things?ConnectorDestinationIdFilter={{ConnectorDestinationIdFilter}}&ConnectorDeviceIdFilter={{ConnectorDeviceIdFilter}}&ConnectorPolicyIdFilter={{ConnectorPolicyIdFilter}}&CredentialLockerFilter={{CredentialLockerFilter}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&OwnerFilter={{OwnerFilter}}&ParentControllerIdentifierFilter={{ParentControllerIdentifierFilter}}&ProvisioningStatusFilter={{ProvisioningStatusFilter}}&RoleFilter={{RoleFilter}}&SerialNumberFilter={{SerialNumberFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedThings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectorDestinationIdFilter](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-ConnectorDestinationIdFilter"></a>
Filter managed things by the connector destination ID they are associated with.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [ConnectorDeviceIdFilter](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-ConnectorDeviceIdFilter"></a>
Filter managed things by the connector device ID they are associated with. When specified, only managed things with this connector device ID will be returned.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.,@-]+`

 ** [ConnectorPolicyIdFilter](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-ConnectorPolicyIdFilter"></a>
 *This parameter has been deprecated.*
Filter on a connector policy id for a managed thing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [CredentialLockerFilter](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-CredentialLockerFilter"></a>
Filter on a credential locker for a managed thing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`

 ** [MaxResults](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-MaxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-NextToken"></a>
A token that can be used to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

 ** [OwnerFilter](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-OwnerFilter"></a>
Filter on device owners when listing managed things.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.,@-]+`

 ** [ParentControllerIdentifierFilter](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-ParentControllerIdentifierFilter"></a>
Filter on a parent controller id for a managed thing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9]+`

 ** [ProvisioningStatusFilter](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-ProvisioningStatusFilter"></a>
Filter on the status of the device. For more information, see [Device Provisioning](https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html).
Valid Values: `UNASSOCIATED | PRE_ASSOCIATED | DISCOVERED | ACTIVATED | DELETION_FAILED | DELETE_IN_PROGRESS | ISOLATED | DELETED`

 ** [RoleFilter](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-RoleFilter"></a>
Filter on the type of device used. This will be the AWS hub controller, cloud device, or AWS IoT device.
Valid Values: `CONTROLLER | DEVICE`

 ** [SerialNumberFilter](#API_ListManagedThings_RequestSyntax) **   <a name="managedintegrations-ListManagedThings-request-uri-SerialNumberFilter"></a>
Filter on the serial number of the device.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`

## Request Body
<a name="API_ListManagedThings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedThings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "ActivatedAt": number,
         "AdvertisedProductId": "string",
         "Arn": "string",
         "Brand": "string",
         "Classification": "string",
         "ConnectorDestinationId": "string",
         "ConnectorDeviceId": "string",
         "ConnectorPolicyId": "string",
         "CreatedAt": number,
         "CredentialLockerId": "string",
         "Id": "string",
         "Model": "string",
         "Name": "string",
         "Owner": "string",
         "ParentControllerId": "string",
         "ProvisioningStatus": "string",
         "Role": "string",
         "SerialNumber": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedThings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListManagedThings_ResponseSyntax) **   <a name="managedintegrations-ListManagedThings-response-Items"></a>
The list of managed things.
Type: Array of [ManagedThingSummary](API_ManagedThingSummary.md) objects

 ** [NextToken](#API_ListManagedThings_ResponseSyntax) **   <a name="managedintegrations-ListManagedThings-response-NextToken"></a>
A token that can be used to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Errors
<a name="API_ListManagedThings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
HTTP Status Code: 401

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_ListManagedThings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/ListManagedThings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/ListManagedThings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ListManagedThings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/ListManagedThings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ListManagedThings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/ListManagedThings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/ListManagedThings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/ListManagedThings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/ListManagedThings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ListManagedThings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
