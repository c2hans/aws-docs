---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEnvironmentHost.html
---

# CreateEnvironmentHost
<a name="API_CreateEnvironmentHost"></a>

Creates an ESX host and adds it to an Amazon EVS environment.

This action can only be used after the Amazon EVS environment is deployed.

You can use the `dedicatedHostId` parameter to specify an Amazon EC2 Dedicated Host for ESX host creation.

 You can use the `placementGroupId` parameter to specify a cluster or partition placement group to launch EC2 instances into.

**Note**
If you don't specify an ESX version when adding hosts using `CreateEnvironmentHost` action, Amazon EVS automatically uses the default ESX version for your environment's VCF version. To find the available ESX versions for a particular VCF version, use the `GetVersions` action.
You cannot use the `dedicatedHostId` and `placementGroupId` parameters together in the same `CreateEnvironmentHost` action. This results in a `ValidationException` response.

## Request Syntax
<a name="API_CreateEnvironmentHost_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "environmentId": "{{string}}",
   "esxVersion": "{{string}}",
   "host": {
      "dedicatedHostId": "{{string}}",
      "hostName": "{{string}}",
      "instanceType": "{{string}}",
      "keyName": "{{string}}",
      "placementGroupId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateEnvironmentHost_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [environmentId](#API_CreateEnvironmentHost_RequestSyntax) **   <a name="evs-CreateEnvironmentHost-request-environmentId"></a>
A unique ID for the environment that the host is added to.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [host](#API_CreateEnvironmentHost_RequestSyntax) **   <a name="evs-CreateEnvironmentHost-request-host"></a>
The host that is created and added to the environment.
Type: [HostInfoForCreate](API_HostInfoForCreate.md) object
Required: Yes

 ** [clientToken](#API_CreateEnvironmentHost_RequestSyntax) **   <a name="evs-CreateEnvironmentHost-request-clientToken"></a>
This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.
A unique, case-sensitive identifier that you provide to ensure the idempotency of the host creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[!-~]+`
Required: No

 ** [esxVersion](#API_CreateEnvironmentHost_RequestSyntax) **   <a name="evs-CreateEnvironmentHost-request-esxVersion"></a>
The ESX version to use for the host.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_CreateEnvironmentHost_ResponseSyntax"></a>

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
<a name="API_CreateEnvironmentHost_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentSummary](#API_CreateEnvironmentHost_ResponseSyntax) **   <a name="evs-CreateEnvironmentHost-response-environmentSummary"></a>
A summary of the environment that the host is created in.
Type: [EnvironmentSummary](API_EnvironmentSummary.md) object

 ** [host](#API_CreateEnvironmentHost_ResponseSyntax) **   <a name="evs-CreateEnvironmentHost-response-host"></a>
A description of the created host.
Type: [Host](API_Host.md) object

## Errors
<a name="API_CreateEnvironmentHost_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_CreateEnvironmentHost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/CreateEnvironmentHost)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/CreateEnvironmentHost)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/CreateEnvironmentHost)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/CreateEnvironmentHost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/CreateEnvironmentHost)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/CreateEnvironmentHost)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/CreateEnvironmentHost)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/CreateEnvironmentHost)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/CreateEnvironmentHost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/CreateEnvironmentHost)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
