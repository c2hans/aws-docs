---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id-users-username.html
---

# User
<a name="brokers-broker-id-users-username"></a>

**Note**
Does not apply to RabbitMQ brokers.

An ActiveMQ user is a person or an application that can access the queues and topics of an ActiveMQ broker. For more information, see [User](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/user.html) in the Amazon MQ Developer Guide.

A user can belong to a group. You can configure which users belong to which groups and which groups have permission to send to, receive from, and administer specific queues and topics.

**Important**
Making changes to a user does not apply the changes to the user immediately. To apply your changes, you must wait for the next maintenance window or reboot the broker.

## URI
<a name="brokers-broker-id-users-username-url"></a>

`/v1/brokers/{{broker-id}}/users/{{username}}`

## HTTP methods
<a name="brokers-broker-id-users-username-http-methods"></a>

### GET
<a name="brokers-broker-id-users-usernameget"></a>

**Operation ID:** `DescribeUser`

Returns information about an ActiveMQ user.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{username}} | String | True | The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeUserOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### POST
<a name="brokers-broker-id-users-usernamepost"></a>

**Operation ID:** `CreateUser`

Creates an ActiveMQ user.

**Important**
 Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames. Broker usernames are accessible to other AWS services, including CloudWatch Logs. Broker usernames are not intended to be used for private or sensitive data.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{username}} | String | True | The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 409 | Error | HTTP Status Code 409: Configuration ID is already in use. Remove the configuration from all brokers and retry the request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### PUT
<a name="brokers-broker-id-users-usernameput"></a>

**Operation ID:** `UpdateUser`

Updates the information for an ActiveMQ user.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{username}} | String | True | The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 409 | Error | HTTP Status Code 409: Configuration ID is already in use. Remove the configuration from all brokers and retry the request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### DELETE
<a name="brokers-broker-id-users-usernamedelete"></a>

**Operation ID:** `DeleteUser`

Deletes an ActiveMQ user.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{username}} | String | True | The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="brokers-broker-id-users-usernameoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{username}} | String | True | The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="brokers-broker-id-users-username-schemas"></a>

### Request bodies
<a name="brokers-broker-id-users-username-request-examples"></a>

#### POST schema
<a name="brokers-broker-id-users-username-request-body-post-example"></a>

```
{
  "password": "string",
  "replicationUser": boolean,
  "groups": [
    "string"
  ],
  "consoleAccess": boolean
}
```

#### PUT schema
<a name="brokers-broker-id-users-username-request-body-put-example"></a>

```
{
  "password": "string",
  "replicationUser": boolean,
  "groups": [
    "string"
  ],
  "consoleAccess": boolean
}
```

### Response bodies
<a name="brokers-broker-id-users-username-response-examples"></a>

#### DescribeUserOutput schema
<a name="brokers-broker-id-users-username-response-body-describeuseroutput-example"></a>

```
{
  "brokerId": "string",
  "replicationUser": boolean,
  "pending": {
    "pendingChange": enum,
    "groups": [
      "string"
    ],
    "consoleAccess": boolean
  },
  "groups": [
    "string"
  ],
  "consoleAccess": boolean,
  "username": "string"
}
```

#### Error schema
<a name="brokers-broker-id-users-username-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="brokers-broker-id-users-username-properties"></a>

### ChangeType
<a name="brokers-broker-id-users-username-model-changetype"></a>

The type of change pending for the ActiveMQ user.
+ `CREATE`
+ `UPDATE`
+ `DELETE`

### CreateUserInput
<a name="brokers-broker-id-users-username-model-createuserinput"></a>

Creates a new ActiveMQ user.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consoleAccess | boolean | False | Enables access to the ActiveMQ Web Console for the ActiveMQ user. |
| groups | Array of type string | False | The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |
| password | string<br />Format: password | True | Required. The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:=). |
| replicationUser | boolean | False | Defines if this user is intended for CRDR replication purposes. |

### DescribeUserOutput
<a name="brokers-broker-id-users-username-model-describeuseroutput"></a>

Returns information about an ActiveMQ user.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerId | string | True | Required. The unique ID that Amazon MQ generates for the broker. |
| consoleAccess | boolean | False | Enables access to the the ActiveMQ Web Console for the ActiveMQ user. |
| groups | Array of type string | False | The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |
| pending | [UserPendingChanges](#brokers-broker-id-users-username-model-userpendingchanges) | False | The status of the changes pending for the ActiveMQ user. |
| replicationUser | boolean | False | Describes whether the user is intended for data replication replication |
| username | string | True | Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |

### Error
<a name="brokers-broker-id-users-username-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### UpdateUserInput
<a name="brokers-broker-id-users-username-model-updateuserinput"></a>

Updates the information for an ActiveMQ user.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consoleAccess | boolean | False | Enables access to the the ActiveMQ Web Console for the ActiveMQ user. |
| groups | Array of type string | False | The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |
| password | string<br />Format: password | False | The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:=). |
| replicationUser | boolean | False | Defines whether the user is intended for data replication replication. |

### UserPendingChanges
<a name="brokers-broker-id-users-username-model-userpendingchanges"></a>

Returns information about the status of the changes pending for the ActiveMQ user.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consoleAccess | boolean | False | Enables access to the the ActiveMQ Web Console for the ActiveMQ user. |
| groups | Array of type string | False | The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |
| pendingChange | [ChangeType](#brokers-broker-id-users-username-model-changetype) | True | Required. The type of change pending for the ActiveMQ user. |

## See also
<a name="brokers-broker-id-users-username-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeUser
<a name="DescribeUser-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DescribeUser)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DescribeUser)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DescribeUser)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DescribeUser)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DescribeUser)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DescribeUser)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DescribeUser)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DescribeUser)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/DescribeUser)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DescribeUser)

### CreateUser
<a name="CreateUser-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/CreateUser)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/CreateUser)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/CreateUser)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/CreateUser)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/CreateUser)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/CreateUser)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/CreateUser)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/CreateUser)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/CreateUser)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/CreateUser)

### UpdateUser
<a name="UpdateUser-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/UpdateUser)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/UpdateUser)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/UpdateUser)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/UpdateUser)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/UpdateUser)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/UpdateUser)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/UpdateUser)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/UpdateUser)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/UpdateUser)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/UpdateUser)

### DeleteUser
<a name="DeleteUser-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DeleteUser)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DeleteUser)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DeleteUser)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DeleteUser)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DeleteUser)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DeleteUser)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DeleteUser)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DeleteUser)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/DeleteUser)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DeleteUser)
