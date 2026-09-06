---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_DisassociateLicense.html
---

# DisassociateLicense
<a name="API_DisassociateLicense"></a>

Removes the Grafana Enterprise license from a workspace.

## Request Syntax
<a name="API_DisassociateLicense_RequestSyntax"></a>

```
DELETE /workspaces/{{workspaceId}}/licenses/{{licenseType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateLicense_RequestParameters"></a>

The request uses the following URI parameters.

 ** [licenseType](#API_DisassociateLicense_RequestSyntax) **   <a name="ManagedGrafana-DisassociateLicense-request-uri-licenseType"></a>
The type of license to remove from the workspace.
Valid Values: `ENTERPRISE | ENTERPRISE_FREE_TRIAL`
Required: Yes

 ** [workspaceId](#API_DisassociateLicense_RequestSyntax) **   <a name="ManagedGrafana-DisassociateLicense-request-uri-workspaceId"></a>
The ID of the workspace to remove the Grafana Enterprise license from.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_DisassociateLicense_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateLicense_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "workspace": {
      "accountAccessType": "string",
      "authentication": {
         "providers": [ "string" ],
         "samlConfigurationStatus": "string"
      },
      "created": number,
      "dataSources": [ "string" ],
      "degradedWorkspaceReason": "string",
      "description": "string",
      "endpoint": "string",
      "freeTrialConsumed": boolean,
      "freeTrialExpiration": number,
      "grafanaToken": "string",
      "grafanaVersion": "string",
      "id": "string",
      "ipAddressType": "string",
      "kmsKeyId": "string",
      "licenseExpiration": number,
      "licenseType": "string",
      "modified": number,
      "name": "string",
      "networkAccessControl": {
         "prefixListIds": [ "string" ],
         "vpceIds": [ "string" ]
      },
      "notificationDestinations": [ "string" ],
      "organizationalUnits": [ "string" ],
      "organizationRoleName": "string",
      "permissionType": "string",
      "stackSetName": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "vpcConfiguration": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ]
      },
      "workspaceRoleArn": "string"
   }
}
```

## Response Elements
<a name="API_DisassociateLicense_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [workspace](#API_DisassociateLicense_ResponseSyntax) **   <a name="ManagedGrafana-DisassociateLicense-response-workspace"></a>
A structure containing information about the workspace.
Type: [WorkspaceDescription](API_WorkspaceDescription.md) object

## Errors
<a name="API_DisassociateLicense_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error while processing the request. Retry the request.
 ** message **
A description of the error.
 ** retryAfterSeconds **
How long to wait before you retry this operation.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** message **
The value of a parameter in the request caused an error.
 ** resourceId **
The ID of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling. Retry the request.
 ** message **
A description of the error.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The value of a parameter in the request caused an error.
 ** fieldList **
A list of fields that might be associated with the error.
 ** message **
A description of the error.
 ** reason **
The reason that the operation failed.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateLicense_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/DisassociateLicense)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/DisassociateLicense)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/DisassociateLicense)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/DisassociateLicense)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/DisassociateLicense)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/DisassociateLicense)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/DisassociateLicense)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/DisassociateLicense)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/DisassociateLicense)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/DisassociateLicense)
