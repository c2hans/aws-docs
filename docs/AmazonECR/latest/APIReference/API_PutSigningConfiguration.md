---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutSigningConfiguration.html
---

# PutSigningConfiguration
<a name="API_PutSigningConfiguration"></a>

Creates or updates the registry's signing configuration, which defines rules for automatically signing images with AWS Signer.

For more information, see [Managed signing](https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html) in the *Amazon Elastic Container Registry User Guide*.

**Note**
To successfully generate a signature, the IAM principal pushing images must have permission to sign payloads with the AWS Signer signing profile referenced in the signing configuration.

## Request Syntax
<a name="API_PutSigningConfiguration_RequestSyntax"></a>

```
{
   "signingConfiguration": {
      "rules": [
         {
            "repositoryFilters": [
               {
                  "filter": "{{string}}",
                  "filterType": "{{string}}"
               }
            ],
            "signingProfileArn": "{{string}}"
         }
      ]
   }
}
```

## Request Parameters
<a name="API_PutSigningConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [signingConfiguration](#API_PutSigningConfiguration_RequestSyntax) **   <a name="ECR-PutSigningConfiguration-request-signingConfiguration"></a>
The signing configuration to assign to the registry.
Type: [SigningConfiguration](API_SigningConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_PutSigningConfiguration_ResponseSyntax"></a>

```
{
   "signingConfiguration": {
      "rules": [
         {
            "repositoryFilters": [
               {
                  "filter": "string",
                  "filterType": "string"
               }
            ],
            "signingProfileArn": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_PutSigningConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [signingConfiguration](#API_PutSigningConfiguration_ResponseSyntax) **   <a name="ECR-PutSigningConfiguration-response-signingConfiguration"></a>
The registry's updated signing configuration.
Type: [SigningConfiguration](API_SigningConfiguration.md) object

## Errors
<a name="API_PutSigningConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_PutSigningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/PutSigningConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/PutSigningConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/PutSigningConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/PutSigningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/PutSigningConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/PutSigningConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/PutSigningConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/PutSigningConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/PutSigningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/PutSigningConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
