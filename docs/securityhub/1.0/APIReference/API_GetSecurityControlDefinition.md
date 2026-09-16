---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetSecurityControlDefinition.html
---

# GetSecurityControlDefinition
<a name="API_GetSecurityControlDefinition"></a>

 Retrieves the definition of a security control. The definition includes the control title, description, Region availability, parameter definitions, and other details.

## Request Syntax
<a name="API_GetSecurityControlDefinition_RequestSyntax"></a>

```
GET /securityControl/definition?SecurityControlId={{SecurityControlId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSecurityControlDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SecurityControlId](#API_GetSecurityControlDefinition_RequestSyntax) **   <a name="securityhub-GetSecurityControlDefinition-request-uri-SecurityControlId"></a>
 The ID of the security control to retrieve the definition for. This field doesn’t accept an Amazon Resource Name (ARN).
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetSecurityControlDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSecurityControlDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SecurityControlDefinition": {
      "CurrentRegionAvailability": "string",
      "CustomizableProperties": [ "string" ],
      "Description": "string",
      "ParameterDefinitions": {
         "string" : {
            "ConfigurationOptions": { ... },
            "Description": "string"
         }
      },
      "Provider": "string",
      "RemediationUrl": "string",
      "SecurityControlId": "string",
      "SeverityRating": "string",
      "Title": "string"
   }
}
```

## Response Elements
<a name="API_GetSecurityControlDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SecurityControlDefinition](#API_GetSecurityControlDefinition_ResponseSyntax) **   <a name="securityhub-GetSecurityControlDefinition-response-SecurityControlDefinition"></a>
 Provides metadata for a security control, including its unique standard-agnostic identifier, title, description, severity, availability in AWS Regions, and a link to remediation steps.
Type: [SecurityControlDefinition](API_SecurityControlDefinition.md) object

## Errors
<a name="API_GetSecurityControlDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_GetSecurityControlDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetSecurityControlDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetSecurityControlDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetSecurityControlDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetSecurityControlDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetSecurityControlDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetSecurityControlDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetSecurityControlDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetSecurityControlDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetSecurityControlDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetSecurityControlDefinition)
