---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDomainMaintenanceStatus.html
---

# GetDomainMaintenanceStatus
<a name="API_GetDomainMaintenanceStatus"></a>

The status of the maintenance action.

## Request Syntax
<a name="API_GetDomainMaintenanceStatus_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/domainMaintenance?maintenanceId={{MaintenanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomainMaintenanceStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_GetDomainMaintenanceStatus_RequestSyntax) **   <a name="opensearchservice-GetDomainMaintenanceStatus-request-uri-DomainName"></a>
The name of the domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [MaintenanceId](#API_GetDomainMaintenanceStatus_RequestSyntax) **   <a name="opensearchservice-GetDomainMaintenanceStatus-request-uri-MaintenanceId"></a>
The request ID of the maintenance action.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([\s\S]*)$`
Required: Yes

## Request Body
<a name="API_GetDomainMaintenanceStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomainMaintenanceStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Action": "string",
   "CreatedAt": number,
   "NodeId": "string",
   "Status": "string",
   "StatusMessage": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_GetDomainMaintenanceStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Action](#API_GetDomainMaintenanceStatus_ResponseSyntax) **   <a name="opensearchservice-GetDomainMaintenanceStatus-response-Action"></a>
The action name.
Type: String
Valid Values: `REBOOT_NODE | RESTART_SEARCH_PROCESS | RESTART_DASHBOARD`

 ** [CreatedAt](#API_GetDomainMaintenanceStatus_ResponseSyntax) **   <a name="opensearchservice-GetDomainMaintenanceStatus-response-CreatedAt"></a>
The time at which the action was created.
Type: Timestamp

 ** [NodeId](#API_GetDomainMaintenanceStatus_ResponseSyntax) **   <a name="opensearchservice-GetDomainMaintenanceStatus-response-NodeId"></a>
The node ID of the maintenance action.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 40.

 ** [Status](#API_GetDomainMaintenanceStatus_ResponseSyntax) **   <a name="opensearchservice-GetDomainMaintenanceStatus-response-Status"></a>
The status of the maintenance action.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | TIMED_OUT`

 ** [StatusMessage](#API_GetDomainMaintenanceStatus_ResponseSyntax) **   <a name="opensearchservice-GetDomainMaintenanceStatus-response-StatusMessage"></a>
The status message of the maintenance action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `^([\s\S]*)$`

 ** [UpdatedAt](#API_GetDomainMaintenanceStatus_ResponseSyntax) **   <a name="opensearchservice-GetDomainMaintenanceStatus-response-UpdatedAt"></a>
The time at which the action was updated.
Type: Timestamp

## Errors
<a name="API_GetDomainMaintenanceStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetDomainMaintenanceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetDomainMaintenanceStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetDomainMaintenanceStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetDomainMaintenanceStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetDomainMaintenanceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetDomainMaintenanceStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetDomainMaintenanceStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetDomainMaintenanceStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetDomainMaintenanceStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetDomainMaintenanceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetDomainMaintenanceStatus)
