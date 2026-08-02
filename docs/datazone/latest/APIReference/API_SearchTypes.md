---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SearchTypes.html
---

# SearchTypes
<a name="API_SearchTypes"></a>

Searches for types in Amazon DataZone.

Prerequisites:
+ The --domain-identifier must refer to an existing Amazon DataZone domain.
+ --search-scope must be one of the valid values including: ASSET\_TYPE, GLOSSARY\_TERM\_TYPE, DATA\_PRODUCT\_TYPE.
+ The --managed flag must be present without a value.
+ The user must have permissions for form or asset types in the domain.
+ If using --filters, ensure that the JSON is valid.
+ Filters contain correct structure (attribute, value, operator).

## Request Syntax
<a name="API_SearchTypes_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/types-search HTTP/1.1
Content-type: application/json

{
   "filters": { ... },
   "managed": {{boolean}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "searchIn": [
      {
         "attribute": "{{string}}"
      }
   ],
   "searchScope": "{{string}}",
   "searchText": "{{string}}",
   "sort": {
      "attribute": "{{string}}",
      "order": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_SearchTypes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_SearchTypes_RequestSyntax) **   <a name="datazone-SearchTypes-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which to invoke the `SearchTypes` action.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_SearchTypes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchTypes_RequestSyntax) **   <a name="datazone-SearchTypes-request-filters"></a>
The filters for the `SearchTypes` action.
Type: [FilterClause](API_FilterClause.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [managed](#API_SearchTypes_RequestSyntax) **   <a name="datazone-SearchTypes-request-managed"></a>
Specifies whether the search is managed.
Type: Boolean
Required: Yes

 ** [maxResults](#API_SearchTypes_RequestSyntax) **   <a name="datazone-SearchTypes-request-maxResults"></a>
The maximum number of results to return in a single call to `SearchTypes`. When the number of results to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `SearchTypes` to list the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_SearchTypes_RequestSyntax) **   <a name="datazone-SearchTypes-request-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `SearchTypes` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [searchIn](#API_SearchTypes_RequestSyntax) **   <a name="datazone-SearchTypes-request-searchIn"></a>
The details of the search.
Type: Array of [SearchInItem](API_SearchInItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [searchScope](#API_SearchTypes_RequestSyntax) **   <a name="datazone-SearchTypes-request-searchScope"></a>
Specifies the scope of the search for types.
Type: String
Valid Values: `ASSET_TYPE | FORM_TYPE | LINEAGE_NODE_TYPE`
Required: Yes

 ** [searchText](#API_SearchTypes_RequestSyntax) **   <a name="datazone-SearchTypes-request-searchText"></a>
Specifies the text for which to search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [sort](#API_SearchTypes_RequestSyntax) **   <a name="datazone-SearchTypes-request-sort"></a>
The specifies the way to sort the `SearchTypes` results.
Type: [SearchSort](API_SearchSort.md) object
Required: No

## Response Syntax
<a name="API_SearchTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      { ... }
   ],
   "nextToken": "string",
   "totalMatchCount": number
}
```

## Response Elements
<a name="API_SearchTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_SearchTypes_ResponseSyntax) **   <a name="datazone-SearchTypes-response-items"></a>
The results of the `SearchTypes` action.
Type: Array of [SearchTypesResultItem](API_SearchTypesResultItem.md) objects

 ** [nextToken](#API_SearchTypes_ResponseSyntax) **   <a name="datazone-SearchTypes-response-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `SearchTypes` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [totalMatchCount](#API_SearchTypes_ResponseSyntax) **   <a name="datazone-SearchTypes-response-totalMatchCount"></a>
Total number of search results.
Type: Integer

## Errors
<a name="API_SearchTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## Examples
<a name="API_SearchTypes_Examples"></a>

### Example
<a name="API_SearchTypes_Example_1"></a>

This example illustrates one usage of SearchTypes.

#### Sample Request
<a name="API_SearchTypes_Example_1_Request"></a>

```
aws datazone search-types \
--domain-identifier "dzd_53ielnpxktdilj" \
--search-scope "ASSET_TYPE" \
--managed
```

#### Sample Response
<a name="API_SearchTypes_Example_1_Response"></a>

```
{
    "items": [
        {
            "assetTypeItem": {
                "createdAt": 1752170908.272,
                "createdBy": "SYSTEM",
                "domainId": "dzd_53ielnpxktdilj",
                "formsOutput": {
                    "AssetCommonDetailsForm": {
                        "required": true,
                        "typeName": "amazon.datazone.AssetCommonDetailsFormType",
                        "typeRevision": "6"
                    },
                    "SageMakerFeatureGroupForm": {
                        "required": true,
                        "typeName": "amazon.datazone.SageMakerFeatureGroupFormType",
                        "typeRevision": "1"
                    }
                },
                "name": "amazon.datazone.SageMakerFeatureGroupAssetType",
                "originDomainId": "dzd_amazon_datazone_domain",
                "originProjectId": "dzd_amazon_datazone_domain_project",
                "owningProjectId": "dzd_amazon_datazone_domain_project",
                "revision": "1",
                "updatedAt": 1752170908.272,
                "updatedBy": "SYSTEM"
            }
        },
        {
            "assetTypeItem": {
                "createdAt": 1748436962.064,
                "createdBy": "SYSTEM",
                "domainId": "dzd_53ielnpxktdilj",
                "formsOutput": {
                    "AssetCommonDetailsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.AssetCommonDetailsFormType",
                        "typeRevision": "6"
                    },
                    "DataSourceReferenceForm": {
                        "required": false,
                        "typeName": "amazon.datazone.DataSourceReferenceFormType",
                        "typeRevision": "4"
                    },
                    "MskTopicForm": {
                        "required": true,
                        "typeName": "amazon.datazone.MskTopicFormType",
                        "typeRevision": "1"
                    },
                    "SchemaMetadataForm": {
                        "required": false,
                        "typeName": "amazon.datazone.SchemaMetadataFormType",
                        "typeRevision": "1"
                    },
                    "SuggestionForm": {
                        "required": false,
                        "typeName": "amazon.datazone.SuggestionFormType",
                        "typeRevision": "3"
                    }
                },
                "name": "amazon.datazone.MskTopicAssetType",
                "originDomainId": "dzd_amazon_datazone_domain",
                "originProjectId": "dzd_amazon_datazone_domain_project",
                "owningProjectId": "dzd_amazon_datazone_domain_project",
                "revision": "3",
                "updatedAt": 1750698545.406,
                "updatedBy": "SYSTEM"
            }
        },
        {
            "assetTypeItem": {
                "createdAt": 1745604393.359,
                "createdBy": "SYSTEM",
                "domainId": "dzd_53ielnpxktdilj",
                "formsOutput": {
                    "AssetCommonDetailsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.AssetCommonDetailsFormType",
                        "typeRevision": "6"
                    },
                    "DataSourceReferenceForm": {
                        "required": false,
                        "typeName": "amazon.datazone.DataSourceReferenceFormType",
                        "typeRevision": "4"
                    },
                    "KinesisDataStreamForm": {
                        "required": true,
                        "typeName": "amazon.datazone.KinesisDataStreamFormType",
                        "typeRevision": "2"
                    },
                    "SchemaMetadataForm": {
                        "required": false,
                        "typeName": "amazon.datazone.SchemaMetadataFormType",
                        "typeRevision": "1"
                    },
                    "SuggestionForm": {
                        "required": false,
                        "typeName": "amazon.datazone.SuggestionFormType",
                        "typeRevision": "3"
                    }
                },
                "name": "amazon.datazone.KinesisDataStreamAssetType",
                "originDomainId": "dzd_amazon_datazone_domain",
                "originProjectId": "dzd_amazon_datazone_domain_project",
                "owningProjectId": "dzd_amazon_datazone_domain_project",
                "revision": "5",
                "updatedAt": 1750698545.564,
                "updatedBy": "SYSTEM"
            }
        },
        {
            "assetTypeItem": {
                "createdAt": 1743523808.154,
                "createdBy": "SYSTEM",
                "domainId": "dzd_53ielnpxktdilj",
                "formsOutput": {
                    "AssetCommonDetailsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.AssetCommonDetailsFormType",
                        "typeRevision": "6"
                    },
                    "QuickSightDashboardForm": {
                        "required": true,
                        "typeName": "amazon.datazone.QuickSightDashboardFormType",
                        "typeRevision": "3"
                    },
                    "SubscriptionTermsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.SubscriptionTermsFormType",
                        "typeRevision": "2"
                    }
                },
                "name": "amazon.datazone.QuickSightDashboardAssetType",
                "originDomainId": "dzd_amazon_datazone_domain",
                "originProjectId": "dzd_amazon_datazone_domain_project",
                "owningProjectId": "dzd_amazon_datazone_domain_project",
                "revision": "3",
                "updatedAt": 1748436962.275,
                "updatedBy": "SYSTEM"
            }
        },
        {
            "assetTypeItem": {
                "createdAt": 1728920863.66,
                "createdBy": "SYSTEM",
                "domainId": "dzd_53ielnpxktdilj",
                "formsOutput": {
                    "AssetCommonDetailsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.AssetCommonDetailsFormType",
                        "typeRevision": "6"
                    },
                    "BedrockModelForm": {
                        "required": true,
                        "typeName": "amazon.datazone.BedrockModelFormType",
                        "typeRevision": "6"
                    },
                    "SubscriptionTermsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.SubscriptionTermsFormType",
                        "typeRevision": "2"
                    }
                },
                "name": "amazon.datazone.BedrockModelAssetType",
                "originDomainId": "dzd_amazon_datazone_domain",
                "originProjectId": "dzd_amazon_datazone_domain_project",
                "owningProjectId": "dzd_amazon_datazone_domain_project",
                "revision": "6",
                "updatedAt": 1746484563.478,
                "updatedBy": "SYSTEM"
            }
        },
        {
            "assetTypeItem": {
                "createdAt": 1728920864.133,
                "createdBy": "SYSTEM",
                "domainId": "dzd_53ielnpxktdilj",
                "formsOutput": {
                    "AssetCommonDetailsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.AssetCommonDetailsFormType",
                        "typeRevision": "6"
                    },
                    "BedrockAppCommonForm": {
                        "required": true,
                        "typeName": "amazon.datazone.BedrockAppCommonFormType",
                        "typeRevision": "2"
                    },
                    "SubscriptionTermsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.SubscriptionTermsFormType",
                        "typeRevision": "2"
                    }
                },
                "name": "amazon.datazone.BedrockFlowAssetType",
                "originDomainId": "dzd_amazon_datazone_domain",
                "originProjectId": "dzd_amazon_datazone_domain_project",
                "owningProjectId": "dzd_amazon_datazone_domain_project",
                "revision": "2",
                "updatedAt": 1730316044.425,
                "updatedBy": "SYSTEM"
            }
        },
        {
            "assetTypeItem": {
                "createdAt": 1728920864.056,
                "createdBy": "SYSTEM",
                "domainId": "dzd_53ielnpxktdilj",
                "formsOutput": {
                    "AssetCommonDetailsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.AssetCommonDetailsFormType",
                        "typeRevision": "6"
                    },
                    "BedrockAppCommonForm": {
                        "required": true,
                        "typeName": "amazon.datazone.BedrockAppCommonFormType",
                        "typeRevision": "2"
                    },
                    "SubscriptionTermsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.SubscriptionTermsFormType",
                        "typeRevision": "2"
                    }
                },
                "name": "amazon.datazone.BedrockPromptAssetType",
                "originDomainId": "dzd_amazon_datazone_domain",
                "originProjectId": "dzd_amazon_datazone_domain_project",
                "owningProjectId": "dzd_amazon_datazone_domain_project",
                "revision": "2",
                "updatedAt": 1730316044.385,
                "updatedBy": "SYSTEM"
            }
        },
        {
            "assetTypeItem": {
                "createdAt": 1728920864.194,
                "createdBy": "SYSTEM",
                "domainId": "dzd_53ielnpxktdilj",
                "formsOutput": {
                    "AssetCommonDetailsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.AssetCommonDetailsFormType",
                        "typeRevision": "6"
                    },
                    "BedrockAppCommonForm": {
                        "required": true,
                        "typeName": "amazon.datazone.BedrockAppCommonFormType",
                        "typeRevision": "2"
                    },
                    "SubscriptionTermsForm": {
                        "required": false,
                        "typeName": "amazon.datazone.SubscriptionTermsFormType",
                        "typeRevision": "2"
                    }
                },
                "name": "amazon.datazone.BedrockChatAssetType",
                "originDomainId": "dzd_amazon_datazone_domain",
                "originProjectId": "dzd_amazon_datazone_domain_project",
                "owningProjectId": "dzd_amazon_datazone_domain_project",
                "revision": "2",
                "updatedAt": 1730316044.502,
                "updatedBy": "SYSTEM"
            }
        }
    ],
    "totalMatchCount": 20
}
```

### Example
<a name="API_SearchTypes_Example_2"></a>

Failuse case - missing parameter:

#### Sample Request
<a name="API_SearchTypes_Example_2_Request"></a>

```
aws datazone search-types \
--domain-identifier "dzd_53ielnpxktdilj" \
--search-scope "ASSET_TYPE"
```

#### Sample Response
<a name="API_SearchTypes_Example_2_Response"></a>

```
Parameter validation failed:
Missing required parameter in input: "managed"
```

### Example
<a name="API_SearchTypes_Example_3"></a>

Failure case - invalid JSON:

#### Sample Request
<a name="API_SearchTypes_Example_3_Request"></a>

```
aws datazone search-types \
--domain-identifier "dzd_53ielnpxktdilj" \
--search-scope "ASSET_TYPE" \
--filters '[{attribute:"TYPE",value:"ASSET"}]'
```

#### Sample Response
<a name="API_SearchTypes_Example_3_Response"></a>

```
Error parsing parameter '—filters': Invalid JSON:
[{attribute:"TYPE",value:"ASSET"}]
```

### Example
<a name="API_SearchTypes_Example_4"></a>

Failure case - invalid input:

#### Sample Request
<a name="API_SearchTypes_Example_4_Request"></a>

```
aws datazone search-types \
--domain-identifier "dzd_53ielnpxktdilj" \
--search-scope "ASSET_TYPE" \
--managed true
```

#### Sample Response
<a name="API_SearchTypes_Example_4_Response"></a>

```
Unknown options: true
```

## See Also
<a name="API_SearchTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/SearchTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/SearchTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SearchTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/SearchTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SearchTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/SearchTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/SearchTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/SearchTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/SearchTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SearchTypes)
