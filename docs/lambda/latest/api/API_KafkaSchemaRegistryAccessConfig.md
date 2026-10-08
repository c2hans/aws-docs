---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_KafkaSchemaRegistryAccessConfig.html
---

# KafkaSchemaRegistryAccessConfig
<a name="API_KafkaSchemaRegistryAccessConfig"></a>

Specific access configuration settings that tell Lambda how to authenticate with your schema registry.

If you're working with an AWS Glue schema registry, don't provide authentication details in this object. Instead, ensure that your execution role has the required permissions for Lambda to access your cluster.

If you're working with a Confluent schema registry, choose the authentication method in the `Type` field, and provide the AWS Secrets Manager secret ARN in the `URI` field.

## Contents
<a name="API_KafkaSchemaRegistryAccessConfig_Contents"></a>

 ** Type **   <a name="lambda-Type-KafkaSchemaRegistryAccessConfig-Type"></a>
 The type of authentication Lambda uses to access your schema registry.
+  `BASIC_AUTH` – The Secrets Manager ARN of your secret key used for basic authentication with your Confluent schema registry.
+  `CLIENT_CERTIFICATE_TLS_AUTH` – The Secrets Manager ARN of your secret key containing the certificate chain (X.509 PEM), private key (PKCS\#8 PEM), and private key password (optional) used for mutual TLS authentication with your Confluent schema registry.
+  `SERVER_ROOT_CA_CERTIFICATE` – The Secrets Manager ARN of your secret key containing the root CA certificate (X.509 PEM) used for TLS encryption with your Confluent schema registry.
+  `OAUTHBEARER_AUTH` – The Secrets Manager ARN of your secret key containing the OAuth 2.0 credentials that Lambda uses to acquire an access token for your Confluent schema registry. For the contents of the secret, see [Configuring the OAuth secret](https://docs.aws.amazon.com/lambda/latest/dg/kafka-cluster-auth.html#smaa-auth-oauth-secret).
Type: String
Valid Values: `BASIC_AUTH | CLIENT_CERTIFICATE_TLS_AUTH | SERVER_ROOT_CA_CERTIFICATE`
Required: No

 ** URI **   <a name="lambda-Type-KafkaSchemaRegistryAccessConfig-URI"></a>
 The URI of the secret (Secrets Manager secret ARN) to authenticate with your schema registry.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

## See Also
<a name="API_KafkaSchemaRegistryAccessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/KafkaSchemaRegistryAccessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/KafkaSchemaRegistryAccessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/KafkaSchemaRegistryAccessConfig)
