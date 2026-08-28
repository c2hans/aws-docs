---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DissociatePackage.html
---

# DissociatePackage
<a name="API_DissociatePackage"></a>

Removes a package from the specified Amazon OpenSearch Service domain. The package can't be in use with any OpenSearch index for the dissociation to succeed. The package is still available in OpenSearch Service for association later. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Request Syntax
<a name="API_DissociatePackage_RequestSyntax"></a>

```
POST /2021-01-01/packages/dissociate/{{PackageID}}/{{DomainName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DissociatePackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_DissociatePackage_RequestSyntax) **   <a name="opensearchservice-DissociatePackage-request-uri-DomainName"></a>
Name of the domain to dissociate the package from.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [PackageID](#API_DissociatePackage_RequestSyntax) **   <a name="opensearchservice-DissociatePackage-request-uri-PackageID"></a>
Internal ID of the package to dissociate from the domain. Use `ListPackagesForDomain` to find this value.
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: Yes

## Request Body
<a name="API_DissociatePackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DissociatePackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainPackageDetails": {
      "AssociationConfiguration": {
         "KeyStoreAccessOption": {
            "KeyAccessRoleArn": "string",
            "KeyStoreAccessEnabled": boolean
         }
      },
      "DomainName": "string",
      "DomainPackageStatus": "string",
      "ErrorDetails": {
         "ErrorMessage": "string",
         "ErrorType": "string"
      },
      "LastUpdated": number,
      "PackageID": "string",
      "PackageName": "string",
      "PackageType": "string",
      "PackageVersion": "string",
      "PrerequisitePackageIDList": [ "string" ],
      "ReferencePath": "string"
   }
}
```

## Response Elements
<a name="API_DissociatePackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainPackageDetails](#API_DissociatePackage_ResponseSyntax) **   <a name="opensearchservice-DissociatePackage-response-DomainPackageDetails"></a>
 Information about a package that has been dissociated from the domain.
Type: [DomainPackageDetails](API_DomainPackageDetails.md) object

## Errors
<a name="API_DissociatePackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DissociatePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DissociatePackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DissociatePackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DissociatePackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DissociatePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DissociatePackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DissociatePackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DissociatePackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DissociatePackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DissociatePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DissociatePackage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
