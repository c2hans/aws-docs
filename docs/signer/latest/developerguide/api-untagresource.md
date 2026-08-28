---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/api-untagresource.html
---

# UntagResource
<a name="api-untagresource"></a>

The following Java example shows how to use the [`UntagResource`](url-signer-api;API_UntagResource.html) operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.UntagResourceRequest;

import java.util.Collections;

public class UntagResource {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileArn = "arn:aws:signer:{{region}}:{{account}}:/signing-profiles/{{MyProfile}}";
        String tagKey = "Key";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("{{region}}")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Remove a tag from a signing profile
        client.untagResource(new UntagResourceRequest()
                .withResourceArn(signingProfileArn)
                .withTagKeys(Collections.singletonList(tagKey)));
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
