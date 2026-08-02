---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_DeleteEnvironmentHost.html
---

# DeleteEnvironmentHost
<a name="API_DeleteEnvironmentHost"></a>

Deletes a host from an Amazon EVS environment.

**Note**
Before deleting a host, you must unassign and decommission the host from within the SDDC Manager user interface. Not doing so could impact the availability of your virtual machines or result in data loss.

## Request Syntax
<a name="API_DeleteEnvironmentHost_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "environmentId": "{{string}}",
   "hostName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEnvironmentHost_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [environmentId](#API_DeleteEnvironmentHost_RequestSyntax) **   <a name="evs-DeleteEnvironmentHost-request-environmentId"></a>
A unique ID for the host's environment.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [hostName](#API_DeleteEnvironmentHost_RequestSyntax) **   <a name="evs-DeleteEnvironmentHost-request-hostName"></a>
The DNS hostname associated with the host to be deleted.
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** [clientToken](#API_DeleteEnvironmentHost_RequestSyntax) **   <a name="evs-DeleteEnvironmentHost-request-clientToken"></a>
This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.
A unique, case-sensitive identifier that you provide to ensure the idempotency of the host deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[!-~]+`
Required: No

## Response Syntax
<a name="API_DeleteEnvironmentHost_ResponseSyntax"></a>

```
{
   "environmentSummary": {
      "createdAt": number,
      "environmentArn": "string",
      "environmentId": "string",
      "environmentName": "string",
      "environmentState": "string",
      "environmentStatus": "string",
      "modifiedAt": number,
      "vcfVersion": "string"
   },
   "host": {
      "createdAt": number,
      "dedicatedHostId": "string",
      "ec2InstanceId": "string",
      "hostName": "string",
      "hostState": "string",
      "instanceType": "string",
      "ipAddress": "string",
      "keyName": "string",
      "modifiedAt": number,
      "networkInterfaces": [
         {
            "networkInterfaceId": "string"
         }
      ],
      "placementGroupId": "string",
      "stateDetails": "string"
   }
}
```

## Response Elements
<a name="API_DeleteEnvironmentHost_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentSummary](#API_DeleteEnvironmentHost_ResponseSyntax) **   <a name="evs-DeleteEnvironmentHost-response-environmentSummary"></a>
A summary of the environment that the host was deleted from.
Type: [EnvironmentSummary](API_EnvironmentSummary.md) object

 ** [host](#API_DeleteEnvironmentHost_ResponseSyntax) **   <a name="evs-DeleteEnvironmentHost-response-host"></a>
A description of the deleted host.
Type: [Host](API_Host.md) object

## Errors
<a name="API_DeleteEnvironmentHost_Errors"></a>

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
<a name="API_DeleteEnvironmentHost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/DeleteEnvironmentHost)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/DeleteEnvironmentHost)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/DeleteEnvironmentHost)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/DeleteEnvironmentHost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/DeleteEnvironmentHost)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/DeleteEnvironmentHost)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/DeleteEnvironmentHost)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/DeleteEnvironmentHost)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/DeleteEnvironmentHost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/DeleteEnvironmentHost)
