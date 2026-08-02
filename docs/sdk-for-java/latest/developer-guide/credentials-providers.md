---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-providers.html
---

# Specify a specific credentials provider in the AWS SDK for Java 2.x
<a name="credentials-providers"></a>

While the default credentials provider chain is convenient for many scenarios, explicitly specifying credentials providers gives you greater control over authentication behavior, performance, and security.

Reasons that you might want to specify a credentials provider might include:
+ The default provider chain checks multiple sources sequentially, which can add latency:

  ```
  // The default provider chain checks might check multiple sources until it finds
  // sufficient configuration.
  S3Client s3Client = S3Client.builder().build();

  // You can specify exactly where to look.
  S3Client optimizedClient = S3Client.builder()
      .credentialsProvider(InstanceProfileCredentialsProvider.create())
      .build();
  ```
+ You need to use non-standard locations for accessing credentials configuration:

  ```
  // Use configuration from a custom file location.
  S3Client s3Client = S3Client.builder()
      .credentialsProvider(ProfileCredentialsProvider.builder()
              .profileFile(ProfileFile.builder()
                      .content(Paths.get("/custom/path/to/configuration/file"))
                      .type(ProfileFile.Type.CONFIGURATION) // Expects all non-default profiles to be prefixed with "profile".
                      .build())
              .profileName("custom")
              .build())
      .build();
  ```
+ Use different credentials for different service clients. For example, if your application needs to access multiple AWS accounts or use different permissions for different services:

  ```
  // S3 client using one set of credentials.
  S3Client s3Client = S3Client.builder()
      .credentialsProvider(ProfileCredentialsProvider.create("s3-readonly"))
      .build();

  // DynamoDB client using different credentials.
  DynamoDbClient dynamoDbClient = DynamoDbClient.builder()
      .credentialsProvider(ProfileCredentialsProvider.create("dynamodb-admin"))
      .build();
  ```
+ Control credential refresh behavior:

  ```
  // Create a provider with custom refresh behavior.
  StsAssumeRoleCredentialsProvider customRefreshProvider =
      StsAssumeRoleCredentialsProvider.builder()
          .refreshRequest(AssumeRoleRequest.builder()
              .roleArn("arn:aws:iam::123456789012:role/my-role")
              .roleSessionName("custom-session")
              .build())
          .stsClient(StsClient.create())
          .asyncCredentialUpdateEnabled(true) // Use a background thread to prefetch credentials.
          .build();

  S3Client s3Client = S3Client.builder()
      .credentialsProvider(customRefreshProvider)
      .build();
  ```
