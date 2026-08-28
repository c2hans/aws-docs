---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CreateCodeSigningConfig.html
---

# CreateCodeSigningConfig
<a name="API_CreateCodeSigningConfig"></a>

Creates a code signing configuration. A [code signing configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validation checks fail).

## Request Syntax
<a name="API_CreateCodeSigningConfig_RequestSyntax"></a>

```
POST /2020-04-22/code-signing-configs HTTP/1.1
Content-type: application/json

{
   "AllowedPublishers": {
      "SigningProfileVersionArns": [ "{{string}}" ]
   },
   "CodeSigningPolicies": {
      "UntrustedArtifactOnDeployment": "{{string}}"
   },
   "Description": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateCodeSigningConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCodeSigningConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowedPublishers](#API_CreateCodeSigningConfig_RequestSyntax) **   <a name="lambda-CreateCodeSigningConfig-request-AllowedPublishers"></a>
Signing profiles for this code signing configuration.
Type: [AllowedPublishers](API_AllowedPublishers.md) object
Required: Yes

 ** [CodeSigningPolicies](#API_CreateCodeSigningConfig_RequestSyntax) **   <a name="lambda-CreateCodeSigningConfig-request-CodeSigningPolicies"></a>
The code signing policies define the actions to take if the validation checks fail.
Type: [CodeSigningPolicies](API_CodeSigningPolicies.md) object
Required: No

 ** [Description](#API_CreateCodeSigningConfig_RequestSyntax) **   <a name="lambda-CreateCodeSigningConfig-request-Description"></a>
Descriptive name for this code signing configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Tags](#API_CreateCodeSigningConfig_RequestSyntax) **   <a name="lambda-CreateCodeSigningConfig-request-Tags"></a>
A list of tags to add to the code signing configuration.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateCodeSigningConfig_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "CodeSigningConfig": {
      "AllowedPublishers": {
         "SigningProfileVersionArns": [ "string" ]
      },
      "CodeSigningConfigArn": "string",
      "CodeSigningConfigId": "string",
      "CodeSigningPolicies": {
         "UntrustedArtifactOnDeployment": "string"
      },
      "Description": "string",
      "LastModified": "string"
   }
}
```

## Response Elements
<a name="API_CreateCodeSigningConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [CodeSigningConfig](#API_CreateCodeSigningConfig_ResponseSyntax) **   <a name="lambda-CreateCodeSigningConfig-response-CodeSigningConfig"></a>
The code signing configuration.
Type: [CodeSigningConfig](API_CodeSigningConfig.md) object

## Errors
<a name="API_CreateCodeSigningConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

## See Also
<a name="API_CreateCodeSigningConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/CreateCodeSigningConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/CreateCodeSigningConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CreateCodeSigningConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/CreateCodeSigningConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CreateCodeSigningConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/CreateCodeSigningConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/CreateCodeSigningConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/CreateCodeSigningConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/CreateCodeSigningConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CreateCodeSigningConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
