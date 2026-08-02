---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/session-credentials-in-your-app.html
---

# Using credentials in your application
<a name="session-credentials-in-your-app"></a>

After the session starts, your application or launch script can call AWS services using the credentials you configured. You do not need to change your code. The AWS SDK automatically discovers and uses the credentials.

To verify that credentials are available, run the following command from your application or launch script:

```
aws sts get-caller-identity
```

The AWS CLI and all AWS SDKs automatically discover session credentials and refresh them before they expire. You do not need to manage credential rotation in your application code.

For more information about how the AWS SDK discovers credentials, see [Credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

**Important**
Do not set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or `AWS_SESSION_TOKEN` environment variables in your session's `AdditionalEnvironmentVariables`. These take precedence and prevent your application from using the IAM role credentials.
