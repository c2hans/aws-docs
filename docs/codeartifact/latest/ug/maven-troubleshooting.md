---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/maven-troubleshooting.html
---

# Maven troubleshooting
<a name="maven-troubleshooting"></a>

The following information might help you troubleshoot common issues with Maven and CodeArtifact.

## Disable parallel puts to fix error 429: Too Many Requests
<a name="disable-parallel-puts"></a>

Starting with version 3.9.0, Maven uploads package artifacts in parallel (up to 5 files at a time). This can cause CodeArtifact to occasionally respond with an error response code 429 (Too Many Requests). If you encounter this error, you can disable parallel puts to fix it.

To disable parallel puts, set the `aether.connector.basic.parallelPut` property to `false` in your profile in your `settings.xml` file as shown by the following example:

```
<settings>
    <profiles>
        <profile>
            <id>default</id>
            <properties>
                <aether.connector.basic.parallelPut>false</aether.connector.basic.parallelPut>
            </properties>
        </profile>
    </profiles>
<settings>
```

For more information, see [Artifact Resolver Configuration Options](https://maven.apache.org/resolver/configuration.html) in the Maven documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
