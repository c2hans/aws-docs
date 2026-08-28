---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteSigningConfiguration.html
---

# DeleteSigningConfiguration
<a name="API_DeleteSigningConfiguration"></a>

Deletes the registry's signing configuration. Images pushed after deletion of the signing configuration will no longer be automatically signed.

For more information, see [Managed signing](https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html) in the *Amazon Elastic Container Registry User Guide*.

**Note**
Deleting the signing configuration does not affect existing image signatures.

## Response Syntax
<a name="API_DeleteSigningConfiguration_ResponseSyntax"></a>

```
{
   "registryId": "string",
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
<a name="API_DeleteSigningConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryId](#API_DeleteSigningConfiguration_ResponseSyntax) **   <a name="ECR-DeleteSigningConfiguration-response-registryId"></a>
The AWS account ID associated with the registry.
Type: String
Pattern: `[0-9]{12}`

 ** [signingConfiguration](#API_DeleteSigningConfiguration_ResponseSyntax) **   <a name="ECR-DeleteSigningConfiguration-response-signingConfiguration"></a>
The registry's deleted signing configuration.
Type: [SigningConfiguration](API_SigningConfiguration.md) object

## Errors
<a name="API_DeleteSigningConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** SigningConfigurationNotFoundException **
The specified signing configuration was not found. This occurs when attempting to retrieve or delete a signing configuration that does not exist.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSigningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DeleteSigningConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DeleteSigningConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DeleteSigningConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DeleteSigningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DeleteSigningConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DeleteSigningConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DeleteSigningConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DeleteSigningConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DeleteSigningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DeleteSigningConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
