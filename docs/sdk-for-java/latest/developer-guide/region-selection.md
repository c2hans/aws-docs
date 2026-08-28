---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/region-selection.html
---

# Setting the AWS Region for the AWS SDK for Java 2.x
<a name="region-selection"></a>

SDK clients connect to an AWS service in a specific AWS Region that you specify when you create the client. This configuration allows your application to interact with AWS resources in that geographical area. When you create a service client without explicitly setting a Region, the SDK uses the default Region from your external configuration.

## Explicitly configure an AWS Region
<a name="region-selection-choose-region"></a>

To explicitly set a Region, we recommend that you use the constants defined in the [Region](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/regions/Region.html) class. This is an enumeration of all publicly available regions.

To create a client with an enumerated Region from the class, use the client builder's `region` method.

```
Ec2Client ec2 = Ec2Client.builder()
          .region(Region.US_WEST_2)
          .build();
```

If the Region you want to use isn’t one of the enumerations in the `Region` class, you can create a new Region by using the static `of` method. This method allows you access to new Regions without upgrading the SDK.

```
Region newRegion = Region.of("us-east-42");
Ec2Client ec2 = Ec2Client.builder()
          .region(newRegion)
          .build();
```

**Note**
After you build a client with the builder, it’s *immutable* and the AWS Region *cannot be changed*. If you need to work with multiple AWS Regions for the same service, you should create multiple clients—​one per Region.

## Let the SDK automatically determine the default AWS Region from the environment
<a name="automatically-determine-the-aws-region-from-the-environment"></a>

When your code runs on Amazon EC2 or AWS Lambda, you might want to configure clients to use the same AWS Region that your code is running on. This decouples your code from the environment it’s running in and makes it easier to deploy your application to multiple AWS Regions for lower latency or redundancy.

To use the default AWS Region provider chain to determine the Region from the environment, use the client builder’s `create` method.

```
Ec2Client ec2 = Ec2Client.create();
```

You can also configure the client in other ways, but not set the Region. The SDK picks up the AWS Region by using the default region provider chain:

```
Ec2Client ec2Client = Ec2Client.builder()
        .credentialsProvider(ProfileCredentialsProvider.builder()
                .profileName("my-profile")
                .build())
        .build();
```

If you don’t explicitly set an AWS Region by using the `region` method, the SDK consults the default region provider chain to determine the Region to use.

### Understanding the default AWS Region provider chain
<a name="default-region-provider-chain"></a>

 **The SDK takes the following steps to look for an AWS Region:**

1. Any explicit Region set by using the `region` method on the builder itself takes precedence over anything else.

1. The SDK looks for the JVM system property `aws.region` and uses its value if found.

1. The `AWS_REGION` environment variable is checked. If it’s set, that Region is used to configure the client.
**Note**
The Lambda container sets this environment variable.

1. The SDK checks the active profile in the [AWS shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html). If the `region` property is present, the SDK uses it.

   The `default` profile is the active profile unless overridden by `AWS_PROFILE` environment variable or `aws.profile` JVM system property. If the SDK finds the `region` property in both files for the same profile (including the `default` profile), the SDK uses the value in the shared credentials file.

1. The SDK attempts to use the Amazon EC2 instance metadata service (IMDS) to determine the Region of the currently running Amazon EC2 instance.
   + For greater security, you should disable the SDK from attempting to use version 1 of IMDS. You use the same setting to disable version 1 that are described in the [Securely acquire IAM role credentials](ec2-iam-roles.md#securely-read-IAM-role_credentials) section.

1. If the SDK still hasn’t found a Region by this point, client creation fails with an exception.

When developing AWS applications, a common approach is to use the *shared configuration file* to set the Region for local development, and rely on the default region provider chain to determine the Region when the application runs on AWS infrastructure. This greatly simplifies client creation and keeps your application portable.

## Check to see if a service is available in a Region
<a name="region-selection-query-service"></a>

To see if a particular AWS service is available in a Region, use the static `serviceMetadata` method on a service client:

```
DynamoDbClient.serviceMetadata().regions().forEach(System.out::println);
```

The previous snippet prints out a long list of AWS Region codes that have the DynamoDB service:

```
af-south-1
ap-east-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-south-1
ap-south-2
ap-southeast-1
...
```

You can use a code to look up the [Region class enumeration](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/regions/Region.html) for the Region you need your service client to use.

For example, if you want to work with DynamoDB in the Region with the code `ap-northeast-2`, create your DynamoDB client with at least the following configuration:

```
DynamoDbClient ddb = DynamoDbClient.builder()
    .region(Region.AP_NORTHEAST_2)
    .build();
```

## Choose a specific endpoint
<a name="choosing-a-specific-endpoint"></a>

In certain situations—such as to test preview features of a service before the features graduate to general availability—you may need to specify a specific endpoint in a Region. In these situations, service clients can be configured by calling the `endpointOverride` method.

For example, to configure an Amazon EC2 client to use the Europe (Ireland) Region with a specific endpoint, use the following code.

```
Ec2Client ec2 = Ec2Client.builder()
               .region(Region.EU_WEST_1)
               .endpointOverride(URI.create("https://ec2.eu-west-1.amazonaws.com"))
               .build();
```

See [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) for the current list of regions and their corresponding endpoints for all AWS services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
