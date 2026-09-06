---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id-users.html
---

# Users
<a name="brokers-broker-id-users"></a>

**Note**
Does not apply to RabbitMQ brokers.

This is a collection of ActiveMQ users for the specified broker. An ActiveMQ user is a person or an application that can access the queues and topics of an ActiveMQ broker. For more information, see [User](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/user.html) in the Amazon MQ Developer Guide.

You can configure to have specific permissions. For example, you can allow some users to access the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).

A user can belong to a group. You can configure which users belong to which groups and which groups have permission to send to, receive from, and administer specific queues and topics.

**Important**
Making changes to a user does not apply the changes to the user immediately. To apply your changes, you must wait for the next maintenance window or reboot the broker.

## URI
<a name="brokers-broker-id-users-url"></a>

`/v1/brokers/{{broker-id}}/users`

## HTTP methods
<a name="brokers-broker-id-users-http-methods"></a>

### GET
<a name="brokers-broker-id-usersget"></a>

**Operation ID:** `ListUsers`

Returns a list of all ActiveMQ users.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| maxResults | String | False | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListUsersOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="brokers-broker-id-usersoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="brokers-broker-id-users-schemas"></a>

### Response bodies
<a name="brokers-broker-id-users-response-examples"></a>

#### ListUsersOutput schema
<a name="brokers-broker-id-users-response-body-listusersoutput-example"></a>

```
{
  "brokerId": "string",
  "nextToken": "string",
  "maxResults": integer,
  "users": [
    {
      "pendingChange": enum,
      "username": "string"
    }
  ]
}
```

#### Error schema
<a name="brokers-broker-id-users-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="brokers-broker-id-users-properties"></a>

### ChangeType
<a name="brokers-broker-id-users-model-changetype"></a>

The type of change pending for the ActiveMQ user.
+ `CREATE`
+ `UPDATE`
+ `DELETE`

### Error
<a name="brokers-broker-id-users-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### ListUsersOutput
<a name="brokers-broker-id-users-model-listusersoutput"></a>

Returns a list of all ActiveMQ users.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerId | string | True | Required. The unique ID that Amazon MQ generates for the broker. |
| maxResults | integer<br />Minimum: 5<br />Maximum: 100 | True | Required. The maximum number of ActiveMQ users that can be returned per page (20 by default). This value must be an integer from 5 to 100. |
| nextToken | string | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| users | Array of type [UserSummary](#brokers-broker-id-users-model-usersummary) | True | Required. The list of all ActiveMQ usernames for the specified broker. Does not apply to RabbitMQ brokers. |

### UserSummary
<a name="brokers-broker-id-users-model-usersummary"></a>

Returns a list of all broker users. Does not apply to RabbitMQ brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pendingChange | [ChangeType](#brokers-broker-id-users-model-changetype) | False | The type of change pending for the broker user. |
| username | string | True | Required. The username of the broker user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |

## See also
<a name="brokers-broker-id-users-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListUsers
<a name="ListUsers-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/ListUsers)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/ListUsers)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/ListUsers)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/ListUsers)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/ListUsers)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/ListUsers)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/ListUsers)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/ListUsers)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/ListUsers)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/ListUsers)
