---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_BatchAssociateServiceActionWithProvisioningArtifact.html
---

# BatchAssociateServiceActionWithProvisioningArtifact
<a name="API_BatchAssociateServiceActionWithProvisioningArtifact"></a>

Associates multiple self-service actions with provisioning artifacts.

## Request Syntax
<a name="API_BatchAssociateServiceActionWithProvisioningArtifact_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "ServiceActionAssociations": [
      {
         "ProductId": "{{string}}",
         "ProvisioningArtifactId": "{{string}}",
         "ServiceActionId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchAssociateServiceActionWithProvisioningArtifact_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_BatchAssociateServiceActionWithProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-BatchAssociateServiceActionWithProvisioningArtifact-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [ServiceActionAssociations](#API_BatchAssociateServiceActionWithProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-BatchAssociateServiceActionWithProvisioningArtifact-request-ServiceActionAssociations"></a>
One or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.
Type: Array of [ServiceActionAssociation](API_ServiceActionAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_BatchAssociateServiceActionWithProvisioningArtifact_ResponseSyntax"></a>

```
{
   "FailedServiceActionAssociations": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "ProductId": "string",
         "ProvisioningArtifactId": "string",
         "ServiceActionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchAssociateServiceActionWithProvisioningArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedServiceActionAssociations](#API_BatchAssociateServiceActionWithProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-BatchAssociateServiceActionWithProvisioningArtifact-response-FailedServiceActionAssociations"></a>
An object that contains a list of errors, along with information to help you identify the self-service action.
Type: Array of [FailedServiceActionAssociation](API_FailedServiceActionAssociation.md) objects
Array Members: Maximum number of 50 items.

## Errors
<a name="API_BatchAssociateServiceActionWithProvisioningArtifact_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchAssociateServiceActionWithProvisioningArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
