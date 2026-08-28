---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_RegisterConnector.html
---

# RegisterConnector
<a name="API_RegisterConnector"></a>

Registers a new custom connector with your AWS account. Before you can register the connector, you must deploy the associated AWS lambda function in your account.

## Request Syntax
<a name="API_RegisterConnector_RequestSyntax"></a>

```
POST /register-connector HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "connectorLabel": "{{string}}",
   "connectorProvisioningConfig": {
      "lambda": {
         "lambdaArn": "{{string}}"
      }
   },
   "connectorProvisioningType": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_RegisterConnector_RequestSyntax) **   <a name="appflow-RegisterConnector-request-clientToken"></a>
The `clientToken` parameter is an idempotency token. It ensures that your `RegisterConnector` request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same `clientToken` parameter value.
If you omit a `clientToken` value, the AWS SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.
If you specify input parameters that differ from your first request, an error occurs. If you use a different value for `clientToken`, Amazon AppFlow considers it a new call to `RegisterConnector`. The token is active for 8 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ -~]+`
Required: No

 ** [connectorLabel](#API_RegisterConnector_RequestSyntax) **   <a name="appflow-RegisterConnector-request-connectorLabel"></a>
 The name of the connector. The name is unique for each `ConnectorRegistration` in your AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** [connectorProvisioningConfig](#API_RegisterConnector_RequestSyntax) **   <a name="appflow-RegisterConnector-request-connectorProvisioningConfig"></a>
The provisioning type of the connector. Currently the only supported value is LAMBDA.
Type: [ConnectorProvisioningConfig](API_ConnectorProvisioningConfig.md) object
Required: No

 ** [connectorProvisioningType](#API_RegisterConnector_RequestSyntax) **   <a name="appflow-RegisterConnector-request-connectorProvisioningType"></a>
The provisioning type of the connector. Currently the only supported value is LAMBDA.
Type: String
Valid Values: `LAMBDA`
Required: No

 ** [description](#API_RegisterConnector_RequestSyntax) **   <a name="appflow-RegisterConnector-request-description"></a>
A description about the connector that's being registered.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\s\w/!@#+=.-]*`
Required: No

## Response Syntax
<a name="API_RegisterConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorArn": "string"
}
```

## Response Elements
<a name="API_RegisterConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorArn](#API_RegisterConnector_ResponseSyntax) **   <a name="appflow-RegisterConnector-response-connectorArn"></a>
The ARN of the connector being registered.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:.*:.*:[0-9]+:.*`

## Errors
<a name="API_RegisterConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
AppFlow/Requester has invalid or missing permissions.
HTTP Status Code: 403

 ** ConflictException **
 There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again.
HTTP Status Code: 409

 ** ConnectorAuthenticationException **
 An error occurred when authenticating with the connector endpoint.
HTTP Status Code: 401

 ** ConnectorServerException **
 An error occurred when retrieving data from the connector endpoint.
HTTP Status Code: 400

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
 The request would cause a service quota (such as the number of flows) to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
API calls have exceeded the maximum allowed API request rate per account and per Region.
HTTP Status Code: 429

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_RegisterConnector_Examples"></a>

### Registering a connector
<a name="API_RegisterConnector_Example_1"></a>

This example shows a sample request for the `RegisterConnector` API and a sample response.

#### Sample Request
<a name="API_RegisterConnector_Example_1_Request"></a>

```
{
  "connectorLabel": "Connector_Label_Value",
  "connectorProvisioningType": "LAMBDA",
  "connectorProvisioningConfig":
  {
    "lambda":
    {
      "lambdaArn": "lambda arn"
    }
  }
}
```

#### Sample Response
<a name="API_RegisterConnector_Example_1_Response"></a>

```
{
  "connectorArn": "arn:aws:appflow:region:<AccountId>:connector/Connector_Label"
}
```

## See Also
<a name="API_RegisterConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/RegisterConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/RegisterConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/RegisterConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/RegisterConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/RegisterConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/RegisterConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/RegisterConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/RegisterConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/RegisterConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/RegisterConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
