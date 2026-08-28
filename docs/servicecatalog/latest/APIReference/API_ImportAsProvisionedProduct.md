---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ImportAsProvisionedProduct.html
---

# ImportAsProvisionedProduct
<a name="API_ImportAsProvisionedProduct"></a>

 Requests the import of a resource as an AWS Service Catalog provisioned product that is associated to an AWS Service Catalog product and provisioning artifact. Once imported, all supported governance actions are supported on the provisioned product.

 Resource import only supports AWS CloudFormation stack ARNs. AWS CloudFormation StackSets, and non-root nested stacks, are not supported.

 The AWS CloudFormation stack must have one of the following statuses to be imported: `CREATE_COMPLETE`, `UPDATE_COMPLETE`, `UPDATE_ROLLBACK_COMPLETE`, `IMPORT_COMPLETE`, and `IMPORT_ROLLBACK_COMPLETE`.

 Import of the resource requires that the AWS CloudFormation stack template matches the associated AWS Service Catalog product provisioning artifact.

**Note**
 When you import an existing AWS CloudFormation stack into a portfolio, AWS Service Catalog does not apply the product's associated constraints during the import process. AWS Service Catalog applies the constraints after you call `UpdateProvisionedProduct` for the provisioned product.

 The user or role that performs this operation must have the `cloudformation:GetTemplate` and `cloudformation:DescribeStacks` IAM policy permissions.

You can only import one provisioned product at a time. The product's AWS CloudFormation stack must have the `IMPORT_COMPLETE` status before you import another.

## Request Syntax
<a name="API_ImportAsProvisionedProduct_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "PhysicalId": "{{string}}",
   "ProductId": "{{string}}",
   "ProvisionedProductName": "{{string}}",
   "ProvisioningArtifactId": "{{string}}"
}
```

## Request Parameters
<a name="API_ImportAsProvisionedProduct_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ImportAsProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-ImportAsProvisionedProduct-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IdempotencyToken](#API_ImportAsProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-ImportAsProvisionedProduct-request-IdempotencyToken"></a>
A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [PhysicalId](#API_ImportAsProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-ImportAsProvisionedProduct-request-PhysicalId"></a>
The unique identifier of the resource to be imported. It only currently supports AWS CloudFormation stack IDs.
Type: String
Required: Yes

 ** [ProductId](#API_ImportAsProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-ImportAsProvisionedProduct-request-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [ProvisionedProductName](#API_ImportAsProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-ImportAsProvisionedProduct-request-ProvisionedProductName"></a>
The user-friendly name of the provisioned product. The value must be unique for the AWS account. The name cannot be updated after the product is provisioned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`
Required: Yes

 ** [ProvisioningArtifactId](#API_ImportAsProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-ImportAsProvisionedProduct-request-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_ImportAsProvisionedProduct_ResponseSyntax"></a>

```
{
   "RecordDetail": {
      "CreatedTime": number,
      "LaunchRoleArn": "string",
      "PathId": "string",
      "ProductId": "string",
      "ProvisionedProductId": "string",
      "ProvisionedProductName": "string",
      "ProvisionedProductType": "string",
      "ProvisioningArtifactId": "string",
      "RecordErrors": [
         {
            "Code": "string",
            "Description": "string"
         }
      ],
      "RecordId": "string",
      "RecordTags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "RecordType": "string",
      "Status": "string",
      "UpdatedTime": number
   }
}
```

## Response Elements
<a name="API_ImportAsProvisionedProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RecordDetail](#API_ImportAsProvisionedProduct_ResponseSyntax) **   <a name="servicecatalog-ImportAsProvisionedProduct-response-RecordDetail"></a>
Information about a request operation.
Type: [RecordDetail](API_RecordDetail.md) object

## Errors
<a name="API_ImportAsProvisionedProduct_Errors"></a>

 ** DuplicateResourceException **
The specified resource is a duplicate.
HTTP Status Code: 400

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** InvalidStateException **
An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ImportAsProvisionedProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ImportAsProvisionedProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ImportAsProvisionedProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ImportAsProvisionedProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ImportAsProvisionedProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ImportAsProvisionedProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ImportAsProvisionedProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ImportAsProvisionedProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
