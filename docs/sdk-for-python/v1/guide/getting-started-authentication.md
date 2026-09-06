---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/getting-started-authentication.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Authenticating with AWS using the AWS SDK for Python
<a name="getting-started-authentication"></a>

You must establish how the AWS SDK for Python authenticates with AWS when you develop with AWS services. The SDK manages credential discovery, signature creation, and credential refreshing completely behind the scenes, letting you focus on your application logic.

**Important**
During Developer Preview, the AWS SDK for Python supports fewer authentication sources than other AWS SDKs. For example, it can't use IAM Identity Center credentials or AWS Management Console sign-in credentials. For the sources this release supports, see [Credential providers](credential-providers.md).

For local development, we recommend short-term credentials. Obtain them with the AWS CLI or from your identity provider, and then supply them to the SDK by using one of the following two methods.

## Set environment variables
<a name="getting-started-auth-environment"></a>

Set your credentials as environment variables on macOS or Linux:

```
export AWS_ACCESS_KEY_ID={{your_access_key_id}}
export AWS_SECRET_ACCESS_KEY={{your_secret_access_key}}
export AWS_SESSION_TOKEN={{your_session_token}}
```

On Windows, use the following commands instead:

```
set AWS_ACCESS_KEY_ID={{your_access_key_id}}
set AWS_SECRET_ACCESS_KEY={{your_secret_access_key}}
set AWS_SESSION_TOKEN={{your_session_token}}
```

Omit `AWS_SESSION_TOKEN` if you use long-term credentials. Short-term credentials expire after a limited period, and requests then fail. In that case, obtain new credentials and set the variables again.

## Use a profile in the shared credentials file
<a name="getting-started-auth-profile"></a>

Instead of setting environment variables in each terminal session, you can store your credentials in a named profile. The `credentials` file is shared by AWS SDKs and tools such as the AWS CLI, so it might already exist on your system. For its location, see [Location of the shared files](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html) in the *AWS SDKs and Tools Reference Guide*.

Add a `[default]` profile to the `credentials` file:

```
[default]
aws_access_key_id = {{your_access_key_id}}
aws_secret_access_key = {{your_secret_access_key}}
aws_session_token = {{your_session_token}}
```

The SDK uses the `[default]` profile unless you select another one. To select a named profile, set the `AWS_PROFILE` environment variable:

```
export AWS_PROFILE={{my-profile}}
```

## Additional authentication options
<a name="getting-started-auth-more-information"></a>

The preceding sections cover local development. Code that runs within an AWS environment or assumes an IAM role uses other credential sources. For more options on authentication for the SDK, see the following:
+ For every credential source the SDK supports, and how to select one in your code, see [Credential providers](credential-providers.md).
+ To create short-term credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.
+ For best practices for protecting your AWS account and credentials, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.
