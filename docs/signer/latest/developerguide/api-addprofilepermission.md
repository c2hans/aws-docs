---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/api-addprofilepermission.html
---

# AddProfilePermission
<a name="api-addprofilepermission"></a>

The following Java example shows how to use the [`AddProfilePermission`](https://docs.aws.amazon.com/signer/latest/api/API_AddProfilePermission.html) operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.AddProfilePermissionRequest;
import com.amazonaws.services.signer.model.AddProfilePermissionResult;

public class AddProfilePermission {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileName = "{{MyProfile}}";
        String signingProfileVersion = "SeFHjuJAjV";
        String principal = "{{account}}";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("{{region}}")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Add the first permission to the profile - no revisionId required.
        // Applies to all versions of the profile
        AddProfilePermissionResult result = client.addProfilePermission(new AddProfilePermissionRequest()
                .withProfileName(signingProfileName)
                .withStatementId("statement1")
                .withPrincipal(principal)
                .withAction("signer:StartSigningJob"));

        // Add the second permission to the profile - revisionId required.
        // Optionally specify a profile version to lock the permission to a specific profile version
        client.addProfilePermission(new AddProfilePermissionRequest()
                .withProfileName(signingProfileName)
                .withProfileVersion(signingProfileVersion)
                .withStatementId("statement2")
                .withPrincipal(principal)
                .withAction("signer:GetSigningProfile")
                .withRevisionId(result.getRevisionId()));
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
