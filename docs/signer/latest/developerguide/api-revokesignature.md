---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/api-revokesignature.html
---

# RevokeSignature
<a name="api-revokesignature"></a>

The following Java example shows how to use the [`RevokeSignature`](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSignature.html) operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.RevokeSignatureRequest;

public class RevokeSignature {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingJobId = "{{jobID}}";
        String revokeReason = "{{Reason for revocation}}";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("{{region}}")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Revoke a signing job
        client.revokeSignature(new RevokeSignatureRequest()
                .withJobId(signingJobId)
                .withReason(revokeReason));
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
