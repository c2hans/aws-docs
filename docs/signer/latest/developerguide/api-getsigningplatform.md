---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/api-getsigningplatform.html
---

# GetSigningPlatform
<a name="api-getsigningplatform"></a>

The following Java example shows how to use the [`GetSigningPlatform`](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningPlatform.html) operation.

```
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSsigner;
import com.amazonaws.services.signer.AWSsignerClient;
import com.amazonaws.services.signer.model.GetSigningPlatformRequest;
import com.amazonaws.services.signer.model.GetSigningPlatformResult;

public class GetSigningPlatform {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String codeSigningPlatformId = "aws-signer-platform-id";

        // Create a client.
        AWSsigner client = AWSsignerClient.builder()
                .withRegion("{{region}}")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        GetSigningPlatformResult result = client.getSigningPlatform(
                new GetSigningPlatformRequest().withPlatformId(codeSigningPlatformId));

        System.out.println("Display Name : " + result.getDisplayName());
        System.out.println("Platform Id : " + result.getPlatformId());
        System.out.println("Signing Configuration : " + result.getSigningConfiguration());
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
