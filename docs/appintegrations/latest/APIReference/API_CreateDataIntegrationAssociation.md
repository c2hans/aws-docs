---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegrationAssociation.html
---

# CreateDataIntegrationAssociation
<a name="API_connect-app-integrations_CreateDataIntegrationAssociation"></a>

Creates and persists a DataIntegrationAssociation resource.

## Request Syntax
<a name="API_connect-app-integrations_CreateDataIntegrationAssociation_RequestSyntax"></a>

```
POST /dataIntegrations/{{Identifier}}/associations HTTP/1.1
Content-type: application/json

{
   "ClientAssociationMetadata": {
      "{{string}}" : "{{string}}"
   },
   "ClientId": "{{string}}",
   "ClientToken": "{{string}}",
   "DestinationURI": "{{string}}",
   "ExecutionConfiguration": {
      "ExecutionMode": "{{string}}",
      "OnDemandConfiguration": {
         "EndTime": "{{string}}",
         "StartTime": "{{string}}"
      },
      "ScheduleConfiguration": {
         "FirstExecutionFrom": "{{string}}",
         "Object": "{{string}}",
         "ScheduleExpression": "{{string}}"
      }
   },
   "ObjectConfiguration": {
      "{{string}}" : {
         "{{string}}" : [ "{{string}}" ]
      }
   }
}
```

## URI Request Parameters
<a name="API_connect-app-integrations_CreateDataIntegrationAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_connect-app-integrations_CreateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegrationAssociation-request-uri-DataIntegrationIdentifier"></a>
A unique identifier for the DataIntegration.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_connect-app-integrations_CreateDataIntegrationAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientAssociationMetadata](#API_connect-app-integrations_CreateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegrationAssociation-request-ClientAssociationMetadata"></a>
The mapping of metadata to be extracted from the data.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `.*\S.*`
Required: No

 ** [ClientId](#API_connect-app-integrations_CreateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegrationAssociation-request-ClientId"></a>
The identifier for the client that is associated with the DataIntegration association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [ClientToken](#API_connect-app-integrations_CreateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegrationAssociation-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [DestinationURI](#API_connect-app-integrations_CreateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegrationAssociation-request-DestinationURI"></a>
The URI of the data destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+$)|(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+[\w/!@#+=.-]+[\w/!@#+=.,-]+$)`
Required: No

 ** [ExecutionConfiguration](#API_connect-app-integrations_CreateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegrationAssociation-request-ExecutionConfiguration"></a>
The configuration for how the files should be pulled from the source.
Type: [ExecutionConfiguration](API_connect-app-integrations_ExecutionConfiguration.md) object
Required: No

 ** [ObjectConfiguration](#API_connect-app-integrations_CreateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegrationAssociation-request-ObjectConfiguration"></a>
The configuration for what data should be pulled from the source.
Type: String to string to array of strings map map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*\S.*`
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*\S.*`
Array Members: Minimum number of 1 item. Maximum number of 2048 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

## Response Syntax
<a name="API_connect-app-integrations_CreateDataIntegrationAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataIntegrationArn": "string",
   "DataIntegrationAssociationId": "string"
}
```

## Response Elements
<a name="API_connect-app-integrations_CreateDataIntegrationAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataIntegrationArn](#API_connect-app-integrations_CreateDataIntegrationAssociation_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegrationAssociation-response-DataIntegrationArn"></a>
The Amazon Resource Name (ARN) for the DataIntegration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [DataIntegrationAssociationId](#API_connect-app-integrations_CreateDataIntegrationAssociation_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegrationAssociation-response-DataIntegrationAssociationId"></a>
A unique identifier. for the DataIntegrationAssociation.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_connect-app-integrations_CreateDataIntegrationAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceError **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ResourceQuotaExceededException **
The allowed quota for the resource has been exceeded.
HTTP Status Code: 429

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_connect-app-integrations_CreateDataIntegrationAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/CreateDataIntegrationAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/CreateDataIntegrationAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/CreateDataIntegrationAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/CreateDataIntegrationAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/CreateDataIntegrationAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/CreateDataIntegrationAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/CreateDataIntegrationAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/CreateDataIntegrationAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/CreateDataIntegrationAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/CreateDataIntegrationAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
