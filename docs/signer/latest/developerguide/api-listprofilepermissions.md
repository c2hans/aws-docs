---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/api-listprofilepermissions.html
---

# ListProfilePermissions
<a name="api-listprofilepermissions"></a>

The following Java example shows how to use the [`ListProfilePermissions`](https://docs.aws.amazon.com/signer/latest/api/API_ListProfilePermissions.html) operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.ListProfilePermissionsRequest;
import com.amazonaws.services.signer.model.ListProfilePermissionsResult;
import com.amazonaws.services.signer.model.Permission;

public class ListProfilePermissions {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileName = "{{MyProfile}}";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("{{region}}")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // List the permissions for a profile
        ListProfilePermissionsResult result = client.listProfilePermissions(new ListProfilePermissionsRequest()
                .withProfileName(signingProfileName));

        // Iterate through the permissions
        for (Permission permission: result.getPermissions()) {
            System.out.println("StatementId: " + permission.getStatementId());
            System.out.println("Principal: " + permission.getPrincipal());
            System.out.println("Action: " + permission.getAction());
            System.out.println("ProfileVersion: " + permission.getProfileVersion());
        }
        System.out.println("RevisionId: " + result.getRevisionId());
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
