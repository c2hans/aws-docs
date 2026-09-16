---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/configurations-configuration-id-revisions.html
---

# Configuration Revisions
<a name="configurations-configuration-id-revisions"></a>

This is a collection of configuration revisions. To keep track of the changes you make to your configuration, you can create configuration revisions. For more information, see [Configuration](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configuration.html) in the Amazon MQ Developer Guide.

**Important**
Making changes to a configuration does not apply the changes to the broker immediately. To apply your changes, you must wait for the next maintenance window or reboot the broker.

## URI
<a name="configurations-configuration-id-revisions-url"></a>

`/v1/configurations/{{configuration-id}}/revisions`

## HTTP methods
<a name="configurations-configuration-id-revisions-http-methods"></a>

### GET
<a name="configurations-configuration-id-revisionsget"></a>

**Operation ID:** `ListConfigurationRevisions`

Returns a list of all revisions for the specified configuration.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{configuration-id}} | String | True | The unique ID that Amazon MQ generates for the configuration. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| maxResults | String | False | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListConfigurationRevisionsOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="configurations-configuration-id-revisionsoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{configuration-id}} | String | True | The unique ID that Amazon MQ generates for the configuration. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="configurations-configuration-id-revisions-schemas"></a>

### Response bodies
<a name="configurations-configuration-id-revisions-response-examples"></a>

#### ListConfigurationRevisionsOutput schema
<a name="configurations-configuration-id-revisions-response-body-listconfigurationrevisionsoutput-example"></a>

```
{
  "nextToken": "string",
  "maxResults": integer,
  "revisions": [
    {
      "created": "string",
      "description": "string",
      "revision": integer
    }
  ],
  "configurationId": "string"
}
```

#### Error schema
<a name="configurations-configuration-id-revisions-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="configurations-configuration-id-revisions-properties"></a>

### ConfigurationRevision
<a name="configurations-configuration-id-revisions-model-configurationrevision"></a>

Returns information about the specified configuration revision.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| created | string<br />Format: date-time | True | Required. The date and time of the configuration revision. |
| description | string | False | The description of the configuration revision. |
| revision | integer | True | Required. The revision number of the configuration. |

### Error
<a name="configurations-configuration-id-revisions-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### ListConfigurationRevisionsOutput
<a name="configurations-configuration-id-revisions-model-listconfigurationrevisionsoutput"></a>

Returns a list of all revisions for the specified configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configurationId | string | False | The unique ID that Amazon MQ generates for the configuration. |
| maxResults | integer | False | The maximum number of configuration revisions that can be returned per page (20 by default). This value must be an integer from 5 to 100. |
| nextToken | string | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| revisions | Array of type [ConfigurationRevision](#configurations-configuration-id-revisions-model-configurationrevision) | False | The list of all revisions for the specified configuration. |

## See also
<a name="configurations-configuration-id-revisions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListConfigurationRevisions
<a name="ListConfigurationRevisions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/ListConfigurationRevisions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/ListConfigurationRevisions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/ListConfigurationRevisions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/ListConfigurationRevisions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/ListConfigurationRevisions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/ListConfigurationRevisions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/ListConfigurationRevisions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/ListConfigurationRevisions)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/ListConfigurationRevisions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/ListConfigurationRevisions)
