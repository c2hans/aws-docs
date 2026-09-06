---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribePackages.html
---

# DescribePackages
<a name="API_DescribePackages"></a>

Describes all packages available to OpenSearch Service. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Request Syntax
<a name="API_DescribePackages_RequestSyntax"></a>

```
POST /2021-01-01/packages/describe HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Value": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribePackages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribePackages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribePackages_RequestSyntax) **   <a name="opensearchservice-DescribePackages-request-Filters"></a>
Only returns packages that match the `DescribePackagesFilterList` values.
Type: Array of [DescribePackagesFilter](API_DescribePackagesFilter.md) objects
Required: No

 ** [MaxResults](#API_DescribePackages_RequestSyntax) **   <a name="opensearchservice-DescribePackages-request-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribePackages_RequestSyntax) **   <a name="opensearchservice-DescribePackages-request-NextToken"></a>
If your initial `DescribePackageFilters` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `DescribePackageFilters` operations, which returns results in the next page.
Type: String
Required: No

## Response Syntax
<a name="API_DescribePackages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "PackageDetailsList": [
      {
         "AllowListedUserList": [ "string" ],
         "AvailablePackageConfiguration": {
            "ConfigurationRequirement": "string",
            "LicenseFilepath": "string",
            "LicenseRequirement": "string",
            "RequiresRestartForConfigurationUpdate": boolean
         },
         "AvailablePackageVersion": "string",
         "AvailablePluginProperties": {
            "ClassName": "string",
            "Description": "string",
            "Name": "string",
            "UncompressedSizeInBytes": number,
            "Version": "string"
         },
         "CreatedAt": number,
         "EngineVersion": "string",
         "ErrorDetails": {
            "ErrorMessage": "string",
            "ErrorType": "string"
         },
         "LastUpdatedAt": number,
         "PackageDescription": "string",
         "PackageEncryptionOptions": {
            "EncryptionEnabled": boolean,
            "KmsKeyIdentifier": "string"
         },
         "PackageID": "string",
         "PackageName": "string",
         "PackageOwner": "string",
         "PackageStatus": "string",
         "PackageType": "string",
         "PackageVendingOptions": {
            "VendingEnabled": boolean
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribePackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribePackages_ResponseSyntax) **   <a name="opensearchservice-DescribePackages-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

 ** [PackageDetailsList](#API_DescribePackages_ResponseSyntax) **   <a name="opensearchservice-DescribePackages-response-PackageDetailsList"></a>
Basic information about a package.
Type: Array of [PackageDetails](API_PackageDetails.md) objects

## Errors
<a name="API_DescribePackages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

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
<a name="API_DescribePackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribePackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribePackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribePackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribePackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribePackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribePackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribePackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribePackages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribePackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribePackages)
