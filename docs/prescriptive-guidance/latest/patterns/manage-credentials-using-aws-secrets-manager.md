---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-credentials-using-aws-secrets-manager.html
---

# Manage credentials using AWS Secrets Manager
<a name="manage-credentials-using-aws-secrets-manager"></a>

*Durga Prasad Cheepuri, Amazon Web Services*

## Summary
<a name="manage-credentials-using-aws-secrets-manager-summary"></a>

This pattern walks you through using AWS Secrets Manager to dynamically fetch database credentials for a Java Spring application.

In the past, when you created a custom application that retrieves information from a database, you typically had to embed the credentials (the secret) for accessing the database directly in the application. When it was time to rotate the credentials, you had to invest time to update the application to use the new credentials, and then distribute the updated application. If you had multiple applications that shared credentials and you missed updating one of them, the application would fail. Because of this risk, many users chose not to regularly rotate their credentials, which effectively substituted one risk for another.

Secrets Manager enables you to replace hard-coded credentials in your code (including passwords) with an API call to retrieve the secret programmatically. This helps ensure that the secret can't be compromised by someone who is examining your code, because the secret simply isn't there. You can also configure Secrets Manager to automatically rotate the secret according to a schedule that you specify. This enables you to replace long-term secrets with short-term ones, which helps significantly reduce the risk of compromise. For more information, see the [AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

## Prerequisites and limitations
<a name="manage-credentials-using-aws-secrets-manager-prereqs"></a>

**Prerequisites**
+ An AWS account with access to Secrets Manager
+ A Java Spring application

## Architecture
<a name="manage-credentials-using-aws-secrets-manager-architecture"></a>

**Source technology stack**
+ A Java Spring application with code that accesses a database, with DB credentials managed from the application.properties file.

**Target technology stack **
+ A Java Spring application with code that accesses a database, with DB credentials managed in Secrets Manager. The application.properties file holds the secrets to Secrets Manager.

**Secrets Manager integration with an application**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/44d359f5-47d9-4228-ac14-a64b5dfa7972/images/fc4b44fd-d1bd-4564-9bc1-c42c896e305b.png)

## Tools
<a name="manage-credentials-using-aws-secrets-manager-tools"></a>
+ **Secrets Manager** – [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) is an AWS service that makes it easier for you to manage secrets. Secrets can be database credentials, passwords, third-party API keys, and even arbitrary text. You can store and control access to these secrets centrally by using the Secrets Manager console, the Secrets Manager command-line interface (CLI), or the Secrets Manager API and SDKs.

## Epics
<a name="manage-credentials-using-aws-secrets-manager-epics"></a>

### Store secret in Secrets Manager
<a name="store-secret-in-secrets-manager"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Store the DB credentials as a secret in Secrets Manager. | Store Amazon Relational Database Service (Amazon RDS) or other DB credentials as a secret in Secrets Manager by following the steps in [Creating a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html) in the Secrets Manager documentation. | Sys Admin |
| Set permissions for the Spring application to access Secrets Manager. | Set the appropriate permissions based on how the Java Spring application uses Secrets Manager. To control access to the secret, create a policy based on the information provided in the Secrets Manager documentation, in the sections [Using identity-based policies (IAM Policies) and ABAC for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_identity-based-policies.html) and [Using resource-based policies for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html). Follow the steps in the section [Retrieving the secret value](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_retrieve-secret.html) in the Secrets Manager documentation. | Sys Admin |

### Update the Spring application
<a name="update-the-spring-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add JAR dependencies to use Secrets Manager. | See the *Additional information* section for details. | Java developer |
| Add the details of the secret to the Spring application. | Update the application.properties file with the secret name, endpoints, and AWS Region. For an example, see the *Additional information* section. | Java developer |
| Update the DB credentials retrieval code in Java. | In the application, update the Java code that fetches the DB credentials to fetch those details from Secrets Manager. For example code, see the *Additional information* section. | Java developer |

## Related resources
<a name="manage-credentials-using-aws-secrets-manager-resources"></a>
+ [AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
+ [Using identity-based policies (IAM Policies) and ABAC for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_identity-based-policies.html)
+ [Using resource-based policies for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html)
+ [Sample code](https://github.com/durgachamz/Spring-secrets-manager)

## Additional information
<a name="manage-credentials-using-aws-secrets-manager-additional"></a>

**Adding JAR dependencies for using Secrets Manager**

*Maven:*

```
<groupId>com.amazonaws</groupId>
    <artifactId>aws-java-sdk-secretsmanager</artifactId>
    <version>1.11. 355 </version>
```

*Gradle:*

```
compile group: 'com.amazonaws', name: 'aws-java-sdk-secretsmanager', version: '1.11.355'
```

**Updating the application.properties file with the details of the secret**

```
spring.aws.secretsmanager.secretName=postgres-local
spring.aws.secretsmanager.endpoint=secretsmanager.us-east-1.amazonaws.com
spring.aws.secretsmanager.region=us-east-1
```

**Updating the DB credentials retrieval code in Java**

```
String  secretName  =  env.getProperty("spring.aws.secretsmanager.secretName");
String  endpoints  =  env.getProperty("spring.aws.secretsmanager.endpoint");
String  AWS Region  =  env.getProperty("spring.aws.secretsmanager.region");
AwsClientBuilder.EndpointConfiguration  config  =  new  AwsClientBuilder.EndpointConfiguration(endpoints, AWS Region);
AWSSecretsManagerClientBuilder  clientBuilder  =  AWSSecretsManagerClientBuilder.standard();
clientBuilder.setEndpointConfiguration(config);
AWSSecretsManager  client  =  clientBuilder.build();

ObjectMapper  objectMapper  =  new  ObjectMapper();

JsonNode  secretsJson  =  null;

ByteBuffer  binarySecretData;

GetSecretValueRequest  getSecretValueRequest  =  new  GetSecretValueRequest().withSecretId(secretName);

GetSecretValueResult  getSecretValueResponse  =  null;

try  {
     getSecretValueResponse  =  client.getSecretValue(getSecretValueRequest);
    }

catch  (ResourceNotFoundException  e)  {
     log.error("The requested secret "  +  secretName  +  " was not found");
    }

catch  (InvalidRequestException  e)  {
     log.error("The request was invalid due to: "  +  e.getMessage());
     }

catch  (InvalidParameterException  e)  {
     log.error("The request had invalid params: "  +  e.getMessage());
     }
if  (getSecretValueResponse  ==  null)  {
     return  null;
     }  // Decrypted secret using the associated KMS key // Depending on whether the secret was a string or binary, one of these fields will be populated

String secret = getSecretValueResponse.getSecretString();

if (secret != null) {
     try {
                secretsJson  =  objectMapper.readTree(secret);
           }

     catch  (IOException  e)  {
                log.error("Exception while retrieving secret values: "  +  e.getMessage());
           }
}

else  {
     log.error("The Secret String returned is null");

     return null;

     }
     String  host  =  secretsJson.get("host").textValue();
     String  port  =  secretsJson.get("port").textValue();
     String  dbname  =  secretsJson.get("dbname").textValue();
     String  username  =  secretsJson.get("username").textValue();
     String  password  =  secretsJson.get("password").textValue();
}
```
