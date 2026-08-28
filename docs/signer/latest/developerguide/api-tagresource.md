---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/api-tagresource.html
---

# TagResource
<a name="api-tagresource"></a>

The following Java example shows how to use the [`TagResource`](https://docs.aws.amazon.com/signer/latest/api/API_TagResource.html) operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.TagResourceRequest;

import java.util.Collections;

public class TagResource {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileArn = "arn:aws:signer:{{region}}:{{account}}:/signing-profiles/{{MyProfile}}";
        String tagKey = "Key";
        String tagValue = "Value";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("{{region}}")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Add a tag to a signing profile
        client.tagResource(new TagResourceRequest()
                .withResourceArn(signingProfileArn)
                .withTags(Collections.singletonMap(tagKey, tagValue)));
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
