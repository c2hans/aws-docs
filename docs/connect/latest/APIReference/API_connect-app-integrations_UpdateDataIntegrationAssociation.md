---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_UpdateDataIntegrationAssociation.html
---

# UpdateDataIntegrationAssociation
<a name="API_connect-app-integrations_UpdateDataIntegrationAssociation"></a>

Updates and persists a DataIntegrationAssociation resource.

**Note**
 Updating a DataIntegrationAssociation with ExecutionConfiguration will rerun the on-demand job.

## Request Syntax
<a name="API_connect-app-integrations_UpdateDataIntegrationAssociation_RequestSyntax"></a>

```
PATCH /dataIntegrations/{{Identifier}}/associations/{{DataIntegrationAssociationIdentifier}} HTTP/1.1
Content-type: application/json

{
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
   }
}
```

## URI Request Parameters
<a name="API_connect-app-integrations_UpdateDataIntegrationAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataIntegrationAssociationIdentifier](#API_connect-app-integrations_UpdateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateDataIntegrationAssociation-request-uri-DataIntegrationAssociationIdentifier"></a>
A unique identifier. of the DataIntegrationAssociation resource
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: Yes

 ** [Identifier](#API_connect-app-integrations_UpdateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateDataIntegrationAssociation-request-uri-DataIntegrationIdentifier"></a>
A unique identifier for the DataIntegration.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_connect-app-integrations_UpdateDataIntegrationAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExecutionConfiguration](#API_connect-app-integrations_UpdateDataIntegrationAssociation_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateDataIntegrationAssociation-request-ExecutionConfiguration"></a>
The configuration for how the files should be pulled from the source.
Type: [ExecutionConfiguration](API_connect-app-integrations_ExecutionConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_connect-app-integrations_UpdateDataIntegrationAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-app-integrations_UpdateDataIntegrationAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-app-integrations_UpdateDataIntegrationAssociation_Errors"></a>

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_connect-app-integrations_UpdateDataIntegrationAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/UpdateDataIntegrationAssociation)
