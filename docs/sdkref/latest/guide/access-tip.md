---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-tip.html
---

# Using the TIP plugin to access AWS services
<a name="access-tip"></a>

 Trusted identity propagation (TIP) is a feature of AWS IAM Identity Center that enables administrators of AWS services to grant permissions based on user attributes such as group associations. With trusted identity propagation, identity context is added to an IAM role to identify the user requesting access to AWS resources. This context is propagated to other AWS services.

 Identity context comprises information that AWS services use to make authorization decisions when they receive access requests. This information includes metadata that identifies the requester (for example, an IAM Identity Center user), the AWS service to which access is requested (for example, Amazon Redshift), and the scope of access (for example, read only access). The receiving AWS service uses this context, and any permissions assigned to the user, to authorize access to its resources. For more information, see in the [Trusted identity propagation overview](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html) in the AWS IAM Identity Center User Guide.

 The TIP plugin can be used with AWS services that support trusted identity propagation. As a reference use case, see [Configuring an Amazon Q Business application using AWS IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html) in the *Amazon Q Business User Guide*.

**Note**
 If you are using Amazon Q Business, see [Configuring an Amazon Q Business application using AWS IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html) for service-specific instructions.

## Prerequisites for using the TIP plugin
<a name="prereq-tip"></a>

The following resources are required in order for the plugin to work:

1. You must be using either the AWS SDK for Java or the AWS SDK for JavaScript.

1. Verify that the service you are using supports the trusted identity propagation.

   See the **Enables trusted identity propagation through IAM Identity Center** column of the [AWS managed applications that integrate with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps-that-work-with-identity-center.html) table in the *AWS IAM Identity Center User Guide*.

1. Enable IAM Identity Center and trusted identity propagation.

   See [TIP prerequisites and considerations](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.html) in the *AWS IAM Identity Center User Guide*.

1. You must have an Identity-Center-integrated application.

   See [AWS managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps-quick-start-setting-up-identity-center-to-test-awsmanagedapps.html) or [Customer managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.html) in the *AWS IAM Identity Center User Guide*.

1. You must set up a trusted token issuer (TTI) and connect your service to IAM Identity Center.

   See [Prerequisites for trusted token issuers](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.html#trusted-token-issuer-prerequisites) and [Tasks for setting up a trusted token issuer](https://docs.aws.amazon.com/singlesignon/latest/userguide/setuptrustedtokenissuer.html#setuptrustedtokenissuer-tasks) in the *AWS IAM Identity Center User Guide*.

## To use the TIP plugin in your code
<a name="using-tip"></a>

1. Create an instance of the trusted identity propagation plugin.

1. Create a service client instance for interacting with your AWS service and customize the service client by adding the trusted identity propagation plugin.

The TIP plugin takes the following input parameters:
+ **`webTokenProvider`**: A function that the customer implements to obtain an OpenID token from their external identity provider.
+ **`accessRoleArn`**: The IAM role ARN to be assumed by the plugin with the user's identity context to get the identity-enhanced credentials.
+ **`applicationArn`**: The unique identifier string for the client or application. This value is an application ARN that has OAuth grants configured.
+ **`ssoOidcClient`**: (Optional) An SSO OIDC client, such as [`SsoOidcClient`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ssooidc/SsoOidcClient.html) for Java or [`client-sso-oidc`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sso-oidc/) for JavaScript, with customer-defined configurations. If not provided, an OIDC client using `applicationRoleArn` will be instantiated and used.
+  **`stsClient`**: (Optional) An AWS STS client with customer-defined configurations, used to assume `accessRoleArn` with the user's identity context. If not provided, an AWS STS client using `applicationRoleArn` will be instantiated and used.
+ **`applicationRoleArn`**: (Optional) The IAM role ARN to be assumed with `AssumeRoleWithWebIdentity` so that the OIDC and AWS STS clients can be bootstrapped.
  + If not provided, **both** of the `ssoOidcClient` and `stsClient` parameters must be provided.
  + If provided, `applicationRoleArn` can't be the same value as the `accessRoleArn` parameter. `applicationRoleArn` is used to build the stsClient, which is used to assume accessRole. If the same role is used for both `applicationRole` and `accessRole`, it would mean using a role to assume itself (self-role assumption), which is discouraged by AWS. See the [announcement](https://aws.amazon.com/blogs/security/announcing-an-update-to-iam-role-trust-policy-behavior/) for more details.

### Considerations for `ssoOidcClient`, `stsClient`, and `applicationRoleArn` parameters
<a name="considerations-tip"></a>

When configuring the TIP plugin, consider the following permission requirements based on which parameters you provide:
+ If you are providing `ssoOidcClient` and `stsClient`:
  + Credentials on the `ssoOidcClient` should have `oauth:CreateTokenWithIAM` permission for calling identity center to get the identity center specific user context.
  + Credentials on `stsClient` should have `sts:AssumeRole`, and `sts:SetContext` permissions on `accessRole`. `accessRole` also needs to be configured with a trust relationship with the credentials on `stsClient`.
+ If you are providing `applicationRoleArn`:
  + `applicationRole` should have the `oauth:CreateTokenWithIAM`, `sts:AssumeRole` and `sts:SetContext` permissions on the required resources (IdC instance, `accessRole`) as it will be used to build OIDC and STS clients.
  + `applicationRole` should have a trust relationship with the identity provider that is used to generate the `webToken`, as the `webToken` will be used to assume the applicationRole via the [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) call by the plugin.

**Example ApplicationRole configuration:**

Trust Policy with Web token provider:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::{{111122223333}}:oidc-provider/IDENTITY_PROVIDER_URL"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "IDENTITY_PROVIDER_URL:aud": "CLIENT_ID_TO_BE_TRUSTED"
                }
            }
        }
    ]
}
```

Permission Policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole",
                "sts:SetContext"
            ],
            "Resource": [
                "arn:aws:iam::{{111122223333}}:role/{{accessRole}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sso-oauth:CreateTokenWithIAM"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

## Code examples using TIP
<a name="tip-code-example"></a>

The examples below show how to implement the TIP plugin in your code using the AWS SDK for Java or the AWS SDK for JavaScript.

------
#### [ Java ]

To use the TIP plugin in your AWS SDK for Java project, you need to declare it as a dependency in your project's `pom.xml` file.

```
<dependency>
<groupId>software.amazon.awsidentity.trustedIdentityPropagation</groupId>
<artifactId>aws-sdk-java-trustedIdentityPropagation-java-plugin</artifactId>
   <version>2.0.0</version>
</dependency>
```

In your source code, include the required package statement for `software.amazon.awssdk.trustedidentitypropagation`.

The following examples show two ways to create an instance of the trusted identity propagation plugin and add it to a service client. Both examples use Amazon S3 as the service and utilize `S3AccessGrantsPlugin` to manage user specific permissions, but can be applied to any AWS service that supports trusted identity propagation (TIP).

**Note**
For these examples, you need to setup the user specific permissions from S3 Access Grants. Refer to the [S3 Access Grants documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html) for more details.

**Option 1: Build and pass OIDC and STS clients**

```
SsoOidcClient oidcClient = SsoOidcClient.builder()
    .region(Region.US_EAST_1)
    .credentialsProvider(credentialsProvider).build();

StsClient stsClient = StsClient.builder()
    .region(Region.US_EAST_1)
    .credentialsProvider(credentialsProvider).build();

TrustedIdentityPropagationPlugin trustedIdentityPropagationPlugin = TrustedIdentityPropagationPlugin.builder()
        .webTokenProvider(() -> webToken)
        .applicationArn(idcApplicationArn)
        .accessRoleArn(accessRoleArn)
        .ssoOidcClient(oidcClient)
        .stsClient(stsClient)
        .build();

S3AccessGrantsPlugin accessGrantsPlugin = S3AccessGrantsPlugin.builder()
        .build();

S3Client s3Client =
        S3Client.builder().region(Region.US_EAST_1)
                .crossRegionAccessEnabled(true)
                .addPlugin(trustedIdentityPropagationPlugin)
                .addPlugin(accessGrantsPlugin)
                .build();

final var resp = s3Client.getObject(GetObjectRequest.builder()
        .key("path/to/object/fileName")
        .bucket("bucketName")
        .build());
```

**Option 2: Pass applicationRoleArn and defer client creation to the plugin**

```
TrustedIdentityPropagationPlugin trustedIdentityPropagationPlugin = TrustedIdentityPropagationPlugin.builder()
        .webTokenProvider(() -> webToken)
        .applicationArn(idcApplicationArn)
        .accessRoleArn(accessRoleArn)
        .applicationRoleArn(applicationRoleArn)
        .build();

S3AccessGrantsPlugin accessGrantsPlugin = S3AccessGrantsPlugin.builder()
        .build();

S3Client s3Client =
        S3Client.builder().region(Region.US_EAST_1)
                .crossRegionAccessEnabled(true)
                .addPlugin(trustedIdentityPropagationPlugin)
                .addPlugin(accessGrantsPlugin)
                .build();

final var resp = s3Client.getObject(GetObjectRequest.builder()
        .key("path/to/object/fileName")
        .bucket("bucketName")
        .build());
```

For additional details and source, see [ trusted-identity-propagation-java](https://github.com/aws-sdk-plugin/trusted-identity-propagation-java) on GitHub.

------
#### [ JavaScript ]

Run the following command to install the TIP authentication plugin package in your AWS SDK for JavaScript project:

```
$  npm i @aws-sdk-extension/trusted-identity-propagation
```

The final `package.json` should include a dependency similar to the following:

```
  "dependencies": {
"@aws-sdk-extension/trusted-identity-propagation": "^2.0.0"
  },
```

 In your source code, import the required `TrustedIdentityPropagationExtension` dependency.

 The following examples show two ways to create an instance of the trusted identity propagation plugin and add it to a service client. Both examples use Amazon S3 as the service and utilize Amazon S3 Access Grants to manage user specific permissions, but can be applied to any AWS service that supports trusted identity propagation (TIP).

**Note**
For these examples, you need to setup the user specific permissions from Amazon S3 Access Grants, refer to the [Amazon S3 Access Grants documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html) for more details.

**Option 1: Build and pass OIDC and STS clients**

```
import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";
import { S3ControlClient, GetDataAccessCommand } from "@aws-sdk/client-s3-control";
import { TrustedIdentityPropagationExtension } from "@aws-sdk-extension/trusted-identity-propagation";

const s3ControlClient = new S3ControlClient({
    region: "us-east-1",
    extensions: [
        TrustedIdentityPropagationExtension.create({
            webTokenProvider: async () => {
                return 'ID_TOKEN_FROM_YOUR_IDENTITY_PROVIDER';
            },
            ssoOidcClient: customOidcClient,
            stsClient: customStsClient,
            accessRoleArn: accessRoleArn,
            applicationArn: applicationArn,
        }),
    ],
});

const getDataAccessParams = {
  Target: "S3_URI_PATH",
  Permission: "READ",
  AccountId: ACCOUNT_ID,
  InstanceArn: S3_ACCESS_GRANTS_ARN,
  TargetType: "Object",
};

try {
  const command = new GetDataAccessCommand(getDataAccessParams);
  const response = await s3ControlClient.send(command);

  const credentials = response.Credentials;

  // Create a new S3 client with the temporary credentials
  const temporaryS3Client = new S3Client({
    region: "us-east-1",
    credentials: {
      accessKeyId: credentials.AccessKeyId,
      secretAccessKey: credentials.SecretAccessKey,
      sessionToken: credentials.SessionToken,
    },
  });

  // Use the temporary S3 client to perform the operation
  const s3Params = {
    Bucket: "BUCKET_NAME",
    Key: "S3_OBJECT_KEY",
  };
  const getObjectCommand = new GetObjectCommand(s3Params);
  const s3Object = await temporaryS3Client.send(getObjectCommand);

  const fileContent = await s3Object.Body.transformToString();

  // Process the S3 object data
  console.log("Successfully retrieved S3 object:", fileContent);
} catch (error) {
  console.error("Error accessing S3 data:", error);
}
```

**Option 2: Pass applicationRoleArn and defer client creation to the plugin**

```
import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";
import { S3ControlClient, GetDataAccessCommand } from "@aws-sdk/client-s3-control";
import { TrustedIdentityPropagationExtension } from "@aws-sdk-extension/trusted-identity-propagation";

const s3ControlClient = new S3ControlClient({
    region: "us-east-1",
    extensions: [
        TrustedIdentityPropagationExtension.create({
            webTokenProvider: async () => {
                return 'ID_TOKEN_FROM_YOUR_IDENTITY_PROVIDER';
            },
            accessRoleArn: accessRoleArn,
            applicationRoleArn: applicationRoleArn,
            applicationArn: applicationArn,
        }),
    ],
});

// Same S3 AccessGrants workflow as Option 1
const getDataAccessParams = {
  Target: "S3_URI_PATH",
  Permission: "READ",
  AccountId: ACCOUNT_ID,
  InstanceArn: S3_ACCESS_GRANTS_ARN,
  TargetType: "Object",
};

try {
  const command = new GetDataAccessCommand(getDataAccessParams);
  const response = await s3ControlClient.send(command);

  const credentials = response.Credentials;

  const temporaryS3Client = new S3Client({
    region: "us-east-1",
    credentials: {
      accessKeyId: credentials.AccessKeyId,
      secretAccessKey: credentials.SecretAccessKey,
      sessionToken: credentials.SessionToken,
    },
  });

  const s3Params = {
    Bucket: "BUCKET_NAME",
    Key: "S3_OBJECT_KEY",
  };
  const getObjectCommand = new GetObjectCommand(s3Params);
  const s3Object = await temporaryS3Client.send(getObjectCommand);

  const fileContent = await s3Object.Body.transformToString();

  console.log("Successfully retrieved S3 object:", fileContent);
} catch (error) {
  console.error("Error accessing S3 data:", error);
}
```

For additional details and source, see [trusted-identity-propagation-js](https://github.com/aws-sdk-plugin/trusted-identity-propagation-js) on GitHub.

------
