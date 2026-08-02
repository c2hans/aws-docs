---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-connection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Connection
<a name="aws-resource-events-connection"></a>

Creates a connection. A connection defines the authorization type and credentials to use for authorization with an API destination HTTP endpoint.

For more information, see [Connections for endpoint targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection.html) in the *Amazon EventBridge User Guide*.

## Syntax
<a name="aws-resource-events-connection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-events-connection-syntax.json"></a>

```
{
  "Type" : "AWS::Events::Connection",
  "Properties" : {
      "[AuthorizationType](#cfn-events-connection-authorizationtype)" : {{String}},
      "[AuthParameters](#cfn-events-connection-authparameters)" : {{AuthParameters}},
      "[Description](#cfn-events-connection-description)" : {{String}},
      "[InvocationConnectivityParameters](#cfn-events-connection-invocationconnectivityparameters)" : {{InvocationConnectivityParameters}},
      "[KmsKeyIdentifier](#cfn-events-connection-kmskeyidentifier)" : {{String}},
      "[Name](#cfn-events-connection-name)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-events-connection-syntax.yaml"></a>

```
Type: AWS::Events::Connection
Properties:
  [AuthorizationType](#cfn-events-connection-authorizationtype): {{String}}
  [AuthParameters](#cfn-events-connection-authparameters): {{
    AuthParameters}}
  [Description](#cfn-events-connection-description): {{String}}
  [InvocationConnectivityParameters](#cfn-events-connection-invocationconnectivityparameters): {{
    InvocationConnectivityParameters}}
  [KmsKeyIdentifier](#cfn-events-connection-kmskeyidentifier): {{String}}
  [Name](#cfn-events-connection-name): {{String}}
```

## Properties
<a name="aws-resource-events-connection-properties"></a>

`AuthorizationType`  <a name="cfn-events-connection-authorizationtype"></a>
The type of authorization to use for the connection.
OAUTH tokens are refreshed when a 401 or 407 response is returned.
*Required*: No
*Type*: String
*Allowed values*: `API_KEY | BASIC | OAUTH_CLIENT_CREDENTIALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthParameters`  <a name="cfn-events-connection-authparameters"></a>
The authorization parameters to use to authorize with the endpoint.
You must include only authorization parameters for the `AuthorizationType` you specify.
*Required*: No
*Type*: [AuthParameters](aws-properties-events-connection-authparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-events-connection-description"></a>
A description for the connection to create.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationConnectivityParameters`  <a name="cfn-events-connection-invocationconnectivityparameters"></a>
For connections to private APIs, the parameters to use for invoking the API.
For more information, see [Connecting to private APIs](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html) in the * *Amazon EventBridge User Guide* *.
*Required*: No
*Type*: [InvocationConnectivityParameters](aws-properties-events-connection-invocationconnectivityparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyIdentifier`  <a name="cfn-events-connection-kmskeyidentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt this connection. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.
If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt the connection.
For more information, see [Identify and view keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-/:]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-events-connection-name"></a>
The name for the connection to create.
*Required*: No
*Type*: String
*Pattern*: `[\.\-_A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-events-connection-return-values"></a>

### Ref
<a name="aws-resource-events-connection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the connection that was created by the request.

### Fn::GetAtt
<a name="aws-resource-events-connection-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-events-connection-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the connection that was created by the request.

`ArnForPolicy`  <a name="ArnForPolicy-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of a connection in resource format, so it can be used in the `Resource` element of IAM permission policy statements. For more information, see [Resource types defined by Amazon EventBridge](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridge.html#amazoneventbridge-resources-for-iam-policies) in the *Service Authorization Reference*.
For example, the following resource defines an IAM policy that grants permission to update a specific connection.

```
Resources:
  ExamplePolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: ExamplePolicy
      PolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
          - Effect: Allow
            Action:
              - events:UpdateConnection
            Resource:
              - !GetAtt myConnection.ArnForPolicy
```

`AuthParameters.ConnectivityParameters.ResourceParameters.ResourceAssociationArn`  <a name="AuthParameters.ConnectivityParameters.ResourceParameters.ResourceAssociationArn-fn::getatt"></a>
For connections to private APIs, the Amazon Resource Name (ARN) of the resource association EventBridge created between the connection and the private API's resource configuration.
For more information, see [ Managing service network resource associations for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html#connection-private-snra) in the * *Amazon EventBridge User Guide* *.

`InvocationConnectivityParameters.ResourceParameters.ResourceAssociationArn`  <a name="InvocationConnectivityParameters.ResourceParameters.ResourceAssociationArn-fn::getatt"></a>
For connections to private APIs, the Amazon Resource Name (ARN) of the resource association EventBridge created between the connection and the private API's resource configuration.
For more information, see [ Managing service network resource associations for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html#connection-private-snra) in the * *Amazon EventBridge User Guide* *.

`SecretArn`  <a name="SecretArn-fn::getatt"></a>
The ARN for the secret created for the connection.

## Examples
<a name="aws-resource-events-connection--examples"></a>

**Topics**
+ [Create a connection with ApiKey authorization parameters](#aws-resource-events-connection--examples--Create_a_connection_with_ApiKey_authorization_parameters)
+ [Create a connection with OAuth authorization parameters](#aws-resource-events-connection--examples--Create_a_connection_with_OAuth_authorization_parameters)

### Create a connection with ApiKey authorization parameters
<a name="aws-resource-events-connection--examples--Create_a_connection_with_ApiKey_authorization_parameters"></a>

The following example creates a connection named pagerduty-connection using ApiKey authorization and stores a secret from Secrets Manager.

#### JSON
<a name="aws-resource-events-connection--examples--Create_a_connection_with_ApiKey_authorization_parameters--json"></a>

```
{
  "Resources": {
    "Connection": {
      "Type": "AWS::Events::Connection",
      "Properties": {
        "Name": "pagerduty-connection",
        "AuthorizationType": "API_KEY",
        "AuthParameters": {
          "ApiKeyAuthParameters": {
            "ApiKeyName": "Authorization",
            "ApiKeyValue": "{{resolve:secretsmanager:arn:aws:secretsmanager:us-west-2:123456789012:secret:pagerdutyApiToken-S9SoDa}}"
          },
          "InvocationHttpParameters": {
            "BodyParameters": [
              {
                "Key": "routing_key",
                "Value": "my-pagerduty-integration-key",
                "IsValueSecret": true
              }
            ]
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-events-connection--examples--Create_a_connection_with_ApiKey_authorization_parameters--yaml"></a>

```
Resources:
  Connection:
    Type: AWS::Events::Connection
    Properties:
      Name: pagerduty-connection
      AuthorizationType: API_KEY
      AuthParameters:
        ApiKeyAuthParameters:
          ApiKeyName: Authorization
          ApiKeyValue: '{{resolve:secretsmanager:arn:aws:secretsmanager:us-west-2:123456789012:secret:pagerdutyApiToken-S9SoDa}}'
        InvocationHttpParameters:
          BodyParameters:
            - Key: routing_key
              Value: my-pagerduty-integration-key
              IsValueSecret: true
```

### Create a connection with OAuth authorization parameters
<a name="aws-resource-events-connection--examples--Create_a_connection_with_OAuth_authorization_parameters"></a>

The following example creates a connection named auth0-connection using OAuth authorization and stores a secret from Secrets Manager.

#### JSON
<a name="aws-resource-events-connection--examples--Create_a_connection_with_OAuth_authorization_parameters--json"></a>

```
{
  "Resources": {
    "Auth0Connection": {
      "Type": "AWS::Events::Connection",
      "Properties": {
        "Name": "auth0-connection",
        "AuthorizationType": "OAUTH_CLIENT_CREDENTIALS",
        "AuthParameters": {
          "OAuthParameters": {
            "AuthorizationEndpoint": "https://yourUserName.us.auth0.com/oauth/token",
            "ClientParameters": {
              "ClientID": "{{resolve:secretsmanager:arn:aws:secretsmanager:us-west-2:123456789012:secret:auth0ClientId}}",
              "ClientSecret": "{{resolve:secretsmanager:arn:aws:secretsmanager:us-west-2:123456789012:secret:auth0ClientSecret}}"
            },
            "HttpMethod": "POST",
            "OAuthHttpParameters": {
              "BodyParameters": [
                {
                  "Key": "audience",
                  "Value": "my-auth0-identifier",
                  "IsValueSecret": true
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-events-connection--examples--Create_a_connection_with_OAuth_authorization_parameters--yaml"></a>

```
Resources:
  Auth0Connection:
    Type: AWS::Events::Connection
    Properties:
      Name: auth0-connection
      AuthorizationType: OAUTH_CLIENT_CREDENTIALS
      AuthParameters:
        OAuthParameters:
          AuthorizationEndpoint: https://yourUserName.us.auth0.com/oauth/token
          ClientParameters:
            ClientID: '{{resolve:secretsmanager:arn:aws:secretsmanager:us-west-2:123456789012:secret:auth0ClientId}}'
            ClientSecret: '{{resolve:secretsmanager:arn:aws:secretsmanager:us-west-2:123456789012:secret:auth0ClientSecret}}'
          HttpMethod: POST
          OAuthHttpParameters:
            BodyParameters:
              - Key: audience
                Value: my-auth0-identifier
                IsValueSecret: true
```
