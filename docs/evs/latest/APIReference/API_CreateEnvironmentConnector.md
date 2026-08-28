---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEnvironmentConnector.html
---

# CreateEnvironmentConnector
<a name="API_CreateEnvironmentConnector"></a>

Creates a connector for an Amazon EVS environment. A connector allows the Amazon EVS control plane to interface with VCF appliances using a fully qualified domain name.

You can create only one connector of each type per environment. For environments where Amazon EVS installs VCF, the `SDDC_MANAGER` connector is created automatically.

**Note**
Amazon EVS requires an active connector to SDDC Manager or VCF Operations Manager to monitor environment health and license compliance.

## Request Syntax
<a name="API_CreateEnvironmentConnector_RequestSyntax"></a>

```
{
   "applianceFqdn": "{{string}}",
   "clientToken": "{{string}}",
   "environmentId": "{{string}}",
   "secretIdentifier": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateEnvironmentConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [applianceFqdn](#API_CreateEnvironmentConnector_RequestSyntax) **   <a name="evs-CreateEnvironmentConnector-request-applianceFqdn"></a>
The fully qualified domain name (FQDN) of the VCF appliance that the connector targets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*`
Required: Yes

 ** [environmentId](#API_CreateEnvironmentConnector_RequestSyntax) **   <a name="evs-CreateEnvironmentConnector-request-environmentId"></a>
A unique ID for the environment to create the connector in.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [secretIdentifier](#API_CreateEnvironmentConnector_RequestSyntax) **   <a name="evs-CreateEnvironmentConnector-request-secretIdentifier"></a>
The ARN or name of the AWS Secrets Manager secret that stores the credentials for the VCF appliance. `SDDC_MANAGER` requires an `apiKey` field; `OPERATIONS_MANAGER` and `VCENTER` require `username` and `password` fields.
Do not use credentials with Administrator privileges. We recommend using a service account with read-only permissions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@!-]+|[a-zA-Z0-9/_+=.@!-]+)`
Required: Yes

 ** [type](#API_CreateEnvironmentConnector_RequestSyntax) **   <a name="evs-CreateEnvironmentConnector-request-type"></a>
The type of connector to create.
+  `OPERATIONS_MANAGER`: Connector to an Operations Manager appliance. Required for VCF 9x environments.
+  `SDDC_MANAGER`: Connector to an SDDC Manager appliance. Required for VCF 5.x environments.
+  `VCENTER`: Connector to a vCenter Server appliance. Required for features that depend on vCenter, such as Windows Server license-included.
Type: String
Valid Values: `OPERATIONS_MANAGER | SDDC_MANAGER | VCENTER`
Required: Yes

 ** [clientToken](#API_CreateEnvironmentConnector_RequestSyntax) **   <a name="evs-CreateEnvironmentConnector-request-clientToken"></a>
This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.
A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[!-~]+`
Required: No

## Response Syntax
<a name="API_CreateEnvironmentConnector_ResponseSyntax"></a>

```
{
   "connector": {
      "applianceFqdn": "string",
      "checks": [
         {
            "impairedSince": number,
            "lastCheckAttempt": number,
            "result": "string",
            "type": "string"
         }
      ],
      "connectorId": "string",
      "createdAt": number,
      "environmentId": "string",
      "modifiedAt": number,
      "secretArn": "string",
      "state": "string",
      "stateDetails": "string",
      "status": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_CreateEnvironmentConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connector](#API_CreateEnvironmentConnector_ResponseSyntax) **   <a name="evs-CreateEnvironmentConnector-response-connector"></a>
A description of the created connector.
Type: [Connector](API_Connector.md) object

## Errors
<a name="API_CreateEnvironmentConnector_Errors"></a>

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
<a name="API_CreateEnvironmentConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/CreateEnvironmentConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/CreateEnvironmentConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/CreateEnvironmentConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/CreateEnvironmentConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/CreateEnvironmentConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/CreateEnvironmentConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/CreateEnvironmentConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/CreateEnvironmentConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/CreateEnvironmentConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/CreateEnvironmentConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
