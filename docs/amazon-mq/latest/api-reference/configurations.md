---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/configurations.html
---

# Configurations
<a name="configurations"></a>

This is a collection of configurations. A configuration contains all of the settings for your broker. For more information, see [Configuration](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configuration.html) and [Amazon MQ Broker Configuration Parameters](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html) in the Amazon MQ Developer Guide.

You can create a configuration before creating any brokers. You can then apply the configuration to one or more brokers.

**Important**
Making changes to a configuration does not apply the changes to the broker immediately. To apply your changes, you must wait for the next maintenance window or reboot the broker.

## URI
<a name="configurations-url"></a>

`/v1/configurations`

## HTTP methods
<a name="configurations-http-methods"></a>

### GET
<a name="configurationsget"></a>

**Operation ID:** `ListConfigurations`

Returns a list of all configurations.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| maxResults | String | False | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListConfigurationsOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### POST
<a name="configurationspost"></a>

**Operation ID:** `CreateConfiguration`

Creates a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and version).

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  CreateConfigurationOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 409 | Error | HTTP Status Code 409: Configuration ID is already in use. Remove the configuration from all brokers and retry the request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="configurationsoptions"></a>

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
  "engineVersion": "string",
  "authenticationStrategy": enum,
  "name": "string",
  "engineType": enum,
  "tags": {
  }
}
```

### Response bodies
<a name="configurations-response-examples"></a>

#### ListConfigurationsOutput schema
<a name="configurations-response-body-listconfigurationsoutput-example"></a>

```
{
  "nextToken": "string",
  "maxResults": integer,
  "configurations": [
    {
      "engineVersion": "string",
      "created": "string",
      "authenticationStrategy": enum,
      "name": "string",
      "description": "string",
      "engineType": enum,
      "id": "string",
      "arn": "string",
      "latestRevision": {
        "created": "string",
        "description": "string",
        "revision": integer
      },
      "tags": {
      }
    }
  ]
}
```

#### CreateConfigurationOutput schema
<a name="configurations-response-body-createconfigurationoutput-example"></a>

```
{
  "created": "string",
  "authenticationStrategy": enum,
  "name": "string",
  "id": "string",
  "arn": "string",
  "latestRevision": {
    "created": "string",
    "description": "string",
    "revision": integer
  }
}
```

#### Error schema
<a name="configurations-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="configurations-properties"></a>

### AuthenticationStrategy
<a name="configurations-model-authenticationstrategy"></a>

Optional. The authentication strategy used to secure the broker. The default is `SIMPLE`.
+ `SIMPLE`
+ `LDAP`
+ `CONFIG_MANAGED`

### Configuration
<a name="configurations-model-configuration"></a>

Returns information about all configurations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | Required. The ARN of the configuration. |
| authenticationStrategy | [AuthenticationStrategy](#configurations-model-authenticationstrategy) | True | Optional. The authentication strategy associated with the configuration. The default is `SIMPLE`. |
| created | string<br />Format: date-time | True | Required. The date and time of the configuration revision. |
| description | string | True | Required. The description of the configuration. |
| engineType | [EngineType](#configurations-model-enginetype) | True | Required. The type of broker engine. Currently, Amazon MQ supports `ACTIVEMQ` and `RABBITMQ`. |
| engineVersion | string | True | The broker engine version. Defaults to the latest available version for the specified broker engine type. For a list of supported engine versions, see the [ActiveMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide. |
| id | string | True | Required. The unique ID that Amazon MQ generates for the configuration. |
| latestRevision | [ConfigurationRevision](#configurations-model-configurationrevision) | True | Required. The latest revision of the configuration. |
| name | string | True | Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 1-150 characters long. |
| tags | object | False | The list of all tags associated with this configuration. |

### ConfigurationRevision
<a name="configurations-model-configurationrevision"></a>

Returns information about the specified configuration revision.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| created | string<br />Format: date-time | True | Required. The date and time of the configuration revision. |
| description | string | False | The description of the configuration revision. |
| revision | integer | True | Required. The revision number of the configuration. |

### CreateConfigurationInput
<a name="configurations-model-createconfigurationinput"></a>

Creates a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and version).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authenticationStrategy | [AuthenticationStrategy](#configurations-model-authenticationstrategy) | False | Optional. The authentication strategy associated with the configuration. The default is `SIMPLE`. |
| engineType | [EngineType](#configurations-model-enginetype) | True | Required. The type of broker engine. Currently, Amazon MQ supports `ACTIVEMQ` and `RABBITMQ`. |
| engineVersion | string | False | The broker engine version. Defaults to the latest available version for the specified broker engine type. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide. |
| name | string | True | Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 1-150 characters long. |
| tags | object | False | Create tags when creating the configuration. |

### CreateConfigurationOutput
<a name="configurations-model-createconfigurationoutput"></a>

Returns information about the created configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | Required. The Amazon Resource Name (ARN) of the configuration. |
| authenticationStrategy | [AuthenticationStrategy](#configurations-model-authenticationstrategy) | True | Optional. The authentication strategy associated with the configuration. The default is `SIMPLE`.  |
| created | string<br />Format: date-time | True | Required. The date and time of the configuration. |
| id | string | True | Required. The unique ID that Amazon MQ generates for the configuration. |
| latestRevision | [ConfigurationRevision](#configurations-model-configurationrevision) | False | The latest revision of the configuration. |
| name | string | True | Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 1-150 characters long. |

### EngineType
<a name="configurations-model-enginetype"></a>

The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ.
+ `ACTIVEMQ`
+ `RABBITMQ`

### Error
<a name="configurations-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### ListConfigurationsOutput
<a name="configurations-model-listconfigurationsoutput"></a>

Returns a list of all configurations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configurations | Array of type [Configuration](#configurations-model-configuration) | False | The list of all revisions for the specified configuration. |
| maxResults | integer | False | The maximum number of configurations that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. |
| nextToken | string | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |

## See also
<a name="configurations-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListConfigurations
<a name="ListConfigurations-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/ListConfigurations)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/ListConfigurations)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/ListConfigurations)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/ListConfigurations)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/ListConfigurations)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/ListConfigurations)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/ListConfigurations)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/ListConfigurations)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/ListConfigurations)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/ListConfigurations)

### CreateConfiguration
<a name="CreateConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/CreateConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/CreateConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/CreateConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/CreateConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/CreateConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/CreateConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/CreateConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/CreateConfiguration)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/CreateConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/CreateConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
