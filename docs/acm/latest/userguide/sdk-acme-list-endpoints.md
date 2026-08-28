---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/sdk-acme-list-endpoints.html
---

# Listing ACME endpoints
<a name="sdk-acme-list-endpoints"></a>

The following example shows how to use the [ListAcmeEndpoints](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeEndpoints.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.ListAcmeEndpointsRequest;
import com.amazonaws.services.certificatemanager.model.ListAcmeEndpointsResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        ListAcmeEndpointsRequest req = new ListAcmeEndpointsRequest()
            .withMaxResults(10);

        // List the ACME endpoints.
        ListAcmeEndpointsResult result = client.listAcmeEndpoints(req);
        System.out.println(result);
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
