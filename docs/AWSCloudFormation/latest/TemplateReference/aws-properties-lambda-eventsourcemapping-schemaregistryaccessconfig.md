---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-schemaregistryaccessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping SchemaRegistryAccessConfig
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryaccessconfig"></a>

Specific access configuration settings that tell Lambda how to authenticate with your schema registry.

If you're working with an AWS Glue schema registry, don't provide authentication details in this object. Instead, ensure that your execution role has the required permissions for Lambda to access your cluster.

If you're working with a Confluent schema registry, choose the authentication method in the `Type` field, and provide the AWS Secrets Manager secret ARN in the `URI` field.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryaccessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryaccessconfig-syntax.json"></a>

```
{
  "[Type](#cfn-lambda-eventsourcemapping-schemaregistryaccessconfig-type)" : {{String}},
  "[URI](#cfn-lambda-eventsourcemapping-schemaregistryaccessconfig-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryaccessconfig-syntax.yaml"></a>

```
  [Type](#cfn-lambda-eventsourcemapping-schemaregistryaccessconfig-type): {{String}}
  [URI](#cfn-lambda-eventsourcemapping-schemaregistryaccessconfig-uri): {{String}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryaccessconfig-properties"></a>

`Type`  <a name="cfn-lambda-eventsourcemapping-schemaregistryaccessconfig-type"></a>
 The type of authentication Lambda uses to access your schema registry.
+ `BASIC_AUTH` – The Secrets Manager ARN of your secret key used for basic authentication with your Confluent schema registry.
+ `CLIENT_CERTIFICATE_TLS_AUTH` – The Secrets Manager ARN of your secret key containing the certificate chain (X.509 PEM), private key (PKCS\#8 PEM), and private key password (optional) used for mutual TLS authentication with your Confluent schema registry.
+ `SERVER_ROOT_CA_CERTIFICATE` – The Secrets Manager ARN of your secret key containing the root CA certificate (X.509 PEM) used for TLS encryption with your Confluent schema registry.
+ `OAUTHBEARER_AUTH` – The Secrets Manager ARN of your secret key containing the OAuth 2.0 credentials that Lambda uses to acquire an access token for your Confluent schema registry. For the contents of the secret, see [Configuring the OAuth secret](https://docs.aws.amazon.com/lambda/latest/dg/kafka-cluster-auth.html#smaa-auth-oauth-secret).
*Required*: No
*Type*: String
*Allowed values*: `BASIC_AUTH | CLIENT_CERTIFICATE_TLS_AUTH | SERVER_ROOT_CA_CERTIFICATE | OAUTHBEARER_AUTH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`URI`  <a name="cfn-lambda-eventsourcemapping-schemaregistryaccessconfig-uri"></a>
 The URI of the secret (Secrets Manager secret ARN) to authenticate with your schema registry.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
