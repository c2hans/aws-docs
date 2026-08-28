---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetResourcesV2.html
---

# GetResourcesV2
<a name="API_GetResourcesV2"></a>

Returns a list of resources.

You can use the `Scopes` parameter to define the data boundary for the query. Currently, `Scopes` supports `AwsOrganizations`, which lets you retrieve resources from your entire organization or from specific organizational units. Only the delegated administrator account can use `Scopes`.

You can use the `Filters` parameter to refine results based on resource attributes. You can use `Scopes` and `Filters` independently or together. When both are provided, `Scopes` narrows the data set first, and then `Filters` refines results within that scoped data set.

For AI/ML resources, the response includes the `ResourceSubCategory` field. For self-hosted AI resources and their host resources, the response also includes `ResourceInfo` with AI-specific details. Self-hosted AI resources use a `ResourceType` with the `SelfHosted::AI::` prefix, such as `SelfHosted::AI::Model`, `SelfHosted::AI::Agent`, `SelfHosted::AI::InferenceEndpoint`, and `SelfHosted::AI::ExternalEndpoint`.

If you filter by `ResourceSubCategory`, you must also include a `ResourceCategory` string filter with comparison set to `EQUALS` and value `AI/ML` in the same request.

## Request Syntax
<a name="API_GetResourcesV2_RequestSyntax"></a>

```
POST /resourcesv2 HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "CompositeFilters": [
         {
            "DateFilters": [
               {
                  "FieldName": "{{string}}",
                  "Filter": {
                     "DateRange": {
                        "Comparison": "{{string}}",
                        "Unit": "{{string}}",
                        "Value": {{number}}
                     },
                     "End": "{{string}}",
                     "Start": "{{string}}"
                  }
               }
            ],
            "MapFilters": [
               {
                  "FieldName": "{{string}}",
                  "Filter": {
                     "Comparison": "{{string}}",
                     "Key": "{{string}}",
                     "Value": "{{string}}"
                  }
               }
            ],
            "NestedCompositeFilters": [
               "ResourcesCompositeFilter"
            ],
            "NumberFilters": [
               {
                  "FieldName": "{{string}}",
                  "Filter": {
                     "Eq": {{number}},
                     "Gt": {{number}},
                     "Gte": {{number}},
                     "Lt": {{number}},
                     "Lte": {{number}}
                  }
               }
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
<a name="API_GetResourcesV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetResourcesV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_GetResourcesV2_RequestSyntax) **   <a name="securityhub-GetResourcesV2-request-Filters"></a>
Filters resources based on a set of criteria.
Type: [ResourcesFilters](API_ResourcesFilters.md) object
Required: No

 ** [MaxResults](#API_GetResourcesV2_RequestSyntax) **   <a name="securityhub-GetResourcesV2-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetResourcesV2_RequestSyntax) **   <a name="securityhub-GetResourcesV2-request-NextToken"></a>
The token required for pagination. On your first call, set the value of this parameter to `NULL`. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.
Type: String
Required: No

 ** [Scopes](#API_GetResourcesV2_RequestSyntax) **   <a name="securityhub-GetResourcesV2-request-Scopes"></a>
Limits the results to resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an `AccessDeniedException`.
This parameter is optional. If you omit it, the delegated administrator sees resources from all accounts across the entire organization. Other accounts see only their own resources.
You can specify up to 10 entries in `Scopes.AwsOrganizations`. If multiple entries are specified, the entries are combined using OR logic.
Type: [ResourceScopes](API_ResourceScopes.md) object
Required: No

 ** [SortCriteria](#API_GetResourcesV2_RequestSyntax) **   <a name="securityhub-GetResourcesV2-request-SortCriteria"></a>
The resource attributes used to sort the list of returned resources.
Type: Array of [SortCriterion](API_SortCriterion.md) objects
Required: No

## Response Syntax
<a name="API_GetResourcesV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Resources": [
      {
         "AccountId": "string",
         "AccountName": "string",
         "DiscoveryType": "string",
         "FindingsSummary": [
            {
               "FindingType": "string",
               "ProductName": "string",
               "Severities": {
                  "Critical": number,
                  "Fatal": number,
                  "High": number,
                  "Informational": number,
                  "Low": number,
                  "Medium": number,
                  "Other": number,
                  "Unknown": number
               },
               "TotalFindings": number
            }
         ],
         "Region": "string",
         "ResourceCategory": "string",
         "ResourceCloudPartition": "string",
         "ResourceConfig": JSON value,
         "ResourceCreationTimeDt": "string",
         "ResourceDetailCaptureTimeDt": "string",
         "ResourceGuid": "string",
         "ResourceId": "string",
         "ResourceInfo": {
            "AIDetails": {
               "CanonicalId": "string",
               "HostResourceGuid": "string",
               "HostResourceType": "string",
               "SelfHostedAIAgentFrameworkResourceCount": number,
               "SelfHostedAIAgentResourceCount": number,
               "SelfHostedAIAgentToolsAndIdentityResourceCount": number,
               "SelfHostedAIDevelopmentResourceCount": number,
               "SelfHostedAIExternalEndpointResourceCount": number,
               "SelfHostedAIModelResourceCount": number,
               "SelfHostedAIModelServingResourceCount": number,
               "SelfHostedTotalAIResourceCount": number
            }
         },
         "ResourceName": "string",
         "ResourceOwnerAccountId": "string",
         "ResourceOwnerOrgId": "string",
         "ResourceProvider": "string",
         "ResourceRegion": "string",
         "ResourceSubCategory": "string",
         "ResourceTags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "ResourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetResourcesV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetResourcesV2_ResponseSyntax) **   <a name="securityhub-GetResourcesV2-response-NextToken"></a>
The pagination token to use to request the next page of results. Otherwise, this parameter is null.
Type: String

 ** [Resources](#API_GetResourcesV2_ResponseSyntax) **   <a name="securityhub-GetResourcesV2-response-Resources"></a>
An array of resources returned by the operation.
Type: Array of [ResourceResult](API_ResourceResult.md) objects

## Errors
<a name="API_GetResourcesV2_Errors"></a>

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
<a name="API_GetResourcesV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetResourcesV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetResourcesV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetResourcesV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetResourcesV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetResourcesV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetResourcesV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetResourcesV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetResourcesV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetResourcesV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetResourcesV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
