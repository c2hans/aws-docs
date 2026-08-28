---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/custom-cred-provider.html
---

# Create custom credential providers
<a name="custom-cred-provider"></a>

You can create a custom credentials provider and give its class name and jar path to the Kinesis agent in the following configuration settings: `userDefinedCredentialsProvider.classname` and `userDefinedCredentialsProvider.location`. For the descriptions of these two configuration settings, see [Specify agent configuration settings](agent-config-settings.md).

To create a custom credentials provider, define a class that implements the `AWSCredentialsProvider` interface, like the one in the following example.

```
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;

public class {{YourClassName}} implements AWSCredentialsProvider {
    public {{YourClassName}}() {
    }

    public AWSCredentials getCredentials() {
        return new BasicAWSCredentials("{{key1}}", "{{key2}}");
    }

    public void refresh() {
    }
}
```

Your class must have a constructor that takes no arguments.

AWS invokes the refresh method periodically to get updated credentials. If you want your credentials provider to provide different credentials throughout its lifetime, include code to refresh the credentials in this method. Alternatively, you can leave this method empty if you want a credentials provider that vends static (non-changing) credentials.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
