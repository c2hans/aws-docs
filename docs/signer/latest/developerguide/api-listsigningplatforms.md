---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/api-listsigningplatforms.html
---

# ListSigningPlatforms
<a name="api-listsigningplatforms"></a>

The following Java example shows how to use the [`ListSigningPlatforms`](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningPlatforms.html) operation.

```
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSsigner;
import com.amazonaws.services.signer.AWSsignerClient;
import com.amazonaws.services.signer.model.ListSigningPlatformsRequest;
import com.amazonaws.services.signer.model.ListSigningPlatformsResult;
import com.amazonaws.services.signer.model.SigningPlatform;

public class ListSigningPlatforms {

    public static void main(String[] s) {

        final String credentialsProfile = "default";

        // Create a client.
        final AWSsigner client = AWSsignerClient.builder()
                .withRegion("{{region}}")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        ListSigningPlatformsResult result;
        String nextToken = null;
        do {
            result = client.listSigningPlatforms(new ListSigningPlatformsRequest().withNextToken(null));

            for (SigningPlatform platform : result.getPlatforms()) {
                System.out.println("Display Name : " + platform.getDisplayName());
                System.out.println("Platform Id : " + platform.getPlatformId());
                System.out.println("Signing Configuration : " + platform.getSigningConfiguration());
            }

            nextToken = result.getNextToken();
        } while (nextToken != null);
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
