---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ListVmEntitlements.html
---

# ListVmEntitlements
<a name="API_ListVmEntitlements"></a>

Lists the Windows Server License entitlements for virtual machines in an Amazon EVS environment. Returns existing entitlements for virtual machines associated with the specified environment and connector.

## Request Syntax
<a name="API_ListVmEntitlements_RequestSyntax"></a>

```
{
   "connectorId": "{{string}}",
   "entitlementType": "{{string}}",
   "environmentId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVmEntitlements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [connectorId](#API_ListVmEntitlements_RequestSyntax) **   <a name="evs-ListVmEntitlements-request-connectorId"></a>
A unique ID for the connector.
Type: String
Pattern: `(cnctr-[a-zA-Z0-9]{10})`
Required: Yes

 ** [entitlementType](#API_ListVmEntitlements_RequestSyntax) **   <a name="evs-ListVmEntitlements-request-entitlementType"></a>
The type of entitlement to list.
Type: String
Valid Values: `WINDOWS_SERVER`
Required: Yes

 ** [environmentId](#API_ListVmEntitlements_RequestSyntax) **   <a name="evs-ListVmEntitlements-request-environmentId"></a>
A unique ID for the environment.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [maxResults](#API_ListVmEntitlements_RequestSyntax) **   <a name="evs-ListVmEntitlements-request-maxResults"></a>
The maximum number of results to return. If you specify `MaxResults` in the request, the response includes information up to the limit specified.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListVmEntitlements_RequestSyntax) **   <a name="evs-ListVmEntitlements-request-nextToken"></a>
A unique pagination token for each page. If `nextToken` is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Required: No

## Response Syntax
<a name="API_ListVmEntitlements_ResponseSyntax"></a>

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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListVmEntitlements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entitlements](#API_ListVmEntitlements_ResponseSyntax) **   <a name="evs-ListVmEntitlements-response-entitlements"></a>
A list of entitlements for virtual machines in the environment.
Type: Array of [VmEntitlement](API_VmEntitlement.md) objects

 ** [nextToken](#API_ListVmEntitlements_ResponseSyntax) **   <a name="evs-ListVmEntitlements-response-nextToken"></a>
A unique pagination token for next page results. Make the call again using this token to retrieve the next page.
Type: String

## Errors
<a name="API_ListVmEntitlements_Errors"></a>

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
<a name="API_ListVmEntitlements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/ListVmEntitlements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/ListVmEntitlements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/ListVmEntitlements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/ListVmEntitlements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/ListVmEntitlements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/ListVmEntitlements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/ListVmEntitlements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/ListVmEntitlements)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/ListVmEntitlements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ListVmEntitlements)
