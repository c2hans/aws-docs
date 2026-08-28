---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateInstanceMetadataOptions.html
---

# UpdateInstanceMetadataOptions
<a name="API_UpdateInstanceMetadataOptions"></a>

Modifies the Amazon Lightsail instance metadata parameters on a running or stopped instance. When you modify the parameters on a running instance, the `GetInstance` or `GetInstances` API operation initially responds with a state of `pending`. After the parameter modifications are successfully applied, the state changes to `applied` in subsequent `GetInstance` or `GetInstances` API calls. For more information, see [Use IMDSv2 with an Amazon Lightsail instance](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-instance-metadata-service) in the *Amazon Lightsail Developer Guide*.

## Request Syntax
<a name="API_UpdateInstanceMetadataOptions_RequestSyntax"></a>

```
{
   "httpEndpoint": "{{string}}",
   "httpProtocolIpv6": "{{string}}",
   "httpPutResponseHopLimit": {{number}},
   "httpTokens": "{{string}}",
   "instanceName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateInstanceMetadataOptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [httpEndpoint](#API_UpdateInstanceMetadataOptions_RequestSyntax) **   <a name="Lightsail-UpdateInstanceMetadataOptions-request-httpEndpoint"></a>
Enables or disables the HTTP metadata endpoint on your instances. If this parameter is not specified, the existing state is maintained.
If you specify a value of `disabled`, you cannot access your instance metadata.
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** [httpProtocolIpv6](#API_UpdateInstanceMetadataOptions_RequestSyntax) **   <a name="Lightsail-UpdateInstanceMetadataOptions-request-httpProtocolIpv6"></a>
Enables or disables the IPv6 endpoint for the instance metadata service. This setting applies only when the HTTP metadata endpoint is enabled.
This parameter is available only for instances in the Europe (Stockholm) AWS Region (`eu-north-1`).
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** [httpPutResponseHopLimit](#API_UpdateInstanceMetadataOptions_RequestSyntax) **   <a name="Lightsail-UpdateInstanceMetadataOptions-request-httpPutResponseHopLimit"></a>
The desired HTTP PUT response hop limit for instance metadata requests. A larger number means that the instance metadata requests can travel farther. If no parameter is specified, the existing state is maintained.
Type: Integer
Required: No

 ** [httpTokens](#API_UpdateInstanceMetadataOptions_RequestSyntax) **   <a name="Lightsail-UpdateInstanceMetadataOptions-request-httpTokens"></a>
The state of token usage for your instance metadata requests. If the parameter is not specified in the request, the default state is `optional`.
If the state is `optional`, you can choose whether to retrieve instance metadata with a signed token header on your request. If you retrieve the IAM role credentials without a token, the version 1.0 role credentials are returned. If you retrieve the IAM role credentials by using a valid signed token, the version 2.0 role credentials are returned.
If the state is `required`, you must send a signed token header with all instance metadata retrieval requests. In this state, retrieving the IAM role credential always returns the version 2.0 credentials. The version 1.0 credentials are not available.
Type: String
Valid Values: `optional | required`
Required: No

 ** [instanceName](#API_UpdateInstanceMetadataOptions_RequestSyntax) **   <a name="Lightsail-UpdateInstanceMetadataOptions-request-instanceName"></a>
The name of the instance for which to update metadata parameters.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_UpdateInstanceMetadataOptions_ResponseSyntax"></a>

```
{
   "operation": {
      "createdAt": number,
      "errorCode": "string",
      "errorDetails": "string",
      "id": "string",
      "isTerminal": boolean,
      "location": {
         "availabilityZone": "string",
         "regionName": "string"
      },
      "operationDetails": "string",
      "operationType": "string",
      "resourceName": "string",
      "resourceType": "string",
      "status": "string",
      "statusChangedAt": number
   }
}
```

## Response Elements
<a name="API_UpdateInstanceMetadataOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_UpdateInstanceMetadataOptions_ResponseSyntax) **   <a name="Lightsail-UpdateInstanceMetadataOptions-response-operation"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_UpdateInstanceMetadataOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** AccountSetupInProgressException **
Lightsail throws this exception when an account is still in the setup in progress state.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_UpdateInstanceMetadataOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/UpdateInstanceMetadataOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/UpdateInstanceMetadataOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/UpdateInstanceMetadataOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/UpdateInstanceMetadataOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/UpdateInstanceMetadataOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/UpdateInstanceMetadataOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/UpdateInstanceMetadataOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/UpdateInstanceMetadataOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/UpdateInstanceMetadataOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/UpdateInstanceMetadataOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
