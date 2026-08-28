---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/api-removeprofilepermission.html
---

# RemoveProfilePermission
<a name="api-removeprofilepermission"></a>

The following Java example shows how to use the [`RemoveProfilePermission`](https://docs.aws.amazon.com/signer/latest/api/API_RemoveProfilePermission.html) operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.ListProfilePermissionsRequest;
import com.amazonaws.services.signer.model.ListProfilePermissionsResult;
import com.amazonaws.services.signer.model.RemoveProfilePermissionRequest;

public class RemoveProfilePermission {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileName = "{{MyProfile}}";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("{{region}}")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Get the latest revisionId for the profile
        ListProfilePermissionsResult result = client.listProfilePermissions(new ListProfilePermissionsRequest()
                .withProfileName(signingProfileName));

        // Remove a specific permission from the profile
        client.removeProfilePermission(new RemoveProfilePermissionRequest()
                .withProfileName(signingProfileName)
                .withStatementId("statement1")
                .withRevisionId(result.getRevisionId()));
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
