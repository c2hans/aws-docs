---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_UpdateEnvironmentConnector.html
---

# UpdateEnvironmentConnector
<a name="API_UpdateEnvironmentConnector"></a>

Updates a connector for an Amazon EVS environment. You can update the AWS Secrets Manager secret ARN or the appliance FQDN to reconfigure the connector metadata.

**Note**
You cannot update both the secret and the FQDN in the same request.

## Request Syntax
<a name="API_UpdateEnvironmentConnector_RequestSyntax"></a>

```
{
   "applianceFqdn": "{{string}}",
   "clientToken": "{{string}}",
   "connectorId": "{{string}}",
   "environmentId": "{{string}}",
   "secretIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEnvironmentConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [connectorId](#API_UpdateEnvironmentConnector_RequestSyntax) **   <a name="evs-UpdateEnvironmentConnector-request-connectorId"></a>
A unique ID for the connector to update.
Type: String
Pattern: `(cnctr-[a-zA-Z0-9]{10})`
Required: Yes

 ** [environmentId](#API_UpdateEnvironmentConnector_RequestSyntax) **   <a name="evs-UpdateEnvironmentConnector-request-environmentId"></a>
A unique ID for the environment that the connector belongs to.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [applianceFqdn](#API_UpdateEnvironmentConnector_RequestSyntax) **   <a name="evs-UpdateEnvironmentConnector-request-applianceFqdn"></a>
The new fully qualified domain name (FQDN) of the VCF appliance that the connector connects to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*`
Required: No

 ** [clientToken](#API_UpdateEnvironmentConnector_RequestSyntax) **   <a name="evs-UpdateEnvironmentConnector-request-clientToken"></a>
This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.
A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector update request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[!-~]+`
Required: No

 ** [secretIdentifier](#API_UpdateEnvironmentConnector_RequestSyntax) **   <a name="evs-UpdateEnvironmentConnector-request-secretIdentifier"></a>
The new ARN or name of the AWS Secrets Manager secret that stores the credentials for the VCF appliance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@!-]+|[a-zA-Z0-9/_+=.@!-]+)`
Required: No

## Response Syntax
<a name="API_UpdateEnvironmentConnector_ResponseSyntax"></a>

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
<a name="API_UpdateEnvironmentConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connector](#API_UpdateEnvironmentConnector_ResponseSyntax) **   <a name="evs-UpdateEnvironmentConnector-response-connector"></a>
A description of the updated connector.
Type: [Connector](API_Connector.md) object

## Errors
<a name="API_UpdateEnvironmentConnector_Errors"></a>

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
<a name="API_UpdateEnvironmentConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/UpdateEnvironmentConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/UpdateEnvironmentConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/UpdateEnvironmentConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/UpdateEnvironmentConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/UpdateEnvironmentConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/UpdateEnvironmentConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/UpdateEnvironmentConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/UpdateEnvironmentConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/UpdateEnvironmentConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/UpdateEnvironmentConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
