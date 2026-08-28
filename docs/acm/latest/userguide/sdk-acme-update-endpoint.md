---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/sdk-acme-update-endpoint.html
---

# Updating an ACME endpoint
<a name="sdk-acme-update-endpoint"></a>

The following example shows how to use the [UpdateAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeEndpoint.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.UpdateAcmeEndpointRequest;
import com.amazonaws.services.certificatemanager.model.CertificateAuthority;
import com.amazonaws.services.certificatemanager.model.PublicCertificateAuthority;

import java.util.Arrays;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Configure an updated certificate authority.
        PublicCertificateAuthority publicCA = new PublicCertificateAuthority()
            .withAllowedKeyAlgorithms(Arrays.asList("RSA_2048", "EC_prime256v1", "EC_secp384r1"));

        CertificateAuthority ca = new CertificateAuthority()
            .withPublicCertificateAuthority(publicCA);

        // Create the request.
        UpdateAcmeEndpointRequest req = new UpdateAcmeEndpointRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withContact("NOT_REQUIRED")
            .withCertificateAuthority(ca);

        // Update the ACME endpoint.
        client.updateAcmeEndpoint(req);
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
