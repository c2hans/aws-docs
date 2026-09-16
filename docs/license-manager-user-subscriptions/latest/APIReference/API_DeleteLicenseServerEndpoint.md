---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DeleteLicenseServerEndpoint.html
---

# DeleteLicenseServerEndpoint
<a name="API_DeleteLicenseServerEndpoint"></a>

Deletes a `LicenseServerEndpoint` resource.

## Request Syntax
<a name="API_DeleteLicenseServerEndpoint_RequestSyntax"></a>

```
POST /license-server/DeleteLicenseServerEndpoint HTTP/1.1
Content-type: application/json

{
   "LicenseServerEndpointArn": "{{string}}",
   "ServerType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteLicenseServerEndpoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteLicenseServerEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LicenseServerEndpointArn](#API_DeleteLicenseServerEndpoint_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DeleteLicenseServerEndpoint-request-LicenseServerEndpointArn"></a>
The Amazon Resource Name (ARN) that identifies the `LicenseServerEndpoint` resource to delete.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: Yes

 ** [ServerType](#API_DeleteLicenseServerEndpoint_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DeleteLicenseServerEndpoint-request-ServerType"></a>
The type of License Server that the delete request refers to.
Type: String
Valid Values: `RDS_SAL`
Required: Yes

## Response Syntax
<a name="API_DeleteLicenseServerEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LicenseServerEndpoint": {
      "CreationTime": number,
      "IdentityProviderArn": "string",
      "LicenseServerEndpointArn": "string",
      "LicenseServerEndpointId": "string",
      "LicenseServerEndpointProvisioningStatus": "string",
      "LicenseServers": [
         {
            "HealthStatus": "string",
            "Ipv4Address": "string",
            "Ipv6Address": "string",
            "ProvisioningStatus": "string"
         }
      ],
      "ServerEndpoint": {
         "Endpoint": "string"
      },
      "ServerType": "string",
      "StatusMessage": "string"
   }
}
```

## Response Elements
<a name="API_DeleteLicenseServerEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseServerEndpoint](#API_DeleteLicenseServerEndpoint_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-DeleteLicenseServerEndpoint-response-LicenseServerEndpoint"></a>
Shows details from the `LicenseServerEndpoint` resource that was deleted.
Type: [LicenseServerEndpoint](API_LicenseServerEndpoint.md) object

## Errors
<a name="API_DeleteLicenseServerEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request couldn't be completed because it conflicted with the current state of the resource.
HTTP Status Code: 500

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request failed because a service quota is exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because of request throttling. Retry the request.
HTTP Status Code: 400

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteLicenseServerEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/DeleteLicenseServerEndpoint)
