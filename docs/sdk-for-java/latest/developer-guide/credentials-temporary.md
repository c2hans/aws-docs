---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-temporary.html
---

# Access credentials for interactive development work using AWS SDK for Java 2.x
<a name="credentials-temporary"></a>

For increased security, AWS recommends that you configure the SDK for Java to [use temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) instead of long-lived credentials. Temporary credentials consist of access keys (access key id and secret access key) and a session token.

Several approaches are available to you to work with temporary credentials. The approach you use, and therefore the configuration that you provide to the SDK, depends on your use case.

When you do interactive development work with the Java SDK, we recommend that you use AWS Console login credentials.

## Using console login credentials
<a name="using-con-login-creds"></a>

You can use your existing AWS Management Console sign-in credentials for programmatic access to AWS services. After a browser-based authentication flow, AWS generates temporary credentials that work across local development tools like the AWS CLI and the SDK for Java 2.x.

With this process, you can authenticate using root credentials created during initial account set up, an IAM user, or a federated identity from your identity provider, and the AWS CLI automatically manages the temporary credentials for you. This approach enhances security by eliminating the need to store long-term credentials locally.

When you run the `aws login` command, you can select from your active console sessions, or sign in through the browser-based authentication flow and this will automatically generate temporary credentials. The SDK for Java 2.x will automatically refresh these credentials for up to 12 hours.

**Important**
In addition to the configuration that you set in the shared config file that works for all projects, each individual Java project requires the following dependency in the Maven `pom.xml` file:

```
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>signin</artifactId>
</dependency>
```
The `signin` dependency provide the code that enables the SDK for Java 2.x to access and use console login credentials.

For more information on prerequsites, logging in and signing out, see [Login for AWS local development using console credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) in the *AWS SDK and Tools Refernce Guide*.

## Single-sign-on approach
<a name="single-sign-on-approach"></a>

When you do interactive development work with the Java SDK, you can alternatively use the single sign-on approach. This approach requires the following setup:
+ [Set up through the IAM Identity Center](get-started-auth.md#setup-auth)
+ [Configure a profile in the AWS shared config file](get-started-auth.md#setup-credentials)
+ using the AWS CLI and [running a command](get-started-auth.md#setup-login-sso) to login and creating an active session

### IAM Identity Center configuration
<a name="credentials-temporary-idc"></a>

When you configure the SDK to use IAM Identity Center single sign-on access as described in [Setup overview](setup.md#setup-overview) in this guide, the SDK uses temporary credentials.

The SDK uses the IAM Identity Center access token to gain access to the IAM role that is configured with the `sso_role_name` setting in your `config` file. The SDK assumes this IAM role and retrieves temporary credentials to sign AWS service requests.

For more details about how the SDK gets temporary credentials from the configuration, see the [Understanding IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html) section of the AWS SDKs and Tools Reference Guide.

**Important**
In addition to the configuration that you set in the shared `config` file that works for all projects, each individual Java project requires the following dependencies in the Maven `pom.xml` file:

```
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>sso</artifactId>
</dependency>
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>ssooidc</artifactId>
</dependency>
```
The `sso` and `ssooidc` dependencies provide the code that enables the SDK for Java 2.x to access temporary credentials.

### Retrieve temporary credentials from the AWS access portal
<a name="credentials-temporary-from-portal"></a>

As an alternative to IAM Identity Center single sign-on configuration, you can copy and use temporary credentials available in the AWS access portal. You can use the temporary credentials in a profile or use them as values for system properties and environment variables.

**Set up a local credentials file for temporary credentials**

1. [Create a shared credentials file](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html)

1. In the credentials file, paste the following placeholder text until you paste in working temporary credentials.

   ```
   [default]
   aws_access_key_id={{<value from AWS access portal>}}
   aws_secret_access_key={{<value from AWS access portal>}}
   aws_session_token={{<value from AWS access portal>}}
   ```

1. Save the file. The file `~/.aws/credentials` should now exist on your local development system. This file contains the [[default] profile](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-profile) that the SDK for Java uses if a specific named profile is not specified.

1. [Sign in to the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosignin.html)

1. Follow these instructions under the [Manual credential refresh](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html#how-to-get-temp-credentials) heading to copy IAM role credentials from the AWS access portal.

   1. For step 2 in the linked instructions, choose `Access keys` for the IAM role name that grants access for your development needs. This role typically has a name like **PowerUserAccess** or ** Developer**.

   1. In the modal dialog box, select the your operating system and copy the contents from **Add a profile to your AWS credentials file**.

1. Paste the copied credentials into your local `credentials` file and remove the generated profile name. Your file should resemble the following.

   ```
   [default]
   aws_access_key_id=AKIAIOSFODNN7EXAMPLE
   aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   aws_session_token=IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE
   ```

1. Save the `credentials` file.

When the SDK for Java creates a service client, it will access these temporary credentials and use them for each request. The settings for the IAM role chosen in step 5a determine [how long the temporary credentials are valid](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html). The maximum duration is twelve hours.

After the temporary credentials expire, repeat steps 4 through 7.
