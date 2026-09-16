---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/configurations.html
---

# Configurations
<a name="configurations"></a>

A collection of MSK configurations.

## URI
<a name="configurations-url"></a>

`/v1/configurations`

## HTTP methods
<a name="configurations-http-methods"></a>

### GET
<a name="configurationsget"></a>

**Operation ID:** `ListConfigurations`

Returns a list of all the MSK configurations.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListConfigurationsResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### POST
<a name="configurationspost"></a>

**Operation ID:** `CreateConfiguration`

Creates a new MSK configuration. To see an example of how to use this operation, first save the following text to a file and name the file `config-file.txt`.

```
auto.create.topics.enable = true

zookeeper.connection.timeout.ms = 1000

log.roll.ms = 604800000
```

Now run the following Python 3.6 script in the folder where you saved `config-file.txt`. This script uses the properties specified in `config-file.txt` to create a configuration named `SalesClusterConfiguration`. This configuration can work with Apache Kafka versions 1.1.1 and 2.1.0.

```
import boto3

client = boto3.client('kafka')

config_file = open('config-file.txt', 'r')

server_properties = config_file.read()

response = client.create_configuration(
    Name='SalesClusterConfiguration',
    Description='The configuration to use on all sales clusters.',
    KafkaVersions=['1.1.1', '2.1.0'],
    ServerProperties=server_properties
)

print(response)
```

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  CreateConfigurationResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 409 | Error | This cluster name already exists. Retry your request using another name. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="configurationsoptions"></a>

Enable CORS by returning the correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="configurations-schemas"></a>

### Request bodies
<a name="configurations-request-examples"></a>

#### POST schema
<a name="configurations-request-body-post-example"></a>

```
{
  "name": "string",
  "description": "string",
  "kafkaVersions": [
    "string"
  ],
  "serverProperties": "string"
}
```

### Response bodies
<a name="configurations-response-examples"></a>

#### ListConfigurationsResponse schema
<a name="configurations-response-body-listconfigurationsresponse-example"></a>

```
{
  "nextToken": "string",
  "configurations": [
    {
      "creationTime": "string",
      "name": "string",
      "description": "string",
      "kafkaVersions": [
        "string"
      ],
      "state": enum,
      "arn": "string",
      "latestRevision": {
        "creationTime": "string",
        "description": "string",
        "revision": integer
      }
    }
  ]
}
```

#### CreateConfigurationResponse schema
<a name="configurations-response-body-createconfigurationresponse-example"></a>

```
{
  "creationTime": "string",
  "name": "string",
  "state": enum,
  "arn": "string",
  "latestRevision": {
    "creationTime": "string",
    "description": "string",
    "revision": integer
  }
}
```

#### Error schema
<a name="configurations-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="configurations-properties"></a>

### Configuration
<a name="configurations-model-configuration"></a>

Represents an MSK Configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | The Amazon Resource Name (ARN) of the configuration. |
| creationTime | string | True | The time when the configuration was created. |
| description | string | True | The description of the configuration. |
| kafkaVersions | Array of type string | False | An array of the versions of Apache Kafka with which you can use this MSK configuration. You can use this configuration for an MSK cluster only if the Apache Kafka version specified for the cluster appears in this array. |
| latestRevision | [ConfigurationRevision](#configurations-model-configurationrevision) | True | Latest revision of the configuration. |
| name | string | True | The name of the configuration. Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$". |
| state | [ConfigurationState](#configurations-model-configurationstate) | False | State of the configuration. |

### ConfigurationRevision
<a name="configurations-model-configurationrevision"></a>

Describes a configuration revision.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationTime | string | True | The time when the configuration revision was created. |
| description | string | False | The description of the configuration revision. |
| revision | integer<br />Format: int64 | True | The revision number. |

### ConfigurationState
<a name="configurations-model-configurationstate"></a>

State of a kafka configuration
+ `ACTIVE`
+ `DELETING`
+ `DELETE_FAILED`

### CreateConfigurationRequest
<a name="configurations-model-createconfigurationrequest"></a>

Request body for CreateConfiguration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string | False | The description of the configuration. |
| kafkaVersions | Array of type string | False | The versions of Apache Kafka with which you can use this MSK configuration. |
| name | string | True | The name of the configuration. Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$". |
| serverProperties | string | True | Contents of the `server.properties` file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of `server.properties` can be in plaintext. |

### CreateConfigurationResponse
<a name="configurations-model-createconfigurationresponse"></a>

Response body for CreateConfiguration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the configuration. |
| creationTime | string | False | The time when the configuration was created. |
| latestRevision | [ConfigurationRevision](#configurations-model-configurationrevision) | False | Latest revision of the configuration. |
| name | string | False | The name of the configuration. Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$". |
| state | [ConfigurationState](#configurations-model-configurationstate) | False | State of the configuration. |

### Error
<a name="configurations-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListConfigurationsResponse
<a name="configurations-model-listconfigurationsresponse"></a>

The response contains an array of Configuration and a next token if the response is truncated.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configurations | Array of type [Configuration](#configurations-model-configuration) | False | An array of MSK configurations. |
| nextToken | string | False | The paginated results marker. When the result of a `ListConfigurations` operation is truncated, the call returns `NextToken` in the response. To get another batch of configurations, provide this token in your next request. |

## See also
<a name="configurations-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListConfigurations
<a name="ListConfigurations-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListConfigurations)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListConfigurations)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListConfigurations)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListConfigurations)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListConfigurations)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListConfigurations)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListConfigurations)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListConfigurations)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/ListConfigurations)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListConfigurations)

### CreateConfiguration
<a name="CreateConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/CreateConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/CreateConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/CreateConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/CreateConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/CreateConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/CreateConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/CreateConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/CreateConfiguration)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/CreateConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/CreateConfiguration)
