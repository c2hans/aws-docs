---
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_SearchDiscoverableRegistryRecords.html
---

# SearchDiscoverableRegistryRecords

 Searches the discoverable registry records in a registry using a natural language query. Returns metadata for the matching records ordered by relevance.

 Returns at most 1000 results across all pages when `searchType` is `KEYWORD`, and at most 20 results when it is `HYBRID` or `SEMANTIC`. To retrieve more records, refine the query or filters, or use `ListDiscoverableRegistryRecords` to list every record.

## Request Syntax
<a name="API_SearchDiscoverableRegistryRecords_RequestSyntax"></a>

```
POST /discoverable-records-search HTTP/1.1
Content-type: application/json

{
   "filters": {{JSON value}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryIds": [ "{{string}}" ],
   "searchQuery": "{{string}}",
   "searchType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchDiscoverableRegistryRecords_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchDiscoverableRegistryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-filters"></a>
 An optional structured JSON metadata filter that narrows the search results. Supports the field-level operators `$eq`, `$ne`, and `$in`, and the logical operators `$and` and `$or` on filterable fields.
 Specifies additional filtering on custom metadata fields using the `customMetadata.{key}` prefix. For example, to filter by a custom metadata field: `{"customMetadata.environment": {"$eq": "production"}}`. For a Boolean field, you can also use a native JSON boolean value, for example: `{"customMetadata.requiresApproval": {"$eq": true}}`.
Type: JSON value
Required: No

 ** [maxResults](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-maxResults"></a>
 The maximum number of results to return in one page. Valid values are 1 through 50 when `searchType` is `KEYWORD`, and 1 through 20 when it is `HYBRID` or `SEMANTIC`. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-nextToken"></a>
 The pagination token from a previous response. Use it to retrieve the next page of results, and send the same `searchQuery`, `registryIds`, `filters`, and `searchType` that you used for the first page. If any of them differ, the request fails with a `ValidationException`. A pagination token expires 15 minutes after the service returns the first page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [registryIds](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-registryIds"></a>
 The registry identifiers to search within. Currently, you must specify exactly one registry identifier. You can provide either the full AWS Resource Name (ARN) or the registry ID.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`
Required: Yes

 ** [searchQuery](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-searchQuery"></a>
 The natural language query to search for matching registry records. If you specify an empty string, the operation returns the records that match the `filters`, most recently updated first, up to the result limit for the `searchType`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [searchType](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-searchType"></a>
 Specifies how the service ranks registry records against the search query. If you omit this parameter, the service uses `HYBRID` in AWS Regions that support semantic search and `KEYWORD` in Regions that do not. The response reports the search type that the service used. Valid values are the following:
+  `KEYWORD` – Ranks records by keyword match between the query terms and the record name, description, descriptors, and custom metadata text values. Available in every AWS Region.
+  `SEMANTIC` – Ranks records by semantic similarity to the query and returns the most similar records, up to `maxResults`, even when none of them closely matches the query.
+  `HYBRID` – Combines keyword ranking and semantic ranking.
 `HYBRID` and `SEMANTIC` are available in a limited number of Regions. If you specify either one in a Region that does not support semantic search, the request fails with a `ValidationException` that has the reason `UnsupportedInRegion`.
Type: String
Valid Values: `HYBRID | SEMANTIC | KEYWORD`
Required: No

## Response Syntax
<a name="API_SearchDiscoverableRegistryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "registryRecords": [
      {
         "artifact": {
            "downloadUrl": "string",
            "sha256": "string"
         },
         "createdAt": "string",
         "customMetadata": JSON value,
         "description": "string",
         "descriptors": {
            "a2aAgentCard": {
               "data": "string",
               "dataSchemaVersion": "string",
               "source": {
                  "fromUrl": {
                     "url": "string"
                  }
               }
            },
            "agentSkillsDefinition": {
               "additionalData": {
                  "skillMd": {
                     "data": "string",
                     "dataSchemaVersion": "string",
                     "source": {
                        "fromUrl": {
                           "url": "string"
                        }
                     }
                  }
               },
               "data": "string",
               "dataSchemaVersion": "string"
            },
            "agui": {
               "source": {
                  "fromUrl": {
                     "url": "string"
                  }
               }
            },
            "custom": {
               "data": "string"
            },
            "http": {
               "source": {
                  "fromUrl": {
                     "url": "string"
                  }
               }
            },
            "mcpServer": {
               "additionalData": {
                  "tools": {
                     "data": "string",
                     "dataSchemaVersion": "string"
                  }
               },
               "data": "string",
               "dataSchemaVersion": "string",
               "source": {
                  "fromUrl": {
                     "url": "string"
                  }
               }
            },
            "signatureAgentCard": {
               "additionalData": {
                  "category": "string"
               },
               "data": "string",
               "dataSchemaVersion": "string",
               "source": {
                  "fromUrl": {
                     "url": "string"
                  }
               }
            }
         },
         "displayName": "string",
         "name": "string",
         "recordArn": "string",
         "recordId": "string",
         "recordType": "string",
         "recordVersion": "string",
         "registryArn": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ],
   "searchType": "string"
}
```

## Response Elements
<a name="API_SearchDiscoverableRegistryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_SearchDiscoverableRegistryRecords_ResponseSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-response-nextToken"></a>
 The pagination token to pass to a subsequent request to retrieve the next page of results. This field is absent when there are no more results, or when the search has returned the maximum number of results for its search type.
Type: String

 ** [registryRecords](#API_SearchDiscoverableRegistryRecords_ResponseSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-response-registryRecords"></a>
 The registry records that match the search query, ordered by relevance. A page can contain fewer than `maxResults` records, or none, even when the response includes a `nextToken`. To retrieve every result, continue until the response has no `nextToken`.
Type: Array of [RegistryRecordSummary](API_RegistryRecordSummary.md) objects

 ** [searchType](#API_SearchDiscoverableRegistryRecords_ResponseSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-response-searchType"></a>
 Specifies the search type that the service used to rank the returned records. If you omitted `searchType` in the request, this is the default for the AWS Region: `HYBRID` where semantic search is supported, and `KEYWORD` elsewhere.
Type: String
Valid Values: `HYBRID | SEMANTIC | KEYWORD`

## Errors
<a name="API_SearchDiscoverableRegistryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform the requested action.
HTTP Status Code: 403

 ** InternalServerException **
The request failed due to an unexpected internal error; the caller may retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling; the caller may retry after a delay.
HTTP Status Code: 429

 ** UnauthorizedException **
The request could not be authenticated.
HTTP Status Code: 401

 ** ValidationException **
The request failed validation of one or more input fields.
 ** fieldList **
The list of input fields that failed validation.
 ** reason **
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_SearchDiscoverableRegistryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords)
