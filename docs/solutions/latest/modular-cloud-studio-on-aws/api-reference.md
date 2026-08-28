---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/api-reference.html
---

# API reference
<a name="api-reference"></a>

This section provides an API reference for the MCS solution.

## POST /modules/deregistered
<a name="post-modulesderegistered"></a>

### Body parameter schema
<a name="body-parameter-schema"></a>

```
{
 "module_name": "string"
}
```

 **Parameters**

|  **Name**  |  **In**  |  **Type**  |  **Required**  |  **Description**  |
| --- | --- | --- | --- | --- |
|  **body**  | body | object | true | none |
| ⇒ **module\_name**  | body | string | false | none |

## POST /modules/disabled
<a name="post-modulesdisabled"></a>

### Body parameter schema
<a name="body-parameter-schema-2"></a>

 **Parameters**

```
{
  "disable": {
    "name": "string",
    "servicecatalogProvisionedProductId": "string",
    "moduleRegion": "string",
    "regionType": "string"
  }
}
```

|  **Name**  |  **In**  |  **Type**  |  **Required**  |  **Description**  |
| --- | --- | --- | --- | --- |
| body | body | object | true | none |
| ⇒ disable | body | object | false | none |
| ⇒⇒ name | body | string | false | none |
| ⇒⇒ servicecatalogProvisionedProductId | body | string | false | none |
| ⇒⇒ moduleRegion | body | string | false | none |
| ⇒⇒ regionType | body | string | false | none |

## GET /modules/enabled
<a name="get-modulesenabled"></a>

### Response schema
<a name="response-schema"></a>

 **Status code 200**

|  **Name**  |  **Type**  |  **Required**  |  **Restrictions**  |  **Description**  |
| --- | --- | --- | --- | --- |
| ⇒ **name**  | string | false | none | none |
| ⇒ **servicecatalogProvisionedProductId**  | string | false | none | none |
| ⇒ **version**  | string | false | none | none |
| ⇒ **region**  | string | false | none | none |
| ⇒ **category**  | string | false | none | none |
| ⇒ **lastUpdateTime**  | string | false | none | none |
| ⇒\*creationTime\* | string | false | none | none |
| ⇒ **status**  | string | false | none | none |
| ⇒ **cloudformationInputParameters**  | [object] | false | none | none |
| ⇒⇒ **Value**  | string | false | none | none |
| ⇒⇒ **Key**  | string | false | none | none |
| ⇒ **consoleUrl**  | string | false | none | none |
| ⇒ **stackId**  | string | false | none | none |
| ⇒ **activeDependents**  | [string] | false | none | none |
| ⇒ **regionType**  | string | false | none | none |
| ⇒ **moduleRegionCategory**  | string | false | none | none |

## POST /modules/enabled
<a name="post-modulesenabled"></a>

### Body parameter schema
<a name="body-parameter-schema-3"></a>

```
{
  "module": {
    "name": "string",
    "version": "string",
    "region": "string",
    "regionType": "string",
    "tags": {
      "useMCSTags": true,
      "customTags": [
        {
          "Key": "string",
          "Value": "string"
        }
      ]
    },
    "inputParameters": [
      {
        "Key": "string",
        "Value": "string"
      }
    ]
  }
}
```

 **Parameters**

|  **Name**  |  **In**  |  **Type**  |  **Required**  |  **Description**  |
| --- | --- | --- | --- | --- |
| body | body | object | true | none |
| ⇒ module | body | object | false | none |
| ⇒⇒ name | body | string | false | none |
| ⇒⇒ version | body | string | false | none |
| ⇒⇒ region | body | string | false | none |
| ⇒⇒ regionType | body | string | false | none |
| ⇒⇒ tags | body | object | false | none |
| ⇒⇒⇒ useMCSTags | body | boolean | false | If set to `true`, non-internal tags from MCS Core stack are used. |
| ⇒⇒⇒ customTags | body | [object] | false | This field is ignored if **useMCSTags** is set to `true`. Otherwise, the tags from this field will are used. |
| ⇒⇒⇒⇒ Key | body | string | false | none |
| ⇒⇒⇒⇒ Value | body | string | false | none |
| ⇒⇒ inputParameters | body | [object] | false | none |
| ⇒⇒⇒ Key | body | string | false | none |
| ⇒⇒⇒Value | body | string | false | none |

## GET /modules/partner
<a name="get-modulespartner"></a>

### Example responses
<a name="example-responses"></a>

 **200 response**

|  **Name**  |  **Meaning**  |  **Description**  |  **Schema**  |
| --- | --- | --- | --- |
| 200 |  [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | 200 response | Inline |

### Response schema
<a name="response-schema-2"></a>

 **Status code 200**

|  **Name**  |  **Type**  |  **Required**  |  **Restrictions**  |  **Description**  |
| --- | --- | --- | --- | --- |
| ⇒ modules | [object] | false | none | none |
| ⇒⇒ name | string | false | none | none |
| ⇒⇒ displayName | string | false | none | none |
| ⇒⇒ category | string | false | none | none |
| ⇒⇒ manifestUrl | string | false | none | none |
| ⇒⇒ status | string | false | none | none |
| ⇒⇒ createAt | string | false | none | none |
| ⇒⇒ updatedAt | string | false | none | none |
| ⇒⇒ isCustom | boolean | false | none | none |
| ⇒ last\_updated\_date | string | false | none | none |

## PUT /modules/partner/sync
<a name="put-modulespartnersync"></a>

### Body parameter schema
<a name="body-parameter-schema-4"></a>

Request body must be empty

### Example responses
<a name="example-responses-2"></a>

 **202 response**

|  **Name**  |  **Meaning**  |  **Description**  |  **Schema**  |
| --- | --- | --- | --- |
| 202 |  [Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)  | Partner module synchronization started successfully. | Inline |
| 409 |  [Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)  | Partner modules are being synchronized and/or registered by another process. | Inline |
| 502 |  [Bad Gateway](https://tools.ietf.org/html/rfc7231#section-6.6.3)  | An error occurred with the remote server hosting the partner module manifests. | Inline |

## GET /modules/registered
<a name="get-modulesregistered"></a>

### Example responses
<a name="example-responses-3"></a>

 **200 response**

|  **Name**  |  **Meaning**  |  **Description**  |  **Schema**  |
| --- | --- | --- | --- |
| 200 |  [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | 200 response | Inline |

### Response schema
<a name="response-schema-3"></a>

 **Status code 200**

|  **Name**  |  **Type**  |  **Required**  |  **Restrictions**  |  **Description**  |
| --- | --- | --- | --- | --- |
| ⇒ name | string | false | none | none |
| ⇒ version | string | false | none | none |
| ⇒ status | string | false | none | none |
| ⇒ category | string | false | none | none |
| ⇒ serviceCatalogPortfolioId | string | false | none | none |
| ⇒ serviceCatalogProductId | string | false | none | none |
| ⇒ inputParametersLocal | [string] | false | none | none |
| ⇒ inputParametersHub | [string] | false | none | none |
| ⇒ regionType | string | false | none | none |
| ⇒ isExternal | boolean | false | none | none |

## POST /modules/registered
<a name="post-modulesregistered"></a>

### Body parameter schema
<a name="body-parameter-schema-5"></a>

```
{
  "params": {
    "manifestUrl": "string",
    "revision": "string"
  }
}
```

 **Parameters**

|  **Name**  |  **In**  |  **Type**  |  **Required**  |  **Description**  |
| --- | --- | --- | --- | --- |
| body | body | object | true | none |
| ⇒ params | body | object | false | none |
| ⇒⇒ manifestUrl | body | string | false | none |
| ⇒⇒ revision | body | string | false | none |

### Example responses
<a name="example-responses-4"></a>

 **200 response**

|  **Status**  |  **Meaning**  |  **Description**  |  **Schema**  |
| --- | --- | --- | --- |
| 200 |  [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | 200 response | Inline |

## GET /modules/registered/inputs
<a name="get-modulesregisteredinputs"></a>

### Parameters
<a name="parameters"></a>

|  **Name**  |  **In**  |  **Type**  |  **Required**  |  **Description**  |
| --- | --- | --- | --- | --- |
| name | query | string | true | none |
| version | query | string | true | none |
| region | query | string | true | none |
| regionType | query | string | true | Either HUB or SPOKE |

### Response schema
<a name="response-schema-4"></a>

 **Status code 200**

|  **Name**  |  **Type**  |  **Required**  |  **Restrictions**  |  **Description**  |
| --- | --- | --- | --- | --- |
| ⇒ cloudformationInputKeys | [object] | false | none | none |
| ⇒⇒ name | string | false | none | none |
| ⇒⇒ category | string | false | none | none |
| ⇒⇒ constraints | object | false | none | none |
| ⇒⇒⇒ allowedPattern | string | false | none | none |
| ⇒⇒⇒ allowedValues | [string] | false | none | none |
| ⇒⇒ default | string | false | none | none |
| ⇒⇒ description | string | false | none | none |
| ⇒ mcsTags | [object] | false | none | none |
| ⇒⇒ key | string | false | none | none |
| ⇒⇒ value | string | false | none | none |

## GET /modules/validate
<a name="get-modulesvalidate"></a>

### Parameters
<a name="parameters-2"></a>

|  **Name**  |  **In**  |  **Type**  |  **Required**  |  **Description**  |
| --- | --- | --- | --- | --- |
| manifest\_url | query | string | true | none |

### Response schema
<a name="response-schema-5"></a>

 **Status code 200**

|  **Name**  |  **Type**  |  **Required**  |  **Restrictions**  |  **Description**  |
| --- | --- | --- | --- | --- |
| ⇒ data | object | false | none | Represents the manifest JSON file defined in the developer guide |

## GET /regions
<a name="get-regions"></a>

### Response schema
<a name="response-schema-6"></a>

 **Status code 200**

|  **Name**  |  **Type**  |  **Required**  |  **Restrictions**  |  **Description**  |
| --- | --- | --- | --- | --- |
| ⇒ regions | [object] | false | none | none |
| ⇒⇒ name | string | false | none | none |
| ⇒⇒ isHub | boolean | false | none | none |
| ⇒⇒ enablementStatus | string | false | none | none |
| ⇒⇒ provisionedProductId | string | false | none | none |
| ⇒⇒ dateEnabled | string | false | none | none |

## PUT /regions
<a name="put-regions"></a>

### Body parameter schema
<a name="body-parameter-schema-6"></a>

```
{
  "region": {
    "name": "string",
    "enablementStatus": "string"
  }
}
```

 **Parameters**

|  **Name**  |  **In**  |  **Type**  |  **Required**  |  **Description**  |
| --- | --- | --- | --- | --- |
| body | body | object | true | none |
| ⇒ region | body | object | false | none |
| ⇒⇒ name | body | string | false | none |
| ⇒⇒ enablementStatus | body | string | false | none |

### Response schema
<a name="response-schema-7"></a>

 **Status code 200**

|  **Name**  |  **Type**  |  **Required**  |  **Restrictions**  |  **Description**  |
| --- | --- | --- | --- | --- |
| ⇒ regions | object | false | none | none |
| ⇒⇒ name | string | false | none | none |
| ⇒⇒ isHub | string | false | none | none |
| ⇒⇒ enablementStatus | string | false | none | none |
| ⇒⇒ provisionedProductId | string | false | none | none |
| ⇒⇒ dateEnabled | string | false | none | none |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
