---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousVirtualMachines.html
---

# ListAutonomousVirtualMachines
<a name="API_ListAutonomousVirtualMachines"></a>

Lists all Autonomous VMs in an Autonomous VM cluster.

## Request Syntax
<a name="API_ListAutonomousVirtualMachines_RequestSyntax"></a>

```
{
   "cloudAutonomousVmClusterId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAutonomousVirtualMachines_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudAutonomousVmClusterId](#API_ListAutonomousVirtualMachines_RequestSyntax) **   <a name="odb-ListAutonomousVirtualMachines-request-cloudAutonomousVmClusterId"></a>
The unique identifier of the Autonomous VM cluster whose virtual machines you're listing.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** [maxResults](#API_ListAutonomousVirtualMachines_RequestSyntax) **   <a name="odb-ListAutonomousVirtualMachines-request-maxResults"></a>
The maximum number of items to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListAutonomousVirtualMachines_RequestSyntax) **   <a name="odb-ListAutonomousVirtualMachines-request-nextToken"></a>
The pagination token to continue listing from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_ListAutonomousVirtualMachines_ResponseSyntax"></a>

```
{
   "autonomousVirtualMachines": [
      {
         "autonomousVirtualMachineId": "string",
         "clientIpAddress": "string",
         "cloudAutonomousVmClusterId": "string",
         "cpuCoreCount": number,
         "dbNodeStorageSizeInGBs": number,
         "dbServerDisplayName": "string",
         "dbServerId": "string",
         "memorySizeInGBs": number,
         "ocid": "string",
         "ociResourceAnchorName": "string",
         "status": "string",
         "statusReason": "string",
         "vmName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAutonomousVirtualMachines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousVirtualMachines](#API_ListAutonomousVirtualMachines_ResponseSyntax) **   <a name="odb-ListAutonomousVirtualMachines-response-autonomousVirtualMachines"></a>
The list of Autonomous VMs in the specified Autonomous VM cluster.
Type: Array of [AutonomousVirtualMachineSummary](API_AutonomousVirtualMachineSummary.md) objects

 ** [nextToken](#API_ListAutonomousVirtualMachines_ResponseSyntax) **   <a name="odb-ListAutonomousVirtualMachines-response-nextToken"></a>
The pagination token from which to continue listing.
Type: String

## Errors
<a name="API_ListAutonomousVirtualMachines_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListAutonomousVirtualMachines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListAutonomousVirtualMachines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListAutonomousVirtualMachines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListAutonomousVirtualMachines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListAutonomousVirtualMachines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListAutonomousVirtualMachines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListAutonomousVirtualMachines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListAutonomousVirtualMachines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListAutonomousVirtualMachines)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListAutonomousVirtualMachines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListAutonomousVirtualMachines)
