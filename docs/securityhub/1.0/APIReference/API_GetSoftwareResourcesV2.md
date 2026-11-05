---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetSoftwareResourcesV2.html
---

# GetSoftwareResourcesV2
<a name="API_GetSoftwareResourcesV2"></a>

Returns a list of resources that contain a specific software package. You identify the package with `PackageName` and `PackageType`. To narrow the results to one version of the package, include `PackageVersion`.

You can use the `Scopes` parameter to define the data boundary for the query. Currently, `Scopes` supports `AwsOrganizations`. With `AwsOrganizations`, you can retrieve resources from your entire organization or from specific organizational units. Only the delegated administrator account can use `Scopes`.

You can use the `Filters` parameter to further refine results based on resource attributes, such as `ResourceType` or `Region`.

This operation returns paginated results. To retrieve additional results, use the `NextToken` value from the previous response.

## Request Syntax
<a name="API_GetSoftwareResourcesV2_RequestSyntax"></a>

```
POST /softwarev2/resources HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "CompositeFilters": [
         {
            "NestedCompositeFilters": [
               "SoftwareCompositeFilter"
            ],
            "Operator": "{{string}}",
            "StringFilters": [
               {
                  "FieldName": "{{string}}",
                  "Filter": {
                     "Comparison": "{{string}}",
                     "Value": "{{string}}"
                  }
               }
            ]
         }
      ],
      "CompositeOperator": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PackageName": "{{string}}",
   "PackageType": "{{string}}",
   "PackageVersion": "{{string}}",
   "Scopes": {
      "AwsOrganizations": [
         {
            "OrganizationalUnitId": "{{string}}",
            "OrganizationId": "{{string}}"
         }
      ]
   },
   "SortCriteria": [
      {
         "Field": "{{string}}",
         "SortOrder": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_GetSoftwareResourcesV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSoftwareResourcesV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_GetSoftwareResourcesV2_RequestSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-request-Filters"></a>
Filters the returned resources based on a set of criteria. You can nest composite filters up to three levels deep.
Type: [SoftwareFilters](API_SoftwareFilters.md) object
Required: No

 ** [MaxResults](#API_GetSoftwareResourcesV2_RequestSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-request-MaxResults"></a>
The maximum number of results to return. Valid values are 1–100. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetSoftwareResourcesV2_RequestSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-request-NextToken"></a>
The token required for pagination. On your first call, set the value of this parameter to `NULL`. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.
A token expires one hour after it's issued. If you change the request parameters between calls, the token is no longer valid and the request fails with a `ValidationException`.
Type: String
Required: No

 ** [PackageName](#API_GetSoftwareResourcesV2_RequestSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-request-PackageName"></a>
The name of the software package, for example `openssl`. This value must match the `PackageName` returned by `GetSoftwareV2`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [PackageType](#API_GetSoftwareResourcesV2_RequestSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-request-PackageType"></a>
The type of the software package, for example `operating-system`, `application`, or `library`. This value must match the `PackageType` returned by `GetSoftwareV2`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [PackageVersion](#API_GetSoftwareResourcesV2_RequestSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-request-PackageVersion"></a>
The version of the software package, for example `3.0.8`. If you omit this value, the response includes resources that contain any version of the package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [Scopes](#API_GetSoftwareResourcesV2_RequestSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-request-Scopes"></a>
Limits the results to resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an `AccessDeniedException`.
This parameter is optional. If you omit it, the delegated administrator sees resources from all accounts across the entire organization. Other accounts see only their own resources.
You can specify up to 10 entries in `Scopes.AwsOrganizations`. If multiple entries are specified, the entries are combined using OR logic.
Type: [SoftwareScopes](API_SoftwareScopes.md) object
Required: No

 ** [SortCriteria](#API_GetSoftwareResourcesV2_RequestSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-request-SortCriteria"></a>
The resource attribute used to sort the list of returned resources, for example `Region` or `ResourceType`. You can specify one sort criterion.
Type: Array of [SortCriterion](API_SortCriterion.md) objects
Required: No

## Response Syntax
<a name="API_GetSoftwareResourcesV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SoftwareResources": [
      {
         "AccountId": "string",
         "Region": "string",
         "ResourceCloudPartition": "string",
         "ResourceId": "string",
         "ResourceOwnerAccountId": "string",
         "ResourceOwnerOrgId": "string",
         "ResourceProvider": "string",
         "ResourceRegion": "string",
         "ResourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetSoftwareResourcesV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetSoftwareResourcesV2_ResponseSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-response-NextToken"></a>
The pagination token to use to request the next page of results. Otherwise, this parameter is null.
Type: String

 ** [SoftwareResources](#API_GetSoftwareResourcesV2_ResponseSyntax) **   <a name="securityhub-GetSoftwareResourcesV2-response-SoftwareResources"></a>
An array of resources that contain the specified software package.
Type: Array of [SoftwareResourceResult](API_SoftwareResourceResult.md) objects

## Errors
<a name="API_GetSoftwareResourcesV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** OrganizationalUnitNotFoundException **
The request failed because one or more organizational units specified in the request don't exist within the caller's organization.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
The request failed because one or more organizations specified in the request don't exist or don't belong to the caller's organization.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_GetSoftwareResourcesV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetSoftwareResourcesV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetSoftwareResourcesV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetSoftwareResourcesV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetSoftwareResourcesV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetSoftwareResourcesV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetSoftwareResourcesV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetSoftwareResourcesV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetSoftwareResourcesV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetSoftwareResourcesV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetSoftwareResourcesV2)
